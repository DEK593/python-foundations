pin = "1234"
pin_inserito = 0
tries = 3

while True:
    
    pin_inserito = input("inserire il pin")
    if pin_inserito == pin:
        print("pin corretto!")
        break
    else:
      tries -= 1
      print("pin errato ti rimangono", tries)
      if tries == 0:
         print("carta intrappolata") 
         break
       