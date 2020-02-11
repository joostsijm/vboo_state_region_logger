"""General functions module"""

import random
import math
import re

from app import LOGGER, database, api


def update_regions(state_id):
    """Update department regions"""
    LOGGER.info('"%s": Run update regions', state_id)
    current_regions = database.get_current_regions(state_id)
    LOGGER.info(
        '"%s": Currently has "%s" regions in database',
        state_id, len(current_regions)
    )
    regions = api.get_regions(state_id)
    LOGGER.info(
        '"%s": Got "%s" regions from API',
        state_id, len(regions)
    )
    database.save_regions(state_id, regions)
    LOGGER.info('"%s": saved regions', state_id)
