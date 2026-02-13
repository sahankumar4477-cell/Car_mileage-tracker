import json
import os

DATA_FILE = "car_data.json"

# Load data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    else:
        return {"fuel_entries": [], "services": []}

# Save data
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add fuel entry
def add_fuel(data):
    try:
        odometer = float(input("Enter current odometer reading (km): "))
        litres = float(input("Enter litres filled: "))
        price_per_litre = float(input("Enter price per litre: "))

        entry = {
            "odometer": odometer,
            "litres": litres,
            "price_per_litre": price_per_litre
        }

        data["fuel_entries"].append(entry)
        save_data(data)
        print("✅ Fuel entry added successfully!")

    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")

# Calculate mileage
def calculate_mileage(data):
    entries = data["fuel_entries"]

    if len(entries) < 2:
        print("⚠ Not enough data to calculate mileage.")
        return

    last = entries[-1]
    previous = entries[-2]

    distance = last["odometer"] - previous["odometer"]
    mileage = distance / last["litres"]

    print(f"🚗 Mileage: {mileage:.2f} km/l")

# Add service record
def add_service(data):
    try:
        service_type = input("Enter service type: ")
        cost = float(input("Enter service cost: "))

        service = {
            "type": service_type,
            "cost": cost
        }

        data["services"].append(service)
        save_data(data)
        print("✅ Service record added!")

    except ValueError:
        print("❌ Invalid cost entered.")

# View summary
def view_summary(data):
    total_fuel_cost = sum(entry["litres"] * entry["price_per_litre"] for entry in data["fuel_entries"])
    total_service_cost = sum(service["cost"] for service in data["services"])

    print("\n📊 SUMMARY")
    print(f"Total fuel cost: ₹{total_fuel_cost:.2f}")
    print(f"Total service cost: ₹{total_service_cost:.2f}")
    print(f"Total fuel entries: {len(data['fuel_entries'])}")
    print(f"Total services: {len(data['services'])}")

# Main menu
def main():
    data = load_data()

    while True:
        print("\n--- 🚗 Car Tracker Menu ---")
        print("1. Add Fuel Entry")
        print("2. Calculate Mileage")
        print("3. Add Service Record")
        print("4. View Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_fuel(data)
        elif choice == "2":
            calculate_mileage(data)
        elif choice == "3":
            add_service(data)
        elif choice == "4":
            view_summary(data)
        elif choice == "5":
            print("👋 Exiting... Drive safe!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
