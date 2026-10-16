from datetime import date
from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Job Tracker API")


class Status(str, Enum):
    applied = "Applied"
    replied = "Replied"
    interview = "Interview"
    technical_test = "Technical test"
    offer = "Offer"
    rejected = "Rejected"
    no_reply = "No reply"


class ApplicationCreate(BaseModel):
    company: str
    role: str
    link: str | None = None
    source: str
    status: Status = Status.applied
    applied_date: date
    follow_up_date: date | None = None
    notes: str | None = None


@app.get("/")
def home():
    return {"message": "Job Tracker API is running"}


@app.post("/applications")
def create_application(application: ApplicationCreate):
    return application