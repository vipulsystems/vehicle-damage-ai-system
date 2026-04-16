# Backend - Vehicle Damage AI System

## Overview

Flask-based backend for AI-powered vehicle damage detection and cost estimation.

## Tech Stack

* Flask
* PostgreSQL
* YOLOv8
* OpenCV

## Run Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

## API Endpoints

* POST `/api/auth/signup`
* POST `/api/auth/login`
* POST `/api/detect`
* GET `/api/reports`

## Notes

* Uses layered architecture (Routes → Controllers → Services → Repositories)
* AI model stored in `ml_models/`
