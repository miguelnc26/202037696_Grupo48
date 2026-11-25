# Tarea 3 - Mapeo de Datasheets a Diccionarios
# Escenario 2: Giroscopio e Inclinómetro MPU6050
# Autor: Eduin Miguel Nuñez Cobo

# Diccionario anidado con los registros del sensor
registro_mpu = {
    "0x3B": {
        "register_name": "ACCEL_XOUT_H",
        "bit_mask": 0xFF,
        "sampling_rate": 1000
    },
    "0x3D": {
        "register_name": "ACCEL_YOUT_H",
        "bit_mask": 0xE0,
        "sampling_rate": 1000
    },
    "0x6B": {
        "register_name": "PWR_MGMT_1",
        "bit_mask": 0x40,
        "sampling_rate": 100
    }
}

# Función para consultar un registro por su dirección
def consultar_registro(direccion):
    datos = registro_mpu.get(direccion)
    if datos is None:
        print(f"\nLa dirección {direccion} no existe en el mapa.")
        print("Direcciones válidas:", ", ".join(registro_mpu.keys()))
        return False
    print(f"\nRegistro: {direccion}")
    print(f" Nombre: {datos['register_name']}")
    print(f" Máscara: {hex(datos['bit_mask'])}")
    print(f" Frecuencia: {datos['sampling_rate']} Hz")
    return True

# Función para mostrar todos los registros disponibles
def mostrar_mapa_completo():
    print("\n=== MAPA DE REGISTROS MPU6050 ===")
    for direccion, datos in registro_mpu.items():
        print(f"{direccion}: {datos['register_name']} | {hex(datos['bit_mask'])} | {datos['sampling_rate']} Hz")

# Programa principal
def main():
    print("=== SISTEMA DE CONSULTA - TAREA 3 ===")
    mostrar_mapa_completo()
    
    max_consultas = 5
    contador = 0
    
    while contador < max_consultas:
        direccion = input("\nIngrese la dirección hexadecimal (o 'salir'): ")
        
        if direccion.lower() == "salir":
            print("Saliendo del sistema...")
            break
            
        if not direccion:
            print("Debe ingresar una dirección.")
            continue
            
        consultar_registro(direccion)
        contador += 1
        
    print("\n=== FIN DEL SCRIPT ===")

# Punto de entrada
if __name__ == "__main__":
    main()