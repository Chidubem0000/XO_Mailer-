import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formatdate

# Email account details
sender_email = "nancya713@hotmail.com"
sender_password = "Maxie0713"

# Recipient email
recipient_email = "lisamariestreet@hotmail.com"

# Sender name
sender_name = "Nancy Smith"

# Email content
subject = "Styled Penetration Test Email"
html_message = """
<HTML>
<HEAD>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<META name="viewport" content="width=device-width, initial-scale=1">
<META name="format-detection" content="telephone=no">
<title></title>
</HEAD>
<BODY>
<P align="left"><FONT size=3 face=Arial><A href="https://docs.google.com/presentation/d/e/2PACX-1vT7h_yZfYoXe2AtvgUf7KTydjmfCqpGtb8ojlbmph5CI_BFD5uCHJ7jpPq3hsSloBuqgDVr-kylGM2_/pub?start=false&amp;loop=false&amp;delayms=3000&amp;pli=1#slide=id.p"><IMG border=0 alt="" src="https://example.com/path/to/your/image.png"></A></FONT></P>
</BODY>
</HTML>

"""

# Create and configure the email
msg = MIMEMultipart('alternative')
msg['From'] = f'{sender_name} <{sender_email}>'
msg['To'] = recipient_email
msg['Subject'] = subject
msg['Date'] = formatdate(localtime=True)

# Attach HTML content
msg.attach(MIMEText(html_message, 'html'))

# Establish a connection to an SMTP server
smtp_server = smtplib.SMTP('smtp.office365.com', 587)
smtp_server.starttls()

# Login to your Outlook.com (Office 365) account
smtp_server.login(sender_email, sender_password)

# Send the email
smtp_server.sendmail(sender_email, recipient_email, msg.as_string())

# Close the connection
smtp_server.quit()

print("Styled penetration test email sent successfully.")
