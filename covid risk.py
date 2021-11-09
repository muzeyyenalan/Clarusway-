age = (input ("Are you a cigarette addict older than 75 years old? :" )).lower().strip()
choronic = (input("Do you have a severe chronic disease?:")).lower().strip()
immune =(input("Your immune system is low?:")).lower().strip()

if age =="Yes" :
   age=True
else:
  age= False
if choronic =="Yes" :
   choronic=True
else:
  choronic= False
if immune =="Yes" :
   immune=True
else:
  immune= False
  

if age and  choronic and immune :
  print("You are in risky group")
else:
  print("you are not in risky group")
