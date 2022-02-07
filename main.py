def division(a, b):
    try:
        result = a / b
        if result < 0:
            raise ValueError('Lo siento, No numeros negativos')
    except ZeroDivisionError:
        print("El divisor no puede ser cero") 
    except TypeError:
        print('¡Solo ingresar caracteres numericos!')
    else:
        print('El resultado es:',result) 
    finally:
        print('Fin del programa')
division(10, 5)




