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
MIT License

Copyright (c) 2026 Edupuganti Vamsi Krishna

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This project is open source and available under the [MIT License](LICENSE).
