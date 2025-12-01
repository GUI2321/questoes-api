"""Sistema de Análise e Relatórios de Qualidade"""
import json
from datetime import datetime

class AnalisadorQuestoes:
    """Analisa qualidade das questões geradas"""
    
    def __init__(self):
        self.questoes_analisadas = 0
        self.estatisticas = {}
    
    def analisar_conjunto(self, questoes):
        """Analisa um conjunto de questões"""
        stats = {
            "total": len(questoes),
            "por_dificuldade": {},
            "gabaritos": {},
            "tempo": datetime.now().isoformat(),
            "qualidade_score": 0
        }
        
        for q in questoes:
            dif = q.get("dificuldade", "desconhecido")
            if dif not in stats["por_dificuldade"]:
                stats["por_dificuldade"][dif] = 0
            stats["por_dificuldade"][dif] += 1
            
            gab = q.get("gabarito", "")
            if gab not in stats["gabaritos"]:
                stats["gabaritos"][gab] = 0
            stats["gabaritos"][gab] += 1
        
        # Score de qualidade
        balanceamento_gabaritos = max(0, 100 - (max(stats["gabaritos"].values()) - min(stats["gabaritos"].values())) * 10)
        balanceamento_dificuldade = 100 if "fácil" in stats["por_dificuldade"] and "médio" in stats["por_dificuldade"] and "difícil" in stats["por_dificuldade"] else 0
        stats["qualidade_score"] = (balanceamento_gabaritos + balanceamento_dificuldade) / 2
        
        return stats
    
    def gerar_relatorio(self, questoes):
        """Gera relatório detalhado"""
        stats = self.analisar_conjunto(questoes)
        
        relatorio = f"""
📊 RELATÓRIO DE QUALIDADE DAS QUESTÕES
{'='*50}

📈 ESTATÍSTICAS GERAIS
- Total de questões: {stats['total']}
- Data: {stats['tempo']}
- Score de qualidade: {stats['qualidade_score']:.1f}%

📌 DISTRIBUIÇÃO POR DIFICULDADE
"""
        for dif, qty in stats['por_dificuldade'].items():
            pct = (qty / stats['total']) * 100
            relatorio += f"  {dif.upper()}: {qty} ({pct:.1f}%)\n"
        
        relatorio += f"\n🔤 DISTRIBUIÇÃO DE GABARITOS\n"
        for gab, qty in sorted(stats['gabaritos'].items()):
            pct = (qty / stats['total']) * 100
            relatorio += f"  {gab}: {qty} ({pct:.1f}%)\n"
        
        # Análise
        relatorio += f"\n✅ ANÁLISE\n"
        if stats['qualidade_score'] >= 80:
            relatorio += "  ✓ Excelente balanceamento\n"
        elif stats['qualidade_score'] >= 60:
            relatorio += "  ⚠ Bom, mas pode melhorar\n"
        else:
            relatorio += "  ✗ Precisa rebalancear\n"
        
        return relatorio

def gerar_gabarito_json(questoes):
    """Gera gabarito em JSON"""
    gabarito = {
        "meta": {
            "total": len(questoes),
            "data": datetime.now().isoformat()
        },
        "questoes": []
    }
    
    for i, q in enumerate(questoes, 1):
        gabarito["questoes"].append({
            "numero": i,
            "gabarito": q.get("gabarito", ""),
            "dificuldade": q.get("dificuldade", ""),
            "tags": q.get("tags", [])
        })
    
    return json.dumps(gabarito, ensure_ascii=False, indent=2)

def gerar_gabarito_xml(questoes):
    """Gera gabarito em XML"""
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<gabarito>\n'
    
    for i, q in enumerate(questoes, 1):
        xml += f'''  <questao numero="{i}">
    <gabarito>{q.get("gabarito", "")}</gabarito>
    <dificuldade>{q.get("dificuldade", "")}</dificuldade>
    <tags>{", ".join(q.get("tags", []))}</tags>
  </questao>\n'''
    
    xml += '</gabarito>'
    return xml
