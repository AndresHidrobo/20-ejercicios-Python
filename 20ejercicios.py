opcion=1
while opcion>=1 and opcion <=20:
	opcion=int(input("Escriba el numero de la actividad que desea ver (Si desea finalizar ingrese algún valor no disponible):"))
	if opcion==1:
		print("Hola mundo")
	elif opcion==2:
		nombre=input("Hola ingrese su nombre ")
		print("Hola un gusto conocerte" ,nombre)
	elif opcion==3:
		num1=int(input("Ingrese un número "))
		num2=int(input("Ingrese otro número "))
		print("La suma de los números es: " ,num1+num2)
	elif opcion==4:
		num1=int(input("ingrese un número "))
		num2=int(input("ingrese otro número "))
		num3=int(input("ingrese un tercer número "))
		suma=num1+num2+num3
		print("El promedio de los 3 números es: " ,suma/3)
	elif opcion==5:
		n=int(input("ingrese un número "))
		if n % 2 == 0:
   	 		print(n, "es par.")
		else:
    			print(n, "es impar.")
	elif opcion==6:
		num1=int(input("ingrese un número "))
		num2=int(input("ingrese otro número "))
		if num1 > num2:
			print(num1," es mayor a ",num2)
		elif num1 < num2:
			print(num2, "es mayor a " ,num1)
		else:
			print(num1, " y " ,num2, " son del mismo valor")
	elif opcion==7:
		edad=int(input("Ingrese su edad "))
		if edad >= 18:
			print("Usted es mayor de edad ")
		elif edad < 18 and edad > 0:
			print("Usted es menor de edad ")
		else:
			print("Ingreso un valor no valido ")
	elif opcion==8:
		C=int(input("Ingrese una temperatura en grados celcius "))
		F =float((C*9/5) + 32)
		print("Los grados ",C," Celcius convertidos a Fahrenheit es: " ,F)
	elif opcion==9:
		base=int(input("Ingrese el valor de la base del triangulo "))
		altura=int(input("Ingrese el valor de la altura del triangulo "))
		print("el area del triangulo es: " ,(base*altura) / 2)
	elif opcion==10:
		n = int(input("Ingrese un número cualquiera "))
		if n > 0:
			print("El número es positivo")
		elif n < 0:
			print("El número es negativo")
		else:
			print("El número 0 no cuenta como positivo ni como negativo")
	elif opcion==11:
		a=input("Ingrese una palabra cualquiera ")
		print("La número de caracteres en esa palabra es: " ,len(a))
	elif opcion==12:
		a=input("Ingrese una palabra cualquiera ")
		l1=a[0]
		l2=a[-1]
		print("La primera letra de la palbra ingresada es: " ,l1, " y la ultima letra es: " ,l2)
	elif opcion==13:
		contraseña="python123"
		validacion=input("Verifique la contraseña ")
		if contraseña == validacion:
			print("Acceso concedido")
		else: print("Acceso denegado")
	elif opcion==14:
		year = int(input("Ingrese un año para comprobar si es bisiesto "))
		if year % 4 != 0:
			print("No es bisiesto")
		elif year % 4 == 0 and year % 100 != 0:
			print("Es bisiesto")
		elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
			print("No es bisiesto")
		elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: 
			print("Es bisiesto")
	elif opcion==15:
		print("En este ejercicio se suman los números del 1 al 10 ")
		suma = 0
		for i in range(1, 11):
	    		suma += i
		print("La suma siempre será ",suma)
	elif opcion==16:
		cad=input("Ingrese una palabra cualquiera ")
		vocales=0
		for c in cad:
			if c in "aeiouAEIOUáéíóúÁÉÍÓÚ":
				vocales = vocales + 1
		print("El número de vocales en la palabra es: ",vocales)
	elif opcion==17:
		num=int(input("Ingrese un número para imprimir su tabla de multiplicar "))
		for i in range(1, 11):
			mult=num*i
			print(num,"X",i,"=",mult)
	elif opcion==18:
		num=int(input("Ingrese un numero cualquiera "))
		if num >=0 and num<=100:
			print("El número ingresado está entre 1 y 100")
		else:
			print("El número está por fuera del rango entre 1 y 100")
	elif opcion==19:
		a=input("Ingrese una palabra cualquiera ")
		n=int(input("Ingrese un número cualquiera "))
		for i in range(0,n):
			print(a)
	elif opcion==20:
		num=1
		suma=0
		while num != 0:
			num=int(input("Ingrese un número "))
			suma=suma+num
		else:
			print("La suma de todos los número ingresados es: ",suma)
	else:
		print("Se finalizo el proceso")
