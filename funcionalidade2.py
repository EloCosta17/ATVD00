peso = float(input("Seu peso (em KG):"))
altura = float(input("Sua altura (em M):"))
idade = int(input("Sua idade:"))

altura = altura * 100

bmr = 10 * peso + 6.25 * altura - 5 * idade + 5

print(f"{bmr:.1f}")