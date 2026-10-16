# Job Tracker API

A REST API for tracking job applications: where I applied, what stage
each one is at, and when to follow up.

> Status: planning. Built with Python, FastAPI and SQLite.

## Features (planned)
- Add, view, update and delete job applications
- Filter applications by status
- Summary of how many applications are in each status

## Data model

Table: `applications`

| Field | Type |
|---|---|
| id | integer (auto) |
| company | text |
| role | text |
| link | text (optional) |
| source | text |
| status | text |
| applied_date | date |
| follow_up_date | date (optional) |
| notes | text (optional) |

Status values: Applied, Replied, Interview, Technical test, Offer, Rejected, No reply

## Endpoints

| Method | URL | Description |
|---|---|---|
| POST | /applications | Add an application |
| GET | /applications | List all (optional `?status=Applied`) |
| GET | /applications/{id} | Get one application |
| PUT | /applications/{id} | Update an application |
| DELETE | /applications/{id} | Delete an application |
| GET | /summary | Count of applications per status |

## Tech stack
Python 3, FastAPI, SQLite, pytest