print "Este programa le 3 numeros e diz qual deles e o maior"
print "Insere tres numeros, dando um enter entre cada um"

num1 = raw_input()
num2 = raw_input()
num3 = raw_input()

if num1 == num2 == num3:
    print "Os numeros sao iguais"
else:
   if num1 > num2 and num1 > num3:
    print num1, "e o maior dos tres numeros"
   else:
    pass

   if num2 > num1 and num2 > num3:
    print num2, "e o maior dos tres numeros"
   else:
    pass

   if num3 > num1 and num3 > num2:
    print num3, "e o maior dos tres numeros"
   else:
    pass

