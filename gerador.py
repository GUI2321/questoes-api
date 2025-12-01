import random
from typing import List, Dict

NIVEIS = ["Fácil", "Médio", "Difícil"]


def formatar_conjunto(elementos):
    if isinstance(elementos, set):
        elementos = sorted(list(elementos))
    if isinstance(elementos, list):
        return ", ".join(str(e) for e in elementos)
    return str(elementos)


def gerar_questao_conjuntos(numero: int) -> Dict:
    tipo = random.randint(1, 6)
    nivel = random.choice(NIVEIS)
    
    if tipo == 1:
        elementos = random.sample(range(1, 20), random.randint(3, 7))
        cardinalidade = len(elementos)
        enunciado = f"Considere o conjunto A = {{{formatar_conjunto(elementos)}}}. Qual é a cardinalidade de A?"
        resposta_correta = cardinalidade
        opcoes_valores = [cardinalidade, cardinalidade + 1, cardinalidade - 1, cardinalidade + 2, cardinalidade - 2]
        resolucao = f"A cardinalidade de A é {cardinalidade}, pois o conjunto possui {cardinalidade} elementos."
        
    elif tipo == 2:
        n = random.randint(2, 5)
        elementos = list(range(1, n + 1))
        subconjuntos = 2 ** n
        enunciado = f"Dado o conjunto B = {{{formatar_conjunto(elementos)}}}, determine quantos subconjuntos B possui."
        resposta_correta = subconjuntos
        opcoes_valores = [subconjuntos, subconjuntos * 2, subconjuntos // 2 if subconjuntos > 1 else 1, subconjuntos + 4, n]
        resolucao = f"O número de subconjuntos de um conjunto com {n} elementos é 2^{n} = {subconjuntos}."
        
    elif tipo == 3:
        a = random.sample(range(1, 10), 4)
        b = random.sample(range(1, 10), 4)
        intersecao = sorted(list(set(a) & set(b)))
        intersecao_str = "{" + formatar_conjunto(intersecao) + "}" if intersecao else "∅"
        enunciado = f"Se A = {{{formatar_conjunto(a)}}} e B = {{{formatar_conjunto(b)}}}, qual é A ∩ B (interseção)?"
        resposta_correta = intersecao_str
        opcoes_valores = [intersecao_str, "∅", "{1, 2, 3}", "{4, 5}", "{1}"]
        resolucao = f"A interseção A ∩ B contém os elementos comuns: {intersecao_str}."
        
    elif tipo == 4:
        a = random.sample(range(1, 10), 3)
        b = random.sample(range(1, 10), 3)
        uniao = sorted(list(set(a) | set(b)))
        uniao_str = "{" + formatar_conjunto(uniao) + "}"
        enunciado = f"Se A = {{{formatar_conjunto(a)}}} e B = {{{formatar_conjunto(b)}}}, qual é A ∪ B (união)?"
        resposta_correta = uniao_str
        opcoes_valores = [uniao_str, "∅", "{1, 2}", "{1, 2, 3, 4, 5, 6, 7, 8, 9}", "{3}"]
        resolucao = f"A união A ∪ B contém todos os elementos: {uniao_str}."
        
    elif tipo == 5:
        n = random.randint(5, 15)
        enunciado = f"Quantos elementos tem o conjunto dos números naturais menores que {n}?"
        resposta_correta = n
        opcoes_valores = [n, n + 1, n - 1, n + 2, n - 2]
        resolucao = f"Os naturais menores que {n} são: 0, 1, 2, ..., {n-1}. Total: {n} elementos."
        
    else:
        n = random.randint(2, 6)
        partes = 2 ** n
        enunciado = f"Se o conjunto A tem {n} elementos, quantos elementos tem o conjunto das partes de A?"
        resposta_correta = partes
        opcoes_valores = [partes, partes * 2, partes + 2, partes // 2 if partes > 1 else 1, n]
        resolucao = f"O conjunto das partes de A (P(A)) tem 2^{n} = {partes} elementos."
    
    opcoes_unicas = list(dict.fromkeys([str(v) for v in opcoes_valores]))
    while len(opcoes_unicas) < 5:
        novo = random.randint(1, 50)
        if str(novo) not in opcoes_unicas:
            opcoes_unicas.append(str(novo))
    
    resposta_str = str(resposta_correta)
    random.shuffle(opcoes_unicas)
    
    letras = ["A", "B", "C", "D", "E"]
    gabarito_letra = "A"
    opcoes_formatadas = []
    
    for i, opcao in enumerate(opcoes_unicas[:5]):
        opcoes_formatadas.append(f"{letras[i]}) {opcao}")
        if opcao == resposta_str:
            gabarito_letra = letras[i]
    
    return {
        "numero": numero,
        "nivel": nivel,
        "enunciado": enunciado,
        "opcoes": opcoes_formatadas,
        "gabarito": gabarito_letra,
        "resolucao": resolucao
    }


def gerar_questao_funcoes(numero: int) -> Dict:
    tipo = random.randint(1, 3)
    nivel = random.choice(NIVEIS)
    
    if tipo == 1:
        a = random.randint(1, 5)
        b = random.randint(-10, 10)
        c = random.randint(-5, 5)
        resultado = a * c + b
        enunciado = f"Seja f(x) = {a}x + {b}. Qual é o valor de f({c})?"
        resposta_correta = resultado
        opcoes_valores = [resultado, resultado + 2, resultado - 2, resultado * 2, resultado + 5]
        resolucao = f"f({c}) = {a}·{c} + {b} = {a*c} + {b} = {resultado}"
        
    elif tipo == 2:
        a = random.choice([x for x in range(-5, 6) if x != 0])
        b = random.randint(-10, 10)
        tipo_funcao = "Crescente" if a > 0 else "Decrescente"
        enunciado = f"A função f(x) = {a}x + {b} é crescente ou decrescente?"
        resposta_correta = tipo_funcao
        opcoes_valores = [tipo_funcao, "Decrescente" if tipo_funcao == "Crescente" else "Crescente", "Constante", "Indefinido", "Não é função"]
        resolucao = f"Como o coeficiente angular é {a} {'> 0' if a > 0 else '< 0'}, a função é {tipo_funcao}."
        
    else:
        a = random.randint(-5, 10)
        dominio = f"x ≥ {a}"
        enunciado = f"Qual é o domínio da função f(x) = √(x - {a})?"
        resposta_correta = dominio
        opcoes_valores = [dominio, "ℝ", f"x < {a}", "x ≤ 0", "∅"]
        resolucao = f"Para a raiz existir, x - {a} ≥ 0, logo x ≥ {a}. Domínio: {dominio}"
    
    resposta_str = str(resposta_correta)
    opcoes_unicas = list(dict.fromkeys([str(v) for v in opcoes_valores]))
    random.shuffle(opcoes_unicas)
    
    letras = ["A", "B", "C", "D", "E"]
    gabarito_letra = "A"
    opcoes_formatadas = []
    
    for i, opcao in enumerate(opcoes_unicas[:5]):
        opcoes_formatadas.append(f"{letras[i]}) {opcao}")
        if opcao == resposta_str:
            gabarito_letra = letras[i]
    
    return {
        "numero": numero,
        "nivel": nivel,
        "enunciado": enunciado,
        "opcoes": opcoes_formatadas,
        "gabarito": gabarito_letra,
        "resolucao": resolucao
    }


def gerar_questao_equacoes(numero: int) -> Dict:
    tipo = random.randint(1, 2)
    nivel = random.choice(NIVEIS)
    
    if tipo == 1:
        a = random.choice([x for x in range(1, 6)])
        x = random.randint(-5, 5)
        b = random.randint(-10, 10)
        c = a * x + b
        enunciado = f"Resolva a equação: {a}x + {b} = {c}"
        resposta_correta = x
        opcoes_valores = [x, x + 1, x - 1, x * 2 if x != 0 else 2, -x if x != 0 else 1]
        resolucao = f"{a}x = {c} - {b} = {c - b}, logo x = {c - b}/{a} = {x}"
        
    else:
        n = random.choice([4, 9, 16, 25, 36, 49, 64, 81, 100])
        raiz = int(n ** 0.5)
        resposta = f"±{raiz}"
        enunciado = f"Qual o valor de x na equação: x² = {n}?"
        resposta_correta = resposta
        opcoes_valores = [resposta, str(raiz), str(-raiz), str(raiz + 1), "0"]
        resolucao = f"x² = {n} → x = ±√{n} = ±{raiz}"
    
    resposta_str = str(resposta_correta)
    opcoes_unicas = list(dict.fromkeys([str(v) for v in opcoes_valores]))
    random.shuffle(opcoes_unicas)
    
    letras = ["A", "B", "C", "D", "E"]
    gabarito_letra = "A"
    opcoes_formatadas = []
    
    for i, opcao in enumerate(opcoes_unicas[:5]):
        opcoes_formatadas.append(f"{letras[i]}) {opcao}")
        if opcao == resposta_str:
            gabarito_letra = letras[i]
    
    return {
        "numero": numero,
        "nivel": nivel,
        "enunciado": enunciado,
        "opcoes": opcoes_formatadas,
        "gabarito": gabarito_letra,
        "resolucao": resolucao
    }


def gerar_questao_generica(numero: int, topico: str) -> Dict:
    topico_lower = topico.lower()
    
    if "conjunto" in topico_lower or "definições" in topico_lower:
        return gerar_questao_conjuntos(numero)
    elif "função" in topico_lower or "funções" in topico_lower:
        return gerar_questao_funcoes(numero)
    elif "equação" in topico_lower or "equações" in topico_lower:
        return gerar_questao_equacoes(numero)
    else:
        geradores = [gerar_questao_conjuntos, gerar_questao_funcoes, gerar_questao_equacoes]
        return random.choice(geradores)(numero)


def gerar_questoes(volume: int, topico: str, quantidade: int) -> str:
    markdown = f"# VOLUME {volume} – TÓPICO: {topico}\n\n"
    markdown += f"**Total de questões:** {quantidade}\n\n"
    markdown += "---\n\n"
    
    for i in range(1, quantidade + 1):
        questao = gerar_questao_generica(i, topico)
        
        markdown += f"### Questão {questao['numero']} — Nível {questao['nivel']}\n\n"
        markdown += f"{questao['enunciado']}\n\n"
        
        for opcao in questao['opcoes']:
            markdown += f"{opcao}  \n"
        
        markdown += f"\n**Gabarito:** {questao['gabarito']}  \n"
        markdown += f"**Resolução:** {questao['resolucao']}\n\n"
        markdown += "---\n\n"
    
    return markdown
