class Person:
    people = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people.append(self)

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age})"

if __name__ == "__main__":
    print("Enter person details. Type 'done' to stop.")

    while True:
        name = input("Enter name: ")

        if name.lower() == "done":
            break
        try:
            age = int(input("Enter age: "))
            person = Person(name, age)
        except ValueError:
            print("Invalid input for age. Please enter a number.")

        print("\nlist of people added: ")
        for person in Person.people:
            print(person)
