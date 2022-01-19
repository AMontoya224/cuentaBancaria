class CuentaBancaria:
    todas_las_cuentas = []

    def __init__(self, tasa_interés=0.01, balance=0): 
        self.tasa_interés = tasa_interés
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)

    def depósito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if CuentaBancaria.estado(self.balance, amount):
            self.balance -= amount
        else:
            self.balance -= 5
            print("Fondos insuficientes: cobrando una tarifa de $5")
        return self

    def mostrar_info_cuenta(self):
        print("Balance: $" + str(self.balance))

    def generar_interés(self):
        if CuentaBancaria.estado(self.balance):
            self.balance += self.balance * self.tasa_interés
        return self

    @staticmethod
    def estado(balance, amount=0):
        if (balance - amount) > 0:
            return True
        else:
            return False
    
    @classmethod
    def todas_las_instancias(cls):
        for cuentas in cls.todas_las_cuentas:
            print("Tasa de interés: " + str(cuentas.tasa_interés) + ", Balance: $" + str(cuentas.balance))