import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Mailer:
    def __init__(self):
        self.smtp_server = "sandbox.smtp.mailtrap.io"
        self.smtp_port = 2525
        self.username = "11cde3421967a2"
        self.password = "49a9c6c0152f4b"

    def send_mail(self, subject, recipients, html_body, sender=None):
        # Create the MIME message
        msg = MIMEMultipart("alternative")
        msg['From'] = sender or self.username
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject

        # Attach the HTML version of the email
        msg.attach(MIMEText(html_body, 'html'))

        try:
            # Set up the SMTP server and login
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()  # Secure the connection
            server.login(self.username, self.password)
            
            # Send the email
            server.sendmail(msg['From'], recipients, msg.as_string())
            server.quit()
        except Exception as e:
            print(f"Failed to send email: {e}")
