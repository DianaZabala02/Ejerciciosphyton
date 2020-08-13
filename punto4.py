cali1= float(input("Digite la calificacion 1 del estudiante: "))
cali2= float(input("Digite la calificacion 2 del estudiante: "))
cali3= float(input("Digite la calificacion 3 del estudiante: "))
exaf= float(input("Digite la calificacion del examen final: "))
trfinal= float(input("Digite la calificacion del trabajo final: "))
prom= (cali1 + cali2 + cali3)/3
pparc= prom * 0.55
promf= exaf*0.30
promtfin= trfinal * 0.15
calfinal= pparc + promf + promtfin
print(f"La calificacion final del estudiante es: {calfinal: .2f}")