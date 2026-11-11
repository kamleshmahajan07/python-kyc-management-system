data = {}

def add_user():

    mobile = input("Enter mobile number: ")

    if len(mobile) != 10:
        print("Invalid mobile number")
        return

    if mobile in data:
        print("User already exists")
        return

    name = input("Enter name: ")

    data[mobile] = {
        "name": name,
        "Paytm": "Pending",
        "PhonePe": "Pending",
        "GooglePay": "Pending"
    }

    print("User added successfully")


def update_kyc():

    mobile = input("Enter mobile number: ")

    if mobile in data:

        platform = input("Enter platform name (Paytm/PhonePe/GooglePay): ")
        status = input("Enter status (Completed/Pending): ")

        data[mobile][platform] = status

        print("KYC updated")

    else:
        print("User not found")


def check_kyc():

    mobile = input("Enter mobile number: ")

    if mobile in data:

        print("\nName:", data[mobile]["name"])
        print("Paytm:", data[mobile]["Paytm"])
        print("PhonePe:", data[mobile]["PhonePe"])
        print("GooglePay:", data[mobile]["GooglePay"])

    else:
        print("User not found")


def delete_user():

    mobile = input("Enter mobile number: ")

    if mobile in data:
        del data[mobile]
        print("User deleted successfully")

    else:
        print("User not found")