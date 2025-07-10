import streamlit as st
import os

HISTORY_FILE = "history.txt"

def show_history():
    if not os.path.exists(HISTORY_FILE) or os.stat(HISTORY_FILE).st_size == 0:
        return ["No history found."]
    with open(HISTORY_FILE, "r") as file:
        lines = file.readlines()
    return reversed(lines)

def clear_history():
    open(HISTORY_FILE, "w").close()

def save_history(equation, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{equation} = {result}\n")

def calculate(expression):
    parts = expression.split()
    if len(parts) != 3:
        return "Invalid format. Use: number operator number"

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        return "Invalid numbers"

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            return "Cannot divide by zero"
        result = num1 / num2
    else:
        return "Unsupported operator. Use only +, -, *, /"

    if int(result) == result:
        result = int(result)

    save_history(expression, result)
    return result

# -------------------- STREAMLIT UI --------------------

st.set_page_config(page_title="Simple Calculator", layout="centered")
st.title("🧮 Simple Calculator")

user_input = st.text_input("Enter calculation (e.g., 5 + 3):")

if st.button("Calculate"):
    if user_input:
        output = calculate(user_input)
        st.success(f"Result: {output}")

if st.button("Show History"):
    st.subheader("📜 Calculation History")
    for line in show_history():
        st.text(line.strip())

if st.button("Clear History"):
    clear_history()
    st.warning("History cleared.")
