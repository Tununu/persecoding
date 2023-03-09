a = str(input())

if a == '+':
    print('+&><+&><')
elif a == '&':
    print('&><+&><+')
elif a == '>':
    print('><+&><+&')
elif a == '<':
    print('<+&><+&>')

    
    
character = input()
dance = '<+$>'
ind = dance.index(character)
for i in range(8):
    print(dance[(ind + i)%4], end='')
