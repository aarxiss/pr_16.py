from abc import ABC, abstractmethod

# Абстрактний базовий клас
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Клас для оплати кредитною карткою
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount} USD")

# Клас для оплати через PayPal
class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount} USD")

# Клас для оплати криптовалютою
class CryptoPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing cryptocurrency payment of {amount} USD")

# Функція, яка приймає будь-який тип платежу
def make_payment(payment_method: Payment, amount):
    payment_method.process_payment(amount)

# Приклад використання:
payment1 = CreditCardPayment()
payment2 = PayPalPayment()
payment3 = CryptoPayment()

make_payment(payment1, 100)
make_payment(payment2, 200)
make_payment(payment3, 300)

# Якщо потрібно додати новий тип платежу, наприклад ApplePay:
class ApplePayPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing Apple Pay payment of {amount} USD")

payment4 = ApplePayPayment()
make_payment(payment4, 150)
