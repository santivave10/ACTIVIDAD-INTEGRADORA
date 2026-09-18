def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def km_a_mi(km):
    return km * 0.621371

def mi_a_km(mi):
    return mi * 1.609

TASA_CAMBIO = 17.23

def pesomex_a_dolar(pesomex):
    return pesomex / TASA_CAMBIO

def dolar_a_pesomex(dolar):
    return dolar * TASA_CAMBIO

def ejecutar_conversion(operacion, valor):
    match operacion:
        case 1:
            return celsius_a_fahrenheit(valor)

        case 2:
            return fahrenheit_a_celsius(valor)

        case 3:
            return km_a_mi(valor)

        case 4:
            return mi_a_km(valor)

        case 5:
            return pesomex_a_dolar(valor)

        case 6:
            return dolar_a_pesomex(valor)

        case _:
            return "Operación no válida"

while True:
    print("===============================\n     CONVERSOR DE UNIDADES \n===============================")
    print(" 1. Celsius → Fahrenheit\n 2. Fahrenheit → Celsius\n 3. Kilómetros → Millas\n 4. Millas → Kilómetros\n 5. Pesos Mexicanos → Dólares\n 6. Dólares → Pesos Mexicanos\n 7. Salir")
    try:
        operacion = int(input("Seleccione una opción: "))

        if operacion < 1 or operacion > 7:
            print("Opción inválida")
        elif operacion == 7:
            print("Programa finalizado.")
            break
        else:
            valor = float(input("Ingresa el valor: "))
            resultado = ejecutar_conversion(operacion, valor)
            print(f"Resultado: {resultado:.2f}")
    except ValueError:
        print("Error: debes ingresar un valor numérico.")