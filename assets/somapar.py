print "Este programa soma os pares com os pares e os impares com os impares"
print "Insere 3 numeros, carregando enter entre cada entrada"
num1 = float(raw_input())
num2 = float(raw_input())
num3 = float(raw_input())

if num1 % 2 == 0:
   test1 = num1
   num1 = 0
else:
    num1 = num1
    test1 = 0

if num2 % 2 == 0:
   test2 = num2
   num2 = 0
else:
    num2 = num2
    test2 = 0

if num3 % 2 == 0:
   test3 = num3
   num3 = 0
else:
    num3 = num3
    test3 = 0

somapar = test1 + test2 + test3
somaimp = num1 + num2 + num3

print "Esta e a soma dos pares com pares e impares com impares:"
print "Soma dos pares", somapar
print "soma dos impares", somaimp

 


