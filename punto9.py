p= float(input("Digite la presion: "))
v= float(input("Digite el volumne: "))
t= float(input("Digite la temperatura: "))
m= (p*v)/(0.37*(t+460))
print(f"La presion es: {p}")
print(f"el volumen es: {v}")
print(f"la temperatura es: {t}")
print(f"El valor de la masa es: {m}")