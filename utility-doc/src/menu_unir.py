import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import tempfile

def unir_pdfs(arquivos_pdf):
    """
    Une múltiplos arquivos PDF em um único PDF, mantendo a ordem dos arquivos.

    Parâmetros:
        arquivos_pdf (list): Lista de arquivos PDF para combinar.

    Retorna:
        pdf_combinado (bytes): Conteúdo do PDF combinado em bytes.
    """
    pdf_writer = PdfWriter()

    # Para cada arquivo PDF
    for arquivo_pdf in arquivos_pdf:
        reader = PdfReader(arquivo_pdf)
        for pagina in range(len(reader.pages)):
            pdf_writer.add_page(reader.pages[pagina])

    # Salvar o PDF combinado em um arquivo temporário
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        pdf_writer.write(temp_file)
        temp_file_path = temp_file.name

    # Ler os bytes do PDF combinado
    with open(temp_file_path, "rb") as output_pdf:
        pdf_combinado = output_pdf.read()

    return pdf_combinado


def exibir_menu_unir_pdf(coluna):
    with coluna:
        st.markdown("""
        ### 🔀 Unir PDFs
                    """)
        
        st.divider()
        st.markdown("""        
        Selecione os arquivos PDF e o sistema irá uni-los na ordem que forem carregados:
        """)

        # Upload dos arquivos PDF
        arquivos_pdf = st.file_uploader(
            label="",
            type="pdf",
            accept_multiple_files=True,
            

        )

        if arquivos_pdf:
            # Exibir o botão de unir PDFs
            clicou_unir = st.button('Unir arquivos PDFs')

            if clicou_unir:
                with st.spinner('Reduzindo e unindo os PDFs...'):
                    try:
                        # Unir os arquivos PDF na ordem em que foram carregados
                        pdf_combinado = unir_pdfs(arquivos_pdf)

                        # Criar o nome do arquivo para download
                        nome_arquivo = "pdf_combinado.pdf"
                        
                        # Oferecer o download do PDF combinado
                        st.download_button(
                            label="Clique para baixar o PDF",
                            data=pdf_combinado,
                            file_name=nome_arquivo,
                            mime="application/pdf",
                            use_container_width=True
                        )
                    except Exception as e:
                        st.error(f"Erro ao unir os PDFs: {e}")
