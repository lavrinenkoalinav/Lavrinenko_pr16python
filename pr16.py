from abc import ABC, abstractmethod

# === Завдання 1: SRP (Single Responsibility Principle) ===

class Book:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content

class BookPrinter:
    @staticmethod
    def print_info(book: Book):
        print(f"{book.title} by {book.author}")

class BookUpdater:
    @staticmethod
    def update_content(book: Book, new_content):
        book.content = new_content

class BookSaver:
    @staticmethod
    def save_to_file(book: Book, filename):
        with open(filename, 'w') as f:
            f.write(book.content)

# === Завдання 2: OCP (Open/Closed Principle) ===

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")

class CryptoPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Cryptocurrency")

def process_payment(payment: Payment, amount):
    payment.pay(amount)

# === Завдання 3: ISP і DIP ===

class Notifier(ABC):
    @abstractmethod
    def notify(self, message: str):
        pass

class EmailNotifier(Notifier):
    def notify(self, message: str):
        print(f"Sending EMAIL: {message}")

class SMSNotifier(Notifier):
    def notify(self, message: str):
        print(f"Sending SMS: {message}")

class PushNotifier(Notifier):
    def notify(self, message: str):
        print(f"Sending PUSH notification: {message}")

class NotificationService:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def send(self, message: str):
        self.notifier.notify(message)

# === Демонстрація роботи всіх частин ===

def main():
    # SRP
    book = Book("1984", "George Orwell", "It was a bright cold day in April...")
    BookPrinter.print_info(book)
    BookUpdater.update_content(book, "New content here.")
    BookSaver.save_to_file(book, "book.txt")

    print()

    # OCP
    payment_method = PayPalPayment()
    process_payment(payment_method, 100)

    print()

    # ISP + DIP
    email_service = NotificationService(EmailNotifier())
    email_service.send("Welcome to our platform!")

    sms_service = NotificationService(SMSNotifier())
    sms_service.send("Your verification code is 1234.")

    push_service = NotificationService(PushNotifier())
    push_service.send("You have a new message!")

if __name__ == "__main__":
    main()
