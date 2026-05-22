quantidadeh = int(input("Quantidade de horas trabalhadas: "))
valor = float(input("Valor por hora: "))

salario = quantidadeh * valor
salarioB = (1+quantidadeh**1.5/valor**2.5) *salario

