#Phone Number information

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

phone_number = phonenumbers.parse(input("Enter your phone number with country code: "))

print("")
service_peovider = (phone_number)

print("This number is from ", geocoder.description_for_number(phone_number,'en'), " and service provider/carrier of this phone number is ", carrier.name_for_number(phone_number,'en'), ".")