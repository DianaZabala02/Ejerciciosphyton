sal_b= float(input("Ingrese el salario basico del vendedor: "))
val1= int(input("Ingrese el valor 1:"))
val2= int(input("Ingrese el valor 2:"))
val3= int(input("Ingrese el valor 3:"))
tvta= val1 + val2 + val3
com= tvta*0.10
tot_pag= sal_b + com
print(f"El total a pagar al vendedor es: {tot_pag}")