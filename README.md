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

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/thrive.git
cd thrive
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:
```env
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

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

## 🔐 Environment Variables

The project uses python-decouple for environment variable management. Required variables:

- `DB_NAME`: PostgreSQL database name
- `DB_USER`: Database user
- `DB_PASSWORD`: Database password
- `DB_HOST`: Database host address

## 👥 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 🙏 Acknowledgments

- [Bootstrap 5 RTL](https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.rtl.min.css)
- [Font Awesome](https://fontawesome.com)
- [Vazir Font](https://github.com/rastikerdar/vazir-font)