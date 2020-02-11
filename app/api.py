"""API module"""

import re
from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup

from app import BASE_URL, HEADERS

def get_regions(state_id):
    """Download list of regions"""
    regions = []
    not_reached_date = True
    page = 0
    while not_reached_date:
        tmp_regions = download_regions(state_id, page)
        if not tmp_regions:
            not_reached_date = False
            break
        # tmp_regions = read_regions()
        if len(tmp_regions) < 25:
            not_reached_date = False
        regions += tmp_regions
        page += 1
    return regions

def download_regions(state_id, page):
    """Download the region"""
    response = requests.get(
        '{}listed/state/{}/{}'.format(BASE_URL, state_id, page*25),
        headers=HEADERS
    )
    return parse_regions(response.text)

def read_regions():
    """Read from file"""
    with open('regions.html') as file:
        return parse_regions(file)

def parse_regions(html):
    """Parse html return regions"""
    soup = BeautifulSoup(html, 'html.parser')
    regions_tree = soup.find_all(class_='list_link')
    regions = []
    for region_tree in regions_tree:
        columns = region_tree.find_all('td')
        regions.append({
            'id': int(region_tree['user']),
            'name': columns[1].string,
        })
    return regions
