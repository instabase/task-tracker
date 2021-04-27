from typing import Dict, List, Optional
from pydantic import BaseModel

class PositionLocation(BaseModel):
    country: str
    state: Optional[str]=None
    city: Optional[str]=None
    is_remote: Optional[bool]=None

class Position(BaseModel):
    name: str
    description: str
    type: str
    location: PositionLocation
    department: Optional[str]=None
    requisition_id: Optional[str]=None
    category: Optional[str]=None
    experience: Optional[str]=None
    education: Optional[str]=None
    custom_attributes: Optional[List[Dict]]=[]
    pipeline_id: Optional[str]=None
    scorecard_id: Optional[str]=None
    questionnaire_id: Optional[str]=None
    tags: Optional[List[str]]=[]


class CandidateWorkHistory(BaseModel):
    company_name: Optional[str]=None
    title: Optional[str]=None
    summary: Optional[str]=None
    start_month: Optional[int]=None
    start_year: Optional[int]=None
    end_month: Optional[int]=None
    end_year: Optional[int]=None

class CandidateEducation(BaseModel):
    school_name: Optional[str]=None
    field_of_study: Optional[str]=None
    start_year: Optional[int]=None
    end_year: Optional[int]=None

class CandidateSocialProfiles(BaseModel):
    facebook: Optional[str]=None
    linkedin: Optional[str]=None
    twitter: Optional[str]=None
    dribbble: Optional[str]=None 
    instagram: Optional[str]=None 
    behance: Optional[str]=None 
    angellist: Optional[str]=None 
    flickr: Optional[str]=None 
    github: Optional[str]=None 
    youtube: Optional[str]=None 
    google_plus: Optional[str]=None  # TODO the API actually requires google-plus, but this name is a python error
    skype: Optional[str]=None 
    globe: Optional[str]=None 

class Candidate(BaseModel):
    name: str
    email_address: Optional[str]=None
    phone_number: Optional[str]=None
    address: Optional[str]=None
    summary: Optional[str]=None
    tags: Optional[List[str]]=None
    headline: Optional[str]=None
    origin: str="sourced"
    source: str="Breezy API"
    work_history: Optional[List[CandidateWorkHistory]]=None
    education: Optional[List[CandidateEducation]]=None
    social_profiles: Optional[CandidateSocialProfiles]=None
    custom_attributes: Optional[List[dict]]=None
    cover_letter: Optional[str]=None

