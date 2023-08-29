def divide():

    try:

        op1=(float(input("Introduce el primer número: ")))

        op2=(float(input("Introduce el primer número: ")))

        print("La division es: "+str(op1/op2))

    except ValueError:

        print("El valor introducido es erroneo")

    except ZeroDivisionError:  

        print("No se puede dividir entre 0")

    finally: #Se ejecuta independiente del escenario actual

        print("Calculo finalizado")

divide()