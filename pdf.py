import os
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def limpar_markdown(texto: str) -> str:
    texto = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', texto)
    texto = re.sub(r'\*(.+?)\*', r'<i>\1</i>', texto)
    texto = re.sub(r'^#{1,6}\s*', '', texto, flags=re.MULTILINE)
    texto = re.sub(r'^---\s*$', '', texto, flags=re.MULTILINE)
    return texto


def salvar_pdf(volume: int, topico: str, markdown_text: str) -> str:
    # 🟢 cria a pasta STATIC ao invés de "pdfs"
    os.makedirs("static", exist_ok=True)

    topico_limpo = re.sub(r'[^\w\s-]', '', topico).replace(' ', '_')
    filename = f"volume_{volume}_{topico_limpo}.pdf"

    # 🟢 salva dentro de static/
    filepath = f"static/{filename}"

    doc = SimpleDocTemplate(
        filepath,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )

    styles = getSampleStyleSheet()

    titulo_style = ParagraphStyle(
        'Titulo',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=20,
        alignment=TA_CENTER,
        textColor='#1a5f7a'
    )

    subtitulo_style = ParagraphStyle(
        'Subtitulo',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=10,
        alignment=TA_CENTER
    )

    questao_style = ParagraphStyle(
        'Questao',
        parent=styles['Heading3'],
        fontSize=12,
        spaceBefore=15,
        spaceAfter=8,
        textColor='#2c3e50'
    )

    texto_style = ParagraphStyle(
        'Texto',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=4,
        alignment=TA_JUSTIFY
    )

    opcao_style = ParagraphStyle(
        'Opcao',
        parent=styles['Normal'],
        fontSize=10,
        leftIndent=20,
        spaceAfter=2
    )

    gabarito_style = ParagraphStyle(
        'Gabarito',
        parent=styles['Normal'],
        fontSize=10,
        spaceBefore=8,
        textColor='#27ae60'
    )

    story = []

    story.append(Paragraph(f"VOLUME {volume}", titulo_style))
    story.append(Paragraph(f"Tópico: {topico}", subtitulo_style))
    story.append(Spacer(1, 0.5*cm))

    linhas = markdown_text.split('\n')

    questao_atual = []
    em_questao = False

    for linha in linhas:
        linha = linha.strip()

        if not linha or linha == '---':
            continue

        if linha.startswith('# VOLUME') or linha.startswith('**Total'):
            continue

        if linha.startswith('### Questão'):
            if em_questao and questao_atual:
                story.append(Spacer(1, 0.3*cm))

            texto_questao = limpar_markdown(linha.replace('### ', ''))
            story.append(Paragraph(texto_questao, questao_style))
            em_questao = True
            questao_atual = []

        elif linha.startswith(('A)', 'B)', 'C)', 'D)', 'E)')):
            texto_opcao = limpar_markdown(linha)
            story.append(Paragraph(texto_opcao, opcao_style))

        elif linha.startswith('**Gabarito:**'):
            story.append(Paragraph(limpar_markdown(linha), gabarito_style))

        elif linha.startswith('**Resolução:**'):
            story.append(Paragraph(limpar_markdown(linha), texto_style))

        elif em_questao and linha:
            story.append(Paragraph(limpar_markdown(linha), texto_style))

    doc.build(story)

    return filename  # 🟢 agora retornamos só o nome
