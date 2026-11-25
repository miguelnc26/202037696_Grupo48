# ESCENARIO 3: Sistema de Bombeo Hidroeléctrico
# Sensor ultrasónico Microsonic
# Refactorizado por: Eduin Miguel Nuñez Cobo

nivel = 50
monitoreo = True
contador = 0

print("=== SISTEMA DE BOMBEO HIDROELÉCTRICO ===")
print(f"Nivel inicial: {nivel}%\n")

while monitoreo:
    contador += 1
    if contador > 20:
        print("Límite de iteraciones alcanzado. Finalizando monitoreo.")
        monitoreo = False
        break

    if nivel == 0 or nivel == 100:
        estado = "ERROR: Falla de lectura del sensor"
        print(f"Iteración {contador}: {estado}")
        monitoreo = False
    elif nivel < 15:
        estado = "Bomba encendida - Nivel bajo"
        print(f"Iteración {contador}: {estado}")
        nivel += 5
    elif 15 <= nivel <= 85:
        estado = "Operación hidráulica normal"
        print(f"Iteración {contador}: {estado}")
        nivel += 2
    else:
        estado = "Bomba apagada - Tanque lleno"
        print(f"Iteración {contador}: {estado}")
        nivel -= 4
        
    print(f"Nivel actual: {nivel:.0f}%\n")

print("=== FIN DEL MONITOREO ===")