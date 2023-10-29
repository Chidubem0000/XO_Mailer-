# XO_Mailer-
This Python script is designed to send a styled email using an Office 365 (Outlook.com) email account. The email content is in HTML format and includes an image. Below is a README text to help users understand and use the script:
Prerequisites

Before using this script, make sure you have the following prerequisites in place:

    Python: Ensure you have Python installed on your system.

    Required Libraries: You will need the following Python libraries installed. You can install them using pip:
        smtplib: This library provides functionality to send emails using the Simple Mail Transfer Protocol (SMTP).
        email.mime: These libraries are used for creating and formatting email messages.
        email.header: This library is used for defining email headers.
        email.utils: This library is used for formatting email-related data.

    Office 365 Email Account: You need to have access to an Office 365 email account, and you will need your email address and password.

    Internet Connection: Ensure that your computer has an active internet connection, as the script will send the email through the Office 365 SMTP server.

Usage Instructions

    Clone or download the script to your local machine.

    Open the script in a text editor or integrated development environment (IDE).

    Update the following variables with your email account and email content details:
        sender_email: Replace with your Office 365 email address.
        sender_password: Replace with your email account password.
        recipient_email: Replace with the email address of the recipient.
        sender_name: Replace with your preferred sender name.
        subject: Replace with the subject of the email.
        html_message: Replace with the HTML content of the email. You can customize the HTML content as needed.

    Save your changes and run the script. It will connect to the Office 365 SMTP server, log in to your account, send the email, and then close the connection.

    After running the script, you should see a message indicating that the styled penetration test email was sent successfully.

    Please be aware that this script is for educational and testing purposes only. Ensure that you have the necessary permissions to send emails from the provided email account, and do not use it for any illegal or unethical activities.

Example

Here's an example of how to use the script:

sender_email = "your_office365_email@example.com"
sender_password = "your_password"
recipient_email = "recipient@example.com"
sender_name = "Your Name"
subject = "Your Subject"
html_message = """
<!-- Your HTML email content here -->
"""

# Rest of the script remains unchanged
