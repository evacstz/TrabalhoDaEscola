hora = int(input("Digite uma hora entre 0 e 23: "))

if(hora <= 11):
    print("O horário é manhã")
elif(hora >= 12 <= 18):
    print("O horário é tarde")
else:
    print("O horário é noite")