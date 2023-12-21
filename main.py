from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number format")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        new_phone = Phone(phone)
        if new_phone not in self.phones:
            self.phones.append(new_phone)

    def remove_phone(self, phone):
        for p in self.phones:
            if str(p) == phone:
                self.phones.remove(p)


    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def edit_phone(self, old_phone, new_phone):
        phone_index = next((i for i, p in enumerate(self.phones) if str(p) == old_phone), None)
        if phone_index is not None:
            self.phones[phone_index] = Phone(new_phone)
        else:
            raise ValueError(f"Phone {old_phone} not found for contact {self.name.value}")


    def __str__(self):
        phones_str = "; ".join(str(p) for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]