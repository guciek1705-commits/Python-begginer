distance = float(input("Enter your distance"))  
unit = input("Miles or Kilometers? (M or K): ")  
  
if unit == "M":  
   distance = distance * 1.60934  
   unit = "kilometers"  
   print(f"Your distance is {round(distance, 2)} {unit} ")  
elif unit == "K":  
    distance = distance / 1.60934  
    unit = "miles"  
    print(f"Your distance is {round(distance, 2)} {unit} ")  
else:  
    print(f"{unit} is not a valid unit")

