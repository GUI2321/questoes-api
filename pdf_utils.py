import os
from PyPDF2 import PdfMerger


def juntar_pdfs(lista_de_arquivos: list, nome_arquivo_final: str) -> str:
    """Junta múltiplos PDFs em um único arquivo.
    
    Args:
        lista_de_arquivos: Lista de caminhos dos PDFs a juntar
        nome_arquivo_final: Nome do arquivo final
        
    Returns:
        Caminho completo do PDF final
    """
    os.makedirs("static", exist_ok=True)
    caminho_final = os.path.join("static", nome_arquivo_final)

    merger = PdfMerger()
    for caminho in lista_de_arquivos:
        if os.path.exists(caminho):
            merger.append(caminho)
    merger.write(caminho_final)
    merger.close()
    
    return caminho_final
