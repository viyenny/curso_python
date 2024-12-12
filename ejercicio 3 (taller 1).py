pelicula = int(input("Que pelicula desea ver? 1 o 2 : "))

if pelicula == 1:
    precio_pelicula = 8500
elif pelicula == 2:
      precio_pelicula = 7700
else :
      print("opcion de pelicula no disponible")


while pelicula==2 or pelicula==1: #mientras pelicula sea igual a 1 o 2

    dia = int(input("¿que dia desea ver la peli?, ¿viernes,sabado,domingo? 1. sí, Otro numero. No: "))
    if dia==1 :
        precio_pelicula *= 1.5
    else:
        precio_pelicula = precio_pelicula
  
    num_boletas = int(input("Por favor, ingrese el numero de boletas : "))
    combo = int(input("¿deseas llevar el combo...1. Sí, Otro número. No: "))
    precio_combo = 50000
    if combo == 1:
        precio_total= (precio_pelicula * num_boletas) + precio_combo
        print("el precio a pagar es: ",precio_total)
    else:
        precio_total= precio_pelicula* num_boletas
        print("el precio a pagar es: ",precio_total)
    pelicula +=2 #para que se rompa elciclo ya que pelicula pasaria a 3 o a 4 y ya no entraria en el ciclo.