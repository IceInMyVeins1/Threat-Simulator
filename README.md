🔐 Password Cracker Simulator (Tkinter GUI)

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

📦 How to Run It
Make sure Python 3 is installed.

Save the script as password_cracker_simulator.py.

Open terminal or command prompt and run:

nginx
Copy
Edit
python password_cracker_simulator.py
A window will open. Type in a password and try cracking it using either method.

🧪 Example Test Passwords
Password	Cracked By
123456	Dictionary attack
a1B	Brute force attack
admin	Dictionary attack
Hello@	Not cracked (too long)

For Brute Force to work, use short passwords (1–3 characters only).

⚠️ Limitations
Brute force attack only supports 3-character passwords

No progress printing in terminal

Not suitable for real cracking — this is just for education

📄 License
This is a fun project for learning purposes only. Do not use it for anything unethical or illegal.

✨ Created by
[Your Name] – exploring basic cybersecurity and password safety using Python and Tkinter.
