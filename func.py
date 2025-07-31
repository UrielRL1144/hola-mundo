def sumar_cualquier_cantidad_numeros():
    entrada = input("Es importante que solo sean número enteros, especificar sin número decimal: ")
    numeros_str = entrada.strip().split()

    try:
        numeros = [float(n) for n in numeros_str]
        suma = sum(numeros)
        print(f"La suma de los {len(numeros)} números es: {suma}")
    except ValueError:
        print("Error: Asegúrate de ingresar solo números válidos separados por espacios.")

sumar_cualquier_cantidad_numeros()
