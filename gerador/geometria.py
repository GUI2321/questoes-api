"""Volumes 6-7: Geometria Analítica e Plana - 20+ tipos cada"""
import random

def gerar_geometria_analitica(qtd, dif):
    questoes = []
    for i in range(qtd):
        if dif == "fácil":
            tipo = (i % 12) + 1
            if tipo <= 4:
                x1, y1, x2, y2 = random.randint(0, 5), random.randint(0, 5), random.randint(5, 10), random.randint(5, 10)
                dist_sq = (x2-x1)**2 + (y2-y1)**2
                dist = int(dist_sq**0.5) if dist_sq**0.5 == int(dist_sq**0.5) else f"√{dist_sq}"
                enum = f"Distância entre P({x1},{y1}) e Q({x2},{y2}):"
                opcoes = [str(dist), str(int(dist_sq**0.5)-1) if isinstance(dist, int) else f"√{dist_sq-1}", str(abs(x2-x1)+abs(y2-y1)), "0", "∞"]
                resolucao = f"d = √[(x₂-x₁)² + (y₂-y₁)²] = √[({x2-x1})² + ({y2-y1})²] = {dist}"
                dica = "Use a fórmula da distância: √[(Δx)² + (Δy)²]"
                erro = "Somar em vez de usar Pitágoras"
            elif tipo <= 8:
                x1, y1, x2, y2 = random.randint(0, 5), random.randint(0, 5), random.randint(5, 10), random.randint(5, 10)
                xm = (x1+x2)//2
                ym = (y1+y2)//2
                enum = f"Ponto médio de A({x1},{y1}) e B({x2},{y2}):"
                opcoes = [f"({xm},{ym})", f"({x1},{y1})", f"({x2},{y2})", f"({(x1+x2)//3},{(y1+y2)//3})", "Origem"]
                resolucao = f"M = (({x1}+{x2})/2, ({y1}+{y2})/2) = ({xm},{ym})"
                dica = "Ponto médio: média aritmética das coordenadas"
                erro = "Usar só uma coordenada"
            else:
                enum = "Qual é a inclinação de reta por (0,0) e (3,2)?"
                opcoes = ["2/3", "3/2", "2", "3", "0"]
                resolucao = "Inclinação m = (y₂-y₁)/(x₂-x₁) = 2/3"
                dica = "m = Δy/Δx"
                erro = "Inverter Δx e Δy"
        elif dif == "médio":
            tipo = (i % 10) + 1
            if tipo <= 4:
                enum = "Qual equação de reta com m=2 passando (1,3)?"
                opcoes = ["y = 2x + 1", "y = 2x - 1", "y = x + 2", "y = 2x + 3", "y = x + 1"]
                resolucao = "y - 3 = 2(x - 1) ⟹ y = 2x + 1"
                dica = "Use y - y₁ = m(x - x₁)"
                erro = "Confundir sinal"
            elif tipo <= 7:
                enum = "Qual é a distância do ponto (3,4) à origem?"
                opcoes = ["5", "7", "4", "3", "12"]
                resolucao = "d = √(3² + 4²) = √(9 + 16) = √25 = 5"
                dica = "Triângulo 3-4-5 é famoso!"
                erro = "Somar em vez de Pitágoras"
            else:
                enum = "Qual é o coeficiente angular de 2x + 3y = 6?"
                opcoes = ["-2/3", "2/3", "2", "3", "6"]
                resolucao = "3y = -2x + 6 ⟹ y = -2x/3 + 2 ⟹ m = -2/3"
                dica = "Isole y e veja coeficiente de x"
                erro = "Não inverter sinais"
        else:
            tipo = (i % 8) + 1
            if tipo <= 3:
                enum = "Qual é a circunferência de raio 5 com centro (2,3)?"
                opcoes = ["(x-2)² + (y-3)² = 25", "(x+2)² + (y+3)² = 25", "(x-2)² + (y-3)² = 5", "x² + y² = 25", "(x-3)² + (y-2)² = 25"]
                resolucao = "Forma padrão: (x-a)² + (y-b)² = r²"
                dica = "Centro (a,b), raio r"
                erro = "Invertir centro e raio"
            else:
                enum = "Qual é a excentricidade de uma elipse com a=5, c=3?"
                opcoes = ["3/5", "5/3", "2/3", "1", "0"]
                resolucao = "e = c/a = 3/5 (onde c=distância focal, a=semi-eixo maior)"
                dica = "e = c/a para elipse"
                erro = "Usar fórmula errada"
    
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
            "tags": ["geometria analítica"]
        })
    return questoes

def gerar_geometria_plana(qtd, dif):
    questoes = []
    for i in range(qtd):
        if dif == "fácil":
            tipo = (i % 11) + 1
            if tipo <= 3:
                a = random.randint(3, 10)
                enum = f"Área de quadrado com lado {a}:"
                area = a**2
                opcoes = [str(area), str(2*a), str(4*a), str(a), "Indefinida"]
                resolucao = f"A = lado² = {a}² = {area}"
                dica = "Quadrado: A = l²"
                erro = "A = 4l (que é perímetro)"
            elif tipo <= 6:
                a, b = random.randint(3, 8), random.randint(3, 8)
                enum = f"Área de retângulo {a}×{b}:"
                area = a*b
                opcoes = [str(area), str(2*(a+b)), str(a+b), "4", "Infinita"]
                resolucao = f"A = comprimento × largura = {a} × {b} = {area}"
                dica = "Retângulo: A = c × l"
                erro = "Confundir com perímetro"
            else:
                enum = "Soma dos ângulos internos de triângulo:"
                opcoes = ["180°", "360°", "90°", "270°", "120°"]
                resolucao = "Propriedade fundamental dos triângulos"
                dica = "Sempre 180°"
                erro = "Usar 360°"
        elif dif == "médio":
            tipo = (i % 10) + 1
            if tipo <= 3:
                a = random.randint(3, 8)
                b = random.randint(3, 8)
                h = random.randint(2, 5)
                enum = f"Área de trapézio com bases {a} e {b}, altura {h}:"
                area = ((a+b)*h)//2
                opcoes = [str(area), str(a*b), str((a+b)*h), str(a+b+h), "0"]
                resolucao = f"A = (b₁ + b₂)h/2 = ({a}+{b})×{h}/2 = {area}"
                dica = "Trapézio: A = (base₁ + base₂)×altura/2"
                erro = "Esquecer de dividir por 2"
            elif tipo <= 7:
                enum = "Qual teorema relaciona lados de triângulo retângulo?"
                opcoes = ["Pitágoras: a² + b² = c²", "a + b = c", "a × b = c", "a - b = c", "Nenhum"]
                resolucao = "a² + b² = c² (hipotenusa)"
                dica = "Memorize: 3-4-5, 5-12-13"
                erro = "Usar sem elevar ao quadrado"
            else:
                a = random.randint(3, 10)
                enum = f"Área de círculo com raio {a}:"
                opcoes = [f"{a}²π", f"{2*a}π", f"{a}π", f"{(a//2)**2}π", "πa"]
                resolucao = f"A = πr² = π×{a}² = {a}²π"
                dica = "Círculo: A = πr²"
                erro = "Usar 2πr (que é perímetro)"
        else:
            tipo = (i % 8) + 1
            if tipo <= 3:
                enum = "Qual é a altura do triângulo equilátero de lado a?"
                opcoes = ["a√3/2", "a/2", "a", "2a", "a√2"]
                resolucao = "h = (lado × √3)/2"
                dica = "Usar Pitágoras dividindo em 2 retângulos"
                erro = "Usar fórmula errada"
            else:
                enum = "Qual é o raio inscrito em triângulo equilátero de lado a?"
                opcoes = ["a/(2√3)", "a/2", "a", "a√3", "2a"]
                resolucao = "r = área/semiperímetro"
                dica = "r = A/s onde s=(perímetro)/2"
                erro = "Confundir com raio circunscrito"
        
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
            "tags": ["geometria plana"]
        })
    return questoes
