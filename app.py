from datetime import datetime, timedelta
import os
import streamlit as st
import random

# ========== UTILITY FUNCTIONS ========== #

def update_streak(name):
    streak_file = f"{name}_streak.txt"
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)

    if not os.path.exists(streak_file):
        with open(streak_file, "w") as f:
            f.write(f"{today}\n1")
        return 1

    with open(streak_file, "r") as f:
        last_date = f.readline().strip()
        streak_count = int(f.readline().strip())

    last_date = datetime.strptime(last_date, "%Y-%m-%d").date()

    if last_date == yesterday:
        streak_count += 1
    elif last_date == today:
        return streak_count  # Already logged today
    else:
        streak_count = 1

    with open(streak_file, "w") as f:
        f.write(f"{today}\n{streak_count}")

    return streak_count

quotes = [
    "You're doing better than you think. 🌈",
    "Even small steps move you forward. 🐾",
    "Today’s effort is tomorrow’s strength. 💥",
    "You showed up — and that matters. 🌟"
]

def suggest_plan(hours):
    hours = int(hours)
    if hours <= 1:
        return "Try a 25-min Pomodoro and 1 quick revision."
    elif hours <= 3:
        return "Plan: 2 Pomodoros, 10-min walk, then review notes."
    else:
        return "Go for 3 focused sessions. Practice + revise + relax."

def mood_response(mood):
    moods = {
        "Sad": "Hugs. Try journaling or a short walk today. 💚",
        "Happy": "That’s amazing! Ride the wave and conquer your goals! ⚡",
        "Anxious": "Breathe in. Breathe out. You are not your thoughts. 🌬️",
        "Other": "No matter what you're feeling, you’re doing your best 💪"
    }
    return moods.get(mood, moods["Other"])

def save_goals(name, goals):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{name}_goals.txt"
    with open(filename, "a") as file:
        file.write(f"\n--- {today} ---\n")
        for i, goal in enumerate(goals, 1):
            file.write(f"Goal {i}: {goal}\n")
        file.write("----------------------\n")

def read_past_goals(name, days=3):
    filename = f"{name}_goals.txt"
    if not os.path.exists(filename):
        return []

    with open(filename, "r") as f:
        content = f.read().strip()

    entries = content.split("---")
    entries = [e.strip() for e in entries if e.strip()]

    goal_entries = []
    for entry in entries:
        lines = entry.splitlines()
        if not lines:
            continue
        date_line = lines[0].strip()
        goals = [line.strip() for line in lines[1:] if line.strip().startswith("Goal")]
        if date_line and goals:
            goal_entries.append((date_line, goals))
    return goal_entries[-days:]

def get_today_goals(name):
    filename = f"{name}_goals.txt"
    if not os.path.exists(filename):
        return []
    today = datetime.now().strftime("%Y-%m-%d")
    with open(filename, "r") as f:
        lines = f.readlines()

    goals = []
    inside_today = False
    for line in lines:
        line = line.strip()
        if line == f"--- {today} ---":
            inside_today = True
            continue
        if inside_today:
            if line.startswith("Goal"):
                goals.append(line)
            elif line.startswith("-"):
                break
    return goals

# ========== APP UI ========== #

st.set_page_config(page_title="AI Wellness & Study Planner", layout="centered")
st.title("🧠 AI Wellness + Study Planner")
st.markdown("Track your mood, plan your day, and grow smarter daily ✨")

name = st.text_input("Enter your name")

if name:
    st.success(f"Welcome, {name}! Let’s check in.")
    streak = update_streak(name)
    st.markdown(f"🔥 **Current Streak: {streak} day(s)**")

    # Show Past Goals
    st.subheader("🕒 Your Last 3 Days of Goals")
    past_goals = read_past_goals(name)
    if past_goals:
        for day, goals_list in past_goals:
            st.markdown(f"**📅 {day}**")
            for goal in goals_list:
                st.markdown(f"- {goal}")
            st.markdown("---")
    else:
        st.info("No past goals found yet. Save some today!")

    # Mood and Study Planning
    mood = st.selectbox("How are you feeling today?", ["Happy", "Sad", "Anxious", "Other"])
    mood_reply = mood_response(mood)
    st.info(mood_reply)

    hours = st.slider("How many hours can you study today?", 0, 10, 2)
    st.write(suggest_plan(hours))

    # Set Goals
    st.subheader("🎯 Set Your Top 3 Goals")
    g1 = st.text_input("Goal 1")
    g2 = st.text_input("Goal 2")
    g3 = st.text_input("Goal 3")
    goals = [g for g in [g1, g2, g3] if g.strip() != ""]

    if st.button("💾 Save My Goals"):
        if goals:
            save_goals(name, goals)
            st.success("Your goals have been saved successfully!")
        else:
            st.warning("Please enter at least one goal.")

    # Quote
    st.subheader("💬 Quote of the Day")
    st.code(random.choice(quotes))

    # Completion Tracker
    st.subheader("✅ Mark Your Completed Goals")
    today_goals = get_today_goals(name)
    completed = []

    if today_goals:
        for goal in today_goals:
            if st.checkbox(goal):
                completed.append(goal)

        if st.button("📌 Save Completed Goals"):
            if completed:
                filename = f"{name}_completed.txt"
                with open(filename, "a") as file:
                    file.write(f"\n--- {datetime.now().strftime('%Y-%m-%d')} ---\n")
                    for goal in completed:
                        file.write(f"{goal}\n")
                    file.write("----------------------\n")
                st.success("Completed goals saved!")
            else:
                st.info("No goals marked.")
    else:
        st.info("You haven’t saved any goals today yet.")

    st.markdown("🧠 End of today’s check-in. Great work!")