# 💸 SpendWise — Smart Expense Tracker

> A full-stack personal finance web application built with Django REST Framework, MySQL, and vanilla JavaScript featuring real OTP email verification.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Django](https://img.shields.io/badge/Django-6.0-green)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🌟 Live Features

| Feature | Description |
|---|---|
| 🔐 Register & Login | Secure account creation with password hashing |
| 📧 Real OTP Email | 6-digit OTP sent to actual Gmail inbox |
| 📊 Dashboard | Live stats — total spent, monthly, daily average |
| ➕ Add Expenses | Category, amount, description, date, notes |
| ✏️ Edit & Delete | Full CRUD on all expenses |
| 📈 Analytics | Category breakdown + monthly trend chart |
| 👤 Profile | Account info and spending stats |
| 🌙 Dark UI | Professional dark theme — feels like a real app |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.0, Django REST Framework |
| Database | MySQL 8.0 |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Authentication | Custom OTP via Gmail SMTP |
| API | RESTful APIs |
| Version Control | Git & GitHub |

---

## 📁 Project Structure


---

## 📸 Screenshots

### Login & OTP Verification
- Beautiful dark themed login page
- Real OTP sent to Gmail inbox
- 6-digit OTP input with auto-focus

### Dashboard
- Total spent, monthly spending, transaction count
- Recent transactions table
- Category breakdown chart

### Analytics
- Category-wise spending bars with percentages
- Monthly trend bar chart

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/register/` | Register new user |
| POST | `/api/auth/login/` | Login user |
| POST | `/api/auth/verify-otp/` | Verify OTP |
| GET | `/api/expenses/` | Get all expenses |
| POST | `/api/expenses/` | Add expense |
| PUT | `/api/expenses/<id>/` | Update expense |
| DELETE | `/api/expenses/<id>/` | Delete expense |
| GET | `/api/analytics/` | Get analytics |
| GET | `/api/profile/<id>/` | Get profile |

---

## 👨‍💻 Developer

**Edupuganti Vamsi Krishna**
- 🎓 B.Tech Computer Science, Parul University (2022–2026)
- 📧 vamsikrishnaedupuganti167@gmail.com
- 🔗 [LinkedIn](https://linkedin.com/in/vamsi-krishna-edupuganti-750966319)
- 💻 [GitHub](https://github.com/Vamsi-57)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
