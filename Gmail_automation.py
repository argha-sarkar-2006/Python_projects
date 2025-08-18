import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path="secrets.env")
import os
def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')
clear_screen()
print("***********************************************\n*                                             *")
print("********* Welcome To Mail Automation **********")
print("*                                             *\n***********************************************\n")
# ---- CONFIGURE THIS ----
sender_email = "Your Email"  # Replace with your email
sender_password = "generate app password"  # Replace with your app password
receiver_email = "reciver mail"
subject = "This is a Automated Email"
receiver_name = "sender_name"  # Replace with the actual receiver's name
# -------------------------
print("Check your email for the automation result.\n")
print("Sending email to:", receiver_email)
print("Subject:", subject)
print("Receiver Name:", receiver_name)
user = input("\nPress Y to continue or any other key to exit.: ").strip().lower()
if user == 'y':
    print("Continuing with email sending...")
else:
    print("Exiting the program.")
    exit()
# Load HTML Template
with open("test_temp.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Replace placeholders like {{name}}
html_content = html_content.replace("{{name}}", receiver_name)

# Create the email message
msg = MIMEMultipart("alternative")
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject

# Attach the HTML content
msg.attach(MIMEText(html_content, "html"))

# Send the email
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print("✅ Email sent successfully! to ", receiver_email)
except Exception as e:
    print("❌ Failed to send email:", e)
print("Exiting the program.\nThanks For using The programme")