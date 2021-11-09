name_= "Muzeyyen"
pasword = " QR123456"
name_enter= (input ("Enter your name:")).title()
if name_ == name_enter :
  print("Hello {} your pasword:{}".format(name_,pasword))
else:
  print("Hi, {}! See you later".format(name_enter))
