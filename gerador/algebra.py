"""Gerador Suprassumo para Álgebra - 20+ tipos de questões"""
import random

NOMES = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo", "Fernanda", "Gabriel", "Helena"]

def gerar_algebra_suprassumo(qtd, dif):
    questoes = []
    for i in range(qtd):
        nome = random.choice(NOMES)
        
        if dif == "fácil":
            tipo = (i % 14) + 1
            if tipo <= 3:
                a, b = random.randint(1, 10), random.randint(1, 20)
                x = random.randint(1, 5)
                resultado = a * x + b
                enum = f"Resolva: {a}x + {b} = {resultado}"
                opcoes = [str(x), str(x-1), str(x+1), str(x-2), str(x+2)]
                res = f"{a}x = {resultado} - {b} = {resultado-b}. Logo x = {x}"
                dica = "Isole x passando constantes para o outro lado"
                erro = "Esquecer de dividir pelo coeficiente de x"
                
            elif tipo <= 6:
                a, b = random.randint(1, 5), random.randint(1, 5)
                enum = f"Expanda (x + {a})(x + {b})"
                resultado = f"x² + {a+b}x + {a*b}"
                opcoes = [resultado, f"x² + {a+b}x", f"x² + {a*b}", f"x² + {(a+b)**2}x", "x² + 1"]
                res = f"(x+{a})(x+{b}) = x² + {a}x + {b}x + {a*b} = {resultado}"
                dica = "Use FOIL: Primeiro, Externo, Interno, Último"
                erro = "Esquecer do termo do meio"
                
            elif tipo <= 9:
                a = random.randint(2, 8)
                enum = f"Fatore: x² + {2*a}x + {a**2}"
                resultado = f"(x + {a})²"
                opcoes = [resultado, f"(x + {a})(x - {a})", f"(x + {a*2})²", f"x(x + {2*a})", "(x + 1)²"]
                res = f"x² + {2*a}x + {a**2} = (x + {a})² (trinômio quadrado perfeito)"
                dica = "Procure por quadrados perfeitos"
                erro = "Confundir com diferença de quadrados"
                
            else:  # tipos 10-14
                a = random.randint(1, 5)
                b = random.randint(1, 5)
                enum = f"Fatore: x² - {a**2}"
                resultado = f"(x + {a})(x - {a})"
                opcoes = [resultado, f"(x - {a})²", f"(x + {a})²", f"x(x - {a**2})", "Primo"]
                res = f"x² - {a**2} = (x + {a})(x - {a}) (diferença de quadrados)"
                dica = "a² - b² = (a+b)(a-b)"
                erro = "Esquecer que é uma diferença"
        
        elif dif == "médio":
            tipo = (i % 11) + 1
            if tipo <= 3:
                a, b, c = random.randint(1, 5), random.randint(-10, 10), random.randint(-10, 10)
                delta = b**2 - 4*a*c
                enum = f"Quantas raízes reais tem {a}x² + {b}x + {c} = 0?"
                if delta > 0:
                    opcoes = ["2 reais distintas", "1 real dupla", "Nenhuma real", "Infinitas", "3 raízes"]
                elif delta == 0:
                    opcoes = ["1 real dupla", "2 reais distintas", "Nenhuma", "Infinitas", "Indeterminado"]
                else:
                    opcoes = ["Nenhuma real", "2 reais distintas", "1 real", "Infinitas", "2 complexas"]
                res = f"Δ = {b}² - 4({a})({c}) = {delta}. {'Δ > 0: 2 reais' if delta > 0 else ('Δ = 0: 1 real' if delta == 0 else 'Δ < 0: nenhuma real')}"
                dica = "Use o discriminante: Δ = b² - 4ac"
                erro = "Calcular Δ errado"
                
            elif tipo <= 6:
                n = random.randint(3, 8)
                enum = f"Resolva o sistema: x + y = 10, x - y = {2*(n-5)}"
                x_val = 5 + (n-5)
                y_val = 5 - (n-5)
                opcoes = [f"x={x_val}, y={y_val}", f"x={y_val}, y={x_val}", f"x={n}, y={10-n}", "Sem solução", f"x=5, y=5"]
                res = f"Somando: 2x = {10 + 2*(n-5)}, x = {x_val}. Subtraindo: y = {y_val}"
                dica = "Some ou subtraia as equações para eliminar variável"
                erro = "Erro na aritmética ao eliminar"
                
            elif tipo <= 9:
                a = random.randint(2, 6)
                enum = f"Simplifique: (x² - {a**2})/(x - {a})"
                opcoes = [f"x + {a}", f"x - {a}", f"x² - {a**2}", "x + 1", "Undefined"]
                res = f"(x² - {a**2})/(x - {a}) = [(x+{a})(x-{a})]/(x-{a}) = x + {a}"
                dica = "Fatore o numerador"
                erro = "Esquecer de cancelar"
                
            else:  # 10-11
                enum = "Se |x - 2| = 5, qual é x?"
                opcoes = ["7 ou -3", "5 ou -5", "2 ou 5", "-3 ou 5", "Apenas 7"]
                res = "x - 2 = 5 ⟹ x = 7 OU x - 2 = -5 ⟹ x = -3"
                dica = "Valor absoluto: |A| = B significa A = B ou A = -B"
                erro = "Considerar apenas uma solução"
        
        else:  # difícil
            tipo = (i % 7) + 1
            if tipo == 1:
                enum = "Para que valor de 'a' o sistema Ax = b é indeterminado?"
                opcoes = ["Quando det(A) = 0 e b é compatível", "Sempre", "Nunca", "Quando a = 1", "Indecidível"]
                res = "Sistema indeterminado: infinitas soluções quando det(A) = 0 e b está no espaço coluna"
                dica = "Relacionado com singularidade de A"
                erro = "Confundir com sistema impossível"
                
            elif tipo == 2:
                enum = "Qual é o conjunto solução de (x-1)² < 0?"
                opcoes = ["Conjunto vazio (∅)", "Todos reais", "Apenas x=1", "x < 1", "x > 1"]
                res = "(x-1)² ≥ 0 para todo real x, logo nunca é < 0. Solução: ∅"
                dica = "Quadrado de número real nunca é negativo"
                erro = "Tentar resolver como equação"
                
            elif tipo == 3:
                enum = "Resolva: √(x-1) = x - 3"
                opcoes = ["x = 5", "x = 1", "x = 2", "Sem solução", "x = 5 e x = 2"]
                res = "Elevando ao quadrado: x - 1 = (x-3)². Testando: x = 5 funciona, x = 2 não"
                dica = "Verificar soluções em equações irracionais"
                erro = "Esquecer de verificar na equação original"
                
            else:
                enum = "Se x² - 5x + 6 = 0, qual é x?"
                opcoes = ["2 ou 3", "1 ou 5", "-2 ou -3", "2", "3"]
                res = "(x-2)(x-3) = 0 ⟹ x = 2 ou x = 3"
                dica = "Fatore como produto de binômios"
                erro = "Usar fórmula quando fatoração é simples"
        
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
            "tags": ["álgebra", "equações"]
        })
    
    return questoes
