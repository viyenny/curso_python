import math

print("Selecciona una figura:")
print("1. Cubo")
print("2. Esfera")
print("3. Cilindro")
print("4. Cono")
print("5. Priasma Rectangular")
opcion = int(input("Ingresa el número de tu elección (1-5): "))

if opcion == 1:  # Cubo
    lado = float(input("Lado del cubo en [cm]: "))
    volumen = lado ** 3
    superficie = 6 * (lado ** 2)
elif opcion == 2:  # Esfera
    radio = float(input("Radio de la esfera en [cm]: "))
    volumen = (4/3) * math.pi * (radio ** 3)
    superficie = 4 * math.pi * (radio ** 2)
elif opcion == 3:  # Cilindro
    radio = float(input("Radio de la base en [cm]: "))
    altura = float(input("Altura en [cm]: "))
    volumen = math.pi * (radio ** 2) * altura
    superficie = 2 * math.pi * radio * (radio + altura)
elif opcion == 4: #Cono
    radio = float(input("Radio de la base en [cm]: "))
    altura = float(input("Altura en [cm]: "))
    volumen = (1/3) * math.pi * (radio ** 2) * altura
    generatriz = math.sqrt((radio ** 2) + (altura ** 2))
    superficie = math.pi * radio * (radio + generatriz)
elif opcion == 5:  # Prisma Rectangular
    largo = float(input("Largo en [cm]: "))
    ancho = float(input("Ancho en [cm]: "))
    altura = float(input("Altura en [cm]: "))
    volumen = largo * ancho * altura
    superficie = 2 * (largo * ancho + largo * altura + ancho * altura)
else:
    print("Opción no válida.")
    exit()

print("El volumen de la figura es: %.3f " %volumen,"[cm3]")
print("La superficie de la figura es: %.3f " %superficie,"[cm2]")
