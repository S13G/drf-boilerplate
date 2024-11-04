import threading
from django.core.mail import send_mail
from django.conf import settings


class EmailThread(threading.Thread):
    """A class to send emails in a separate thread."""

    def __init__(self, subject, message, recipient_list):
        super().__init__()
        self.subject = subject
        self.message = message
        self.recipient_list = recipient_list

    def run(self):
        """Override the run method to send the email."""
        send_mail(
            self.subject, self.message, settings.DEFAULT_FROM_EMAIL, self.recipient_list
        )


def send_email(subject, message, recipient_list):
    """Function to start the email thread."""
    email_thread = EmailThread(subject, message, recipient_list)
    email_thread.start()
