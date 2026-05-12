# Company Incident Tracker

A lightweight internal incident management web application built with Flask.

---

# Features

This application allows users to:

- Create incidents
- Upload multiple screenshots
- Track incident severity and status
- Add resolutions and closed dates
- Export incidents to Excel
- Export screenshots into separate Excel sheets
- Store incidents locally in CSV format
- Run locally or deploy to Azure App Service

---

# Incident Management

Users can:

- Create incidents
- Add:
  - Incident title
  - Description
  - Severity
  - Assignee / Name
  - Multiple screenshots
- Close incidents
- Add a resolution/fix description
- Add a manual closed date
- Delete incidents

---

# Severity Levels

Supported severity levels:

- Low
- Medium
- High
- Critical

Each severity has its own:

- Row color
- Badge color
- Excel export styling

---

# Screenshot Uploads

The application supports:

- Multiple image uploads per incident
- PNG
- JPG
- JPEG
- GIF

Uploaded screenshots are stored in:

```text
/uploads
```

Screenshots are:

- Visible in the web application
- Exported to Excel
- Added to separate Excel sheets per incident

---

# Excel Export

The application exports incidents to a fully formatted Excel workbook.

## Main Features

- Styled incident table
- Severity color coding
- Proper date formatting (DD-MM-YYYY)
- Hyperlinks to screenshot sheets
- Embedded screenshots
- Proportional image resizing
- Resolution field
- Closed date field

---

# Excel Structure

## Main Sheet

Contains:

- Incident details
- Severity
- Status
- Resolution
- Closed date
- Hyperlink to image sheet

## Per-Incident Image Sheets

Each incident with screenshots receives its own Excel sheet:

```text
Incident 1
Incident 2
Incident 3
```

These sheets contain:

- Incident title
- Embedded screenshots
- Automatically resized images

---

# Technologies Used

## Backend

- Python
- Flask

## Excel Export

- openpyxl

## Image Handling

- Pillow (PIL)

## Frontend

- Bootstrap 5
- HTML
- CSS
- JavaScript

---

# Folder Structure

```text
Incident Tracker/
├── static/
├── uploads/
├── incident.py
├── incidents.csv
├── incidents.db
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Install Python

Recommended:

- Python 3.10+

Download:

https://www.python.org/downloads/

---

## 2. Install Dependencies

Open PowerShell or Command Prompt:

```powershell
python -m pip install flask openpyxl pillow werkzeug
```

---

# Running the Application

Run:

```powershell
python incident.py
```

Application URL:

```text
http://127.0.0.1:42069
```

---

# Authentication

Viewing incidents requires a password.

Current password:

```python
VIEW_PASSWORD = "mypassword"
```

Recommended for production:

- Move password to environment variables
- Implement user authentication

---

# CSV Storage

Incidents are stored in:

```text
incidents.csv
```

The CSV stores:

| Field | Description |
|---|---|
| ID | Incident ID |
| Title | Incident title |
| Description | Incident description |
| Severity | Severity level |
| Status | Open / Closed |
| DateCreated | Incident creation date |
| Assignee | Assigned person |
| Screenshots | Uploaded image filenames |
| Resolution | Resolution description |
| ClosedDate | Incident closed date |

---

# Supported File Types

Supported screenshot formats:

- PNG
- JPG
- JPEG
- GIF

---

# Styling

The application uses:

- Bootstrap 5
- Custom CSS
- Severity-based row coloring
- Status badges
- Soft enterprise-style UI

---

# Copyright

```text
© 2026 Gerben Rohof — All rights reserved
```

---

# Production Recommendations

For enterprise deployment:

## Recommended Improvements

- Replace CSV with SQLite or PostgreSQL
- Use Azure Blob Storage for screenshots
- Add user authentication
- Add role-based access control
- Add automatic backups
- Add incident comments/history
- Add audit logging
- Add dashboard analytics

---

# Known Limitations

Current limitations:

- CSV storage is not ideal for high concurrency
- No multi-user authentication
- Local uploads folder storage
- No incident edit functionality
- No email notifications

---

# Troubleshooting

## Images not exporting

Install Pillow:

```powershell
python -m pip install pillow
```

---

## Flask app does not start

Check dependencies:

```powershell
python -m pip install flask openpyxl pillow werkzeug
```

---

## Port already in use

Change:

```python
app.run(host="0.0.0.0", port=42069)
```

to another port.

---

# License

MIT License

Copyright (c) 2026 Gerben Rohof
