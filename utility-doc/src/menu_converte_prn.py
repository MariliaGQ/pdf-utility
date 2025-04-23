import streamlit as st
import tempfile
from pathlib import Path
import subprocess
import os

def exibir_menu_converte_prn(coluna):
    with coluna:
        st.markdown("""
        ### :page_with_curl: Converte arquivos PRN para Word                  
        
        """)
        st.divider()
        st.markdown("""
                       
        Escolha um arquivo PRN para converter para Word (RTF). O arquivo convertido pode ser baixado em seguida.:
        """)

        # Upload do arquivo PRN
        arquivo_prn = st.file_uploader(
            label='',
            type='prn',
            accept_multiple_files=False
        )

        # Ativar/desativar botões com base no arquivo
        botoes_desativados = not bool(arquivo_prn)

        # Botão para extrair páginas
        clicou_converter = st.button(
            'Clique aqui para converter',
            use_container_width=True,
            disabled=botoes_desativados
        )

        if clicou_converter and arquivo_prn:
            try:
                # Salva o arquivo PRN em um arquivo temporário
                with tempfile.NamedTemporaryFile(delete=False, suffix=".prn") as temp_prn:
                    temp_prn.write(arquivo_prn.read())
                    temp_prn_path = temp_prn.name

                # Define o caminho de saída para o arquivo RTF
                temp_rtf_path = temp_prn_path.replace(".prn", ".rtf")

                # Caminho para o DOSPrinter.exe dentro do projeto
                dosprinter_path = os.path.join(os.path.dirname(__file__), "../tools/DOSPrinter.exe")

                # Comando para converter PRN para RTF usando DOSPrinter
                comando = f'"{dosprinter_path}" /RTF /GON /FILE "{temp_prn_path}" /72 /LEFT1.0 /TOP1.0'
                resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

                # Verifica se houve erros na execução do comando
                if resultado.returncode != 0:
                    st.error(f"Erro ao converter o PRN para RTF: {resultado.stderr}")
                else:
                    # Lê o arquivo RTF gerado
                    with open(temp_rtf_path, "rb") as rtf_file:
                        dados_rtf = rtf_file.read()

                    # Define o nome do arquivo para download
                    nome_arquivo = f'{Path(arquivo_prn.name).stem}_convertido.rtf'

                    # Botão para download do arquivo RTF
                    st.download_button(
                        label='Clique para fazer o download do arquivo Word (RTF)',
                        type='primary',
                        data=dados_rtf,
                        file_name=nome_arquivo,
                        mime='application/rtf',
                        use_container_width=True
                    )
            except Exception as e:
                st.error(f"Erro ao processar o PRN: {e}")


