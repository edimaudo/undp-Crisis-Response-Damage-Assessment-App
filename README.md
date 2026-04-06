# Crisis Response & Damage Assessment App

## Overview
The Problem: Crisis response partners need a "ground-truth" signal within the first 48 hours of a disaster to classify building damage and guide rapid intervention.
The Objective: A highly user-friendly, open-source tool for communities to submit photos, classify damage (Minimal, Partial, Complete), and geolocate infrastructure (via building footprints) in low-connectivity environments.

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
Crisis Response & Damage Assessment App
├── main.py              # FastAPI entry point & Routing
├── models.py            # PostGIS database models (Infrastructure & Crisis types)
├── schemas.py           # Data validation (Infrastructure, Damage Levels)
├── database.py          # PostgreSQL/PostGIS connection logic
├── crud.py              # Logic for Versioning & Redundancy detection
├── /templates             
│   ├── index.html         # Landing page 
│   ├── report_form.html   # Report damage (Photo, Footprints, Core Questions)
│   ├── community_map.html # Public map with "My Report" highlighting
│   ├── admin_triage.html  # Staffer verification & data update page
│   ├── dashboard.html     # Analytics & GIS Export interface
│   ├── login.html         # UNDP Staffer login
│   └── 404_error.html     # Error page
├── /static               
│   ├── /css              # 
│   ├── /js               # Local storage logic for "Upload Later"
│   ├── /images           # Store UNDP images
│   └── /maps             # Cached building footprint vector tiles
├── /services             
│   ├── translation.py    # Auto-translation for descriptions
│   ├── anonymization.py  # PII/Metadata stripping logic
│   └── export_engine.py  # GeoJSON/Shapefile generation
├── /migrations           # Database versioning (Alembic)
├── docker-compose.yml    # Deployment
└── requirements.txt      # Python dependencies 
```
