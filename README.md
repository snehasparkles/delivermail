# Delivermail

`delivermail` is a simple Python utility for sending emails using the SMTP protocol. It supports sending emails with different content types (plain text, HTML, or XML) and to multiple recipients.

## Features

- Send emails via SMTP.
- Support for plain text, HTML, and XML content types.
- Send emails to multiple recipients.
- Easy to use and customizable.

## Installation

Install the package using pip:


pip install delivermail
Usage
Import the package
python
Copy code
from delivermail import delivermail
Send an email
python
Copy code
from delivermail import delivermail

Define email details
sender = "your_email@example.com"
password = "your_password"
recipient = ["recipient1@example.com", "recipient2@example.com"]
message = "Hello, this is a test email!"
subject = "Test Email"
contenttype = "html"  # Options: "plain", "html", "xml"

## Send the email
delivermail(
    sender=sender,
    password=password,
    recipient=recipient,
    message=message,
    subject=subject,
    contenttype=contenttype
)
Parameters
sender: The email address of the sender.
password: The sender's email password.
recipient: A string or list of recipient email addresses.
message: The message content.
subject (optional): The subject of the email.
contenttype (optional): The content type of the email. Supports plain, html, or xml. Defaults to plain.
Requirements
Python 3.6 or later.
Example
Sending a plain text email:


