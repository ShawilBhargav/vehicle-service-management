from database import connect, setup_database

setup_database()

def add_customer():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    vehicle = input("Enter vehicle type: ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO customers (name, phone, vehicle_type) VALUES (?, ?, ?)",
        (name, phone, vehicle)
    )

    conn.commit()
    conn.close()
    print("Customer added successfully!")

def add_mechanic():
    name = input("Enter name: ")
    spec = input("Enter specialization: ")
    phone = input("Enter phone: ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO mechanics (name, specialization, phone) VALUES (?, ?, ?)",
        (name, spec, phone)
    )

    conn.commit()
    conn.close()
    print("Mechanic added successfully!")

def create_service():
    customer_id = input("Customer ID: ")
    mechanic_id = input("Mechanic ID: ")
    issue = input("Describe issue: ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO services (customer_id, mechanic_id, issue) VALUES (?, ?, ?)",
        (customer_id, mechanic_id, issue)
    )

    conn.commit()
    conn.close()
    print("Service request created!")

def view_services():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.id, c.name, m.name, s.issue, s.status, s.date
        FROM services s
        JOIN customers c ON s.customer_id = c.id
        JOIN mechanics m ON s.mechanic_id = m.id
    """)

    rows = cursor.fetchall()

    print("\n--- Services ---")
    for row in rows:
        print(f"ID: {row[0]}, Customer: {row[1]}, Mechanic: {row[2]}, Issue: {row[3]}, Status: {row[4]}, Date: {row[5]}")

    conn.close()

def view_customers():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()

    print("\n--- Customers ---")
    for row in rows:
        print(row)

    conn.close()


def view_mechanics():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM mechanics")
    rows = cursor.fetchall()

    print("\n--- Mechanics ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Spec: {row[2]}, Phone: {row[3]}")

    conn.close()
    
def update_status():
    service_id = input("Service ID: ")
    status = input("New status (Pending/Completed): ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE services SET status=? WHERE id=?",
        (status, service_id)
    )

    conn.commit()
    conn.close()
    print("Status updated!")

while True:
    print("\n--- Vehicle Service System ---")
    print("1. Add Customer")
    print("2. Add Mechanic")
    print("3. Create Service Request")
    print("4. View Services")
    print("5. Update Status")
    print("6. View Customers")
    print("7. View Mechanics")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_customer()
    elif choice == "2":
        add_mechanic()
    elif choice == "3":
        create_service()
    elif choice == "4":
        view_services()
    elif choice == "5":
        update_status()
    elif choice == "6":
        view_customers()
    elif choice == "7":
        view_mechanics()
    elif choice == "8":
        break
    else:
        print("Invalid Option!")