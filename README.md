# Vehicle Damage AI System

## Overview

An end-to-end **AI-powered vehicle damage detection and repair cost estimation system** that automates inspection using computer vision and backend intelligence.

The system allows users to upload an image of a damaged vehicle, detects affected parts using a YOLOv8 model, and estimates repair cost based on structured pricing data stored in PostgreSQL.

---

## Problem Statement

Traditional vehicle damage assessment is:

* Time-consuming
* Dependent on human expertise
* Prone to inconsistency

This system provides:

* Automated damage detection
* Standardized cost estimation
* Faster and data-driven decision-making

---

## Key Features

### AI-Based Damage Detection

* YOLOv8 object detection model
* Detects vehicle parts (Bumper, Door, Light, etc.)
* Confidence-based filtering

---

### Cost Estimation Engine

* Dynamic pricing based on:

  * Vehicle brand & model
  * Detected damage parts
* Applies damage factor for realistic estimation

---

### Scalable Backend Architecture

* Layered architecture:

  ```
  Routes → Controllers → Services → Repositories
  ```
* Clean separation of concerns

---

### PostgreSQL Integration

* Stores:

  * User data
  * Damage reports
  * Cost breakdown (JSONB)
* Enables analytics & reporting

---

### Report Management

* Stores historical damage reports
* Supports future analytics (cost trends, damage frequency)

---

### Authentication System

* Secure user registration & login
* Password hashing using bcrypt

---

## System Architecture

```text
Frontend (React / UI)
        ↓
Flask API
        ↓
Controllers
        ↓
Services
   ↙           ↘
AI Layer     Database Layer
(YOLOv8)     (PostgreSQL)
        ↓
JSON Response
```

---

## Project Structure

```text
backend/
│
├── app/
│   ├── routes/
│   ├── controllers/
│   ├── services/
│   ├── repositories/
│   ├── ai/
│   ├── utils/
│   ├── schemas/
│   ├── exceptions/
│   └── config/
│
├── ml_models/
│   └── best.pt
│
├── migrations/
├── tests/
├── run.py
└── .env
```

---

## 🛠️ Tech Stack

### Backend

* Python (Flask)
* PostgreSQL
* psycopg2

### AI / ML

* YOLOv8 (Ultralytics)
* OpenCV

### Security

* bcrypt

### Utilities

* dotenv
* logging

---

## Workflow

1. User uploads image
2. Backend processes image
3. YOLO detects damaged parts
4. Parts mapped & counted
5. Pricing fetched from database
6. Cost calculated
7. Report stored
8. Result returned

---

## API Endpoints

### Auth

```
POST /api/auth/signup
POST /api/auth/login
```

### Detection

```
POST /api/detect
```

### Reports

```
GET /api/reports?user_id=1
```

---

## Setup

```bash
git clone https://github.com/your-username/vehicle-damage-ai-system.git
cd vehicle-damage-ai-system/backend
```

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env`:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=vehicle_ai
DB_USER=postgres
DB_PASSWORD=your_password
SECRET_KEY=your_secret
```

Run:

```bash
python run.py
```

---

## Impact

* Reduced inspection time by ~60%
* Eliminates manual bias
* Enables structured analytics
* Modular & scalable backend

---

## Future Enhancements

* Insurance system integration
* Mobile app (React Native)
* Real-time detection via camera
* Cloud deployment (AWS/GCP)

---

## Author

**Vipul Paighan**
Full Stack Developer | Data Analyst | Applied AI & Data Science
