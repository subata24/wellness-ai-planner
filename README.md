# 🧠 AI Wellness & Study Planner

> **A lightweight productivity companion for planning study sessions, tracking daily goals, and reflecting on mood.**

AI Wellness & Study Planner is a **Python and Streamlit-based productivity application** designed to combine study planning with simple wellness and consistency tracking.

Users can log their daily mood, receive study suggestions based on available time, set daily goals, track their consistency streak, and view recent progress — all through a simple interactive interface.

🚀 **[Try the Live Demo](https://wellness-ai-planner-zkvqeehytezreqy452rryg.streamlit.app/)**

---

## ✨ Features

### 😊 Daily Mood Logging

Record your current mood as part of your daily productivity routine.

### 📚 Personalized Study Suggestions

Get study recommendations based on the amount of time available.

### 🎯 Daily Goals

Set and save goals to create a more structured daily routine.

### 🔥 Consistency Streak

Track consecutive days of activity and build consistency over time.

### 💬 Wellness Quotes

Receive rotating motivational and wellness-focused quotes.

### 📊 Recent Progress

View activity and progress from the previous three days.

### 💾 File-Based Persistence

Goals and streak information are stored using a lightweight file-based tracking system, keeping the application simple without requiring a database.

---

## 🧠 How It Works

```text
              👤 User Input
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
     😊 Mood    ⏱️ Time     🎯 Goals
        │          │          │
        │          ▼          │
        │    📚 Study Plan    │
        │          │          │
        └──────────┼──────────┘
                   ▼
            💾 Save Progress
                   │
          ┌────────┴────────┐
          ▼                 ▼
      🔥 Streak        📊 Recent Progress
```

The application combines user input, simple planning logic, and file-based persistence to provide a lightweight daily productivity workflow.

---

## 🛠️ Tech Stack

| Technology                   | Purpose                      |
| ---------------------------- | ---------------------------- |
| 🐍 Python                    | Core application logic       |
| 🎈 Streamlit                 | Interactive web interface    |
| 💾 File-Based Storage        | Goals and streak persistence |
| ☁️ Streamlit Community Cloud | Deployment                   |

---

## 🎯 Use Cases

The planner can be useful for:

* 🎓 **Students** — organize study time around daily schedules
* 📚 **Self-learners** — maintain consistent learning habits
* 🎯 **Goal-oriented users** — keep track of daily objectives
* ⏱️ **Busy learners** — get study suggestions based on available time
* 📊 **Productivity experiments** — explore simple progress and streak tracking

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/subata24/wellness-ai-planner.git
cd wellness-ai-planner
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

> **Note:** The repository currently uses a file-based persistence approach rather than a database. This makes local setup simple but is not intended for multi-user production storage.

---

## 📁 Project Structure

```text
wellness-ai-planner/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🌐 Live Demo

🚀 **[Launch AI Wellness & Study Planner](https://wellness-ai-planner-zkvqeehytezreqy452rryg.streamlit.app/)**

The application is deployed using **Streamlit Community Cloud**.

> The free deployment may sleep after periods of inactivity, so the first request after inactivity may take longer to load.

---

## 💾 Data & Privacy

The current version uses **file-based tracking** rather than a database.

Because this is a publicly deployed demonstration application, users should avoid entering sensitive or personally identifying information.

The project is intended primarily as a **productivity and software-development demonstration**, rather than a professional health or mental-health service.

---

## ⚠️ Limitations

* Study suggestions are based on the application's predefined planning logic and available-time input.
* Mood logging is intended for simple self-reflection and does not provide psychological or medical assessment.
* File-based storage is suitable for a lightweight application but is not ideal for scalable multi-user persistence.
* The current version provides a short recent-progress view rather than long-term analytics.
* The application does not replace professional academic, medical, or mental-health guidance.

---

## 🎯 Project Objective

This project demonstrates how a simple Streamlit application can combine **personalized planning, user input, persistence, and progress tracking** into a practical productivity tool.

The main objectives are to:

* Build an interactive productivity application with Streamlit
* Create personalized study suggestions based on available time
* Implement lightweight file-based persistence
* Track daily goals and consistency
* Present recent progress in an accessible interface
* Deploy the application as a cloud-hosted web app

---

## 👤 Author

**Subata Khan**

GitHub: **[@subata24](https://github.com/subata24)**

---

⭐ **If you find this project useful, consider giving the repository a star!**
