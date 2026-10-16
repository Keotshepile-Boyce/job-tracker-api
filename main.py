from datetime import date
from enum import Enum

from fastapi import FastAPI, HTTPException
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


class Application(ApplicationCreate):
    id: int


applications: list[Application] = []
next_id = 1


@app.get("/")
def home():
    return {"message": "Job Tracker API is running"}


@app.post("/applications", response_model=Application, status_code=201)
def create_application(data: ApplicationCreate):
    global next_id
    application = Application(id=next_id, **data.model_dump())
    applications.append(application)
    next_id += 1
    return application


@app.get("/applications", response_model=list[Application])
def list_applications():
    return applications


@app.get("/applications/{application_id}", response_model=Application)
def get_application(application_id: int):
    for application in applications:
        if application.id == application_id:
            return application
    raise HTTPException(status_code=404, detail="Application not found")


@app.put("/applications/{application_id}", response_model=Application)
def update_application(application_id: int, data: ApplicationCreate):
    for index, application in enumerate(applications):
        if application.id == application_id:
            updated = Application(id=application_id, **data.model_dump())
            applications[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Application not found")


@app.delete("/applications/{application_id}", status_code=204)
def delete_application(application_id: int):
    for index, application in enumerate(applications):
        if application.id == application_id:
            applications.pop(index)
            return
    raise HTTPException(status_code=404, detail="Application not found")