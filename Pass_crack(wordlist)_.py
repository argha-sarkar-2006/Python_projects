from PyPDF2 import PdfReader
import os 
import requests
url_1 = "https://gitlab.com/kalilinux/packages/seclists/-/raw/kali/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt?inline=false"
url_2= "https://gitlab.com/kalilinux/packages/seclists/-/raw/kali/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt?inline=false"  
url_3 = "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"
print("intencity 1 : 10000 Combination of Password\nintencity 2 : 1-Million Combination of Password \nintencity 3 : 30-Million Combination of Password\nonly enter the intencity number like 1,2,3")
intencity = int(input("Enter the intencity of the attack : "))
if intencity == 1:
    url = url_1
    print("Intencity 1 Selected")
elif intencity == 2:
    url = url_2
    print("Intencity 2 Selected")
elif intencity == 3:
    url = url_3
    print("Intencity 3 Selected")
try:
    # Use a non-routable IP address to simulate "no network"
    requests.get("https://www.google.com", timeout=3)
    pass
except requests.exceptions.ConnectionError as e:
    print("⚠️ Simulated Offline Error: No Internet Connection")
    print(f"Plese check your network connection. \nError: {e}")
    exit(1)
print("Downloading password list...")
response = requests.get(url)
if response.status_code != 200:
    print("Failed to download the password list.")
    exit(1)
with open("pass_list.txt", "wb") as f:
    f.write(response.content)
print("Download complete!")

password_list_path = "pass_list.txt" 
pdf_path = input("Enter The file Path : ")
if not os.path.isfile(pdf_path):
    print("Please provide a valid PDF file path.")
    exit(1)

def crack_pdf(pdf_path, password_list_path):
    with open(password_list_path, 'r', encoding='utf-8', errors='ignore') as file:
        passwords = [line.strip() for line in file]

    for pwd in passwords:
        try:
            reader = PdfReader(pdf_path)

            if not reader.is_encrypted:
                print("PDF is not encrypted.")
                return None

            result = reader.decrypt(pwd)
            print(f"Trying '{pwd}' \nResult: {result}")

            if result in [1, 2]:
                print(f"[✔] Password found: {pwd}")
                return pwd
            else:
                print(f"Pass Not Matched: {pwd}")

        except Exception as e:
            print(f"Error with '{pwd}': {e}")
            continue

    print("[X] Password not found in list.")
    print("Please Select Higher Intencity")
    return None

crack_pdf(pdf_path, password_list_path)
os.remove(password_list_path)  # Clean up the downloaded password list
