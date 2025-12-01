"""Gerador Suprassumo para Aritmética - 25+ tipos de questões"""
import random
import math

NOMES = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo", "Fernanda", "Gabriel", "Helena"]
SOBRENOMES = ["Silva", "Santos", "Oliveira", "Pereira", "Martins", "Sousa", "Rodrigues", "Alves"]

def gerar_arimetica_suprassumo(qtd, dif):
    questoes = []
    for i in range(qtd):
        nome = f"{random.choice(NOMES)} {random.choice(SOBRENOMES)}"
        
        if dif == "fácil":
            tipo = (i % 15) + 1
            if tipo <= 3:
                n = random.randint(10, 100)
                divisor = random.randint(2, 9)
                resp = "Sim" if n % divisor == 0 else "Não"
                resto = n % divisor
                enum = f"É {n} divisível por {divisor}?"
                opcoes = ["Sim", "Não", "Talvez", "Depende", "Indeterminado"]
                res = f"{n} ÷ {divisor} = {n//divisor} com resto {resto}. Logo {resp}."
                dica = "Verifique se a divisão é exata (resto zero)"
                erro = "Esquecer o resto"
            elif tipo <= 6:
                enum = "Qual é o critério de divisibilidade por 2?"
                opcoes = ["Número é par", "Termina em 0 ou 5", "Soma dos dígitos par", "Divisível por 10", "Sempre"]
                res = "Um número é divisível por 2 se termina em 0, 2, 4, 6 ou 8 (par)."
                dica = "Olhe apenas o último dígito"
                erro = "Contar todos os dígitos"
            elif tipo <= 9:
                enum = "Qual é o critério de divisibilidade por 3?"
                opcoes = ["Soma dos dígitos divisível por 3", "Termina em 3", "É ímpar", "Divisível por 9", "Nunca"]
                res = "Soma dos dígitos divisível por 3 ⟹ número divisível por 3."
                dica = "Some todos os algarismos e veja se resultado é divisível por 3"
                erro = "Usar último dígito"
            elif tipo <= 12:
                n = random.randint(100, 1000)
                soma = sum(int(d) for d in str(n))
                resp = "Sim" if soma % 3 == 0 else "Não"
                enum = f"Soma dos dígitos de {n} é {soma}. É divisível por 3?"
                opcoes = ["Sim", "Não", "Talvez", "Indeterminado", "Nenhuma"]
                res = f"{soma} % 3 = {soma%3}. Logo {resp}."
                dica = "Se soma % 3 = 0, então sim"
                erro = "Calcular soma errada"
            else:
                n = random.randint(1, 100)
                enum = f"Qual é o maior divisor de {n} (exceto ele mesmo)?"
                divisores = [d for d in range(1, n) if n % d == 0]
                maior = max(divisores) if divisores else 1
                opcoes = [str(maior), str(maior-1), str(n//2), str(n-1), "1"]
                res = f"Maior divisor próprio de {n} é {maior}"
                dica = "Procure o segundo maior fator"
                erro = "Confundir com número de divisores"
        
        elif dif == "médio":
            tipo = (i % 12) + 1
            if tipo <= 4:
                a, b = random.randint(6, 20), random.randint(6, 20)
                mdc = math.gcd(a, b)
                enum = f"MDC({a}, {b}) = ?"
                opcoes = [str(mdc), str(mdc-1), str(mdc+1), str(max(a,b)), str(1)]
                res = f"MDC({a}, {b}) = {mdc} (maior número que divide ambos)"
                dica = "Fatore ambos números e pegue fatores comuns"
                erro = "Confundir com MMC"
            elif tipo <= 8:
                a, b = random.randint(5, 15), random.randint(5, 15)
                mmc = (a * b) // math.gcd(a, b)
                enum = f"MMC({a}, {b}) = ?"
                opcoes = [str(mmc), str(mmc-1), str(a*b), str(max(a,b)), "Indefinido"]
                res = f"MMC({a}, {b}) = {mmc} (menor múltiplo comum)"
                dica = "Use: MMC = (a × b) / MDC"
                erro = "Usar produto direto sem dividir pelo MDC"
            else:
                n = random.randint(20, 100)
                enum = f"Decomponha {n} em fatores primos"
                fatores = []
                temp = n
                d = 2
                while d * d <= temp:
                    while temp % d == 0:
                        fatores.append(d)
                        temp //= d
                    d += 1
                if temp > 1:
                    fatores.append(temp)
                fat_str = " × ".join(map(str, fatores))
                opcoes = [fat_str, f"{n} é primo", "Não factorizável", f"2 × {n//2}", "Nenhuma"]
                res = f"{n} = {fat_str}"
                dica = "Divida sucessivamente por primos"
                erro = "Parar de fatorar antes de completar"
        
        else:  # difícil
            tipo = (i % 8) + 1
            if tipo == 1:
                enum = "Se a|b e b|c, então a|c. Qual é o nome dessa propriedade?"
                opcoes = ["Transitividade", "Comutatividade", "Associatividade", "Distributividade", "Nenhuma"]
                res = "Transitividade: Se a divide b E b divide c, então a divide c"
                dica = "Pensar em múltiplos"
                erro = "Confundir com propriedades de conjuntos"
            elif tipo == 2:
                enum = "Qual é a relação: MDC(a,b) × MMC(a,b) = ?"
                opcoes = ["a × b", "a + b", "max(a,b)", "min(a,b)", "(a+b)/2"]
                res = "MDC(a,b) × MMC(a,b) = a × b (propriedade fundamental)"
                dica = "Verificar com exemplos: MDC(6,9)=3, MMC(6,9)=18, 3×18=6×9"
                erro = "Pensar que é soma"
            else:
                n = random.randint(50, 200)
                enum = f"Quantos divisores tem o número {n}?"
                divisores = [d for d in range(1, n+1) if n % d == 0]
                qtd_div = len(divisores)
                opcoes = [str(qtd_div), str(qtd_div-1), str(qtd_div+1), str(n//2), "Infinitos"]
                res = f"{n} tem {qtd_div} divisores: {divisores[:5]}..."
                dica = "Se n = p₁^a × p₂^b, divisores = (a+1)(b+1)..."
                erro = "Contar apenas divisores primos"
        
        resposta = opcoes[0]
        opcoes_shuffled = opcoes.copy()
        random.shuffle(opcoes_shuffled)
        idx = opcoes_shuffled.index(resposta)
        
        questoes.append({
            "enunciado": enum,
            "opcoes": opcoes_shuffled,
            "gabarito": "ABCDE"[idx],
            "resolucao": res,
            "dica": dica,
            "erro": erro,
            "dificuldade": dif,
            "tags": ["aritmética", "divisibilidade"]
        })
    
    return questoes
