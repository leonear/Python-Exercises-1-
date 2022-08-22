import math 

custo = float(input('Custo espetáculo:'))
ingresso = float (input ('Preço ingresso:'))
min = custo/ingresso
lucro = custo*0.23+custo
ingressolucro = math.ceil(lucro)/ingresso

print("Mínimo de ingressos:", math.ceil(min))
print("Valor com o lucro de 23%:", lucro)
print("Ingressos para ter lucro de 23%:", math.ceil(ingressolucro))
