# Crisis Watch

## Overview
Problem: Crisis response partners need a "ground-truth" signal within the first 48 hours of a disaster to classify building damage and guide rapid intervention.

Objective: A highly user-friendly, open-source tool for communities to submit photos, classify damage (Minimal, Partial, Complete), and geolocate infrastructure (via building footprints) in low-connectivity environments.

## Architecture
- **Backend**: FastAPI (Python) with sqlite database
- **Frontend**: Jinja2 templates + Tailwind CSS + Vanilla JavaScript  
- **Authentication**: JWT-based with role-based access control
- **Image Processing**: Automatic compression and WebP conversion
- **Analytics**: Comprehensive statistics, trends, and predictive insights
- **Translations**: 6 UN languages (EN, AR, ZH, FR, RU, ES)

## Key Features 
- Photo & Data Capture: Input photo, description, and 3-tier damage classification.
- Building Footprint Geolocation: Interactive map overlay allowing users to select specific building footprints or describe locations via landmarks.
- Offline Functionality: "Upload now, send later" queue for low-connectivity settings.
- Multilingual Support: Full support for the 6 official UN languages (AR, ZH, EN, FR, RU, ES) for both UI and user-submitted descriptions.
- Modular Assessment Fields: Ability to toggle additional survey sections (Electricity condition, Health services, Pressing needs) as a crisis evolves.
- Scalable Backend: Designed to handle 500k+ reports per crisis across hundreds of crises annually.
- Structured Export: Data export in standard formats (CSV, GeoJSON, Shapefiles, REST API) for UNDP GIS integration.
- Non-Monetary Incentives: Features to encourage engagement without promoting bad actors or duplicate submissions.

## Project Structure
```
crisis_watch/
├── app/
│   ├── main.py
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   ├── auth.py
│   │   ├── i18n.py
│   │   ├── storage.py
│   │   └── accessibility.py
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── init_db.py
│   ├── models/
│   │   ├── user.py
│   │   ├── report.py
│   │   ├── transaction.py
│   │   ├── reward.py
│   │   └── achievement.py
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── report_service.py
│   │   ├── reward_service.py
│   │   ├── analytics_service.py
│   │   ├── duplicate_service.py
│   │   ├── export_service.py
│   │   ├── predictive_service.py
│   │   ├── image_duplicate_service.py
│   │   ├── gis_service.py
│   │   ├── fulfillment_service.py
│   │   └── ai_classification.py
│   ├── api/routes/
│   │   ├── public.py
│   │   ├── auth.py
│   │   ├── reports.py
│   │   ├── dashboard.py
│   │   ├── export.py
│   │   └── rewards.py
│   ├── templates/
│   │   ├── base.html
|   |   ├── index.html # landing page
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── submit.html
│   │   ├── map.html
│   │   ├── dashboard/admin.html
│   │   ├── dashboard/analytics.html
│   │   └── components/navbar.html
│   ├── static/
│   │   ├── js/app.js
│   │   ├── js/indexeddb.js
│   │   ├── sw.js
│   │   └── css/tailwind.css
├── locale/
├── requirements.txt
├── babel.cfg
└── vercel.json
```





