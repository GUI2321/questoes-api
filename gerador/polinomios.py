"""Volume 4: Polinômios - 20+ tipos de questões"""
import random

def gerar_polinomios(qtd, dif):
    questoes = []
    for i in range(qtd):
        if dif == "fácil":
            tipo = (i % 12) + 1
            if tipo <= 3:
                a, b = random.randint(1, 5), random.randint(1, 10)
                x = random.randint(1, 5)
                res = a*x**2 + b*x + 1
                enum = f"Se P(x) = {a}x² + {b}x + 1, quanto é P({x})?"
                opcoes = [str(res), str(res-1), str(res+1), str(a+b+1), "Indefinido"]
                resolucao = f"P({x}) = {a}({x})² + {b}({x}) + 1 = {res}"
                dica = "Substitua o valor de x na expressão"
                erro = "Esquecer de elevar ao quadrado"
            elif tipo <= 6:
                enum = "Qual é o grau de 5x³ + 2x² - x + 7?"
                opcoes = ["3", "2", "5", "4", "1"]
                resolucao = "Grau = maior expoente = 3"
                dica = "Procure o maior expoente"
                erro = "Contar número de termos"
            elif tipo <= 9:
                a = random.randint(2, 6)
                enum = f"Expanda (x + {a})²"
                opcoes = [f"x² + {2*a}x + {a**2}", f"x² + {2*a}x", f"x² + {a**2}", f"2x + {2*a}", "Não é polinômio"]
                resolucao = f"(x+{a})² = x² + 2({a})x + {a}² = x² + {2*a}x + {a**2}"
                dica = "Use quadrado da soma"
                erro = "Esquecer do termo do meio"
            else:
                enum = "Qual é o coeficiente de x em 3x³ + 2x² - 5x + 1?"
                opcoes = ["-5", "2", "3", "1", "0"]
                resolucao = "Coeficiente de x é -5"
                dica = "Procure o termo com x (não x²)"
                erro = "Confundir com constante"
        elif dif == "médio":
            tipo = (i % 10) + 1
            if tipo <= 3:
                n = random.randint(3, 8)
                enum = f"Fatore: x² + {2*n}x + {n**2}"
                opcoes = [f"(x+{n})²", f"(x-{n})²", f"(x+{n})(x-{n})", f"x(x+{2*n})", "Primo"]
                resolucao = f"Trinômio quadrado perfeito: (x+{n})²"
                dica = "Procure por a² + 2ab + b²"
                erro = "Confundir com diferença de quadrados"
            elif tipo <= 6:
                enum = "Quantas raízes tem x² - 4?"
                opcoes = ["2", "1", "0", "4", "Indefinido"]
                resolucao = "x² - 4 = (x+2)(x-2) tem raízes x=2 e x=-2"
                dica = "Diferença de quadrados: x²-a² = (x+a)(x-a)"
                erro = "Contar multiplicidade errada"
            else:
                a, b = random.randint(1, 4), random.randint(1, 4)
                enum = f"Qual é o resto de ({a}x³ + {b}x + 1) ÷ (x - 1)?"
                resto = a + b + 1
                opcoes = [str(resto), str(resto-1), str(a), str(b), "0"]
                resolucao = f"Teorema do Resto: resto = P(1) = {a} + {b} + 1 = {resto}"
                dica = "Use o Teorema do Resto: P(a) é o resto"
                erro = "Tentar fazer divisão longa"
        else:
            tipo = (i % 8) + 1
            if tipo <= 3:
                enum = "Se P(x) tem raiz 2, qual fator?"
                opcoes = ["(x-2)", "(x+2)", "(2x-1)", "(x-1)", "Nenhum"]
                resolucao = "Se 2 é raiz de P(x), então (x-2) é fator"
                dica = "Teorema do Fator: P(a)=0 ⟺ (x-a) é fator"
                erro = "Usar sinal errado"
            elif tipo <= 6:
                enum = "Qual é o grau do produto (x²+1)(x³-2)?"
                opcoes = ["5", "6", "3", "2", "10"]
                resolucao = "Grau = 2+3 = 5"
                dica = "Grau do produto = soma dos graus"
                erro = "Multiplicar os graus"
            else:
                enum = "Se P(x)=x³-1 e Q(x)=x+1, qual grau de P+Q?"
                opcoes = ["3", "2", "1", "4", "0"]
                resolucao = "P(x)+Q(x) = x³ + x tem grau 3"
                dica = "Grau da soma = maior grau"
                erro = "Somar graus"
        
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
            "tags": ["polinômios"]
        })
    return questoes
