import pandas
from abc import ABC, abstractmethod

df = pandas.read_csv("hotels.csv", dtype={"id": str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_card_security = pandas.read_csv("card_security.csv", dtype=str)

class Hotel:
    watermark = "The Real Estate Company"

    def __init__(self, hotel_id): # Instance Method
        self.hotel_id = hotel_id # Instance Variables
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False

class Spa(Hotel):
    def book_spa_package(self):
        pass


class Ticket(ABC):

    @abstractmethod # Defining a rule that all classes should inherit
    def generate(self):
        pass


class SpaTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here is your Spa booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content

class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here is your booking data:
        Name: {self.the_customer_name}
        Hotel name: {self.hotel.name}
        """
        return content

    @property # Don't need to add () to instance method call, behaves like a variable
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(amount):
        return amount * 1.2

hotel1 = Hotel(hotel_id="188")
hotel2 = Hotel(hotel_id="134")

ticket = ReservationTicket(customer_name="john smith", hotel_object=hotel1)
print(ticket.the_customer_name)
print(ticket.generate())

converted = ReservationTicket.convert(10)
print(converted)