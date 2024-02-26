from collections import UserDict
import datetime as dt
from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value
    
    def is_valid(self,value):
        return True
        
    def __str__(self):
        return str(self.value)
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self,value):
        if not self.is_valid(value):
            raise ValueError
        else:
            self.__value = value


class Name(Field):
    def if_valid(self,value):
        return bool(value)


class Phone(Field):
    def is_valid(self,value):
        return len(value)==10 and value.isdigit()

        
class Birthsday(Field):        
    def is_valid(self,value):
        try:
            datetime.strptime(value, "%d-%Y-%m")
        except:
            return False
        return True
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self,value):
        if not self.is_valid(value):
            raise ValueError
        else:
            self.__value = datetime.strptime(value, "%d-%Y-%m")
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, value):
        number=Phone(value) 
        if len(value) == 10 and value.isdigit():
            self.phones.append(number)

    def add_birthday(self,birthday:str):
        self.birthday = Birthsday(birthday)

    def remove_phone(self,phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
    
    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                if len(p.value)!=10:
                    raise ValueError("Phone number must be Longer than 10 numbers")
                else:
                    return p                
            else:
                raise ValueError

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p                  

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {str(self.birthday)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name not in self.data:
            raise ValueError
        else:
            return self.data[name]


    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(users=None):
        tdate=datetime.today().date()
        birthdays=[]
        for user in users:
            bdate=user["birthday"] 
            bdate=str(tdate.year)+bdate[4:]
            bdate=datetime.strptime(bdate, "%Y.%m.%d").date()
            week_day=bdate.isoweekday() 
            days_between=(bdate-tdate).days 
            if 0<=days_between<7:
                if week_day<6:
                    birthdays.append({'name':user['name'], 'birthday':bdate.strftime("%Y.%m.%d")}) 
                else:
                    if (bdate+dt.timedelta(days=1)).weekday()==0:
                        birthdays.append({'name':user['name'], 'birthday':(bdate+dt.timedelta(days=1)).strftime("%Y.%m.%d")})
                    elif (bdate+dt.timedelta(days=2)).weekday()==0:
                        birthdays.append({'name':user['name'], 'birthday':(bdate+dt.timedelta(days=2)).strftime("%Y.%m.%d")})
        return birthdays

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

# book = AddressBook()

# # Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")

# # Додавання запису John до адресної книги
# book.add_record(john_record)

# # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

# # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

# # Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# # Видалення запису Jane
# book.delete("Jane")




