import streamlit as st
import pypdf
import tempfile
from pathlib import Path

def exibir_menu_extrair(coluna):
    with coluna:
        st.markdown("""
        ### :page_with_curl: Extrair páginas do PDF                  
        
        """)
        st.divider()
        st.markdown("""
                       
        Escolha um arquivo PDF e informe as páginas que deseja extrair:
        """)

        # Upload do arquivo PDF
        arquivo_pdf = st.file_uploader(
            label='',
            type='pdf',
            accept_multiple_files=False
        )

      
        # Ativar/desativar botões com base no arquivo
        botoes_desativados = not bool(arquivo_pdf)

        # Entrada para páginas
        paginas_input = st.text_input(
            'Digite as páginas ou intervalos para extrair (ex.: 1, 3, 5-7):',
            disabled=botoes_desativados
        )

        # Botão para extrair páginas
        clicou_extrair = st.button(
            'Extrair páginas',
            use_container_width=True,
            disabled=botoes_desativados
        )

        if clicou_extrair and arquivo_pdf:
            try:
                # Processar páginas da entrada
                paginas = processar_paginas(paginas_input)

                # Validar se páginas estão dentro do limite
                dados_pdf = extrair_paginas_pdf(arquivo_pdf, paginas)

                nome_arquivo = f'{Path(arquivo_pdf.name).stem}_paginas_extraidas.pdf'
                st.download_button(
                    label='Clique para fazer o download do PDF',
                    type='primary',
                    data=dados_pdf,
                    file_name=nome_arquivo,
                    mime='application/pdf',
                    use_container_width=True
                )
            except Exception as e:
                st.error(f"Erro ao processar o PDF: {e}")

def processar_paginas(input_paginas):
    """
    Converte uma string de páginas/intervalos para uma lista de inteiros.
    Ex.: "1, 3, 5-7" => [1, 3, 5, 6, 7]
    """
    paginas = []
    for parte in input_paginas.split(','):
        if '-' in parte:
            inicio, fim = map(int, parte.split('-'))
            paginas.extend(range(inicio, fim + 1))
        else:
            paginas.append(int(parte))
    return sorted(set(paginas))  # Ordena e remove duplicados

def extrair_paginas_pdf(arquivo_pdf, paginas):
    """
    Extrai as páginas especificadas de um arquivo PDF e retorna os dados em bytes.
    """
    leitor = pypdf.PdfReader(arquivo_pdf)
    escritor = pypdf.PdfWriter()

    # Validar número máximo de páginas
    total_paginas = len(leitor.pages)
    paginas_validas = [p for p in paginas if 1 <= p <= total_paginas]

    if not paginas_validas:
        raise ValueError("Nenhuma página válida foi selecionada.")

    for pagina in paginas_validas:
        escritor.add_page(leitor.pages[pagina - 1])  # Índice começa em 0

    # Escrever em um arquivo temporário
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_pdf_file = Path(temp_dir) / 'paginas_extraidas.pdf'
        escritor.write(temp_pdf_file)
        with open(temp_pdf_file, 'rb') as output_pdf:
            pdf_data = output_pdf.read()

    return pdf_data
