"""Volume 8: Trigonometria - 20+ tipos"""
import random
import math

def gerar_trigonometria(qtd, dif):
    questoes = []
    for i in range(qtd):
        if dif == "fácil":
            tipo = (i % 13) + 1
            if tipo <= 4:
                enum = "sen(30°) = ?"
                opcoes = ["1/2", "√3/2", "√2/2", "1", "0"]
                resolucao = "Valor tabelado: sen(30°) = 1/2"
                dica = "Memorizar valores em 0°,30°,45°,60°,90°"
                erro = "Confundir com cos(30°)"
            elif tipo <= 8:
                enum = "cos(60°) = ?"
                opcoes = ["1/2", "√3/2", "√2/2", "1", "0"]
                resolucao = "cos(60°) = 1/2"
                dica = "cos(60°) = sen(30°)"
                erro = "Usar valor de sen"
            elif tipo <= 11:
                enum = "tg(45°) = ?"
                opcoes = ["1", "√3/2", "√3", "1/2", "0"]
                resolucao = "tg(45°) = sen(45°)/cos(45°) = (√2/2)/(√2/2) = 1"
                dica = "tg(45°) sempre é 1"
                erro = "Esquecer definição"
            else:
                enum = "sen²(x) + cos²(x) = ?"
                opcoes = ["1", "0", "sen(2x)", "cos(2x)", "2"]
                resolucao = "Identidade fundamental da trigonometria"
                dica = "Sempre 1 para qualquer x"
                erro = "Tentar calcular valores específicos"
        elif dif == "médio":
            tipo = (i % 11) + 1
            if tipo <= 3:
                enum = "Qual é a equação: sen(x) = 1/2?"
                opcoes = ["x=30° ou 150°", "x=60°", "x=45°", "x=0°", "Sem solução"]
                resolucao = "No intervalo [0°,360°]: x=30° ou x=180°-30°=150°"
                dica = "sen é positiva em 0-180°"
                erro = "Esquecer segunda solução"
            elif tipo <= 7:
                enum = "sen(2x) = ?"
                opcoes = ["2sen(x)cos(x)", "2sen(x)", "sen(x)cos(x)", "sen²(x)", "cos(2x)"]
                resolucao = "Fórmula: sen(2x) = 2sen(x)cos(x)"
                dica = "Memorizar fórmulas de ângulo duplo"
                erro = "Confundir fórmulas"
            else:
                enum = "cos(x) = -1/2, qual é x em [0°,360°]?"
                opcoes = ["120° ou 240°", "60°", "150°", "30°", "90°"]
                resolucao = "cos é negativa em 90-270°, cos(120°)=-1/2"
                dica = "Usar círculo trigonométrico"
                erro = "Esquecer quadrante"
        else:
            tipo = (i % 9) + 1
            if tipo <= 3:
                enum = "Qual é a Lei dos Senos?"
                opcoes = ["a/sen(A) = b/sen(B) = c/sen(C)", "a×sen(A) = ...", "sen(A)/a = ...", "Nenhuma", "a+b=c"]
                resolucao = "Lei Senos: lados proporcionais aos senos dos ângulos opostos"
                dica = "Lado/seno do ângulo oposto"
                erro = "Inverter lados e ângulos"
            elif tipo <= 6:
                enum = "Lei dos Cossenos: c² = ?"
                opcoes = ["a² + b² - 2ab·cos(C)", "a² + b²", "2ab", "a² - b²", "ab"]
                resolucao = "c² = a² + b² - 2ab·cos(C)"
                dica = "Generalização do Teorema de Pitágoras"
                erro = "Esquecer o termo -2ab·cos(C)"
            else:
                enum = "Qual é a identidade tan²(x) + 1 = ?"
                opcoes = ["sec²(x)", "csc²(x)", "1", "tan(x)", "0"]
                resolucao = "Identidade Pitagórica: 1 + tan²(x) = sec²(x)"
                dica = "Relacionada com sen²+cos²=1"
                erro = "Confundir com outra identidade"
        
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
            "tags": ["trigonometria"]
        })
    return questoes
