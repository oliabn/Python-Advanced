""" Task3
·        функція відправлення email з листом подяки.
Протестувати цей функціонал, використовуючи заглушки у місцях надсилання пошти.
Під час штатного запуску програми вона має відправляти повідомлення на вашу реальну
поштову скриньку (необхідно налаштувати SMTP, використовуючи доступи від провайдера
вашого email-сервісу).
"""
"""Function for Sending email"""

import smtplib
from email_password import EMAIL, APP_PASSWORD

MESSAGE = "You have been successfully registered, thank you."
MSG_AND_SUBJ = f'Subject: Registration with Python\n{MESSAGE}'


def send_email(message: str,
               email_of_sender: str,
               password_of_sender: str,
               email_of_receiver: str) -> bool:
    """Send gmail message from sender to receiver.
    Returns True if the letter is successfully sent."""

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(EMAIL, password_of_sender)
        server.sendmail(email_of_sender, email_of_receiver, message)
        return True
    except Exception as ex:
        print(f'Something went wrong. {ex}.')
        return False


# Test
if __name__ == '__main__':
    print(send_email(MSG_AND_SUBJ, EMAIL, APP_PASSWORD, EMAIL))
