import random
import mysql.connector
from geopy.distance import geodesic


class Aircraft:
    def __init__(self, name, passenger_capacity, flight_range, price):
        self.name = name
        self.passenger_capacity = passenger_capacity
        self.flight_range = flight_range
        self.price = price


class Player:
    def __init__(self):
        self.funds = 5000
        self.carbon_emissions = 0
        self.aircrafts = [Aircraft("Basic Plane", 50, 500, 0)]
        self.purchased_aircraft_names = ["Basic Plane"]

    def complete_task(self, task, aircraft, tutorial=False):
        distance = task.distance
        failure_reason = ""

        # Calculate the carbon emission
        carbon_emission = calculate_carbon_emission(distance)

        if aircraft.passenger_capacity < task.passengers:
            failure_reason = "Chosen aircraft's passenger capacity is insufficient."
            return False, failure_reason

        if aircraft.flight_range < distance:
            failure_reason = "Chosen aircraft's flight range is insufficient."
            return False, failure_reason

        if tutorial:
            fuel_cost = carbon_emission * 0.02 * distance
            carbon_fee = carbon_emission * distance * 0.04
        else:
            fuel_cost = carbon_emission * 0.04 * distance
            carbon_fee = carbon_emission * distance * 0.08

        total_cost = fuel_cost + carbon_fee

        if (task.offer_price - total_cost) <= 0:
            failure_reason = f"The task is not profitable due to high operational costs. Potential loss: {-total_cost + task.offer_price} coins."
            return False, failure_reason

        self.funds += (task.offer_price - total_cost)
        self.carbon_emissions += carbon_emission
        return True, f"Profit from the task: {task.offer_price - total_cost} coins."

    def buy_aircraft(self, aircraft):
        self.funds -= aircraft.price
        self.aircrafts.append(aircraft)
        self.purchased_aircraft_names.append(aircraft.name)


class Task:
    def __init__(self, start, destination, passengers, offer_price, distance):
        self.start = start
        self.destination = destination
        self.passengers = passengers
        self.offer_price = offer_price
        self.distance = distance


def calculate_carbon_emission(distance):
    """
    Calculate the carbon emission based on the given distance.
    """
    if distance <= 200:
        return distance * 0.275
    elif 200 < distance <= 1000:
        return 55 + 0.105 * (distance - 200)
    else:
        return distance * 0.139


def shop(player_instance):
    while True:
        print("\nAircraft Shop:")
        aircrafts_to_buy = available_aircrafts_to_buy(player_instance)
        display_aircrafts(aircrafts_to_buy)
        print("0. Exit Shop")
        buy_choice = int(input("Choose an aircraft to buy by number (or 0 to exit shop): "))

        if buy_choice == 0:
            break

        selected_aircraft = aircrafts_to_buy[buy_choice - 1]
        if player_instance.funds >= selected_aircraft.price:
            player_instance.buy_aircraft(selected_aircraft)
            print(f"\n{selected_aircraft.name} purchased successfully!")
        else:
            print("\nInsufficient funds!")


# Database functions
def get_database_connection():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='12121122',
        autocommit=True
    )
    return connection


def get_random_airport_from_db():
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT name, latitude_deg, longitude_deg FROM airport WHERE continent = 'EU' ORDER BY RAND() LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    if result:
        return {"name": result[0], "coords": (result[1], result[2])}
    return None


# Task generation function
def generate_task(tutorial=False):
    if tutorial:
        start_airport = {"name": "Berlin", "coords": (52.5200, 13.4050)}
        destination_airport = {"name": "Hamburg", "coords": (53.5511, 9.9937)}
        distance = geodesic(start_airport["coords"], destination_airport["coords"]).kilometers
        fuel_cost = calculate_carbon_emission(distance) * 0.02 * distance
        carbon_fee = calculate_carbon_emission(distance) * distance * 0.04
        total_cost = fuel_cost + carbon_fee
        offer_price = int(total_cost + 500)
        return Task(start_airport["name"], destination_airport["name"], 40, offer_price, distance)

    start_airport = {"name": "Berlin", "coords": (52.5200, 13.4050)}
    destination_airport = get_random_airport_from_db()
    distance = geodesic(start_airport["coords"], destination_airport["coords"]).kilometers
    offer_price = random.randint(int(distance * 10), int(distance * 20))
    passengers = random.randint(10, 150)
    return Task(start_airport["name"], destination_airport["name"], passengers, offer_price, distance)


# Display and purchase functions
def display_aircrafts(aircraft_list):
    for idx, aircraft in enumerate(aircraft_list, 1):
        print(f"{idx}. {aircraft.name} | Capacity: {aircraft.passenger_capacity} | "
              f"Range: {aircraft.flight_range} | Price: {aircraft.price}")


def available_aircrafts_to_buy(player_instance):
    all_aircrafts = [
        Aircraft("Advanced Plane", 100, 1000, 10000),
        Aircraft("Eco Plane", 60, 800, 7000),
        Aircraft("Super Plane", 150, 1500, 15000),
        Aircraft("Ultimate Plane", 200, 2000, 50000)
    ]
    return [aircraft for aircraft in all_aircrafts if aircraft.name not in player_instance.purchased_aircraft_names]


# Main game loop
def game_loop():
    player = Player()
    tutorial_task = generate_task(tutorial=True)
    print("--- Tutorial Task ---")
    print(f"Fly from {tutorial_task.start} to {tutorial_task.destination}.")
    print(f"Distance: {tutorial_task.distance:.2f} km")
    print(f"Carry {tutorial_task.passengers} passengers for an offer of {tutorial_task.offer_price} coins\n")
    display_aircrafts(player.aircrafts)
    aircraft_choice = int(input("Choose an aircraft by number to complete the tutorial task: "))
    selected_aircraft = player.aircrafts[aircraft_choice - 1]
    task_status, reason = player.complete_task(tutorial_task, selected_aircraft, tutorial=True)
    if task_status:
        print(f"\nTutorial task completed using {selected_aircraft.name}!")
    else:
        print(f"\nTutorial task failed with {selected_aircraft.name}! Reason: {reason}")
    input("Press Enter to continue to the main game...")

    # Main Game Loop
    while player.funds < 50000:
        print(f"\nFunds: {player.funds}, Carbon Emissions: {player.carbon_emissions}\n")
        task = generate_task()
        print(f"New task: Fly from {task.start} to {task.destination}.")
        print(f"Distance: {task.distance:.2f} km")
        print(f"Carry {task.passengers} passengers for an offer of {task.offer_price} coins\n")
        display_aircrafts(player.aircrafts)
        aircraft_choice = int(input("Choose an aircraft by number (or 0 to skip task): "))

        if aircraft_choice == 0:
            continue

        # Main Game Loop
        while player.funds < 50000:
            print(f"\nFunds: {player.funds}, Carbon Emissions: {player.carbon_emissions}\n")
            task = generate_task()
            print(f"New task: Fly from {task.start} to {task.destination}.")
            print(f"Distance: {task.distance:.2f} km")
            print(f"Carry {task.passengers} passengers for an offer of {task.offer_price} coins\n")
            display_aircrafts(player.aircrafts)
            aircraft_choice = int(input("Choose an aircraft by number (or 0 to skip task): "))

            if aircraft_choice == 0:
                continue

            selected_aircraft = player.aircrafts[aircraft_choice - 1]
            task_status, reason = player.complete_task(task, selected_aircraft)
            if task_status:
                print(f"\nTask completed using {selected_aircraft.name}! {reason}")
            else:
                print(f"\nTask failed with {selected_aircraft.name}! Reason: {reason}")

            # After task completion, ask player for the next action
            while True:
                next_action = input(
                    "\nDo you want to [N]ext task, [S]hop for aircrafts, [C]heck funds, or [M]ain menu? (N/S/C/M): ").upper()
                if next_action == 'S':
                    shop(player)
                elif next_action == 'C':
                    print(f"\nYour current funds: {player.funds} coins")
                elif next_action == 'M':
                    return  # Return to the main menu
                else:
                    break

        print(
            "\nCongratulations! You've accumulated enough coins to purchase "
            "the Ultimate Aircraft and complete the game!")


def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Start Game")
        print("2. Shop")
        print("3. View Aircraft Hangar")
        print("4. Leaderboard (Feature not implemented)")
        print("5. Exit Game")

        choice = input("Enter your choice: ")

        if choice == '1':
            game_loop()
        elif choice == '2':
            shop(Player())  # Using a dummy player instance for now
        elif choice == '3':
            view_hangar(Player())  # Using a dummy player instance for now
        elif choice == '4':
            # Placeholder for the leaderboard feature
            print("\nFeature not implemented yet!")
        elif choice == '5':
            print("\nThank you for playing!")
            break
        else:
            print("\nInvalid choice! Please choose a valid option.")


def view_hangar(player_instance):
    print("\n--- Your Aircraft Hangar ---")
    display_aircrafts(player_instance.aircrafts)


if __name__ == "__main__":
    main_menu()