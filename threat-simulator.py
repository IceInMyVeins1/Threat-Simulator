import tkinter as tk
from tkinter import messagebox
import string
import time
import threading
    
# Dictionary for dictionary attack simulation
# This is a simple list of common passwords for demonstration purposes.
DICTIONARY = [
    "123456", "password", "123456789", "admin", "12345678",
    "qwerty", "123123", "111111", "12345", "1234",
    "iloveyou", "welcome", "password1", "abc123", "qwerty123",
    "1q2w3e", "1qaz2wsx", "sunshine", "monkey", "letmein",
    "football", "dragon", "master", "hello", "freedom",
    "whatever", "zaq1zaq1", "baseball", "trustno1", "passw0rd",
    "000000", "696969", "superman", "asdfgh", "654321",
    "Password123", "Qwerty@123", "Welcome#123", "Admin@2024",
    "User2023!", "P@ssw0rd", "MyPass123!", "Test@123", 
    "Pass1234", "1234abcd", "Abcd@123", "Login@2023",
    "Aa123456", "Secure#123", "ChangeMe!", "Root@123",
    "Summer2024", "Winter2023", "Hello@World", "India@123"
]

# To check password strength
def password_strength(password):
    score = 0
    if len(password) >= 6:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Moderate"
    else:
        return "Strong"

# Brute Force attack
def brute_force_attack(password):
    charset = string.ascii_letters + string.digits + string.punctuation
    tries = 0
    found = False

    for c1 in charset:
        for c2 in charset:
            for c3 in charset:
                guess = c1 + c2 + c3
                tries += 1
                if guess == password:
                    found = True
                    return guess, tries
    return None, tries

# Dictionary attack
def dictionary_attack(password):
    tries = 0
    for word in DICTIONARY:
        tries += 1
        time.sleep(0.3)
        if word == password:
            return word, tries
    return None, tries

# Start the attack
def start_attack(mode):
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Required", "Please enter a password.")
        return

    strength = password_strength(password)
    strength_label.config(text=f"🔐 Password Strength: {strength}")

    btn_brute.config(state="disabled")
    btn_dict.config(state="disabled")
    status_label.config(text="🔄 Cracking in progress...")

    def attack():
        if mode == "brute":
            result, tries = brute_force_attack(password)
        else:
            result, tries = dictionary_attack(password)

        if result:
            messagebox.showinfo("✅ Success", f"Password '{result}' cracked in {tries} tries!")
        else:
            messagebox.showinfo("❌ Failed", f"Could not crack the password.\nTried {tries} combinations.")

        btn_brute.config(state="normal")
        btn_dict.config(state="normal")
        status_label.config(text="")

    threading.Thread(target=attack).start()

# GUI
window = tk.Tk()
window.title("🔐 Password Security Simulator")
window.geometry("450x300")

title = tk.Label(window, text="Password Cracker Simulator", font=("Arial", 16))
title.pack(pady=10)

entry_label = tk.Label(window, text="Enter a password (short for brute force):")
entry_label.pack()

entry = tk.Entry(window, font=("Courier", 14), justify="center")
entry.pack(pady=5)

strength_label = tk.Label(window, text="🔐 Password Strength: N/A", font=("Arial", 10))
strength_label.pack(pady=5)

btn_brute = tk.Button(window, text="Brute Force Attack", command=lambda: start_attack("brute"), bg="#2196F3", fg="white")
btn_brute.pack(pady=5)

btn_dict = tk.Button(window, text="Dictionary Attack", command=lambda: start_attack("dict"), bg="#9C27B0", fg="white")
btn_dict.pack(pady=5)

status_label = tk.Label(window, text="", fg="blue", font=("Arial", 10))
status_label.pack(pady=10)

window.mainloop()
