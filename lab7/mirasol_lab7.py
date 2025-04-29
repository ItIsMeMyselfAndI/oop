'''
Instructions:
    Create a simple Vehicle Rental System where people can rent different types of vehicles (Car, Bike, Truck).
    •	Create an abstract class Vehicle with:
        o	Abstract methods: calculate_rental_cost(hours) and get_vehicle_type().
    •	Concrete classes like Car, Bike, and Truck must implement these methods.
    •	Each vehicle type has different rental cost rules (e.g., trucks are more expensive than bikes).
    •	Add a RentalService class that can:
        o	List available vehicles.
        o	Calculate the total rental cost for selected vehicles.
        o	Include discounts for rentals over a certain number of hours.
'''
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @staticmethod
    @abstractmethod
    def get_vehicle_type() -> str:
        pass

    @staticmethod
    @abstractmethod
    def get_pesos_per_hour() -> float:
        pass

    @staticmethod
    @abstractmethod
    def calculate_rental_cost(hours:float) -> float:
        pass
    

class Bike(Vehicle):
    @staticmethod
    def get_vehicle_type() -> str:
        return "Bike"
    
    @staticmethod
    def get_pesos_per_hour() -> float:
        return 75.00

    @staticmethod
    def calculate_rental_cost(hours:float) -> float:
        return hours * Bike.get_pesos_per_hour()
    

class Car(Vehicle):
    @staticmethod
    def get_vehicle_type() -> str:
        return "Car"
    
    @staticmethod
    def get_pesos_per_hour() -> float:
        return 250.00

    @staticmethod
    def calculate_rental_cost(hours:float) -> float:
        return hours * Car.get_pesos_per_hour()
    

class Truck(Vehicle):
    @staticmethod
    def get_vehicle_type() -> str:
        return "Truck"
    
    @staticmethod
    def get_pesos_per_hour() -> float:
        return 450.00
    
    @staticmethod
    def calculate_rental_cost(hours:float) -> float:
        return hours * Truck.get_pesos_per_hour()
    

class RentalService:
    def __init__(self, vehicles:list):
        self.vehicles = vehicles
        self.DISCOUNT_SMALLEST_HOURS = 5
        self.DISCOUNT_RATE = 0.1 # 10%

    def list_available_vehicles(self) -> None:
        print("="*100)
        print(f"{'ID':>10}{'Vehicle Type':>30}{'Pesos/Hour':>30}")
        print("="*100)
        for i, vehicle in enumerate(self.vehicles):
            print(
                f"{i:>10}{vehicle.get_vehicle_type():>30}{vehicle.get_pesos_per_hour():>30}"
            )
        print("="*100)

    def _getValidNumberOfVehiclesToRent(self) -> int:
        while True:
            try:
                num_of_vehicles = int(input(f"How many vehicle will you rent: "))
            except ValueError:
                print("\t[!] Only enter positive whole number")
                continue
            if num_of_vehicles <= 0:
                print("\t[!] Only enter positive whole number")
                continue
            return num_of_vehicles

    def _getValidVehicleID(self, i:int, length:int) -> int:
        while True:
            vehicle_id = input(f"#{i} Enter vehicle ID to rent ({0}-{length-1}): ")
            if vehicle_id not in [str(j) for j in range(length)]:
                print(f"\t[!] Only choose from {0} to {length-1}")
                continue
            return int(vehicle_id)
        
    def _getValidRentalHours(self) -> float:
        while True:
            try:
                hours = float(input(f"\tEnter rental hours: "))
            except ValueError:
                print("\t[!] Only enter positive whole number")
                continue
            if hours <= 0:
                print("\t[!] Only enter positive whole number")
                continue
            return hours

    def getRentedVehicles(self) -> list:
        rented_vehicles = []
        length = len(self.vehicles)
        num_of_vehicles = self._getValidNumberOfVehiclesToRent()
        for i in range(num_of_vehicles):
            print("="*100)
            vehicle_id = self._getValidVehicleID(i, length)
            hours = self._getValidRentalHours()
            rented_vehicles.append({
                "id":vehicle_id, "type":self.vehicles[vehicle_id].get_vehicle_type(), "hours":hours
            })
        return rented_vehicles 

    def calculate_total_rental_cost(self, rented_vehicles:list) -> float:
        total = 0
        for vehicle in rented_vehicles:
            cost = self.vehicles[vehicle["id"]].calculate_rental_cost(vehicle["hours"])
            # discount
            if vehicle["hours"] >= 5:
                cost -= cost * self.DISCOUNT_RATE

            total += cost
        return total
    

def main():
    service = RentalService([Bike, Car, Truck])
    service.list_available_vehicles()
    rented_vehicles = service.getRentedVehicles()
    total_cost = service.calculate_total_rental_cost(rented_vehicles)
    print("="*100)
    print("Total cost:", total_cost)
    print("="*100)

if __name__ == "__main__":
    print()
    main()
    print()

    