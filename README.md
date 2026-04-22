# 🏥 MediCare — Hospital Management System

A Django-based web application for managing hospital operations including departments, doctors, and patients with role-based access control.

---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Models](#models)
- [User Roles](#user-roles)
- [Getting Started](#getting-started)
- [URL Reference](#url-reference)
- [Template Overview](#template-overview)
- [Recommendations](#recommendations)

---

## ✨ Features

- **Role-Based Access Control** — Admin, Doctor, and Patient roles with different permissions
- **Department Management** — Add, edit, delete, and view departments with their assigned doctors
- **Doctor Management** — Full CRUD for doctors; view their assigned patients
- **Patient Management** — Full CRUD for patients; restrict actions based on user role
- **User Authentication** — Login, logout, and registration for each role type
- **User Profiles** — Profile page with picture, phone number, and address
- **Responsive UI** — Bootstrap 5 sidebar layout with clean, modern design

---

## 🛠 Tech Stack

| Layer      | Technology                        |
|------------|-----------------------------------|
| Backend    | Python 3, Django                  |
| Frontend   | Bootstrap 5, Bootstrap Icons      |
| Database   | SQLite (default, swappable)       |
| Auth       | Django `AbstractUser` (custom)    |
| Media      | Django `ImageField` (Pillow)      |

---

## 📁 Project Structure

```
hospital_management_task/
│
├── doctor_management_task/        # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── myapp/                         # Main application
│   ├── models.py                  # Database models
│   ├── views.py                   # View functions
│   ├── urls.py                    # App URL patterns
│   ├── forms.py                   # Django forms
│   ├── admin.py                   # Admin registration
│   ├── migrations/                # Database migrations
│   │
│   └── templates/
│       ├── master/
│       │   ├── base.html          # Base layout (sidebar + topbar)
│       │   ├── base-form.html     # Reusable form layout
│       │   └── nav.html           # Navigation (legacy)
│       ├── department/
│       │   ├── department_list.html
│       │   └── view_department.html
│       ├── doctor/
│       │   ├── doctor_list.html
│       │   └── view_doctor.html
│       ├── patient/
│       │   ├── patient_list.html
│       │   └── view_patient.html
│       ├── home.html
│       ├── login.html
│       ├── register.html
│       ├── dashboard.html
│       └── profile.html
│
└── media/                         # Uploaded profile images
```

---

## 🗄 Models

### `UserInfoModel` (extends `AbstractUser`)
| Field       | Type         | Notes                          |
|-------------|--------------|--------------------------------|
| `full_name` | CharField    | Max 100 chars, nullable        |
| `address`   | TextField    | nullable                       |
| `user_type` | CharField    | Choices: Admin, Doctor, Patient|

### `ProfileModel`
| Field          | Type         | Notes                          |
|----------------|--------------|--------------------------------|
| `user`         | OneToOneField| Links to `UserInfoModel`       |
| `profile_pic`  | ImageField   | Uploads to `media/`            |
| `phone_number` | CharField    | Max 20 chars                   |

### `DepartmentModel`
| Field         | Type          | Notes               |
|---------------|---------------|---------------------|
| `name`        | CharField     | Max 100 chars       |
| `description` | TextField     | nullable            |
| `created_at`  | DateTimeField | Auto-set on create  |

### `DoctorModel`
| Field            | Type       | Notes                     |
|------------------|------------|---------------------------|
| `name`           | CharField  | Max 120 chars             |
| `email`          | EmailField | Max 120 chars             |
| `phone`          | CharField  | Max 100 chars             |
| `specialization` | CharField  | Max 100 chars             |
| `department`     | ForeignKey | → `DepartmentModel`       |
| `joining_date`   | DateField  | Auto-set on create        |

### `PatientModel`
| Field        | Type       | Notes                 |
|--------------|------------|-----------------------|
| `name`       | CharField  | Max 120 chars         |
| `age`        | IntegerField | nullable            |
| `gender`     | CharField  | Max 120 chars         |
| `disease`    | TextField  | nullable              |
| `doctor`     | ForeignKey | → `DoctorModel`       |
| `admit_date` | DateField  | Auto-set on create    |

---

## 👥 User Roles

| Permission                  | Admin | Doctor | Patient |
|-----------------------------|:-----:|:------:|:-------:|
| View departments            | ✅    | ✅     | ✅      |
| Add / Edit / Delete dept    | ✅    | ❌     | ❌      |
| View doctors                | ✅    | ✅     | ✅      |
| Add / Edit / Delete doctor  | ✅    | ✅     | ❌      |
| View patients               | ✅    | ✅     | ✅      |
| Add / Edit / Delete patient | ✅    | ✅     | ❌      |
| View doctor's patient list  | ✅    | ✅     | ❌      |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/hospital-management.git
cd hospital-management
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install django pillow
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** in your browser.

---

## 🔗 URL Reference

| URL Pattern                      | View                  | Name                  |
|----------------------------------|-----------------------|-----------------------|
| `/`                              | `home`                | `home`                |
| `/dashboard/`                    | `dashboard`           | `dashboard`           |
| `/login/`                        | `login_page`          | `login_page`          |
| `/logout/`                       | `logout_page`         | `logout_page`         |
| `/register/admin/`               | `register_admin`      | `register_admin`      |
| `/register/doctor/`              | `register_doctor`     | `register_doctor`     |
| `/register/patient/`             | `register_patient`    | `register_patient`    |
| `/profile/`                      | `profile`             | `profile`             |
| `/department/`                   | `department_list`     | `department_list`     |
| `/department/add/`               | `add_department`      | `add_department`      |
| `/department/edit/<id>/`         | `edit_department`     | `edit_department`     |
| `/department/delete/<id>/`       | `delete_department`   | `delete_department`   |
| `/department/view/<id>/`         | `view_department`     | `view_department`     |
| `/doctor/`                       | `doctor_list`         | `doctor_list`         |
| `/doctor/add/`                   | `add_doctor`          | `add_doctor`          |
| `/doctor/edit/<id>/`             | `edit_doctor`         | `edit_doctor`         |
| `/doctor/delete/<id>/`           | `delete_doctor`       | `delete_doctor`       |
| `/doctor/view/<id>/`             | `view_doctor`         | `view_doctor`         |
| `/patient/`                      | `patient_list`        | `patient_list`        |
| `/patient/add/`                  | `add_patient`         | `add_patient`         |
| `/patient/edit/<id>/`            | `edit_patient`        | `edit_patient`        |
| `/patient/delete/<id>/`          | `delete_patient`      | `delete_patient`      |
| `/patient/view/<id>/`            | `view_patient`        | `view_patient`        |

---

## 🖼 Template Overview

| Template                          | Description                                      |
|-----------------------------------|--------------------------------------------------|
| `master/base.html`                | Main layout: sidebar, topbar, flash messages     |
| `master/base-form.html`           | Reusable form page with styled inputs            |
| `home.html`                       | Landing page with login / register links         |
| `login.html`                      | Standalone login page                            |
| `register.html`                   | Standalone registration page (all roles)         |
| `dashboard.html`                  | Post-login dashboard with stat cards             |
| `profile.html`                    | User profile with picture and contact info       |
| `department/department_list.html` | Table of all departments                         |
| `department/view_department.html` | Department detail + its doctors table            |
| `doctor/doctor_list.html`         | Table of all doctors                             |
| `doctor/view_doctor.html`         | Doctor detail + assigned patients table          |
| `patient/patient_list.html`       | Table of all patients                            |
| `patient/view_patient.html`       | Patient detail card                              |

---

## ⚠️ Recommendations


### Security Recommendations

5. **No CSRF protection on delete** — DELETE actions are triggered via simple `<a>` links (GET requests). Use POST forms or at minimum a JavaScript `confirm()` prompt (already added in improved templates).

6. **`DEBUG = True` in production** — Make sure to set `DEBUG = False` and configure `ALLOWED_HOSTS` before deploying.

7. **SECRET_KEY exposure** — Move `SECRET_KEY` to an environment variable using `python-decouple` or `django-environ`.

   ```bash
   pip install python-decouple
   ```

   ```python
   # settings.py
   from decouple import config
   SECRET_KEY = config('SECRET_KEY')
   ```

### Code Quality Recommendations

8. **Use `{% empty %}` in for loops** — Instead of checking `{% if form_data %}` outside the loop, use Django's built-in `{% empty %}` tag for cleaner templates.

9. **Filter doctors in view, not template** — In `view_department.html` and `view_doctor.html`, filtering (`{% if x.department == form_data %}`) happens in the template. Move this to the view:
   ```python
   # views.py
   def view_department(request, d_id):
       department = DepartmentModel.objects.get(id=d_id)
       doctors = DoctorModel.objects.filter(department=department)
       ...
   ```

10. **Use `get_object_or_404`** — Replace `Model.objects.get(id=...)` with `get_object_or_404(Model, id=...)` to return proper 404 responses instead of unhandled exceptions.

    ```python
    from django.shortcuts import get_object_or_404
    department = get_object_or_404(DepartmentModel, id=d_id)
    ```

11. **Bootstrap version mismatch** — Original templates mixed Bootstrap 4 classes with Bootstrap 5 CDN in some places. Standardize on Bootstrap 5 throughout.

12. **`nav.html` is redundant** — Navigation is now handled inside `base.html` sidebar. The separate `nav.html` include can be removed.

13. **Add `requirements.txt`** — Create a `requirements.txt` for easier setup:
    ```
    Django>=4.2
    Pillow>=10.0
    ```
    Generate with: `pip freeze > requirements.txt`

---

## 📄 License

This project was created as a learning exercise. Feel free to use and modify it for your own projects.
