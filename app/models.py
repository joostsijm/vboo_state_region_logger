"""Database models"""

from sqlalchemy import Column, ForeignKey, Integer, String, \
    SmallInteger, DateTime, BigInteger, Date
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Region(Base):
    """Model for region"""
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class State(Base):
    """Model for state"""
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class StateRegion(Base):
    """Model for state region"""
    __tablename__ = 'state_region'
    state_id = Column(Integer, ForeignKey('state.id'), primary_key=True)
    region_id = Column(Integer, ForeignKey('region.id'), primary_key=True)
    from_date_time = Column(DateTime, primary_key=True)
    until_date_time = Column(DateTime)

    region = relationship(
        'Region',
        backref=backref('state_regions', lazy='dynamic')
    )
    state = relationship(
        'State',
        backref=backref('state_regions', lazy='dynamic')
    )
