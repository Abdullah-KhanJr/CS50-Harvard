class flight:
    def __init__ (self, cap):
        self.cap = cap
        self.pas = []

    def booking(self, name):
        if len(self.pas) < self.cap:
            self.pas.append(name)
            print(f"{name} added to flight successfully.")
        else:
            print(f"Limit Exceeded! Can not add {name}")

f = flight(5)


passengers = ["John", "Harry", "Ron", "Hermonie", "Doe", "Kris"]

for p in passengers:
    f.booking(p)

print("New Commit")

