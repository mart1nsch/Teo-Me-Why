import streamlit as st
import pandas as pd

def config_padroes():
    # MUDA O NOME DA ABA E O ICONE DA ABA
    st.set_page_config(page_title='Finanças', page_icon=':moneybag:')
    st.markdown('''
# Boas Vindas!

## Nosso aplicativo de finanças
Projetamos ele para contar sem parar
''')

def dados_brutos(df):
    exp1 = st.expander('Dados Brutos')
    exp1.dataframe(df, hide_index=True)

def dados_institucionais(df):
    df_instituicao = df.pivot_table(index='Data', columns='Instituição', values='Valor')
    exp2 = st.expander('Dados Institucionais')
    tab_dados2, tab_grafico2, tab_distri2 = exp2.tabs(['Dados', 'Gráfico', 'Distribuição'])
    with tab_dados2:
        st.dataframe(df_instituicao)
    with tab_grafico2:
        st.line_chart(df_instituicao)
    with tab_distri2:
        data_filtro = st.selectbox('Data', df_instituicao.sort_index().index)
        st.bar_chart(df_instituicao.loc[data_filtro])

def dados_data(df):
    df_data = df.groupby(by='Data')[['Valor']].sum()
    df_data['lag1'] = df_data['Valor'].shift(1)
    df_data['Diferença Mensal'] = df_data['Valor'] - df_data['lag1']
    df_data['Média 6 Meses'] = df_data['Diferença Mensal'].rolling(6).mean()
    df_data['Média 12 Meses'] = df_data['Diferença Mensal'].rolling(12).mean()
    df_data['Média 24 Meses'] = df_data['Diferença Mensal'].rolling(24).mean()
    df_data['Evolução 6 Meses'] = df_data['Valor'].rolling(6).apply(lambda x: x[-1] - x[0])
    df_data['Evolução 12 Meses'] = df_data['Valor'].rolling(12).apply(lambda x: x[-1] - x[0])
    df_data['Evolução 24 Meses'] = df_data['Valor'].rolling(24).apply(lambda x: x[-1] - x[0])
    df_data['Diferença Relativa Mensal'] = df_data['Valor'] / df_data['lag1'] - 1
    df_data = df_data.drop('lag1', axis=1)

    columns_config = {
        'Valor': st.column_config.NumberColumn('Valor', format='R$ %.2f'),
        'Diferença Mensal': st.column_config.NumberColumn('Diferença Mensal', format='R$ %.2f'),
        'Média 6 Meses': st.column_config.NumberColumn('Média 6 Meses', format='R$ %.2f'),
        'Média 12 Meses': st.column_config.NumberColumn('Média 12 Meses', format='R$ %.2f'),
        'Média 24 Meses': st.column_config.NumberColumn('Média 24 Meses', format='R$ %.2f'),
        'Evolução 6 Meses': st.column_config.NumberColumn('Evolução 6 Meses', format='R$ %.2f'),
        'Evolução 12 Meses': st.column_config.NumberColumn('Evolução 12 Meses', format='R$ %.2f'),
        'Evolução 24 Meses': st.column_config.NumberColumn('Evolução 24 Meses', format='R$ %.2f'),
        'Diferença Relativa Mensal': st.column_config.NumberColumn('Diferença Relativa Mensal', format='percent')
    }

    exp3 = st.expander('Dados por Data')
    tab_dados3, tab_grafico3 = exp3.tabs(['Dados', 'Gráfico'])
    with tab_dados3:
        st.dataframe(df_data, column_config=columns_config)
    with tab_grafico3:
        st.line_chart(df_data['Valor'])
        st.line_chart(df_data[['Diferença Mensal', 'Média 6 Meses', 'Média 12 Meses']])
    return df_data

def dados_metas(df):
    exp4 = st.expander('Metas')
    data_inicio = exp4.date_input('Data Referência')
    patrimonio_referencia = df[df.loc[data_inicio]]['Valor']

    #exp4.text('Patrimônio Referência', patrimonio_referencia)

config_padroes()

file_upload = st.file_uploader(label='Selecione o(s) arquivo(s)', type=['csv'])

if file_upload:
    df = pd.read_csv(file_upload)
    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y').dt.date

    dados_brutos(df)
    dados_institucionais(df)
    df_data = dados_data(df)
    dados_metas(df_data)