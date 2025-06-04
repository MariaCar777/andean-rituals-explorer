import json

# Load the rituals
with open('rituals.json') as file:
    rituals = json.load(file)

def list_all():
    for r in rituals:
        print(f"\n🪶 {r['name']}")
        print(f"  Country: {r['country']}")
        print(f"  Region: {r['region']}")
        print(f"  Month: {r['month']}")
        print(f"  Purpose: {r['purpose']}")
        print(f"  Description: {r['description']}")

def search_by_country(country_name):
    print(f"\nRituals in {country_name.title()}:\n")
    for r in rituals:
        if r['country'].lower() == country_name.lower():
            print(f"- {r['name']} ({r['region']})")

def search_by_month(month):
    print(f"\nRituals in {month.title()}:\n")
    for r in rituals:
        if r['month'].lower() == month.lower():
            print(f"- {r['name']} ({r['country']})")

# Menu
while True:
    print("\n✨ Andean Ritual Explorer ✨")
    print("1. View all rituals")
    print("2. Search by country")
    print("3. Search by month")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        list_all()
    elif choice == '2':
        search_by_country(input("Enter country: "))
    elif choice == '3':
        search_by_month(input("Enter month: "))
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
