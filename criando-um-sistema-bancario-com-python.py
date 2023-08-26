menu = '''Menu de opções:
1 = Saque
2 = Depósito
3 = Extrato
4 = Sair

Qual operação deseja realizar? 
'''
saque = 0
deposito = 0
extrato = str()
saldo = 0
quantidade_saques = 0
solicitacao = 0   # acrescentei essa variável para estabelecer um limite de solicitações


while menu != 4:
   opcao = float(input(menu))

   if opcao == 1: #saque
      saque = float(input('Quanto deseja sacar? \n'))
      while saque > 500: # saque excede limite
         solicitacao += 1
         saque = float(input(f'''Valores superiores a RS 500.00 não são permitidos para sua conta. 
Você tem mais {3 - solicitacao} tentativa(s)...
Digite um novo valor: \n'''))
         if solicitacao == 2 and saque > 500:
            print('Excesso de solicitações. Retornando ao menu principal...\n')
            break
      solicitacao = 0
      
      while saque > saldo: # saldo insuficiente
         if saldo == 0:
            print("O seu saldo está zerado. Retornando ao menu principal.\n")
            break
         else:
            solicitacao += 1
            saque = float(input(f'''Saldo insuficiente (R$ {saldo}). 
   Você tem mais {3 - solicitacao} tentativa(s)...
   Digite um novo valor: \n'''))
            if solicitacao == 2:
               print('Excesso de solicitações. Retornando ao menu principal.\n')
               break
      solicitacao = 0
      
      while quantidade_saques > 2: # ultrpassou limite de saque
         print('''Limite de saques diários atingido. 
Retornando ao menu principal...\n''')
         break
      
      if saque <= 500 and (saldo - saque >= 0) and quantidade_saques < 3:
         print('''Atenção à saída da máquina...
Pode retirar seu dinheiro!\n''')
         quantidade_saques += 1
         saldo -= saque
         extrato += (f'Realizado saque de R$ {saque:.2f}.\n')

   elif opcao == 2: # depósito
      deposito = float(input('Quanto deseja depositar? \n'))
      while deposito < 0:
         solicitacao += 1
         deposito = float(input(f'''Opção inválida. 
Você tem mais {3 - solicitacao} tentativa(s)...
Digite um novo valor: \n'''))
         if solicitacao == 2 and deposito < 0:
            print('Excesso de solicitações. Retornando ao menu principal.\n')
            break    
      
      if deposito > 0:
         saldo += deposito
         print(f'''Depósito realizado com sucesso!
Seu saldo atual é de R$ {saldo:.2f}\n''')
         extrato += (f'Realizado depósito de R$ {deposito:.2f}.\n')
      solicitacao = 0 

   elif opcao == 3: # extrato
      if saque == 0 and deposito == 0: 
         print(f'''{10*"#"} EXTRATO BANCÁRIO {10*"#"}\n
Não houveram movimentações.
Saldo: R$ {saldo:.2f}\n''')
      else:
         print(f'''{38*"#"}\n''')
         print(f'''{10*"#"} EXTRATO BANCÁRIO {10*"#"}\n
{extrato}\n
Saldo: R$ {saldo:.2f}\n''')
         

   elif opcao == 4: # sair
      print('''Operação finalizada.
Tenha um bom dia!\n''')
      print(f'''{38*"#"}\n''')
      break
   
   else:
      print('Opção inválida. Tente novamente\n')
