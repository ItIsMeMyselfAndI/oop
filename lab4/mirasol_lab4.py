"""
- Attributes: 
    radius (float)
    color (string)
    total_count (int)
- Behaviors:
    get_radius()
    get_diameter()
    calculate_area()
    calculate_circumference()
    get_color()
    set_color()
    update_total_count()
    get_circle_total_count()
- The total_count tracks the total number of circle objects that 
- was created from the Circle class. 
    (hint: implement this within the __init__() method)

"""

class Circle:
    total_count = 0

    def __init__(self, radius:float, color:str) -> None:
        self.radius = radius
        self.color = color
        self.pi = 3.14159265
        # self.total_count = 0

    def get_radius(self) -> float:
        return self.radius

    def get_diameter(self) -> float:
        d = self.radius * 2
        return d

    def calculate_area(self) -> float:
        a = self.pi * (self.radius ** 2)
        return a

    def calculate_circumference(self) -> float:
        c = 2 * self.pi * self.radius
        return c

    def get_color(self) -> str:
        return self.color

    def set_color(self, new:str) -> None:
        self.color = new

    @classmethod 
    def update_total_count(cls) -> None:
        cls.total_count += 1

    @classmethod
    def get_circle_total_count(cls) -> int:
        return cls.total_count


def main() -> None:
    radius = float(input("Enter circle radius: ").strip())
    color = input("Enter circle color: ").strip()
    if color == "":
        color = "None"
    
    c = Circle(radius, color)
    Circle.update_total_count()
    print(f"\tradius: {c.get_radius()}")
    print(f"\tdiameter: {c.get_diameter()}")
    print(f"\tarea: {c.calculate_area()}")
    print(f"\tcircumference: {c.calculate_circumference()}")
    print(f"\tcolor: {c.get_color()}")
    
    color = input("Enter new color: ").strip()
    if color == "":
        color = "None"
    c.set_color(color)
    print(f"\tcolor: {c.get_color()}")
    print(f"Total objects created: {Circle.get_circle_total_count()}")


if __name__ == "__main__":
    print()
    print(" "*23 + "*"*4)

    while True:
        print("="*50)
        try:
            main()
            
            print("="*50)
            choice = input("Do you want to continue (y/n)? ").strip()
            print("="*50)
            print(" "*23 + "*"*4)
            if choice.upper() != "Y":
                print()
                break
        
        except (KeyboardInterrupt, EOFError):
            print("\n" + "="*50)
            print("[*] Exits program.")
            print("="*50)
            print(" "*23 + "*"*4)
            print()
            exit(0)
        except ValueError:
            print("="*50)
            print("[!] Invalid number. Try again.")
            continue



