john = 10
adam = 6
mary = 5
precio_manzana = 3000
cantidad = 8
estudiantes = 5
manzanas = 47

print(john, adam, mary, sep=", ")
total_apples = john + adam + mary
print("Número total de manzanas:", total_apples)

print("\n--- Experimentar el codigo ---")
manzanas_restantes = total_apples - 3
print("Si john se roba 3, estarian quedando:", manzanas_restantes)

total_pagar = precio_manzana * cantidad
print("Precio total por 8 manzanas:", total_pagar, "pesos")

por_estudiante = manzanas // estudiantes
print("Cada estudiante recibe", por_estudiante, "manzanas enteras")