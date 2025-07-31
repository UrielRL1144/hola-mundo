def multiplicar_cualquier_cantidad_numeros():
    entrada = input("Ingresa los números separados por espacio (puede ser cualquier cantidad): ")
    numeros_str = entrada.strip().split()

    try:
        numeros = [float(n) for n in numeros_str]
        resultado = 1
        for num in numeros:
            resultado *= num
        print(f"El resultado de multiplicar los {len(numeros)} números es: {resultado}")
    except ValueError:
        print("Error: Asegúrate de ingresar solo números válidos separados por espacios.")

multiplicar_cualquier_cantidad_numeros()
