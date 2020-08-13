ed=int(input("Digite su edad: "))
sexo=input("Digite si es Masculino o Femenino (M o F): ")

if sexo == 'F':
    npul= (220-ed)/10
    print(f"El numero de pulsaciones es: {npul}")
else:
    npul= (210-ed)/10
    print(f"El numero de pulsaciones que ud tiene es: {npul}")