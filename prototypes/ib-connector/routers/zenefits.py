import requests

from typing import Dict, Optional, Text
from fastapi import APIRouter

router = APIRouter(
    prefix='/zenefits',
    tags=['Zenefits']
)

BASE_URL = 'https://api.zenefits.com/core/'
TOKEN = 'yoeK58+eRRyiJTgCkN7e'

def _get(url: Text, params: Dict={}, headers: Dict={}) -> requests.Response:
    headers.update(dict(
        Authorization=f'Bearer {TOKEN}'
    ))
    resp = requests.get(url=url, params=params, headers=headers)
    resp.raise_for_status()
    return resp

@router.get('/companies/')
def get_companies(id: Optional[Text]=None) -> Dict:
    url = BASE_URL + 'companies/'
    if id:
        url += id

    resp = _get(url=url)
    return resp.json()

@router.get('/people/')
def get_people(company_id: Optional[Text]=None) -> Dict:

    if company_id:
        # get people for company_id
        url = BASE_URL + f'companies/{company_id}/people'
    else:
        # get all people for the company the access token routerlies to
        url = BASE_URL + 'people'
    resp = _get(url)
    return resp.json()

@router.get('/person/')
def get_person(person_id: Text) -> Dict:
    url = BASE_URL + f'people/{person_id}'
    resp = _get(url)
    return resp.json()

@router.get('/me/')
def get_me() -> Dict:
    url = BASE_URL + 'me/'
    resp = _get(url)
    return resp.json()