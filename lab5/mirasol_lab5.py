import math
import os 


class Polygon:
    def __init__(self):
        self.type = ""
        self.sides = 0 
        self.total_angle = 0
        self.perimeter = 0
        self.area = 0

    def displayShape(self):
        pass

    def getLengths(self):
        pass
    
    def calcLengths(self):
        pass
    
    def getAngles(self):
        pass
    
    def calcAngles(self):
        pass

    def calcPerimeter(self):
        pass

    def calcArea(self):
        pass

    def displayMeasurements(self):
        pass

    def run(self):
        pass


"""-------------------------------------------------------"""


class Triangle(Polygon):
    def __init__(self):
        super().__init__()
        self.sides = 3
        # lengths
        self.a = 0
        self.b = 0
        self.c = 0
        self.total_angle = 180
        # angles 
        self.A = 0
        self.B = 0
        self.C = 0

    def displayShape(self, left, right, bot):
        shape = (
            f"\n{"="*50}\n"
            f"{self.type.center(50)}"
            f"\n{"="*50}\n\n"
            f"{"*".center(50)}\n"
            f"{"* *".center(50)}\n"
            f"{"* C *".center(50)}\n"
            f"{"*     *".center(50)}\n"
            f"{f"a   {left}       {right}   b".center(50)}\n"
            f"{"*         *".center(50)}\n"
            f"{"* B       A *".center(50)}\n"
            f"{f"* * * *{bot}* * * *".center(50)}\n\n"
            f"{"c".center(50)}\n\n"
            f"{"="*50}"
        )
        print(shape)

    def calcAngles(self):
        a_rad = math.acos((self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c))
        b_rad = math.acos((self.a**2 + self.c**2 - self.b**2) / (2 * self.a * self.c))
        self.A = math.degrees(a_rad)
        self.B = math.degrees(b_rad)
        self.C = 180 - self.A - self.B
    
    def calcLengths(self):
        self.b = (math.sin(math.radians(self.B)) / math.sin(math.radians(self.A))) * self.a
        self.c = (math.sin(math.radians(self.C)) / math.sin(math.radians(self.A))) * self.a

    def calcPerimeter(self):
        self.perimeter = self.a + self.b + self.c

    def calcArea(self):
        semi = self.perimeter / 2
        self.area = math.sqrt(semi * (semi - self.a) * (semi - self.b) * (semi - self.c))

    def displayMeasurements(self):
        meas = (
            f"{"="*50}\n"
            "Lengths:\n"
            f"\ta = {self.a:.3f} units\n"
            f"\tb = {self.b:.3f} units\n"
            f"\tc = {self.c:.3f} units\n"
            "Angles:\n"
            f"\tA = {self.A:.3f} degrees\n"
            f"\tB = {self.B:.3f} degrees\n"
            f"\tC = {self.C:.3f} degrees\n"
            "Perimeter:\n"
            f"\t= {self.perimeter:.3f} units\n"
            "Area:\n"
            f"\t= {self.area:.3f} squared units\n"
            f"{"="*50}\n"
        )
        print(meas)


class Equilateral(Triangle):
    def __init__(self):
        super().__init__()
        self.type = "Equilateral Triangle"

    def getLengths(self):
        self.a = self.b = self.c = float(input("Enter side (a/b/c) length: "))
        if self.a <= 0:
            print("="*50)
            print("[*] Only enter decimal/integer number(s)")
            print("\tgreater than 0.")
            print("="*50)
            self.getLengths()

    def run(self):
        self.displayShape("——", "——", "|")
        self.getLengths()
        self.calcAngles()
        self.calcPerimeter()
        self.calcArea()
        self.displayMeasurements()


class Isosceles(Triangle):
    def __init__(self):
        super().__init__()
        self.type = "Isosceles Triangle"

    def getLengths(self):
        self.a = self.b = float(input("Enter side (a/b) length: "))
        self.c = float(input("Enter side (c) length: "))
        if (self.a <= 0) or (self.c <= 0):
            print("="*50)
            print("[*] Only enter decimal/integer number(s)")
            print("\tgreater than 0.")
            print("="*50)
            self.getLengths()
        elif (self.a == self.c):
            print("="*50)
            print("[*] The side lengths (a) and (b)")
            print("\tshould not be equal to side length (c).")
            print("="*50)
            self.getLengths()
        elif (self.a + self.b) <= self.c:
            print("="*50)
            print("[*] The sum of side lengths (a) and (b)")
            print("\tshould be greater than side length (c).")
            print("="*50)
            self.getLengths()

    def run(self):
        self.displayShape("——", "——", " ")
        self.getLengths()
        self.calcAngles()
        self.calcPerimeter()
        self.calcArea()
        self.displayMeasurements()


class Scalene(Triangle):
    def __init__(self):
        super().__init__()
        self.type = "Scalene Triangle"

    def getLengths(self):
        self.a = float(input("Enter side (a) length: "))
        self.b = float(input("Enter side (b) length: "))
        self.c = float(input("Enter side (c) length: "))
        if (self.a <= 0) or (self.b <= 0) or (self.c <= 0):
            print("="*50)
            print("[*] Only enter decimal/integer number(s)")
            print("\tgreater than 0.")
            print("="*50)
            self.getLengths()
        elif (self.a == self.b) or (self.a == self.c) or (self.b == self.c):
            print("="*50)
            print("[*] The side lengths (a), (b), and (c)")
            print("\tshould all be different.")
            print("="*50)
            self.getLengths()
        elif ((self.a + self.b) <= self.c) or ((self.a + self.c) <= self.b) or ((self.b + self.c) <= self.a):
            print("="*50)
            print("[*] The sum of any 2 side lengths")
            print("\tshould be greater than the other.")
            print("="*50)
            self.getLengths()

    def run(self):
        self.displayShape("*", "*", " ")
        self.getLengths()
        self.calcAngles()
        self.calcPerimeter()
        self.calcArea()
        self.displayMeasurements()


class Right(Triangle):
    def __init__(self):
        super().__init__()
        self.type = "Right Triangle"
        self.A = 90.0

    def displayShape(self):
        shape = (
            f"\n{"="*50}\n"
            f"{self.type.center(50)}"
            f"\n{"="*50}\n\n"
            f"{"                  *    ".center(50)}\n"
            f"{"               *  *    ".center(50)}\n"
            f"{"      a     *   C *    ".center(50)}\n"
            f"{"         *        *   b".center(50)}\n"
            f"{"      *           *    ".center(50)}\n"
            f"{"   *   B       [A]*    ".center(50)}\n"
            f"{"* * * * * * * * * *    ".center(50)}\n\n"
            f"{"c    ".center(50)}\n\n"
            f"{"="*50}"
        )
        print(shape)
    
    def getAngles(self):
        print(f"Right angle (A) in degrees: {self.A:.3f}")
        self.B = float(input("Enter angle (B) in degrees: "))
        self.C = float(input("Enter angle (C) in degrees: "))
        if (self.B <= 0) or (self.C <= 0):
            print("="*50)
            print("[*] Only enter decimal/integer number(s)")
            print("\tgreater than 0.")
            print("="*50)
            self.getAngles()
        elif (self.A + self.B + self.C) != 180:
            print("="*50)
            print("[*] The sum of angles (A), (B), and (C)")
            print("\tshould be equal to (180) degrees.")
            print("="*50)
            self.getAngles()
    
    def getLengths(self):
        self.a = float(input("Enter side (a) length: "))
        if (self.a <= 0):
            print("="*50)
            print("[*] Only enter decimal/integer number(s)")
            print("\tgreater than 0.")
            print("="*50)
            self.getLengths()

    def run(self):
        self.displayShape()
        self.getAngles()
        self.getLengths()
        self.calcLengths()
        self.calcPerimeter()
        self.calcArea()
        self.displayMeasurements()
    

class Acute(Triangle):
    def __init__(self):
        super().__init__()
        self.type = "Acute Triangle"

    def getAngles(self):
        self.A = float(input("Enter angle (A) in degrees: "))
        self.B = float(input("Enter angle (B) in degrees: "))
        self.C = float(input("Enter angle (C) in degrees: "))
        if (self.A <= 0) or (self.B <= 0) or (self.C <= 0):
            print("="*50)
            print("[*] Only enter decimal/integer number(s)")
            print("\tgreater than 0.")
            print("="*50)
            self.getAngles()
        elif (self.A + self.B + self.C) != 180:
            print("="*50)
            print("[*] The sum of angles (A), (B), and (C)")
            print("\tshould be equal to (180) degrees.")
            print("="*50)
            self.getAngles()
        elif (self.A >= 90) or (self.B >= 90) or (self.C >= 90):
            print("="*50)
            print("[*] The angles (A), (B), and (C)")
            print("\tshould all be less than (90) degrees.")
            print("="*50)
            self.getAngles()
    
    def getLengths(self):
        self.a = float(input("Enter side (a) length: "))
        if (self.a <= 0):
            print("="*50)
            print("[*] Only enter decimal/integer number(s)")
            print("\tgreater than 0.")
            print("="*50)
            self.getLengths()
    
    def run(self):
        self.displayShape("*", "*", " ")
        self.getAngles()
        self.getLengths()
        self.calcLengths()
        self.calcPerimeter()
        self.calcArea()
        self.displayMeasurements()


class Obtuse(Triangle):
    def __init__(self):
        super().__init__()
        self.type = "Obtuse Triangle"

    def getAngles(self):
        self.A = float(input("Enter angle (A) in degrees: "))
        self.B = float(input("Enter angle (B) in degrees: "))
        self.C = float(input("Enter angle (C) in degrees: "))
        if (self.A <= 0) or (self.B <= 0) or (self.C <= 0):
            print("="*50)
            print("[*] Only enter decimal/integer number(s)")
            print("\tgreater than 0.")
            print("="*50)
            self.getAngles()
        elif (self.A + self.B + self.C) != 180:
            print("="*50)
            print("[*] The sum of angles (A), (B), and (C)")
            print("\tshould be equal to (180) degrees.")
            print("="*50)
            self.getAngles()
        elif (self.A <= 90) and (self.B <= 90) and (self.C <= 90):
            print("="*50)
            print("[*] One angle should be")
            print("\tgreater than (90) degrees.")
            print("="*50)
            self.getAngles()
    
    def getLengths(self):
        self.a = float(input("Enter side (a) length: "))
        if (self.a <= 0):
            print("="*50)
            print("[*] Only enter decimal/integer number(s)")
            print("\tgreater than 0.")
            print("="*50)
            self.getLengths()

    def run(self):
        self.displayShape("*", "*", " ")
        self.getAngles()
        self.getLengths()
        self.calcLengths()
        self.calcPerimeter()
        self.calcArea()
        self.displayMeasurements()


"""-------------------------------------------------------"""


class Quadrilateral(Polygon):
    def __init__(self):
        super().__init__()
        self.sides = 4
        # lengths
        self.h = 0
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        
        self.total_angle = 360
        # angles
        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0
    

class Trapezoid(Quadrilateral):
    def __init__(self):
        super().__init__()
        self.type = "Trapezoid"
        # lengths
        self.base_1 = 0
        self.base_2 = 0
        self.h = 0
        
    def displayShape(self):
        shape = (
            f"\n{"="*50}\n"
            f"{self.type.center(50)}"
            f"\n{"="*50}\n\n"
            f"{"base 1".center(50)}\n\n"
            f"{"* * * > * * *".center(50)}\n"
            f"{"*    |        *".center(50)}\n"
            f"{"*     |         *".center(50)}\n"
            f"{"*      | h        *".center(50)}\n"
            f"{"*       |           *".center(50)}\n"
            f"{"*        |            *".center(50)}\n"
            f"{"* * * * * * > * * * * * *".center(50)}\n\n"
            f"{"base 2".center(50)}\n\n"
            f"{"="*50}"
        )
        print(shape)

    def getLengths(self):
        self.base_1 = float(input("Enter length of (base 1): "))
        self.base_2 = float(input("Enter length of (base 2): "))
        self.h = float(input("Enter height (h): "))
        if (self.base_1 <= 0) or (self.base_2 <= 0) or (self.h <= 0):
            print("="*50)
            print("[*] Only enter decimal/integer number(s)")
            print("\tgreater than 0.")
            print("="*50)
            self.getLengths()
        elif (self.base_1 == self.base_2):
            print("="*50)
            print("[*] The lengths of (base 1) and (base 2)")
            print("\tshould be different.")
            print("="*50)
            self.getLengths()

    def calcArea(self):
        self.area = ((self.base_1 + self.base_2) / 2) * self.h

    def displayMeasurements(self):
        meas = (
            f"{"="*50}\n"
            "Lengths:\n"
            f"\tBase 1 = {self.base_1:.3f} units\n"
            f"\tBase 2 = {self.base_2:.3f} units\n"
            f"\th = {self.h:.3f} units\n"
            "Area:\n"
            f"\t= {self.area:.3f} squared units\n"
            f"{"="*50}\n"
        )
        print(meas)

    def run(self):
        self.displayShape()
        self.getLengths()
        self.calcArea()
        self.displayMeasurements()


class Parallelogram(Quadrilateral):
    def __init__(self):
        super().__init__()
        self.type = "Parallelogram"

    def displayShape(self):
        shape = (
            f"\n{"="*50}\n"
            f"{self.type.center(50)}"
            f"\n{"="*50}\n\n"
            f"{"                 b             ".center(50)}\n\n"
            f"{"      * * * * * *>>* * * * * *".center(50)}\n"
            f"{"     * B   |              C * ".center(50)}\n"
            f"{"a   *      |               *  ".center(50)}\n"
            f"{"   V       | h            V   ".center(50)}\n"
            f"{"  *        |             *   c".center(50)}\n"
            f"{" * A       |         D  *     ".center(50)}\n"
            f"{"* * * * * *>>* * * * * *      ".center(50)}\n\n"
            f"{"           d                  ".center(50)}\n\n"
            f"{"="*50}"
        )
        print(shape)

    def getLengths(self):
        self.a = self.c = float(input("Enter side length (a/c): "))
        self.b = self.d = float(input("Enter side length (b/d): "))
        if (self.a <= 0) or (self.c <= 0):
            print("="*50)
            print("[*] Only enter decimal/integer number(s)")
            print("\tgreater than 0.")
            print("="*50)
            self.getLengths()
        elif (self.a == self.b):
            print("="*50)
            print("[*] Any adjacent sides")
            print("\tshould have different lengths.")
            print("="*50)
            self.getLengths()

    def getAngles(self):
        self.A = self.C = float(input("Enter angle (A/C) in degrees: "))
        if (self.A <= 0):
            print("="*50)
            print("[*] Only enter decimal/integer number(s)")
            print("\tgreater than 0.")
            print("="*50)
            self.getAngles()
        elif (self.A == 90) or (self.A >= 180):
            print("="*50)
            print("[*] Any angle should not be equal to (90)")
            print("\tand should be less than (180) degrees.")
            print("="*50)
            self.getAngles()

    def calcAngles(self):
        self.B = self.D = 180 - self.A 

    def calcPerimeter(self):
        self.perimeter = self.a + self.b + self.c + self.d

    def calcArea(self):
        self.h = math.sin(math.radians(self.A)) * self.a
        self.area = self.b * self.h

    def displayMeasurements(self):
        meas = (
            f"{"="*50}\n"
            "Lengths:\n"
            f"\th = {self.h:.3f} units\n"
            f"\ta = {self.a:.3f} units\n"
            f"\tb = {self.b:.3f} units\n"
            f"\tc = {self.c:.3f} units\n"
            f"\td = {self.d:.3f} units\n"
            "Angles:\n"
            f"\tA = {self.A:.3f} units\n"
            f"\tB = {self.B:.3f} units\n"
            f"\tC = {self.C:.3f} units\n"
            f"\tD = {self.D:.3f} units\n"
            "Perimeter:\n"
            f"\t= {self.perimeter:.3f} squared units\n"
            "Area:\n"
            f"\t= {self.area:.3f} squared units\n"
            f"{"="*50}\n"
        )
        print(meas)

    def run(self):
        self.displayShape()
        self.getLengths()
        self.getAngles()
        self.calcAngles()
        self.calcPerimeter()
        self.calcArea()
        self.displayMeasurements()


class Rectangle(Parallelogram):
    def __init__(self):
        super().__init__()

    def displayShape(self):
        self.type = "Rectangle"
        shape = (
            f"\n{"="*50}\n"
            f"{self.type.center(50)}"
            f"\n{"="*50}\n\n"
            f"{"b".center(50)}\n\n"
            f"{"* * * * * * || * * * * * *".center(50)}\n"
            f"{"*[B]                  [C]*".center(50)}\n"
            f"{"*                        *".center(50)}\n"
            f"{"*                        *".center(50)}\n"
           f"{"a   ——                        ——   c".center(50)}\n"
            f"{"*                        *".center(50)}\n"
            f"{"*                        *".center(50)}\n"
            f"{"*[A]                  [D]*".center(50)}\n"
            f"{"* * * * * * || * * * * * *".center(50)}\n\n"
            f"{"d".center(50)}\n\n"
            f"{"="*50}"
        )
        print(shape)

    def getAngles(self):
        self.A = self.B = self.C = self.D = 90.000


class Rhombus(Parallelogram):
    def __init__(self):
        super().__init__()

    def displayShape(self):
        self.type = "Rhombus"
        shape = (
            f"\n{"="*50}\n"
            f"{self.type.center(50)}"
            f"\n{"="*50}\n\n"
            f"{"                 b         ".center(50)}\n\n"
            f"{"        * * * * / * * * *  ".center(50)}\n"
            f"{"       * B  |        C *   ".center(50)}\n"
            f"{"      *     |         *    ".center(50)}\n"
            f"{"a   ——      | h      ——   c".center(50)}\n"
            f"{"    *       |       *      ".center(50)}\n"
            f"{"   * A      |    D *       ".center(50)}\n"
            f"{"  * * * * / * * * *        ".center(50)}\n\n"
            f"{"         d                 ".center(50)}\n\n"
            f"{"="*50}"
        )
        print(shape)

    def getLengths(self):
        self.a = self.b = self.c = self.d = float(input("Enter side length (a/b/c/d): "))
        if (self.a <= 0):
            print("="*50)
            print("[*] Only enter decimal/integer number(s)")
            print("\tgreater than 0.")
            print("="*50)
            self.getLengths()


class Square(Rectangle, Rhombus):
    def __init__(self):
        super().__init__()

    def displayShape(self):
        self.type = "Square"
        shape = (
            f"\n{"="*50}\n"
            f"{self.type.center(50)}"
            f"\n{"="*50}\n\n"
            f"{"b".center(50)}\n\n"
            f"{"* * * * | * * * *".center(50)}\n"
            f"{"*[B]         [C]*".center(50)}\n"
            f"{"*               *".center(50)}\n"
            f"{"a  ——               ——  c".center(50)}\n"
            f"{"*               *".center(50)}\n"
            f"{"*[A]         [D]*".center(50)}\n"
            f"{"* * * * | * * * *".center(50)}\n\n"
            f"{"d".center(50)}\n\n"
            f"{"="*50}"
        )
        print(shape)


class Kite(Parallelogram):
    def __init__(self):
        super().__init__()

    def displayShape(self):
        self.type = "Kite"
        shape = (
            f"\n{"="*50}\n"
            f"{self.type.center(50)}"
            f"\n{"="*50}\n\n"
            f"{"*".center(50)}\n"
            f"{"b     *       *     c".center(50)}\n"
            f"{"\\\\           //".center(50)}\n"
            f"{"*                  *".center(50)}\n"
            f"{"*    A              B    *".center(50)}\n"
            f"{"*                    *".center(50)}\n"
            f"{"*                *".center(50)}\n"
            f"{"a   ——            ——   d".center(50)}\n"
            f"{"*        *".center(50)}\n"
            f"{"*    *".center(50)}\n"
            f"{"**".center(50)}\n\n"
            f"{"="*50}"
        )
        print(shape)

    def getLengths(self):
        self.a = self.d = float(input("Enter side length (a/d): "))
        self.b = self.c = float(input("Enter side length (b/c): "))
        if (self.a <= 0) or (self.b <= 0):
            print("="*50)
            print("[*] Only enter decimal/integer number(s)")
            print("\tgreater than 0.")
            print("="*50)
            self.getLengths()
        elif (self.a == self.b):
            print("="*50)
            print("[*] Sides (a) and (b), ")
            print("\tshould have different lengths.")
            print("[*] Sides (c) and (d), ")
            print("\tshould have different lengths.")
            print("="*50)
            self.getLengths()

    def getAngles(self):
        self.A = self.B = float(input("Enter angle (A/B) in degrees: "))
        if (self.A <= 0):
            print("="*50)
            print("[*] Only enter decimal/integer number(s)")
            print("\tgreater than 0.")
            print("="*50)
            self.getAngles()
        elif (self.A == 90) or (self.A >= 180):
            print("="*50)
            print("[*] Any angle should not be equal to (90)")
            print("\tand should be less than (180) degrees.")
            print("="*50)
            self.getAngles()

    def calcArea(self):
        self.area = math.sin(math.radians(self.A)) * self.a * self.b

    def displayMeasurements(self):
        meas = (
            f"{"="*50}\n"
            "Lengths:\n"
            f"\ta = {self.a:.3f} units\n"
            f"\tb = {self.b:.3f} units\n"
            f"\tc = {self.c:.3f} units\n"
            f"\td = {self.d:.3f} units\n"
            "Angles:\n"
            f"\tA = {self.A:.3f} units\n"
            f"\tB = {self.B:.3f} units\n"
            "Perimeter:\n"
            f"\t= {self.perimeter:.3f} squared units\n"
            "Area:\n"
            f"\t= {self.area:.3f} squared units\n"
            f"{"="*50}\n"
        )
        print(meas)
    

"""-------------------------------------------------------"""


class Pentagon(Polygon):
    def __init__(self):
        super().__init__()
        self.type = "Pentagon (Regular)"
        self.sides = 5
        # lengths
        self.a = 0

        self.total_angle = 540

    def displayShape(self):
        shape = (
            f"\n{"="*50}\n"
            f"{self.type.center(50)}"
            f"\n{"="*50}\n\n"
            f"{"a      *      a".center(50)}\n"
            f"{"*       *".center(50)}\n"
            f"{"*              *".center(50)}\n"
            f"{"*                    *".center(50)}\n"
            f"{"*                  *".center(50)}\n"
            f"{"a   *                *   a".center(50)}\n"
            f"{"*              *".center(50)}\n"
            f"{"* * * * * * * *".center(50)}\n\n"
            f"{"a".center(50)}\n\n"
            f"{"="*50}"
        )
        print(shape)

    def getLengths(self):
        self.a = float(input("Enter side length (a): "))
        if (self.a <= 0):
            print("="*50)
            print("[*] Only enter decimal/integer number(s)")
            print("\tgreater than 0.")
            print("="*50)
            self.getLengths()

    def calcPerimeter(self):
        self.perimeter = self.a * 5

    def calcArea(self):
        self.area = (5 / 4) * (self.a ** 2) * (1 / math.tan(math.pi / 5))

    def displayMeasurements(self):
        meas = (
            f"{"="*50}\n"
            "Lengths:\n"
            f"\ta = {self.a:.3f} units\n"
            "Perimeter:\n"
            f"\t= {self.perimeter:.3f} squared units\n"
            "Area:\n"
            f"\t= {self.area:.3f} squared units\n"
            f"{"="*50}\n"
        )
        print(meas)

    def run(self):
        self.displayShape()
        self.getLengths()
        self.calcPerimeter()
        self.calcArea()
        self.displayMeasurements()


"""-------------------------------------------------------"""


class Hexagon(Polygon):
    def __init__(self):
        super().__init__()
        self.type = "Hexagon (Regular)"
        self.sides = 6
        # lengths
        self.a = 0

        self.total_angle = 720

    def displayShape(self):
        shape = (
            f"\n{"="*50}\n"
            f"{self.type.center(50)}"
            f"\n{"="*50}\n\n"
            f"{"*".center(50)}\n"
            f"{"a       *     *       a".center(50)}\n"
            f"{"*           *".center(50)}\n"
            f"{"*                 *".center(50)}\n"
            f"{"*                       *".center(50)}\n"
            f"{"*                       *".center(50)}\n"
            f"{"a   *                       *   a".center(50)}\n"
            f"{"*                       *".center(50)}\n"
            f"{"*                       *".center(50)}\n"
            f"{"*                 *".center(50)}\n"
            f"{"*           *".center(50)}\n"
            f"{"a       *     *       a".center(50)}\n"
            f"{"*".center(50)}\n\n"
            f"{"="*50}"
        )
        print(shape)

    def getLengths(self):
        self.a = float(input("Enter side length (a): "))
        if (self.a <= 0):
            print("="*50)
            print("[*] Only enter decimal/integer number(s)")
            print("\tgreater than 0.")
            print("="*50)
            self.getLengths()

    def calcPerimeter(self):
        self.perimeter = self.a * 6

    def calcArea(self):
        self.area = (3 * math.sqrt(3) / 2) * (self.a ** 2)

    def displayMeasurements(self):
        meas = (
            f"{"="*50}\n"
            "Lengths:\n"
            f"\ta = {self.a:.3f} units\n"
            "Perimeter:\n"
            f"\t= {self.perimeter:.3f} squared units\n"
            "Area:\n"
            f"\t= {self.area:.3f} squared units\n"
            f"{"="*50}\n"
        )
        print(meas)

    def run(self):
        self.displayShape()
        self.getLengths()
        self.calcPerimeter()
        self.calcArea()
        self.displayMeasurements()


# t = Equilateral()
# t = Isosceles()
# t = Scalene()
# t = Right()
# t = Acute()
# t = Obtuse()

# q = Trapezoid()
# q = Parallelogram()
# q = Rectangle()
# q = Rhombus()
# q = Square()
# q = Kite()

# p = Pentagon().run()
# h = Hexagon().run()

def main():
    os.system("cls")
    print()
    print("="*50)
    print(f"{"Polygons".center(50)}")
    print("="*50)
    print("\t1 - Triangles")
    print("\t2 - Quadrilaterals")
    print("\t3 - Pentagon (Regular)")
    print("\t4 - Hexagon (Regular)")
    print("\tq - Quit")
    print("="*50)
    choice_1 = input("Choose from 1 to 4 (q to quit): ")
    print("="*50)

    if choice_1 not in ["1", "2", "3", "4", "q"]:
        main()
    elif choice_1 == "q":
        print("[*] Exited")
        print("="*50)
        exit(0)

    os.system("cls")
    if choice_1 == "1":
        print()
        print("="*50)
        print(f"{"Triangles".center(50)}")
        print("="*50)
        print("\t1 - Equilateral")
        print("\t2 - Isosceles")
        print("\t3 - Scalene")
        print("\t4 - Right")
        print("\t5 - Acute")
        print("\t6 - Obtuse")
        print("\tq - Quit")
        print("="*50)
        choice_2 = input("Choose from 1 to 6 (q to quit): ")
        print("="*50)

        if choice_1 not in ["1", "2", "3", "4", "5", "6" "q"]:
            main()
        elif choice_2 == "q":
            print("[*] Exited")
            print("="*50)
            exit(0)

        os.system("cls")
        if choice_2 == "1": shape = Equilateral().run()
        elif choice_2 == "2": shape = Isosceles().run()
        elif choice_2 == "3": shape = Scalene().run()
        elif choice_2 == "4": shape = Right().run()
        elif choice_2 == "5": shape = Acute().run()
        elif choice_2 == "6": shape = Obtuse().run()

    elif choice_1 == "2":
        print()
        print("="*50)
        print(f"{"Quadrilaterals".center(50)}")
        print("="*50)
        print("\t1 - Trapezoid")
        print("\t2 - Parallelogram")
        print("\t3 - Rectangle")
        print("\t4 - Rhombus")
        print("\t5 - Square")
        print("\t6 - Kite")
        print("\tq - Quit")
        print("="*50)
        choice_2 = input("Choose from 1 to 6 (q to quit): ")
        print("="*50)

        if choice_1 not in ["1", "2", "3", "4", "5", "6" "q"]:
            main()
        elif choice_2 == "q":
            print("[*] Exited")
            print("="*50)
            exit(0)

        os.system("cls")
        if choice_2 == "1": shape = Trapezoid().run()
        elif choice_2 == "2": shape = Parallelogram().run()
        elif choice_2 == "3": shape = Rectangle().run()
        elif choice_2 == "4": shape = Rhombus().run()
        elif choice_2 == "5": shape = Square().run()
        elif choice_2 == "6": shape = Kite().run()

    elif choice_1 == "3":
        shape = Pentagon().run()
    
    elif choice_1 == "4":
        shape = Hexagon().run()
        

if __name__ == "__main__":
    while True:
        try:
            main()
            input("{Enter to continue}\n")
        except KeyboardInterrupt:
            print(f"\n{"="*50}")
            print("[*] Exited")
            print("="*50)
            exit(0)
        except (ValueError, TypeError):
            print("="*50)
            print("[!] Invalid input,")
            print("\tonly enter decimal/integer number(s)")
            print("="*50)
            input("\n{Enter to restart}\n")




