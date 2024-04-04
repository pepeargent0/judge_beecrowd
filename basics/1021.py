n = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for nota in notas:
    quantidaden = int(n / nota)
    print('{} nota(s) de R$ {:.2f}'.format(quantidaden, nota))
    n -= quantidaden * nota

print('MOEDAS:')
for moeda in moedas:
    quantidadem = int(n / moeda)
    print('{} moeda(s) de R$ {:.2f}'.format(quantidadem, moeda))
    n -= quantidadem * moeda