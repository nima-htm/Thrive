# Thrive - Online appointment reservation system 🏥

A web-based consultation booking system built with Django that enables users to schedule appointments with advisors. The system supports RTL (Right-to-Left) text and is fully localized in Persian.

## ✨ Features

- 👥 User Management
  - Role-based authentication (Admin, Advisor, Patient)
  - Custom user profiles with phone verification
  - Secure login/signup system

 *future plans:
- 📅 Appointment System
  - Book consultations with advisors
  - View and manage upcoming appointments
  - Cancel/reschedule functionality

- 👨‍⚕️ Advisor Portal
  - Professional advisor profiles
  - Availability management
  - Appointment tracking

- 🎨 Modern UI/UX
  - RTL support with Vazir font
  - Responsive Bootstrap 5 design
  - Interactive dashboards
  - Custom styling with Font Awesome icons

## 🔧 Tech Stack

- **Backend**: Django 5.2
- **Frontend**: Bootstrap 5 RTL
- **Database**: PostgreSQL
- **Forms**: django-crispy-forms with Bootstrap 5
- **Authentication**: Custom User Model
- **UI Components**: Font Awesome 6.4.0

## 📁 Project Structure

```
Thrive/
├── accounts/              # User authentication and profiles
├── appointments/          # Appointment management
├── core/                 # Core functionality
├── static/               # Static assets
│   ├── css/             # Custom styles
│   ├── fonts/           # Vazir font files
│   ├── images/          # Image assets
│   └── js/              # JavaScript files
├── templates/            # HTML templates
└── Thrive/              # Project settings
```



## 🙏 Acknowledgments

- [Bootstrap 5 RTL](https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.rtl.min.css)
- [Font Awesome](https://fontawesome.com)
- [Vazir Font](https://github.com/rastikerdar/vazir-font)
