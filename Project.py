import os

script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, "Data")
complaints_dir = os.path.join(data_dir, "complaints")
os.makedirs(complaints_dir, exist_ok=True)

serial_file = os.path.join(data_dir, "serial_counter.txt")
index_file = os.path.join(data_dir, "complaint_index.txt")
resolved_file = os.path.join(data_dir, "resolved_complaints.txt")
print(f"All files will be saved in: {data_dir}")

if not os.path.exists(serial_file):
    with open(serial_file, "w") as f:
        f.write("0")
if not os.path.exists(index_file):
    open(index_file, "a").close()
if not os.path.exists(resolved_file):
    open(resolved_file, "a").close()

def get_next_serial():
    with open(serial_file, "r+") as f:
        serial = int(f.read()) + 1
        f.seek(0)
        f.write(str(serial))
    return serial

def file_append(filename, text):
    with open(filename, "a") as f:
        f.write(text + "\n")

def submit_complaint():
    name = input("Enter your name: ")
    room = input("Enter your room number: ")

    categories = [
        "Food Issues",
        "Water Supply",
        "Electricity Problems",
        "Internet Issues",
        "Room Maintenance",
        "Other Complaints"
    ]

    print("\nComplaint Categories:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")

    cat_choice = int(input("Select a category: "))
    category = categories[cat_choice - 1]

    subcategories = {
        "Food Issues": ["Food Quality", "Meal Timings", "Canteen Staff Behavior", "Other"],
        "Water Supply": ["Drinking Water Problems", "Wash Water Issues", "Other"],
        "Electricity Problems": ["Power Outages", "Voltage Issues", "Other"],
        "Internet Issues": ["No Internet Access", "Slow Internet Speed", "Other"],
        "Room Maintenance": ["Room Cleaning Required", "Bathroom Not Cleaned", "Broken Items", "Other"],
        "Other Complaints": ["User Defined"]
    }

    print("\nSubcategories:")
    for i, sub in enumerate(subcategories[category], 1):
        print(f"{i}. {sub}")

    sub_choice = int(input("Select a subcategory: "))
    subcategory = subcategories[category][sub_choice - 1]
    if subcategory == "Other" or subcategory == "User Defined":
        subcategory = input("Enter your complaint subcategory: ")

    details = input("\nEnter details about your complaint: ")

    
    serial = get_next_serial()
    filename = os.path.join(complaints_dir, f"complaint_{serial}.txt")

    with open(filename, "w") as f:
        f.write(f"Complaint No: {serial}\n")
        f.write(f"Name: {name}\n")
        f.write(f"Room: {room}\n")
        f.write(f"Main Category: {category}\n")
        f.write(f"Sub Category: {subcategory}\n")
        f.write(f"Complaint: {details}\n")

    file_append(index_file, f"{serial} | {name} | Room {room} | {category}")
    print("\nComplaint submitted successfully!")

def admin_login():
    password = input("Enter admin password: ")
    return password == "admin123"

def view_complaints():
    with open(index_file, "r") as f:
        lines = f.readlines()
        if not lines:
            print("\nNo unresolved complaints.")
            return

        print("\nCurrent Complaints:")
        for line in lines:
            print(line.strip())

        serial = input("\nEnter serial number to view details or press Enter to return: ")
        if serial.strip():
            file = os.path.join(complaints_dir, f"complaint_{serial}.txt")
            if os.path.exists(file):
                with open(file, "r") as comp:
                    print("\nComplaint Details:")
                    print(comp.read())
                resolve = input("Mark as resolved? (Y/N): ")
                if resolve.lower() == 'y':
                    resolve_complaint(serial)
            else:
                print("Invalid serial number.")

def resolve_complaint(serial):
    with open(index_file, "r") as f:
        lines = f.readlines()

    new_lines = []
    resolved_line = ""
    for line in lines:
        if line.startswith(f"{serial} "):
            resolved_line = line
        else:
            new_lines.append(line)

    with open(index_file, "w") as f:
        f.writelines(new_lines)

    file_append(resolved_file, resolved_line.strip())
    print("Complaint marked as resolved.")

def view_resolved():
    with open(resolved_file, "r") as f:
        lines = f.readlines()
        if not lines:
            print("\nNo resolved complaints yet.")
        else:
            print("\nResolved Complaints:")
            for line in lines:
                print(line.strip())

def admin_panel():
    if not admin_login():
        print("Incorrect password!")
        return

    while True:
        print("\nAdmin Panel:")
        print("1. View Current Complaints")
        print("2. View Resolved Complaints")
        print("3. Logout")
        choice = input("Select an option: ")

        if choice == "1":
            view_complaints()
        elif choice == "2":
            view_resolved()
        elif choice == "3":
            break
        else:
            print("Invalid option.")

def main():
    while True:
        print("\n============================")
        print("| HOSTEL COMPLAINTS SYSTEM |")
        print("============================")
        print("1. Submit Complaint")
        print("2. Admin Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            submit_complaint()
        elif choice == "2":
            admin_panel()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()