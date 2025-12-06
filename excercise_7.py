# BMI Calculator
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
print("BMI:", round(bmi, 2))

if bmi < 18.5:
    print(f"Your BMI is {round(bmi,2)} and you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {round(bmi,2)} and you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {round(bmi,2)} and you are overweight.")
elif bmi < 35:
    print(f"Your BMI is {round(bmi,2)} and you are obese.")
else:
    print(f"Your BMI is {round(bmi,2)} and you are clinically obese.")