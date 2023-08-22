import smtplib

class EmailService:
    def send_email(self, subject: str, body: str, recipient: str) -> bool:
        try:
            with smtplib.SMTP('smtp.example.com', 587) as server:
                server.starttls()
                server.login('user@example.com', 'password')
                message = f"Subject: {subject}\\n\\n{body}"
                server.sendmail('user@example.com', recipient, message)
            return True
        except Exception as e:
            print(f"An error occurred while sending the email: {e}")
            return False
