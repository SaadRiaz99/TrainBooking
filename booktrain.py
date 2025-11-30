import random

class Train:
    def __init__(self, trainname):
        self.trainname = trainname
        self.trainbogie = random.randint(1, 20)
        self.trainno = random.randint(1, 73)

    def book(self, from_place, to_place):
        print(f"The ticket is booked in train {self.trainname} from {from_place} to {to_place} in Coach No {self.trainbogie}")

    def status(self):
        print(f"The train {self.trainname} - Ticket No {self.trainno} and Coach No {self.trainbogie} is running on time")

    def get_fare(self, from_place, to_place):
        fare = random.randint(300, 5550)
        print(f"The fare of Train {self.trainname} from {from_place} to {to_place} is Rs. {fare}")


name = input("Enter The Train Name: ")
jana = input("Enter The Destination You go From: ")
kahahn = input("Enter The Destination you Reached: ")

t = Train(name)
t.book(jana, kahahn)
t.status()
t.get_fare(jana, kahahn)
