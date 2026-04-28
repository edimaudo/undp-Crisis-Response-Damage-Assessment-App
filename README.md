# Crisis Watch

## Overview
Problem: Crisis response partners need a "ground-truth" signal within the first 48 hours of a disaster to classify building damage and guide rapid intervention.
Objective: A highly user-friendly, open-source tool for communities to submit photos, classify damage (Minimal, Partial, Complete), and geolocate infrastructure (via building footprints) in low-connectivity environments.

## Architecture
- **Backend**: FastAPI (Python) with PostgreSQL database
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

## Features Breakdonw
### Authentication & Authorization
- JWT-based authentication
- Password hashing with bcrypt
- Role-based access control (user/admin)
- First registered user becomes admin
- Session management

### Damage Reporting
- Submit reports with photos
- Automatic image compression (WebP, <1MB)
- Geolocation support
- Damage classification
- Infrastructure/crisis categorization
- Filtering and pagination
- Anonymous submissions

### Analytics & Statistics
- Overview statistics
- Temporal trends
- Geospatial distribution
- Damage severity heatmap
- Comparative analysis
- Predictive insights

### Data Export
- CSV export
- GeoJSON export
- Admin-only access

### Translations
- 6 UN languages: EN, AR, ZH, FR, RU, ES
- JSON-based translation files
- Client-side language switching


## Project Structure

```
Crisis Watch

```



## Setup

### 1. Install Dependencies
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Setup Database
```bash
# Install PostgreSQL first, then:
createdb crisis_watch
```

### 3. Configure Environment
```bash
cp .env.example .env
# Edit .env with your database URL and secret keys
```

### 4. Initialize Database
```bash
python init_db.py
# This creates tables and a default admin user:
# Username: admin
# Password: admin123
# Change this password immediately!
```

### 5. Run Server
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Visit http://localhost:8000


