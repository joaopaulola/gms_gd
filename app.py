import streamlit as st
import pandas as pd
import io

def gms_para_decimal(valor):
    try:
        # Usamos string para garantir que 89.5724 pegue exatamente 57 e 24
        s_valor = f"{float(valor):.4f}"
        graus_str, decimal_str = s_valor.split('.')
        g = int(graus_str)
        m = int(decimal_str[:2])
        s = int(decimal_str[2:4])
        return g + (m / 60) + (s / 3600)
    except:
        return 0.0

st.set_page_config(page_title="Conversor GMS Online", page_icon="🌍")

st.title("🌍 Conversor de Coordenadas GMS")
st.markdown("""
Suba seu arquivo `.txt` ou `.csv` no formato:  
`E1,E0,R,0.0000,89.5724,...`  
O programa converterá automaticamente as colunas 4 e 5 (índices 3 e 4).
""")

# Upload do arquivo
uploaded_file = st.file_uploader("Selecione o arquivo de entrada", type=["txt", "csv"])

if uploaded_file is not None:
    # Lendo o arquivo subido
    df = pd.read_csv(uploaded_file, header=None)
    
    st.subheader("Dados Originais (Prévia)")
    st.dataframe(df.head())

    if st.button("Converter para Graus Decimais"):
        # Aplicando a função nas colunas 3 e 4 conforme seu script original
        df[3] = df[3].apply(gms_para_decimal)
        df[4] = df[4].apply(gms_para_decimal)
        
        st.subheader("✅ Dados Convertidos")
        st.dataframe(df.head())

        # Criando o botão de download
        output = io.StringIO()
        df.to_csv(output, index=False, header=False)
        st.download_button(
            label="Baixar Arquivo Convertido",
            data=output.getvalue(),
            file_name="dados_graus_dec.csv",
            mime="text/csv"
        )
