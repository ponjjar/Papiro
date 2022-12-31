cidade = input('Digite uma cidade: ').strip()
cidadem = cidade.lower()
div = cidadem.split()

n = 0
if 'santo' in div[0]:
    print('A cidade começa com santo no nome.')

else:
    print('A cidade não começa com santo no nome.')