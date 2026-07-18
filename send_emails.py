import csv
import smtplib
from email.message import EmailMessage

def main():
    emails_list = get_recipients("emails.csv")
    for r in emails_list:
        print(r)

    print()

    credentials = get_credentials("credentials.txt")
    print(credentials)

    for row in emails_list:
        msg = build_message(credentials["email"], row, "Send Emails from CSV File mini project", "this is a test message")
        print(msg)


def get_recipients(filename):
    emails_list = []
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            emails_list.append(row["email"])
    return emails_list

def get_credentials(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        credentials = {"email" : lines[0].strip(), "password" : lines[1].strip()}
    return credentials


def build_message(sender, recipient, subject, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    msg.set_content(body)
    return msg
    

if __name__ == "__main__":
    main() 