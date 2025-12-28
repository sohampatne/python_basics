# Imports
from ast import match_case
from turtle import circle

# --------------------------------------------------------------------------------------------------------------------------------

# Value retrieval
def length():
    return input("Please enter the length: ")


def breadth():
    return input("Please enter the breadth: ")


def radius():
    return input("Please enter the length of the radius: ")


def height():
    return input("Please enter the height: ")


def base():
    return input("Please enter the base: ")


def pi_value():
    return input(
        "Do you want pi to be used in it's Decimal (1) value, or in it's Fractional (2) value?: "
    )


def side():
    return input("Please enter the length of the side: ")


def diagonal1():
    return input("Please enter the length of the 1st diagonal: ")


def diagonal2():
    return input("Please enter the length of the 2nd diagonal: ")


# Criterion specification
def perimeterOrArea():
    return input("Do you want to find the Perimeter ('1') or the Area('2')? :")


def areaORvolumeORperimeter():
    return input(
        "Do you want to find the Area ('1'), Volume('2') or the Perimeter(3)? :"
    )


def circumferenceOrArea():
    return input("Do you want to find the Circumference ('1') or the Area('2')? :")


def totalSurfaceAreaORlateralsurfacearea():
    return input(
        "Do you want to find the Total Surface Area \{TSA\} ('1') or the Curved/Lateral Surface Area \{CSA/LSA\} ('2')? :"
    )


def welcome():
    category = input(
        "\nThis is a program that helps you calculate the mensurational quantities of 2D and 3D objects.\n\n"
        + "Please choose a category ['2D'(1) or '3D'(2)]: "
    )
    return category


# --------------------------------------------------------------------------------------------------------------------------------

# Function definitions
# Dimensions
# 2 Dimensional

# -------------------------------------------------------------------

# 1. Rectangle


class Rectangle:

    # init method or constructor
    def __init__(self) -> None:
        self.length = int(length())
        self.breadth = int(breadth())

    # 1.1 Perimeter
    def perimeter(self):
        result = 2 * (self.length + self.breadth)
        print("Your result: ", str(result))

    # 1.2 Area
    def area(self):
        result = self.length * self.breadth
        print("Your result: ", str(result))

    # Calculation
    def calculate(self):
        pOa = perimeterOrArea()

        if pOa == "1":
            self.perimeter()

        elif pOa == "2":
            self.area()


# -------------------------------------------------------------------

# 2. Square


class Square:

    # init method or constructor
    def __init__(self) -> None:
        self.side = int(side())

    # 2.1 Perimeter
    def perimeter(self):
        result = 4 * self.side
        print("Your result: ", str(result))

    # 2.2 Area
    def area(self):
        result = self.side**2
        print("Your result: ", str(result))

    # Calculation
    def calculate(self):
        pOa = perimeterOrArea()

        if pOa == "1":
            self.perimeter()

        elif pOa == "2":
            self.area()


# -------------------------------------------------------------------

# 3. Circle


class Circle:

    # init method or constructor
    def __init__(self) -> None:
        self.radius = int(radius())
        self.pip = pi_value()
        self.pi = 0

    # 3.1 Circumference
    def circumference(self):

        # 3.0 Pi
        if self.pip == "1":
            self.pi = 3.14
        if self.pip == "2":
            self.pi = 22 / 7

        result = 2 * self.pi * self.radius
        print("Your result: ", str(result))

    # 3.2 Area
    def area(self):

        # 3.0 Pi
        if self.pip == "1":
            self.pi = 3.14
        if self.pip == "2":
            self.pi = 22 / 7

        result = self.pi * (self.radius**2)
        print("Your result: ", str(result))

    # Calculation
    def calculate(self):
        cOa = circumferenceOrArea()

        if cOa == "1":
            self.circumference()

        elif cOa == "2":
            self.area()


# -------------------------------------------------------------------

# 4. Semi-circle


class Semi_circle:

    # init method or constructor
    def __init__(self) -> None:
        self.radius = int(radius())
        self.pi = int(pi_value())

    # 3.1 Circumference
    def circumference(self):
        result = (self.pi * self.radius) + radius
        print("Your result: ", str(result))

    # 3.2 Area
    def area(self):
        result = (self.pi * (self.radius**2)) / 2
        print("Your result: ", str(result))

    # Calculation
    def calculate(self):
        cOa = circumferenceOrArea()

        if cOa == "1":
            self.circumference()

        elif cOa == "2":
            self.area()


# -------------------------------------------------------------------

# 4. Triangle


class Triangle:

    # init method or constructor
    def __init__(self) -> None:
        self.height = int(height())
        self.base = int(base())

    # 4.1 Area
    def area(self):
        result = 1 / 2 * self.height * self.base
        print("Your result: ", str(result))

    # 4.2 Perimeter
    def perimeter(self):
        side1 = input("Please enter the length of the 1st side: ")
        side2 = input("Please enter the length of the 2nd side: ")
        side3 = input("Please enter the length of the 3rd side: ")

        result = side1 + side2 + side3
        print("Your result: ", result)

    # Calculation
    def calculate(self):
        pOa = perimeterOrArea()

        if pOa == "1":
            self.perimeter()

        elif pOa == "2":
            self.area()


# -------------------------------------------------------------------

# 6. Parallelogram


class Parallelogram:

    # init method or constructor
    def __init__(self) -> None:
        self.base = int(base())
        self.height = int(height())

    # 6.1 Area
    def area(self):
        result = self.height * self.base
        print("Your result: ", str(result))

    # 6.2 Perimeter
    def perimeter(self):
        side1 = input("Please enter the length of the 1st side: ")
        side2 = input("Please enter the length of the 2nd side: ")
        side3 = input("Please enter the length of the 3rd side: ")
        side4 = input("Please enter the length of the 3rd side: ")

        result = side1 + side2 + side3 + side4
        print("Your result: ", result)

    # Calculation
    def calculate(self):
        pOa = perimeterOrArea()

        if pOa == "1":
            self.perimeter()

        elif pOa == "2":
            self.area()


# -------------------------------------------------------------------

# 7. Rhombus


class Rhombus:

    # init method or constructor
    def __init__(self) -> None:
        self.diagonal1 = int(diagonal1())
        self.diagonal2 = int(diagonal2())
        self.side = int(side())

    # 7.1 Perimeter
    def perimeter(self):
        result = 4 * self.side
        print("Your result: ", result)

    # 7.2 Area
    def area(self):
        result = 1 / 2 * self.diagonal1 * self.diagonal2
        print("Your result: ", result)

    # Calculation
    def calculate(self):
        pOa = perimeterOrArea()

        if pOa == "1":
            self.perimeter()

        elif pOa == "2":
            self.area()


# -------------------------------------------------------------------

# 8. Trapezoid


class Trapezoid:

    # init method or constructor
    def __init__(self) -> None:
        self.parallel_side1 = input(
            "Please enter the length of the 1st parallel side: "
        )
        self.parallel_side2 = input(
            "Please enter the length of the 2nd parallel side: "
        )
        self.side3 = input("Please enter the length of the 1st non-parallel side: ")
        self.side4 = input("Please enter the length of the 2nd non-parallel side: ")

    # 8.1 Perimeter
    def perimeter(self):
        result = self.parallel_side1 + self.parallel_side2 + self.side3 + self.side4
        print("Your result: ", result)

    # 8.2 Area
    def area(self):
        result = 1 / 2 * (self.parallel_side1 + self.parallel_side2)
        print("Your result: ", result)

    # Calculation
    def calculate(self):
        pOa = perimeterOrArea()

        if pOa == "1":
            self.perimeter()

        elif pOa == "2":
            self.area()


# -------------------------------------------------------------------

# 9. Regular Hexagon


class Hexagon:

    # init method or constructor
    def __init__(self) -> None:
        self.side = input(
            "Please enter the length of the side \{all sides should be common in this case\}: "
        )

    # 9.1 Perimeter
    def perimeter(self):
        result = 6 * self.side
        print("Your result: ", result)

    # 9.2 Area
    def area(self):
        result = 1 / 2 * (self.parallel_side1 + self.parallel_side2)
        print("Your result: ", result)

    # Calculation
    def calculate(self):
        pOa = perimeterOrArea()

        if pOa == "1":
            self.perimeter()

        elif pOa == "2":
            self.area()


# -------------------------------------------------------------------

# 10. Any Quadrilateral


class Quadrilateral:

    # init method or constructor
    def __init__(self) -> None:
        self.offset1 = input("Please enter the length of the 1st offset: ")
        self.offset2 = input("Please enter the length of the 2nd offset: ")
        self.diagonal = input("Please enter the length of the diagonal: ")
        self.side1 = input("Please enter the length of the 1st side :")
        self.side2 = input("Please enter the length of the 2nd side :")
        self.side3 = input("Please enter the length of the 3rd side :")
        self.side4 = input("Please enter the length of the 4th side :")

    # 10.1 Perimeter

    def perimeter(self):
        result = self.side1 + self.side2 + self.side3 + self.side4
        print(result)

    # 10.2 Area
    def area(self):
        result = 1 / 2 * self.diagonal * (self.offset1 + self.offset2)
        print(result)

    # Calculation
    def calculate(self):
        pOa = perimeterOrArea()
        if pOa == "1":
            self.perimeter()

        elif pOa == "2":
            self.area()


# --------------------------------------------------------------------------------------------------------------------------------

# 3 Dimensional

# 1. Cube


class Cube:

    # init constructor
    def __init__(self) -> None:
        self.side = input("Please enter the length of the side of the cube: ")

    # Area
    def tsa(self):
        result = 6 * (self.side**2)
        print(result)

    def csa(self):
        result = 4 * (self.side**2)
        print(result)

    # Volume
    def volume(self):
        result = self.side**3
        print(result)

    # Perimeter
    def perimeter(self):
        result = self.side * 12
        print(result)

    # Calculate
    def calculate(self):
        aOvOp = areaORvolumeORperimeter()

        if aOvOp == "1":
            tOl = totalSurfaceAreaORlateralsurfacearea()
            if tOl == "1":
                self.tsa()
            elif tOl == "2":
                self.csa()

        if aOvOp == "2":
            self.volume()

        if aOvOp == "3":
            self.perimeter()


# -------------------------------------------------------------

# 2. Cuboid


class Cuboid:

    # init constructor
    def __init__(self) -> None:
        self.length = int(length())
        self.height = int(height())
        self.breadth = int(breadth())

    # Area
    def tsa(self):
        result = 2 * (
            self.lenght * self.height
            + self.breadth * self.height
            + self.lenght * self.breadth
        )
        print(result)

    def csa(self):
        result = 2 * (self.legnth * self.height + self.breadth * self.height)
        print(result)

    # Volume
    def volume(self):
        result = self.length * self.breadth * self.height
        print(result)

    # Perimeter
    def perimeter(self):
        result = 4 * (self.length + self.breadth + self.height)
        print(result)

    # Calculate
    def calculate(self):
        aOvOp = areaORvolumeORperimeter()

        if aOvOp == "1":
            tOl = totalSurfaceAreaORlateralsurfacearea()
            if tOl == "1":
                self.tsa()
            elif tOl == "2":
                self.csa()

        if aOvOp == "2":
            self.volume()

        if aOvOp == "3":
            self.perimeter()


# -------------------------------------------------------------

# 2. Cylidner


class Cylinder:

    # init constructor
    def __init__(self) -> None:
        self.pi = pi_value()
        self.radius = radius()
        self.height = height()

    # Area
    def tsa(self):
        result = (
            2 * self.pi * (self.radius**2) + 2 * self.pi * self.radius * self.height
        )
        print(result)

    def csa(self):
        result = 2 * self.pi * self.radius * self.height
        print(result)

    # Volume
    def volume(self):
        result = 2 * self.pi * (self.radius**2) * self.height
        print(result)


# -------------------------------------------------------------

# 2. Cone


class Cone:

    # init constructor
    def __init__(self) -> None:
        pass


# -------------------------------------------------------------

# 2. Sphere


class Sphere:

    # init constructor
    def __init__(self) -> None:
        pass


# --------------------------------------------------------------------------------------------------------------------------------

# Main Program

categoryRun = welcome()


def run2D():
    dimensionInput2D = input(
        "Selection criteria:"
        + "\n'1' - Rectangle"
        + "\n'2' - Square"
        + "\n'3' - Circle"
        + "\n'4' - Semi-circle"
        + "\n'5' - Triangle"
        + "\n'6' - Parallelogram"
        + "\n'7' - Rhombus"
        + "\n'8' - Trapezoid"
        + "\n'9' - Regular Hexagon"
        + "\n'10' - Any Quadrilateral"
        + "\n\nYour input: "
    )

    match dimensionInput2D:
        case "1":
            Rectangle().calculate()
        case "2":
            Square().calculate()
        case "3":
            Circle().calculate()
        case "4":
            Semi_circle().calculate()
        case "5":
            Triangle().calculate()
        case "6":
            Parallelogram().calculate()
        case "7":
            Rhombus().calculate()
        case "8":
            Trapezoid().calculate()
        case "9":
            Hexagon().calculate()
        case "10":
            Quadrilateral().calculate()


def run3D():
    dimensionInput3D = input(
        "Selection criteria:"
        + "\n1. Cube"
        + "\n2. Cuboid"
        + "\n3. Cylinder"
        + "\n4. Cone"
        + "\n5. Sphere"
    )

    match dimensionInput3D:
        case "1":
            Cube().calculate()
        case "2":
            Cuboid().calculate()
        case "3":
            Cylinder().calculate()
        case "4":
            Cone().calculate()
        case "5":
            Sphere().calculate()


if categoryRun == "1":
    run2D()
elif categoryRun == "2":
    run3D()


# ---------------------------------------------------------x---END_OF_CODE---x-----------------------------------------------------------------
