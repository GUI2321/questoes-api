"""Sistema novo simplificado de geração com múltipla escolha"""
import random

class Questao:
    def __init__(self, enunciado, opcoes, gabarito_indice, dificuldade):
        self.enunciado = enunciado
        self.opcoes = opcoes  # Lista de 5 strings
        self.gabarito = "ABCDE"[gabarito_indice]
        self.dificuldade = dificuldade

def gerar_questoes(volume, topico, quantidade):
    """Gera questões com 40% fácil, 40% médio, 20% difícil"""
    
    qtd_facil = int(quantidade * 0.4)
    qtd_medio = int(quantidade * 0.4)
    qtd_dificil = quantidade - qtd_facil - qtd_medio
    
    questoes = []
    
    # SEÇÃO A: QUESTÕES FÁCEIS
    for i in range(qtd_facil):
        idx_gabarito = i % 5  # Distribui A, B, C, D, E
        if volume == 1:
            n = random.randint(3, 10)
            enunciado = f"Qual é a cardinalidade de {{1, 2, 3, ..., {n}}}?"
            resposta = str(n)
            opcoes = [resposta, str(n-1), str(n+1), str(n+2), str(n//2)]
            opcoes = opcoes[:5]
            while len(opcoes) < 5:
                opcoes.append(str(random.randint(1, 20)))
        else:
            enunciado = f"Questão Fácil {i+1} do Volume {volume}"
            resposta = "Opção A"
            opcoes = ["Opção A", "Opção B", "Opção C", "Opção D", "Opção E"]
        
        # Move resposta para posição correta
        if resposta not in opcoes:
            opcoes[idx_gabarito] = resposta
        else:
            idx_gabarito = opcoes.index(resposta)
        
        questoes.append(Questao(enunciado, opcoes, idx_gabarito, "fácil"))
    
    # SEÇÃO B: QUESTÕES MÉDIAS
    for i in range(qtd_medio):
        idx_gabarito = i % 5
        enunciado = f"Questão Média {i+1} do Volume {volume}"
        opcoes = ["Opção A", "Opção B", "Opção C", "Opção D", "Opção E"]
        questoes.append(Questao(enunciado, opcoes, idx_gabarito, "médio"))
    
    # SEÇÃO C: QUESTÕES DIFÍCEIS
    for i in range(qtd_dificil):
        idx_gabarito = i % 5
        enunciado = f"Questão Difícil {i+1} do Volume {volume}"
        opcoes = ["Opção A", "Opção B", "Opção C", "Opção D", "Opção E"]
        questoes.append(Questao(enunciado, opcoes, idx_gabarito, "difícil"))
    
    # Gera markdown
    markdown = f"# VOLUME {volume} - {topico.upper()}\n\n"
    
    # Seção A
    faceis = [q for q in questoes if q.dificuldade == "fácil"]
    if faceis:
        markdown += f"## SEÇÃO A — QUESTÕES FÁCEIS\n\n**Total: {len(faceis)} questões**\n\n---\n\n"
        for num, q in enumerate(faceis, 1):
            markdown += f"### Questão {num}\n\n{q.enunciado}\n\n"
            for i, op in enumerate(q.opcoes):
                markdown += f"**{chr(65+i)})** {op}\n"
            markdown += f"\n**Gabarito: {q.gabarito}**\n\n---\n\n"
    
    # Seção B
    medios = [q for q in questoes if q.dificuldade == "médio"]
    if medios:
        markdown += f"## SEÇÃO B — QUESTÕES MÉDIAS\n\n**Total: {len(medios)} questões**\n\n---\n\n"
        for num, q in enumerate(medios, len(faceis) + 1):
            markdown += f"### Questão {num}\n\n{q.enunciado}\n\n"
            for i, op in enumerate(q.opcoes):
                markdown += f"**{chr(65+i)})** {op}\n"
            markdown += f"\n**Gabarito: {q.gabarito}**\n\n---\n\n"
    
    # Seção C
    dificeis = [q for q in questoes if q.dificuldade == "difícil"]
    if dificeis:
        markdown += f"## SEÇÃO C — QUESTÕES DIFÍCEIS\n\n**Total: {len(dificeis)} questões**\n\n---\n\n"
        for num, q in enumerate(dificeis, len(faceis) + len(medios) + 1):
            markdown += f"### Questão {num}\n\n{q.enunciado}\n\n"
            for i, op in enumerate(q.opcoes):
                markdown += f"**{chr(65+i)})** {op}\n"
            markdown += f"\n**Gabarito: {q.gabarito}**\n\n---\n\n"
    
    return markdown
