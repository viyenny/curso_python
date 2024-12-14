tipo_usuario = input("Ingrese el tipo de usuario A, B o C (Mayúscula): ")
if tipo_usuario == "A":
    valor_base = 150000
    descuento = 0.17
elif tipo_usuario == "B":
    valor_base = 650000
    descuento = 0.22
elif tipo_usuario == "C":
    valor_base = 950000
    descuento = 0.27
else:
    print("Error: Tipo de usuario no válido.")
    exit()# Finaliza el programa si el tipo de usuario no es válido
puntaje = int(input("Ingrese el puntaje obtenido (entre 10 y 17): "))
puntos_porcentuales = 75000 * puntaje
valor_matricula = valor_base + puntos_porcentuales
print("El valor de la matricula es: $%.2f" % valor_matricula)

if puntaje == 17:
    valor_con_descuento = valor_matricula * (1 - descuento) 
    print("El valor de la matricula con descuento es: $%.2f" %valor_con_descuento)




