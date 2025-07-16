❄️ Cold Storage Management System

A Django-based web application for managing cold storage facilities, bookings, and users. This system provides role-based access for admins and users, allowing efficient management of storage, applications, and reporting.

---

🧰 Tech Stack

🐍 Python 3.x

🌐 Django (Backend Framework)

🗄️ SQLite (Default Django Database)

🖥️ HTML5, CSS3, JavaScript (Frontend)

🎨 Bootstrap (UI Styling)

⭐ FontAwesome (Icons)

---

🚀 Features

👤 User Roles:

  🛡️ Admin:
  
    👥 Manage users and storage units
    
    ✅ Approve/reject storage applications
    
    📊 View reports and analytics
    
    🔑 Change admin password
  
  🙋 User:
    
    📝 Register and log in
    
    📦 Apply for storage
    
    🔍 View application status
    
    🔑 Change user password

🛠️ Core Functions:
  
  🏪 Storage management (add, edit, delete, view)
  
  📨 Application processing (apply, approve, reject)
  
  👤 User management (registration, edit, view all users)
  
  📅 Reporting and search by date
  
  🖼️ Gallery and 📬 contact pages

---

🗂️ Project Structure

ColdStorageManagementSystem/

├── ColdStorage/

│   ├── admin.py

│   ├── models.py

│   ├── views.py

│   ├── templates/

│   ├── static/

│   └── ...

├── ColdStorageManagementSystem/

│   ├── settings.py

│   ├── urls.py

│   └── ...

├── manage.py

└── db.sqlite3

ColdStorage/: Main Django app with models, views, templates, and static files.

templates/: HTML templates for all pages (admin, user, gallery, etc).

static/: CSS, JS, images, and icon assets.

---

🎨 Icons & Assets

Icons:
  FontAwesome and custom icons are used throughout the admin and user interfaces.
  Located in ColdStorage/static/admin/fonts/ and ColdStorage/static/assets/fonts/.
  
Images:
  Stored in ColdStorage/static/admin/images/ and ColdStorage/static/assets/images/.

---

⚡ Getting Started

1. Clone the repository:
   git clone https://github.com/kkraddi111/ColdStorageManagementSystem.git
   cd ColdStorageManagementSystem
2. Install dependencies:
   pip install django
3. Apply migrations:
   python manage.py migrate
4. Run the server:
   python manage.py runserver
5. Access the app:
   Open http://127.0.0.1:8000/ in your browser.

---

📄 License

This project is licensed under the MIT License (LICENSE).

---

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change. 
