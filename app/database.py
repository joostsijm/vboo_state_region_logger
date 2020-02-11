"""Database module"""

from datetime import datetime, timedelta

from app import SESSION
from app.models import State, Region, StateRegion


def get_current_regions(state_id):
    """Get latest professor from database"""
    session = SESSION()
    current_regions = session.query(Region) \
        .join(Region.state_regions) \
        .filter(StateRegion.state_id == state_id) \
        .filter(StateRegion.until_date_time == None) \
        .all()
    session.close()
    return current_regions

def save_regions(state_id, regions):
    """Save residents to database"""
    session = SESSION()
    region_ids = []
    state = session.query(State).get(state_id)
    if state is None:
        state = save_state(session, state_id)
    for region_dict in regions:
        region = session.query(Region).get(region_dict['id'])
        if region is None:
            region = save_region(session, region_dict)
        region_ids.append(region.id)
        state_region = session.query(StateRegion) \
            .filter(StateRegion.state_id == state.id) \
            .filter(StateRegion.region_id == region.id) \
            .filter(StateRegion.until_date_time == None) \
            .first()
        if not state_region:
            state_region = StateRegion()
            state_region.state_id = state.id
            state_region.region_id = region.id
            state_region.from_date_time = datetime.now().replace(second=0, minute=0)
            session.add(state_region)
            session.commit()

    saved_state_regions = session.query(StateRegion) \
        .filter(StateRegion.state_id == state.id) \
        .filter(StateRegion.until_date_time == None) \
        .all()
    for saved_state_region in saved_state_regions:
        if saved_state_region.region_id not in region_ids:
            saved_state_region.until_date_time = datetime.now().replace(second=0, minute=0)
    session.commit()
    session.close()

def save_state(session, state_id):
    """Save state to database"""
    state = State()
    state.id = state_id
    state.name = 'UNKNOWN'
    session.add(state)
    session.commit()
    return state

def save_region(session, region_dict):
    """Save region to database"""
    region = Region()
    region.id = region_dict['id']
    region.name = region_dict['name']
    session.add(region)
    session.commit()
    return region
