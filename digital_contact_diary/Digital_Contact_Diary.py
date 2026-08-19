 
 
# ============================================================ 
#              DIGITAL CONTACT DIARY 
# ============================================================ 
 
contacts = {} 
 
 
def add_contact(): 
    name = input("Enter contact name: ").strip() 
 
    if name == "": 
        print("Name cannot be empty!") 
        return 
 
    phone = input("Enter phone number: ").strip() 
    email = input("Enter email: ").strip() 
 
    contacts[name] = { 
        "phone": phone, 
        "email": email 
    } 
 
    print("Contact added successfully!") 
 
 
def view_contacts(): 
    if not contacts: 
        print("No contacts found.") 
        return 
 
    print("\n========== ALL CONTACTS ==========") 
 
    for name, details in contacts.items(): 
        print("Name :", name) 
        print("Phone:", details["phone"]) 
        print("Email:", details["email"]) 
        print("----------------------------------") 
 
 
def search_contact(): 
    name = input("Enter name to search: ").strip() 
 
    if name in contacts: 
        print("\nContact Found!") 
        print("Name :", name) 
        print("Phone:", contacts[name]["phone"]) 
        print("Email:", contacts[name]["email"]) 
    else: 
        print("Contact not found.") 
 
 
def update_contact(): 
    name = input("Enter contact name to update: ").strip() 
 
    if name not in contacts: 
        print("Contact not found.") 
        return 
 
    phone = input("Enter new phone number: ").strip() 
    email = input("Enter new email: ").strip() 
 
    contacts[name]["phone"] = phone 
    contacts[name]["email"] = email 
 
    print("Contact updated successfully!") 
 
 
def delete_contact(): 
    name = input("Enter contact name to delete: ").strip() 
 
    if name in contacts: 
        del contacts[name] 
        print("Contact deleted successfully!") 
    else: 
        print("Contact not found.") 
 
 
def main(): 
    while True: 
 
        print("\n======================================") 
        print("         DIGITAL CONTACT DIARY") 
        print("======================================") 
        print("1. Add Contact") 
        print("2. View Contacts") 
        print("3. Search Contact") 
        print("4. Update Contact") 
        print("5. Delete Contact") 
        print("6. Exit") 
        print("======================================") 
 
        choice = input("Enter your choice (1-6): ").strip() 
 
        if choice == "1": 
            add_contact() 
 
        elif choice == "2": 
            view_contacts() 
 
        elif choice == "3": 
            search_contact() 
 
        elif choice == "4": 
            update_contact() 
 
        elif choice == "5": 
            delete_contact() 
 
        elif choice == "6": 
            print("Thank you for using Digital Contact Diary!") 
            break 
 
        else: 
            print("Invalid choice! Please enter a number from 1 to 6.") 
 
 
# Start the program 
main() 
      
====================================== 
         DIGITAL CONTACT DIARY 
====================================== 
1. Add Contact 
2. View Contacts 
3. Search Contact 
4. Update Contact 
5. Delete Contact 
6. Exit 
====================================== 
Enter your choice (1-6): 1 
Enter contact name: Anand kumar sahu 
Enter phone number: 8810609109 
Enter email: rakshasahu278@gmail.com 
Contact added successfully! 
 
====================================== 
         DIGITAL CONTACT DIARY 
====================================== 
1. Add Contact 
2. View Contacts 
3. Search Contact 
4. Update Contact 
5. Delete Contact 
6. Exit 
====================================== 
Enter your choice (1-6): 7 
Invalid choice! Please enter a number from 1 to 6. 
 
====================================== 
         DIGITAL CONTACT DIARY 
====================================== 
1. Add Contact 
2. View Contacts 
3. Search Contact 
4. Update Contact 
5. Delete Contact 
6. Exit 
====================================== 
Enter your choice (1-6): 6 
Thank you for using Digital Contact Diary! 
