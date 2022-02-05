height = int(input("Enter your height in metres: "))
weight = int(input("Enter your weight in kilogrammes: "))

bmi = weight / height**2

if bmi <= 18.5:
    print("Underweight")
elif bmi > 18.5 and bmi <= 24.9:
    print("Normal weight")
elif bmi > 24.9 and bmi <= 29.9:
    print("Overweight")
else:
    print("Obesity")