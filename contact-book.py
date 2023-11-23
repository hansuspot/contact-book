from os import system

contacts = {}  

def add_contact():
    global contacts
    print("\nAdding a New Contact:")
    name = input("Name: ")
    address = input("Address: ")
    phone = input("Phone number: ")
    email = input("Email address: ")

    details = {'address': address, 'phone': phone, 'email': email}
    contacts[name] = details
    print(f"\nContact '{name}' added successfully! ✅")

def delete_contact():
    global contacts
    if not contacts:
        print("\nYou don't have any contacts saved! Consider adding a few new contacts.")
    else:
        print("\nYour Contacts:")
        for name in contacts:
            print(f'> {name}')

        name_del = input("\nEnter the name of the Contact you want to delete "
                         "[Write 'DEL_ALL' to delete all contacts]: ")

        if name_del == 'DEL_ALL':
            del_choice = input("\nAre you sure you want to delete all contacts? (y/n): ").lower()
            if del_choice == "y":
                contacts.clear()
                print("All contacts deleted successfully! ✅")
            else:
                print("Contacts were not deleted.")
        elif name_del in contacts:
            del contacts[name_del]
            print(f"\nContact '{name_del}' deleted successfully! ✅")
        else:
            print("The contact name entered does not exist.")

def view_details():
    global contacts
    if not contacts:
        print("\nYou don't have any contacts saved! Consider adding a few new contacts.")
    else:
        print("\nYour Contacts:")
        for name in contacts:
            print(f'> {name}')
        name_info = input("\nEnter the name of the contact whose details you wish to view: ")

        if name_info in contacts:
            print(f"\nContact Details for '{name_info}':")
            for key, value in contacts[name_info].items():
                print(f"{key.capitalize()}: {value}")
        else:
            print("The contact name entered does not exist.")

def main_menu():
    print("\n------------ Contact Book ------------")
    print("[1] Add a New Contact")
    print("[2] View Your Contacts")
    print("[3] Delete a Contact")
    print("[Q] Quit")

def contact_book():
    while True:
        system('cls')
        main_menu()
        choice = input("\nEnter your choice (1/2/3/Q): ").upper()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_details()
        elif choice == '3':
            delete_contact()
        elif choice == 'Q':
            print("\nExiting Contact Book. Goodbye!")
            break
        else:
            print("\nInvalid Choice. Please Try Again.")

        if input("\nDo you want to open your Contact Book again? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    contact_book()
