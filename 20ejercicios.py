opcion=int(input("Hola escriba el numero de la actividad que desea ver:"))
if opcion==1:
	print("Hola mundo")
elif opcion==2:
	nombre=input("Hola ingrese su nombre")
	print("Hola un gusto conocerte " ,nombre)
elif opcion==3:
	num1=int(input("Ingrese un número"))
	num2=int(input("Ingrese otro número"))
	print("La suma de los números es: " ,num1+num2)
elif opcion==4:
	num1=int(input("ingrese un número"))
	num2=int(input("ingrese otro número"))
	num3=int(input("ingrese un tercer número"))
	suma=num1+num2+num3
	float(print("El promedio de los 3 números es: " ,suma/3))
elif opcion==5:
	n=int(input("ingrese un número"))
	if n % 2 == 0:
   	 	print(n, "es par.")
	else:
    		print(n, "es impar.")
elif opcion==6:
	num1=int(input("ingrese un número"))
	num2=int(input("ingrese otro número"))
	if num1 < num2:
		print(num1," es mayor a ",num2)
	elif num1 > num2:
		print(num2, "es mayor a " ,num1)
	else:
		print(num1, " y " ,num2, " son del mismo valor")
elif opcion==7:
	edad=int(input("Ingrese su edad"))
	if edad >= 18:
		print("Usted es mayor de edad")
	elif edad < 18 and edad > 0:
		print("Usted es menor de edad")
	else:
		print("Ingreso un valor no valido")
elif opcion==8:
	grados=int(input("Ingrese una temperatura en grados celcius"))
	F =int((C × 9/5) + 32)
	print("Los grados " ,grados, " Celcius convertidos a Fahrenheit es: " ,F)
elif opcion==9:
	base=int(input("Ingrese el valor de la base del triangulo"))
	altura=int(input("Ingrese el valor de la altura del triangulo"))
	print("el area del triangulo es: " ,(base × altura) / 2)
elif opcion==10:
	n = int(input("Ingrese un número cualquiera"))
	if n > 0:
		print("El número es positivo")
	elif n < 0:
		print("El número es negativo")
	elif:
		print("El número 0 no cuenta como positivo ni como negativo")
elif opcion==11:
	a=input("Ingrese una palabra cualquiera")
	print("La número de caracteres en esa palabra es: " ,len(a))
elif opcion==12:
	a=input("Ingrese una palabra cualquiera")
	l1=a[0]
	l2=a[-1]
	print("La primera letra de la palbra ingresada es: " ,l1, " y la ultima letra es: " ,l2)
elif opcion==13:
	contraseña=input("Ingrese una contraseña")
	validacion=input("Ingrese la contraseña")
	if contraseña == validacion:
		print("La contraseña es correcta")
	elif: print("La contraseña es incorrecta")
elif opcion==14;
	year = int(input("Ingrese un año para comprobar si es bisiesto"))
	if year % 4 != 0:
		print("No es bisiesto")
	elif year % 4 == 0 and year % 100 != 0:
		print("Es bisiesto")
	elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
		print("No es bisiesto")
	elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: 
		print("Es bisiesto")
