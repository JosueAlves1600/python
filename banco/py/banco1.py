# exemplo de utilização: 


def saque(saldo, valor_saque):


    return saldo - valor_saque



def deposito(saldo, valor_deposito):
    return saldo +  valor_deposito


def extrato (saldo):
    return saldo



def banco():
   op = input('1 - saque - 2 - deposito - 3 - extrato')
   saldo = 50000.
   if op == '1':
      valor_saque =  float(input('R$: '))
      saque2  =  saque(saldo, valor_saque)
      print('Saque - ', valor_saque )
      print('Em conta R$: ', saque2)
   elif op == '2':
      valor_deposito =  float(input('R$: '))
      total  =  deposito(saldo, valor_deposito)
      print('Saque - ', valor_deposito )
      print('Em conta R$: ', total)
   elif op == '3':
        saldo =  extrato(saldo)
        print('R$',saldo)         


banco()