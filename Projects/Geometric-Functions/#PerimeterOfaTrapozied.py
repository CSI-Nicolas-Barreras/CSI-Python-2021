# PerimeterOfATrapezoid.py

# Calculate Perimeter Of A Trapezoid

def PerimeterOfATrapezoid(a:float, b:float, c:float, d:float):
        return ( a+b+c+d )

# Values to 2 decimal places and using scientific notation. 

def printPerimeterOfATrapezoid(PerimeterOfATrapezoid:float, unit:str):
        print(f"The speed in scientific notation is: {PerimeterOfATrapezoid:.2e} {unit}.")


# Add a header to your execution. It includes 2 newline characters '\n'

printPerimeterOfATrapezoid(PerimeterOfATrapezoid(20, 30), "m")
printPerimeterOfATrapezoid(PerimeterOfATrapezoid(60, 10), "mm")
printPerimeterOfATrapezoid(PerimeterOfATrapezoid(27, 83), "cm")
printPerimeterOfATrapezoid(PerimeterOfATrapezoid(100, 500), "foot")

