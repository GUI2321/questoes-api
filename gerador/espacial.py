"""Volume 9: Geometria Espacial - 20+ tipos"""
import random

def gerar_espacial(qtd, dif):
    questoes = []
    for i in range(qtd):
        if dif == "fácil":
            tipo = (i % 12) + 1
            if tipo <= 3:
                a = random.randint(2, 8)
                enum = f"Volume de cubo com aresta {a}:"
                vol = a**3
                opcoes = [str(vol), str(6*a**2), str(12*a), str(a), "Indefinido"]
                resolucao = f"V = aresta³ = {a}³ = {vol}"
                dica = "Cubo: V = a³"
                erro = "Confundir com área"
            elif tipo <= 6:
                a, b, h = random.randint(2, 6), random.randint(2, 6), random.randint(2, 5)
                enum = f"Volume de paralelepípedo {a}×{b}×{h}:"
                vol = a*b*h
                opcoes = [str(vol), str(2*(a*b+b*h+a*h)), str(a+b+h), str(a*b), "Infinito"]
                resolucao = f"V = comprimento × largura × altura = {a}×{b}×{h} = {vol}"
                dica = "Paralelepípedo: V = a×b×h"
                erro = "Confundir com superfície"
            else:
                r = random.randint(2, 6)
                enum = f"Volume de esfera com raio {r}:"
                opcoes = [f"(4/3)π{r}³", f"4π{r}²", f"(4/3)π{r}²", f"π{r}³", f"2π{r}³"]
                resolucao = f"V = (4/3)πr³ = (4/3)π×{r}³"
                dica = "Esfera: V = (4/3)πr³"
                erro = "Usar fórmula de área"
        elif dif == "médio":
            tipo = (i % 11) + 1
            if tipo <= 3:
                r = random.randint(2, 5)
                h = random.randint(3, 8)
                enum = f"Volume de cilindro r={r}, h={h}:"
                opcoes = [f"π{r}²×{h}", f"2π{r}×{h}", f"{r}²×{h}", f"π{r}×{h}", f"(1/3)π{r}²×{h}"]
                resolucao = f"V = πr²h = π×{r}²×{h}"
                dica = "Cilindro: V = πr²h"
                erro = "Confundir com cone"
            elif tipo <= 7:
                r = random.randint(2, 5)
                h = random.randint(3, 8)
                enum = f"Volume de cone r={r}, h={h}:"
                opcoes = [f"(1/3)π{r}²×{h}", f"π{r}²×{h}", f"πr×h", f"(1/2)π{r}²×{h}", f"π{r}³"]
                resolucao = f"V = (1/3)πr²h"
                dica = "Cone: V = (1/3)πr²h (1/3 do cilindro)"
                erro = "Esquecer o 1/3"
            else:
                a = random.randint(3, 6)
                enum = f"Área superficial de cubo aresta {a}:"
                area = 6*a**2
                opcoes = [str(area), str(a**3), str(12*a), str(4*a**2), "Nenhuma"]
                resolucao = f"A = 6×aresta² = 6×{a}² = {area}"
                dica = "Cubo tem 6 faces quadradas"
                erro = "Contar menos faces"
        else:
            tipo = (i % 9) + 1
            if tipo <= 3:
                enum = "Qual é a diagonal de cubo aresta a?"
                opcoes = ["a√3", "a√2", "a", "2a", "3a"]
                resolucao = "Diagonal = √(a² + a² + a²) = a√3"
                dica = "Usar 3D Pitágoras"
                erro = "Usar apenas 2D"
            elif tipo <= 6:
                enum = "Qual é a altura de pirâmide quadrada base a, volume V?"
                opcoes = ["3V/a²", "V/a²", "Va²", "a²/3", "V/3"]
                resolucao = "V = (1/3)×base×altura ⟹ h = 3V/base = 3V/a²"
                dica = "Fórmula de volume: isole altura"
                erro = "Esquecer o 1/3"
            else:
                enum = "Qual é o volume de tetraedro regular aresta a?"
                opcoes = ["(a³√2)/12", "(a³)/12", "(a³√3)/12", "(a³)/3", "Indefinido"]
                resolucao = "V = (a³√2)/12 (fórmula especial)"
                dica = "Tetraedro = pirâmide com base triangular"
                erro = "Confundir com outros poliedros"
        
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
            "tags": ["geometria espacial"]
        })
    return questoes
