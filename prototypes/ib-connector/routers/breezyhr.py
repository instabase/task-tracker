import requests
import json

from fastapi import APIRouter
from typing import Dict, Optional, Text
from .models import Position, Candidate

router = APIRouter(
    prefix='/breezyhr',
    tags=['Breezy HR']
)

BASE_URL = 'https://api.breezy.hr/v3/'
TOKEN = 'DUMMY_VALUE'

def _del_none(d: Dict) -> None:
    for key, value in list(d.items()):
        if not value:
            del d[key]
        elif isinstance(value, dict):
            _del_none(value)
    

def _refresh_token() -> None:
    global TOKEN

    url = BASE_URL + 'signin'
    data = dict(
        email='naveen@instabase.com',
        password='Instabase15'
    )
    resp = requests.post(url, data=data)
    resp.raise_for_status()
    resp = resp.json()

    TOKEN = resp['access_token']

def _get(url: Text, params: Dict={}, headers: Dict={}) -> Dict:

    headers.update(dict(
        Authorization=TOKEN
    ))
    resp = requests.get(url=url, params=params, headers=headers)
    if resp.status_code == 401:
        _refresh_token()
        return _get(url, params, headers)

    resp.raise_for_status()

    return resp.json()


def _post(url: Text, data: Dict={}, headers: Dict={}) -> Dict:

    headers.update({
        'Authorization': TOKEN,
        'content-type':'application/json'
    })
    resp = requests.post(url, data=json.dumps(data), headers=headers)
    if resp.status_code == 401:
        _refresh_token()
        return _post(url, data, headers)
    resp.raise_for_status()

    return resp.json()

def _put(url: Text, data: Dict={}, headers: Dict={}) -> Dict:

    headers.update({
        'Authorization': TOKEN,
        'content-type':'application/json'
    })
    resp = requests.put(url, data=json.dumps(data), headers=headers)
    if resp.status_code == 401:
        _refresh_token()
        return _post(url, data, headers)
    resp.raise_for_status()

    return resp.json()



@router.get('/companies')
def get_companies():
    url = BASE_URL + 'companies/'
    resp = _get(url)
    return resp


@router.get('/company/{company_id}')
def get_company(company_id: Text):
    url = BASE_URL + f'company/{company_id}'
    resp = _get(url)
    return resp


# instabase id: 53cbd28cb728
@router.get('/positions/{company_id}')
def get_positions(company_id: Text, position_id: Optional[Text]=None):
    if position_id:
        url = BASE_URL + f'company/{company_id}/position/{position_id}/'
    else:
        url = BASE_URL + f'company/{company_id}/positions/'

    params = dict(
        state='draft' # we won't actually want to publish job postings
    )
    resp = _get(url, params=params)
    return resp


@router.post('/positions/{company_id}')
def create_position(company_id: Text, position: Position):

    url = BASE_URL + f'company/{company_id}/positions'
    data = position.dict()
    _del_none(data)

    resp = _post(url, data=data)
    return resp


@router.get('/candidates/{company_id}/{position_id}')
def get_candidate(company_id: Text, position_id: Text, candidate_id: Optional[Text]=None):
    if candidate_id:
        url = BASE_URL + f'company/{company_id}/position/{position_id}/candidate/{candidate_id}'
    else:
        url = BASE_URL + f'company/{company_id}/position/{position_id}/candidates'
    
    resp = _get(url)
    return resp


@router.post('/candidates/{company_id}/{position_id}')
def create_candidate(company_id: Text, position_id: Text, candidate: Candidate):
    url = BASE_URL + f'company/{company_id}/position/{position_id}/candidates'
    data = candidate.dict()
    _del_none(data)

    resp = _post(url, data=data)
    return resp


@router.put('/candidates/{company_id}/{position_id}/{candidate_id}')
def edit_candidate(company_id: Text, position_id: Text, candidate_id: Text, candidate: Candidate):
    url = BASE_URL + f'company/{company_id}/position/{position_id}/candidate/{candidate_id}'
    data = candidate.dict()
    _del_none(data)

    resp = _put(url, data=data)
    return resp