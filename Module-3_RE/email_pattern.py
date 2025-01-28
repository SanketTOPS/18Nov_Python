import re

email = input("Enter an email id:")

# sanket1002@gmail.com
email_pattern = "^[a-z0-9]+[@]+[a-z]+[\.]+[a-z]"  # email pattern

x = re.findall(email_pattern, email)
print(x)

if x:
    print("Email address is valid!")
else:
    print("Error!Invalid Email address!")
