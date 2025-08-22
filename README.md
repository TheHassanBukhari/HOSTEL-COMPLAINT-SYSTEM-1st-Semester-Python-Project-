# Hostel Complaint System (1st Semester Python Project)

This repository contains my **first semester Python project**: a **Hostel Complaint Management System**. It is a **console-based application** that allows hostel residents to **submit complaints with categories and details**, while administrators can **review, track, and resolve complaints**. The project demonstrates Python fundamentals such as **functions, file handling, and simple data structures**.

---

## Features

* **Submit Complaints**: Students can submit complaints with details like name, room number, category, subcategory, and description.
* **Complaint Categories**: Organized complaint system with categories such as Food, Water, Electricity, Internet, Maintenance, and Others.
* **Automatic Serial Numbers**: Each complaint is assigned a unique serial number.
* **Persistent Storage**: Complaints are stored as text files in a structured `Data/complaints` folder.
* **Admin Panel**: Admin can log in (password protected) to:

  * View unresolved complaints
  * View detailed complaint files
  * Mark complaints as resolved
  * View the list of resolved complaints
* **File-based Tracking**: Uses `complaint_index.txt` for current complaints and `resolved_complaints.txt` for resolved ones.

---

## How to Run

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/Hostel-Complaint-System.git
```

2. **Navigate to the project folder:**

```bash
cd Hostel-Complaint-System
```

3. **Run the program:**

```bash
python Project.py
```

> The program will automatically create a `Data` folder and required text files on the first run.

---

## Learning Outcomes

* Implemented **functions** for modular programming
* Practiced **file handling** for complaint submission and storage
* Learned how to create a **basic admin system** with password protection
* Understood the use of **data persistence** using plain text files
* Built a **menu-driven console application** in Python

---

## Admin Access

* Admin Panel is protected with a password.
* **Default password**: `admin123`

---

## Additional Resources

For a **detailed explanation of the code, logic, and implementation**, visit my blog post:
[Full Blog Post Explanation](https://hassan-codes.blogspot.com/2025/08/hostel-complaint-system-1st-semester.html)

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---
