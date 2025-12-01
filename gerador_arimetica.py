"""Gerador para Aritmética - Divisibilidade, MDC, MMC, Números Primos"""
import random
import math

CONTEXTOS_ARITMETICA = [
    "Uma loja de doces", "Uma fábrica de parafusos", "Um banco de alimentos", 
    "Uma agência de viagens", "Um estoque de mercado", "Uma distribuição de caixas"
]

def nome_aleatorio():
    NOMES = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo", "Fernanda", "Gabriel", "Helena"]
    SOBRENOMES = ["Silva", "Santos", "Oliveira", "Pereira", "Martins", "Sousa", "Rodrigues", "Alves"]
    return f"{random.choice(NOMES)} {random.choice(SOBRENOMES)}"

def gerar_divisibilidade_mega(qtd, dif):
    """Questões sobre divisibilidade e critérios"""
    questoes = []
    for i in range(qtd):
        idx = i % 5
        
        if dif == "fácil":
            tipo = random.randint(1, 5)
            if tipo == 1:
                n = random.randint(10, 100)
                por = random.randint(2, 10)
                resp = "Sim" if n % por == 0 else "Não"
                opcoes = ["Sim", "Não", "Talvez", "Sempre", "Nunca"]
                enum = f"É {n} divisível por {por}?"
                res = f"{n} ÷ {por} = {n/por if n%por==0 else 'não inteiro'}. Logo {resp}."
            elif tipo == 2:
                enum = "Qual é o critério de divisibilidade por 2?"
                opcoes = ["Número é par", "Soma dos dígitos é par", "Termina em 0", "Divisível por 1", "Sempre"]
                res = "Um número é divisível por 2 se seu último dígito é 0, 2, 4, 6 ou 8 (par)."
            elif tipo == 3:
                enum = "Qual é o critério de divisibilidade por 3?"
                opcoes = ["Soma dos dígitos divisível por 3", "Número é par", "Termina em 3", "Divisível por 2", "Não existe"]
                res = "Um número é divisível por 3 se a soma de seus dígitos é divisível por 3."
            elif tipo == 4:
                n = random.randint(100, 999)
                soma = sum(int(d) for d in str(n))
                resp = "Sim" if soma % 3 == 0 else "Não"
                enum = f"Usando o critério, {n} é divisível por 3? (soma dos dígitos = {soma})"
                opcoes = ["Sim", "Não", "Talvez", "Não se sabe", "Indeterminado"]
                res = f"Soma = {soma}. {soma} % 3 = {soma % 3}. Logo {resp}."
            else:  # tipo == 5
                n = random.randint(100, 1000)
                enum = f"Qual é o maior divisor de {n} (exceto ele mesmo)?"
                div = [d for d in range(1, n) if n % d == 0]
                maior_div = max(div) if div else 1
                opcoes = [str(maior_div), str(maior_div-1), str(n//2), str(n-1), str(1)]
                res = f"Fatorando {n} encontramos {maior_div} como maior divisor próprio."
        
        elif dif == "médio":
            tipo = random.randint(1, 4)
            if tipo == 1:
                nome = nome_aleatorio()
                ctx = random.choice(CONTEXTOS_ARITMETICA)
                n = random.randint(20, 50)
                por = random.randint(3, 7)
                enum = f"Em {ctx}, {nome} tem {n} itens. Pode dividir em grupos de {por} igualmente?"
                resp = "Sim" if n % por == 0 else "Não"
                opcoes = ["Sim", "Não", "Depende", "Indeterminado", "Impossível"]
                resto = n % por
                res = f"{n} ÷ {por} = {n//por} com resto {resto}. Logo {'Sim, grupos iguais!' if resto==0 else f'Não, sobraria {resto}'}."
            elif tipo == 2:
                enum = "Um número é divisível por 5 se:"
                opcoes = ["Termina em 0 ou 5", "É ímpar", "Soma dos dígitos = 5", "Divisível por 2", "Múltiplo de 10"]
                res = "Critério: o último dígito é 0 ou 5."
            elif tipo == 3:
                n1, n2 = random.randint(6, 20), random.randint(6, 20)
                enum = f"Quais números dividem ambos {n1} e {n2}? (divisores comuns)"
                divs_comuns = [d for d in range(1, min(n1,n2)+1) if n1%d==0 and n2%d==0]
                res_text = f"Divisores comuns: {divs_comuns[:3]}... O maior é {max(divs_comuns)}."
                opcoes = [res_text, "Nenhum", "Apenas 1", "Infinitos", "Não calculável"]
                res = res_text
            else:  # tipo == 4
                enum = "Qual é a importância dos números primos em divisibilidade?"
                opcoes = ["Todo número se decompõe em primos (fatoração)", "São os maiores números", "Dividem todos", "Não têm uso", "São 0 ou 1"]
                res = "Teorema Fundamental da Aritmética: Todo inteiro > 1 é produto único de primos."
        
        else:  # difícil
            tipo = random.randint(1, 3)
            if tipo == 1:
                n = random.randint(100, 500)
                # Encontrar fatores primos
                temp = n
                factors = []
                d = 2
                while d * d <= temp:
                    while temp % d == 0:
                        factors.append(d)
                        temp //= d
                    d += 1
                if temp > 1:
                    factors.append(temp)
                enum = f"Decomponha {n} em fatores primos:"
                res = f"{n} = {' × '.join(map(str, factors))}"
                opcoes = [res, "Não decomponível", "São infinitos", f"{n} é primo", "Indeterminado"]
            elif tipo == 2:
                enum = "Se um número é divisível por 6, deve ser divisível por:"
                opcoes = ["2 E 3", "4 E 5", "2 OU 3", "12", "Não há necessidade"]
                res = "6 = 2 × 3. Logo, divisível por 6 ⟹ divisível por 2 E por 3."
            else:  # tipo == 3
                enum = "Qual é a relação entre divisibilidade e múltiplos?"
                opcoes = ["a|b ⟺ b é múltiplo de a", "Nenhuma relação", "Múltiplos são maiores", "Apenas em primos", "Não relacionado"]
                res = "a divide b (a|b) significaexatamente que b = a·k para algum inteiro k. b é múltiplo de a."
        
        resposta = opcoes[0]
        opcoes_shuffle = opcoes.copy()
        random.shuffle(opcoes_shuffle)
        gabarito_idx = opcoes_shuffle.index(resposta)
        
        questoes.append({
            "enunciado": enum,
            "opcoes": opcoes_shuffle,
            "gabarito": "ABCDE"[gabarito_idx],
            "resolucao": res,
            "dificuldade": dif
        })
    
    return questoes

def gerar_mdc_mmc_mega(qtd, dif):
    """Questões sobre MDC e MMC"""
    questoes = []
    for i in range(qtd):
        if dif == "fácil":
            tipo = random.randint(1, 3)
            if tipo == 1:
                a, b = random.randint(4, 15), random.randint(4, 15)
                mdc = math.gcd(a, b)
                enum = f"Qual é o MDC({a}, {b})?"
                opcoes = [str(mdc), str(mdc-1), str(mdc+1), str(max(a,b)), str(1)]
            elif tipo == 2:
                enum = "MDC significa:"
                opcoes = ["Máximo Divisor Comum", "Mínimo Divisor Comum", "Máximo Divisível Comum", "Mínimo Divisível Comum", "Nenhuma"]
            else:
                a, b = random.randint(4, 10), random.randint(4, 10)
                mmc = (a * b) // math.gcd(a, b)
                enum = f"Qual é o MMC({a}, {b})?"
                opcoes = [str(mmc), str(mmc-1), str(mmc+1), str(a*b), str(min(a,b))]
        elif dif == "médio":
            tipo = random.randint(1, 2)
            if tipo == 1:
                a, b = random.randint(10, 30), random.randint(10, 30)
                mdc = math.gcd(a, b)
                enum = f"Se MDC({a}, {b}) = {mdc}, então {a} e {b} são:"
                opcoes = [f"Compatíveis com mdc={mdc}", "Primos", "Iguais", "Incomuns", "Indeterminados"]
            else:
                nome = nome_aleatorio()
                ctx = random.choice(CONTEXTOS_ARITMETICA)
                a, b = random.randint(10, 40), random.randint(10, 40)
                enum = f"{nome} em {ctx} quer agrupar {a} e {b} itens em lotes iguais máximos. Quantos por lote?"
                mdc = math.gcd(a, b)
                opcoes = [str(mdc), str(mdc-1), str(mdc+1), str(max(a,b)), "Não é possível"]
        else:  # difícil
            enum = "Qual é a relação: MDC(a,b) × MMC(a,b) = ?"
            opcoes = ["a × b", "a + b", "(a×b)/2", "max(a,b)", "min(a,b)"]
        
        resposta = opcoes[0]
        opcoes_shuffle = opcoes.copy()
        random.shuffle(opcoes_shuffle)
        gabarito_idx = opcoes_shuffle.index(resposta)
        
        questoes.append({
            "enunciado": enum,
            "opcoes": opcoes_shuffle,
            "gabarito": "ABCDE"[gabarito_idx],
            "resolucao": "",
            "dificuldade": dif
        })
    
    return questoes
