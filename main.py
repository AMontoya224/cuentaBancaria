from cuentaBancaria import CuentaBancaria

cuenta_1 = CuentaBancaria(0.02, 200)
cuenta_2 = CuentaBancaria(0.01, 500)

print("Cuenta #1")
cuenta_1.mostrar_info_cuenta()
cuenta_1.depósito(50).depósito(150).depósito(38).retiro(200).generar_interés().mostrar_info_cuenta()

print(" ")
print("Cuenta #2")
cuenta_2.mostrar_info_cuenta()
cuenta_2.depósito(75).depósito(25).retiro(250).retiro(400).generar_interés().mostrar_info_cuenta()

print(" ")
print("BONUS")
CuentaBancaria.todas_las_instancias()