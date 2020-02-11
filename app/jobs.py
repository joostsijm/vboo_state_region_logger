"""Jobs for scheduler module"""

from app import app


def update_regions(state_id):
    """Update regions"""
    app.update_regions(state_id)
