from abc import ABC, abstractmethod

# Інтерфейс оповіщення (ISP)
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

# Конкретні реалізації (Email, SMS, Push)
class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending Email: {message}")

class SMSNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending SMS: {message}")

class PushNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending Push Notification: {message}")

# Клас, який використовує абстракцію (DIP)
class NotificationService:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier
    
    def notify(self, message: str):
        self.notifier.send(message)

# Приклад використання:
email_service = NotificationService(EmailNotifier())
sms_service = NotificationService(SMSNotifier())
push_service = NotificationService(PushNotifier())

email_service.notify("Hello via Email!")
sms_service.notify("Hello via SMS!")
push_service.notify("Hello via Push!")

# Додати новий тип повідомлення (наприклад TelegramNotifier)
class TelegramNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending Telegram message: {message}")

telegram_service = NotificationService(TelegramNotifier())
telegram_service.notify("Hello via Telegram!")
