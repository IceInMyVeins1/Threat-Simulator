🔐 Threat Simulator (Tkinter GUI)

This is a beginner-friendly Python project that shows how passwords can be cracked using two basic techniques:

🛠️ Brute Force Attack (up to 3-character passwords)

📘 Dictionary Attack (checks common passwords from a list)

It also checks how strong your password is and shows the result using a simple Tkinter GUI.

🧠 What It Does
Takes a password input from the user

Shows password strength (Weak / Moderate / Strong)

Cracks the password using either:

Dictionary Attack (tries a list of common passwords)

Brute Force Attack (tries every 3-character combination using letters, digits, and symbols)

Tells you how many tries it took (or if it failed)

✅ Features
Easy-to-use GUI with Tkinter

Password strength checker

Dictionary list of 50+ common passwords

Brute force attack using all possible 3-character combinations

Runs attacks in a separate thread (doesn’t freeze the UI)

🧪 Example Test Passwords
Password
123456
a1B	
admin

For Brute Force to work, use short passwords (1–3 characters only).

⚠️ Limitations
Brute force attack only supports 3-character passwords

No progress printing in terminal

Not suitable for real cracking — this is just for education

📄 License
This is a fun project for learning purposes only. Do not use it for anything unethical or illegal.

✨ Created by
Daiwik Puri
