txt = str(input('Type a text:'))
txt=''.join(txt)

txt_invet = txt[::-1] #i
somador = 0

for c in range(0,len(txt)):
    if txt[c] == txt_invet[c]:
        print('Phrase ACK!')
        break
    else:
        print('Phrase NACK!')
        break