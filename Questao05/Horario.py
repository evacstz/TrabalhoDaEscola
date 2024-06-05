hora = int(input("Digite uma hora entre 0 e 23: "))

if(hora <= 11):
    print("O horário é manhã")
elif(12 <= hora < 18):
    print("O horário é tarde")
else:
    print("O horário é noite")