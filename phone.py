import phonenumbers
from phonenumbers import carrier

mobileno = input("Enter mobile number with country code: ")
service_p = phonenumbers.parse(mobileno)
print(carrier.name_for_number(service_p, "en"))