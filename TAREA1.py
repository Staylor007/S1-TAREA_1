# EJERCICIOS DE TAREA 1
# Nombre: Stalin Manuel Espinoza Calle
# Semestre: 4to Nivel
# Carrera: Ingenieria de Software

# ESTRUCTURAS SECUENCIALES
#* En una tienda se ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber 
#* cuánto deberá pagar finalmente por su compra.

class DEBER1:
    def __init__(self):
        pass
    def descuento(self):
        totCompra = float(input("Ingrese el total de compra: "))
        descu = totCompra * 0.15           # 15% --- 0.15
        cantPagar = totCompra - descu
        print("*** El cliente debera pagar finalmente : $ {}  y el descuento es de : $ {} ***"  .format(cantPagar,descu))
        
        print("******************************************************************************************************")




# ESTRUCTURAS SECUENCIALES
#* Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas. 
#* El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas 
#* que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y sus comisiones.

    def sueldo(self):
        salarBase = float(input(("Ingrese el sueldo base : ")))
        val1 = float(input(("Ingrese el primer valor : ")))
        val2 = float(input(("Ingrese el segundo valor : ")))
        val3 = float(input(("Ingrese el tercer valor : ")))
        totVentas = val1 + val2 + val3
        com = totVentas * 0.1               # 10%  ----- 0.1
        totRecib = salarBase + com
        print("*** El total del sueldo que recibira es de: $ {}  ***"  .format(totRecib,com))
        
        print("******************************************************************************************************")
        
        


# ESTRUCTURAS SELECTIVAS SIMPLES
#* Construir un algoritmo tal, que dado como dato la calificación de un alumno en un examen, escriba
#* “Aprobado” en caso que esa calificación fuese mayor o igual que 7.

    def calificacion(self):
        calif = float(input("Ingrese la nota del examen: "))
        if calif >= 7:
            print("*** ESTA APROBADO ***")
        else:
            return
        
        print("******************************************************************************************************")
        
        
        
        
        
# ESTRUCTURAS SELECTIVAS DOBLES
#* Dado como dato la calificación de un alumno en un examen, escriba “aprobado” 
#* si su calificación es mayor o igual que 7 y “Reprobado” en caso contrario.

    def calificacionExamen(self):
        nota = float(input("Ingrese la nota del examen: "))
        if nota >= 7:
            print("*** ESTA APROBADO ***")
        else:
            print("*** REPROBADO ***")
            
            print("******************************************************************************************************")
        





#ESTRUCTURAS SELECTIVAS DOBLES
#* Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10% 
#* si su sueldo es inferior a $600, en caso contrario no tendrá aumento.

    def empleado(self):
        sueldo = 0
        sueldo = float(input("Ingrese el sueldo del empleado: "))
        if sueldo < 600:
            nueSueldo = sueldo * 0.10          # 10%----0.1
            print("*** El nuevo sueldo del empleado es de : $ {} ***" .format(nueSueldo))
        else:
            print("*** No tendra aumento ***")
            
        print("******************************************************************************************************")
        




# ESTRUCTURAS SELECTIVAS COMPUESTAS
#* Determinar la cantidad de dinero que recibirá un trabajador por concepto de las horas extras trabajadas en una empresa,
#* sabiendo que cuando las horas de trabajo exceden de 40, el resto  se consideran horas extras y que éstas se pagan 
#* al doble de una hora normal cuando no exceden de 8;  si las horas extras exceden de 8 se pagan las primeras 8 al doble 
#* de lo que se paga por una hora normal y el resto al triple.

    def pagoJornadaExtra(self):
        horas_trabajadas, horas_extras, horas_extras_triple = 0,0,0
        valor_hora, pago_horas_extras,pago_total = 0,0,0
        horas_trabajadas = int(input("Ingrese horas trabajadas: "))
        valor_hora = float(input("Ingrese el valor de hora: "))
        
        if(horas_trabajadas > 40):
            horas_extras = horas_trabajadas - 40
            if (horas_extras > 8):
                horas_extras_triple = horas_extras - 8
                pago_horas_extras = valor_hora * 2 * 8 + valor_hora * 3 * horas_extras_triple
            else:
                pago_horas_extras = valor_hora * 2 * horas_extras
            pago_total = valor_hora * 40 + pago_horas_extras
        
        else:
            pago_total = valor_hora * horas_trabajadas
        print("""*** Horas trabajadas:{}    *** Horas Extras: {} ***   *** Horas Triple: {} ***  
              *** Valor Hora: {} ***     *** Pago Extra: {} ***    *** Pago Total: {} ***"""
              .format(horas_trabajadas, horas_extras, horas_extras_triple,valor_hora,pago_horas_extras,pago_total))
        
        print("******************************************************************************************************")
        
        
        



# ESTRUCTURAS SELECTIVAS COMPUESTAS
#* Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres.

    def numerosEnteros(self):
        n1,n2,n3=0,0,0
        n1 = int(input("Ingrese Numero1: "))
        n2 = int(input("Ingrese Numero2: "))
        n3 = int(input("Ingrese Numero3: "))
        if(n1>n2>n3):
            print("*** El numero mayor es: ",(n1)," ***")
        elif(n2>n1>n3):
            print("*** El numero mayor es: ",(n2)," ***")
        else:
            print("*** El numero mayor es: ",(n3)," ***")
        
        print("******************************************************************************************************")






# ESTRUCTURAS SELECTIVAS MULTIPLES
#* Diseñar un algoritmo tal que dados como datos dos variables de tipo entero, obtenga el resultado de la siguiente función:

    def funcion(self):
        num = float(input(("Ingrese un numero : ")))
        var = float(input(("Ingrese cualquier valor : ")))
        
        if num == 1:
            resul = 100 * var
        elif num == 2:
            resul = 100 ** var
        elif num == 3:
            resul = 100 / var
        else:
            resul = 0
        print("*** El resultado de la siguiente funcion es de : {} ***" .format(resul))
        
        print("******************************************************************************************************")
        
        





# EXPRESIONES LOGICAS
#* Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene dos calificaciones denotadas 
#* como C1 y C2. El aspirante que obtenga calificaciones mayores que 80 en ambos exámenes es aceptado; 
#* en caso contrario es rechazado.

    def aspirante(self):
        cal1 = float(input(("Ingrese la primera calificacion : ")))
        cal2 = float(input(("Ingrese la segunda calificacion : ")))
        if cal1 >= 80 and cal2 >= 80:
            print("*** Es aceptado ***")
        else:
            print("*** Rechazado ***")
        # USO DEL OR
        if cal1 >= 90 or cal2 >= 90:
            print("*** Es aceptado ***")
        else:
            print("*** Rechazado ***")
        
        print("******************************************************************************************************")
        
        
        



# ESTRUCTURA FOR
#* Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado.

    def cuadrado(self):
        for var in range(1,101):    # el rango de todos los cuadrados aumentando uno
            suma = 0
            cuadr = (var) * (var)
            suma = suma + cuadr
            print("*** El cuadrado de {} es = {} ***".format(var,cuadr))
        print("*** La suma total de los cuadrados es de: {} ***".format(suma))
        
        print("******************************************************************************************************")





# ESTRUCTURA WHILE
#* Elabore pseudocódigo para el caso en que se desean escribir los números del 1 al 100.

    def caso(self):
        i = 0
        while i < 100:
            i = i + 1
            print(i ," * ", end=" ")
        
        print("******************************************************************************************************")





# ESTRUCTURA WHILE
#* Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, 
#* utilizando un bucle controlado por el usuario.

    def bucle(self):
        i = 1
        suma = 0
        resp = int(input("Ingrese cantidad de los numeros que va realizar: "))
        while i <= resp:
            num = int(input("Ingrese su numero: "))
            suma = suma + num
            i = i + 1
            produc = suma * num
        print("*** La suma total de los numeros es de: {} ***".format(suma))
        print("*** El total del producto es: {} ***".format(produc))
        
        print("******************************************************************************************************")





# ESTRUCTURA WHILE
#* Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, utilizando un bucle controlado por centinela.

    def centinela(self):
        suma = 0
        prod = 1
        num = int(input("Ingrese un numero diferente a -1 : "))
        while num != -1:
            suma = suma + num
            prod = prod * num
            num = int(input("Ingrese otro numero( Para salir ingrese -1): "))
        print("*** La suma total de los numeros enteros es: {}***".format(suma))
        print("*** El producto total de los numeros enteros es: {}***".format(prod))
        
        print("******************************************************************************************************")






# ESTRUCTURA WHILE
#* Determinar si un número entero proporcionado por el usuario es primo. Un número primo es un entero que no tiene 
#* más divisores que él mismo y la unidad.

    def numeroPrimos(self):
        primo = "T"
        divis = 2
        num = int(input("Ingrese un numero entero: "))
        while divis < num and primo == "T":
            resul = num % divis
            if resul == 0:
                primo = "F"
            divis = divis + 1
        if primo == "V":
            print("*** El numero {} es primo ***".format(num))
        else:
            print("*** El numero {} no es primo ***".format(num))
        
        print("******************************************************************************************************")






# ESTRUCTURA REPEAT
#* Aplicar los pasos de la metodología para la solución de un problema para leer un número entero N y calcular el resultado de la siguiente serie:
#* 1 – 1/2+ 1/3 – 1/4 +.... +/- 1/N. Resolveremos el problema utilizando bucle Repeat controlado por contador y usando banderas.

    def bucleRepeat(self):
        serie = 0
        l = 1
        num = int(input("Ingrese un numero entero : "))
        band = "T"
        while l < num:
            if band == "T":
                serie = serie + (1/1)
                band = "F"
            else:
                serie = serie - (1/1)
                band = "T"
            l = l + 1
            
        print("*** El resultado de la serie es de: {} ***".format(serie))
        
        print("******************************************************************************************************")





# BUCLES ANIDADOS
#*Calcular el factorial de N números enteros leídos de teclado.
#* El problema consistirá en realizar una estructura de N iteraciones aplicando el factorial de un número.

    def factorial(self):
        numero = int(input("Ingrese un numero: "))
        fact = 1
        if numero != 0:
            for i in range(1,numero +1):
                fact = fact * i
        print("*** EL factorial del numero {} es de: {} ***".format(numero,fact))
        
        print("******************************************************************************************************")





# ARREGLOS EN UNA DIMENSION
#* Sea un vector “Calificaciones” de 100 componentes:

    def vectorCalif(self):
        calificaciones=[]
        a = 0
        b = 1
        for i in range(0,100,1):
            cal=int(input("Escriba su calificación: "))
            calificaciones.append(cal)
            a = a + 1
            print("")
        for i in range (0,a,1):
            b = b + 1
            print("*** La calificación {} es {} ***".format(b,calificaciones[i]))
            
        print("******************************************************************************************************")





# ARREGLOS DE UNA DIMENSION
#* Aplicar las fases  para  la resolución de un problema para leer un vector de 20 números enteros y a continuación 
#* escribir en un vector A todos los números negativos y en un vector B todos los positivos o iguales a cero. 
#* Imprimir dichos vectores.

    def vectores(self):
        A = []
        B = []
        j = 0
        k = 0
        num = []
        for i in range (0,20,1):
            n = int(input("Ingrese un numero: "))
            num.append(n)
            if num[i] < 0:
                A.insert(j,num[i])                
                j = j + 1
            else:
                B.insert(k,num[i])
                k = k + 1
        for i in range(0,j,1):
              print("*** Vector A tiene el valor de {} ***".format(A[i]))  
        for i in range (0,k,1):
              print("*** Vector B tiene el valor de {} ***".format(B[i]))
              
        print("******************************************************************************************************")






# ARREGLOS DE DOS DIMENSIONES
#* Se tiene información sobre las calificaciones de 6 exámenes de un grupo de 30 alumnos. 
#* Los datos sobre estos exámenes se proporcionan de la siguiente manera:

    def dimensiones(self):
        calif = []
        prom = []
        for i in range(30):
            calif.append([])
            for j in range(30):
                calif[i].append(None)
                calif[i][j] = float(input("Ingresar calificacion que obtuvo el alumno {} en el examen {}: ".format(i + 1,j + 1)))
        for i in range(30):
            for j in range(30):
                print(calif[i][j],end=" ")
            print() 
        for j in range(30):
            sum = 0
            for i in range(30):
                sum=sum + calif[i][j]
            prom.append(sum/len(calif))
            print("El promedio del examen {} : {:.2f}".format(j + 1,sum/len(calif)))   # Agregue {}:.2f} por los decimales
        for i in range(30):
            sum = 0
            for j in range(30):
                sum = sum + calif[i][j]
            print("El promedio del alumno {} : {:.2f}".format(i + 1,sum/len(calif)))   
        examen = 0
        proMayor = prom[1]
        for j in range(30):    
            if proMayor < prom[j]:
                proMayor = prom[j]
                examen = j
        print("El examen {} obtuvo el mayor promedio siendo este: {}".format(examen + 1,proMayor))




deber = DEBER1()
deber.descuento()
deber.sueldo()
deber.calificacion()
deber.calificacionExamen()
deber.empleado()
deber.pagoJornadaExtra()
deber.numerosEnteros()
deber.funcion()
deber.aspirante()
deber.cuadrado()
deber.caso()
deber.bucle()
deber.centinela()
deber.numeroPrimos()
deber.bucleRepeat()
deber.factorial()
deber.vectorCalif()
deber.vectores()
deber.dimensiones()
