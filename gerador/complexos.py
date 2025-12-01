"""Volume 5: Números Complexos - 20+ tipos"""
import random
import math

def gerar_complexos(qtd, dif):
    questoes = []
    for i in range(qtd):
        if dif == "fácil":
            tipo = (i % 11) + 1
            if tipo <= 3:
                a, b = random.randint(1, 5), random.randint(1, 5)
                mod = int(math.sqrt(a**2 + b**2))
                enum = f"|{a} + {b}i| = ?"
                opcoes = [str(mod), str(mod-1), str(a+b), str(a), str(b)]
                resolucao = f"Módulo = √({a}² + {b}²) = √{a**2+b**2} = {mod}"
                dica = "Módulo = √(a² + b²)"
                erro = "Somar em vez de usar Pitágoras"
            elif tipo <= 6:
                enum = "O conjugado de 3 + 2i é:"
                opcoes = ["3 - 2i", "3 + 2i", "-3 + 2i", "-3 - 2i", "2 + 3i"]
                resolucao = "Conjugado troca sinal da parte imaginária"
                dica = "z = a+bi ⟹ z̄ = a-bi"
                erro = "Trocar sinal da parte real"
            elif tipo <= 9:
                enum = "i² = ?"
                opcoes = ["-1", "1", "i", "-i", "0"]
                resolucao = "i² = √(-1)² = -1 (definição)"
                dica = "Memorizar: i²=-1, i³=-i, i⁴=1"
                erro = "Achar que i² = 1"
            else:
                enum = "(2+i) + (3-2i) = ?"
                opcoes = ["5 - i", "5 + i", "6 - i", "1 + 3i", "-1 + 3i"]
                resolucao = "Soma partes reais e imaginárias: (2+3) + (1-2)i = 5 - i"
                dica = "Somar reais com reais, imaginárias com imaginárias"
                erro = "Misturar partes"
        elif dif == "médio":
            tipo = (i % 9) + 1
            if tipo <= 3:
                enum = "Qual é o módulo de (1+i)(1-i)?"
                opcoes = ["2", "1", "4", "√2", "0"]
                resolucao = "(1+i)(1-i) = 1² - i² = 1-(-1) = 2, |2|=2"
                dica = "(a+bi)(a-bi) = a² + b²"
                erro = "Calcular módulos separados"
            elif tipo <= 6:
                enum = "Se z = 1 + i, qual é z²?"
                opcoes = ["2i", "1", "1 + 2i", "0", "i"]
                resolucao = "(1+i)² = 1 + 2i + i² = 1 + 2i - 1 = 2i"
                dica = "Use (a+b)² = a²+2ab+b²"
                erro = "Esquecer que i²=-1"
            else:
                enum = "Qual forma trigonométrica de 1+i?"
                opcoes = ["√2(cos45° + i sen45°)", "2(cos45° + i sen45°)", "cos45° + i sen45°", "i", "1"]
                resolucao = "|1+i|=√2, arg=45°, forma: √2(cos45°+i sen45°)"
                dica = "z = |z|(cosθ + i senθ)"
                erro = "Confundir módulo com argumento"
        else:
            tipo = (i % 7) + 1
            if tipo <= 2:
                enum = "Quantas raízes complexas tem x²+1=0?"
                opcoes = ["2 (±i)", "0", "1", "4", "Infinitas"]
                resolucao = "x² = -1 ⟹ x = ±i (duas raízes complexas)"
                dica = "Em ℂ, todo polinômio tem raízes"
                erro = "Pensar que não tem solução"
            elif tipo <= 4:
                enum = "Se z=cos60°+i sen60°, qual z³?"
                opcoes = ["1", "i", "-1", "-i", "z"]
                resolucao = "z³ = [cos(3×60°) + i sen(3×60°)] = cos180° + i sen180° = -1"
                dica = "Fórmula de Moivre: z^n = |z|^n(cos(nθ)+i sen(nθ))"
                erro = "Não multiplicar o ângulo"
            else:
                enum = "Qual é e^(iπ)?"
                opcoes = ["-1", "1", "i", "-i", "π"]
                resolucao = "Fórmula de Euler: e^(iπ) = cos(π) + i sen(π) = -1"
                dica = "e^(iθ) = cosθ + i senθ"
                erro = "Confundir com números reais"
        
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
            "tags": ["complexos"]
        })
    return questoes
