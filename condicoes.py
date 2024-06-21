'''JOGO DA FORCA'''
import random

from listaforca import lista


escolher_letras = []
chances = 5
ganhar = False
palavra_secreta = random.choice(lista)

print('----x----x---- JOGO DA FORCA ----x----x----')



while True:
   for letra in palavra_secreta:
      if letra.upper() in escolher_letras:
        print(letra, end=' ')
      else:
        print('_', end=' ')
   print(f'Você tem {chances} chances.')
   tentativas = input('Digite uma letra para adivinhar a palavra secreta: ')
   escolher_letras.append(tentativas.upper())
   if tentativas.upper() not in lista:
      chances -= 1

   ganhar = True
   for letra in palavra_secreta:
      if letra.upper() not in escolher_letras:
         ganhar = False

   if chances == 0 or ganhar:

      break