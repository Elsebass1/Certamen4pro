'''
cartas = { "A001": {"nivel": "***", "energia": 45}, 
"B107": {"nivel": "*", "energia": 10}, 
... 
}
'''
carta = {}

def agregar_carta(cartas, codigo, datos):
    if codigo in cartas:
        return False
    try:
        Energia_inicial = int(datos[0])
        if Energia_inicial < 0:
            return False
        cartas[codigo] = {
            'Gasto': 0,
            'Energia': Energia_inicial
        }
        return True
    except:
        return False

def usar_carta(cartas, codigo, monto):
    if codigo not in cartas:
        return False
    try:
        monto = int(monto)
        if monto <= 0:
            return False
        if cartas[codigo]['Energia'] >= monto:
            cartas[codigo]['Energia'] -= monto
            cartas[codigo]['Gasto'] += 1
            return True
        else:
            return False
    except:
        return False

def listar_cartas(cartas):
    for codigo, datos in cartas.items():
        print(f"la carta {codigo} -> tiene: {datos['Gasto']} uso, y una Energia de: {datos['Energia']}")

def cartas_con_poca_energia(cartas, umbral):
    try:
        umbral = int(umbral)
        for codigo, datos in cartas.items():
            if datos['Energia'] < umbral:
                print(f"La carta de codigo: {codigo} tienes energia crítica: {datos['Energia']}")
    except:
        print("Energia mínima inválida")

while True:
    print("--- MENÚ JUEGO DE CARTAS ---")
    print("1. Registrar carta")
    print("2. Usar carta")
    print("3. Listar carta")
    print("4. Ver cartas con poca energia")
    print("5. Salir")
    
    opcion = input("Opción: ")
    
    if opcion == '1':
        codigo = input("Ingrese código de carta: ")
        while True:
            try:
                saldo = int(input("Energia inicial: "))
                break
            except:
                print("Debe ingresar un número válido.")
        if agregar_carta(carta, codigo, [saldo]):
            print("Carta registrada.")
        else:
            print("No se pudo registrar la carta (ya existe o Energia inválida).")

    elif opcion == '2':
        codigo = input("Código de carta a usar: ")
        while True:
            try:
                monto = int(input("Monto de uso de energia: "))
                break
            except:
                print("Monto debe ser un número válido.")
        if usar_carta(carta, codigo, monto):
            print("Uso de energia realizado con éxito.")
        else:
            print("Uso no autorizado (Energia insuficiente o carta no existe).")

    elif opcion == '3':
        listar_cartas(carta)

    elif opcion == '4':
        while True:
            try:
                critico = int(input("Energia mínima para alerta: "))
                break
            except:
                print("Debe ser un número válido.")
        cartas_con_poca_energia(carta, critico)

    elif opcion == '5':
        print("Saliendo del sistema.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")