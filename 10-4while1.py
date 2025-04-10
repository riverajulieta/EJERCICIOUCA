contra = "UCA2025"
entrada = ""
intentos = 0

while entrada != contra and intentos < 3:
    entrada = input("Ingrese su contrasenia: ")
    if entrada != contra:
        print("Incorrecta-siga participando:")
        intentos += 1

if entrada == contra:
    print("Correcto!!!")
else:
    print("No hay más intentos.")
