import phonenumbers
from phonenumbers import timezone,geocoder,carrier

number = input("enter number : ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone,"ukr")
reg = geocoder.description_for_number(phone,"en")
print(time)
print(phone)
print(car)
print(reg)