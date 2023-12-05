# collect email from user
# slice the email using thw @, the first part will be user name, the second part as dormain,
# split domain using ..

def main():
    print("welcome to the email slicer")
    print("")

    email_input = input("input your email address:  ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("username : ", username)
    print("Domain : ", domain)
    print("Extension : ", extension)


while True:
    main()
