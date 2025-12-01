"""Volume 10: Combinatória e Probabilidade - 20+ tipos"""
import random
import math

def gerar_combinatoria(qtd, dif):
    questoes = []
    for i in range(qtd):
        if dif == "fácil":
            tipo = (i % 13) + 1
            if tipo <= 4:
                n = random.randint(3, 7)
                fatorial = math.factorial(n)
                enum = f"Quanto é {n}!?"
                opcoes = [str(fatorial), str(fatorial-1), str(2*n), str(n**2), str(n)]
                resolucao = f"{n}! = {n}×{n-1}×...×1 = {fatorial}"
                dica = "Fatorial n! = n×(n-1)×...×1"
                erro = "Confundir com potência"
            elif tipo <= 8:
                n = random.randint(3, 6)
                enum = f"Quantas permutações de {n} objetos?"
                perm = math.factorial(n)
                opcoes = [str(perm), str(n**2), str(2**n), str(n), "Infinitas"]
                resolucao = f"P({n}) = {n}! = {perm}"
                dica = "Permutação = n!"
                erro = "Contar combinações"
            elif tipo <= 11:
                n, k = random.randint(3, 6), random.randint(2, 4)
                comb = math.comb(n, k)
                enum = f"C({n},{k}) = ?"
                opcoes = [str(comb), str(math.factorial(n)), str(n**k), str(n-k), "Indefinido"]
                resolucao = f"C({n},{k}) = {n}!/({k}!×{n-k}!) = {comb}"
                dica = "Combinação: ordem não importa"
                erro = "Confundir com arranjo"
            else:
                enum = "Qual é a diferença entre arranjo e combinação?"
                opcoes = ["Arranjo: ordem importa; Combinação: não", "Nenhuma", "Arranjo é maior", "Combinação usa fatorial", "São iguais"]
                resolucao = "A(n,k) = n!/(n-k)!, C(n,k) = n!/(k!(n-k)!)"
                dica = "A é permutação de seleção"
                erro = "Usar mesma fórmula"
        elif dif == "médio":
            tipo = (i % 11) + 1
            if tipo <= 3:
                enum = "Quantos anagramas tem AMOR?"
                opcoes = ["24", "4", "16", "12", "6"]
                resolucao = "4 letras diferentes: 4! = 24"
                dica = "Sem repetição: n!"
                erro = "Contar inadequadamente"
            elif tipo <= 7:
                n, k = random.randint(4, 8), random.randint(2, 4)
                arr = n*math.factorial(n-1)//math.factorial(n-k)
                enum = f"A({n},{k}) = ?"
                opcoes = [str(arr), str(math.comb(n,k)), str(math.factorial(n)), str(n**k), "Indefinido"]
                resolucao = f"A({n},{k}) = {n}!/({n-k}!)"
                dica = "Arranjo: ordem importa"
                erro = "Usar combinação"
            else:
                enum = "Qual é P(A) se em 100 eventos 25 favorem A?"
                opcoes = ["25/100 = 1/4", "75/100", "100/25", "0", "1"]
                resolucao = "P(A) = favoráveis/total = 25/100 = 0,25"
                dica = "Probabilidade = casos favoráveis/total"
                erro = "Invertir numerador e denominador"
        else:
            tipo = (i % 9) + 1
            if tipo <= 3:
                enum = "Se P(A)=0.3 e P(B)=0.5 independentes, P(A∩B)=?"
                opcoes = ["0.15", "0.8", "0.2", "0.5", "0.3"]
                resolucao = "Eventos independentes: P(A∩B) = P(A)×P(B) = 0.3×0.5 = 0.15"
                dica = "Independentes: multiplica"
                erro = "Somar em vez de multiplicar"
            elif tipo <= 6:
                enum = "Qual é P(A∪B) se P(A)=0.4, P(B)=0.3, P(A∩B)=0.1?"
                opcoes = ["0.6", "0.7", "0.4", "1", "0.3"]
                resolucao = "P(A∪B) = P(A) + P(B) - P(A∩B) = 0.4+0.3-0.1 = 0.6"
                dica = "Inclusão-exclusão: soma - interseção"
                erro = "Esquecer de subtrair interseção"
            else:
                enum = "Se P(não chover) = 0.7, qual P(chover)?"
                opcoes = ["0.3", "0.7", "1", "0", "0.5"]
                resolucao = "P(A) + P(¬A) = 1 ⟹ P(chover) = 1-0.7 = 0.3"
                dica = "Evento e complementar somam 1"
                erro = "Não subtrair de 1"
        
        resposta = opcoes[0]
        opcoes_shuffled = opcoes.copy()
        random.shuffle(opcoes_shuffled)
        idx = opcoes_shuffled.index(resposta)
        
        questoes.append({
            "enunciado": enum,
            "opcoes": opcoes_shuffled,
            "gabarito": "ABCDE"[idx],
            "resolucao": resolucao,
            "dica": dica,
            "erro": erro,
            "dificuldade": dif,
            "tags": ["combinatória", "probabilidade"]
        })
    return questoes
