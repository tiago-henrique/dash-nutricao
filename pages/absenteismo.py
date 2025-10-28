import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')
url = ("https://imunogenetica.famerp.br/dash/nutricao_paula/indicadores.csv")
df = pd.read_csv(url)

ab = df['data_v2_d499ef'].count()

topografias = {
    1: 'Aparelho digestivo alto',
    2: 'Aparelho digestivo baixo',
    3: 'Bilio pancreática',
    4: 'Fígado',
    5: 'Ginecologia',
    6: 'Hematologia',
    7: 'Mastologia',
    8: 'Otorrino',
    9: 'Pulmão',
    10: 'Urologia',
    11: 'Neurologia',
    12: 'Pele/Melanoma',
    13: 'Outros oncológicos',
    14: 'Não oncológicos'
}

modalidade_tratamento = {
    1: 'Estadiamento',
    2: 'Clínico',
    3: 'Cirúrgico (até 45 dias pré ou pós)',
    4: 'Reestadiamento',
    5: 'Seguimento clínico',
    6: 'Cuidados paliativo pleno'
}

ganho_ponderal = {
    1: 'Ganho intencional',
    2: 'Manutenção',
    3: 'Falha do emagrecimento'
}

perda_ponderal = {
    1: 'Intencional',
    2: 'Perda Ponderal não Intencional'
}

asg = {
    1: 'Bem nutrido',
    2: 'Desnutrição suspeita ou moderada',
    3: 'Gravemente desnutrido'
}

via_alimentar = {
    1: 'Oral',
    2: 'Oral e suplementação nutricional',
    3: 'Oral e enteral',
    4: 'Enteral'
}

modalidade = {
    1: 'Presencial',
    2: 'Telemedicina'
}

tipo_via = {
    1: 'SNE',
    2: 'Gastrostomia',
    3: 'Jejunostomia'
}

tomo = {
    0: 'Não',
    1: 'Sim'
}

col0, col01 = st.columns([4,1])
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)
col7, col8 = st.columns(2)

#Criando os Gráficos dos Pacientes em Absenteístas
col0.title('Absenteísmo')
col1.subheader('Atendimentos')
col1.text(ab)

df['topografia_v2_9594b2'] = df['topografia_v2_9594b2'].map(topografias)
df['analise_tc'] = df['analise_tc'].map(tomo)

freq_topografias = df['topografia_v2_9594b2'].value_counts().reset_index()
freq_topografias.columns = ['Topografia', 'Frequência']

graf_topografia = px.bar(freq_topografias, x='Frequência', y='Topografia', color='Frequência', title='Topografias - Primeira consulta', text_auto=True, orientation='h')
col1.plotly_chart(graf_topografia, use_container_width=True)

df['modalidade_tratamento_v2_e9afd4'] = df['modalidade_tratamento_v2_e9afd4'].map(modalidade_tratamento)
freq_modalidade = df['modalidade_tratamento_v2_e9afd4'].value_counts().reset_index()
freq_modalidade.columns = ['Modalidade', 'Frequência']
graf_modalidade = px.pie(freq_modalidade, values='Frequência', names='Modalidade', title='Modalidade de tratamento - Primeira consulta')
col3.plotly_chart(graf_modalidade, use_container_width=True)

df['modalidade_consulta_v2_66a4eb'] = df['modalidade_consulta_v2_66a4eb'].map(modalidade)
freq_modalidade = df['modalidade_consulta_v2_66a4eb'].value_counts().reset_index()
freq_modalidade.columns = ['Classificação', 'Frequência']
freq_modalidade = px.pie(freq_modalidade, values='Frequência', names='Classificação', title='Modalidade de Atendimento')
col4.plotly_chart(freq_modalidade, use_container_width=True)

#Criando os Gŕafico com os Resultados filtrados por Topologia
col5.title('Dados filtrados por topografia')
topo = st.sidebar.selectbox('Selecione a Topografia', df['topografia_v2_9594b2'].unique())
df_filtered = df[df['topografia_v2_9594b2'] == topo]

freq_modalidade_filtered = df_filtered['modalidade_tratamento_v2_e9afd4'].value_counts().reset_index()
freq_modalidade_filtered.columns = ['Modalidade', 'Frequência']
graf_modalidade_filtered = px.pie(freq_modalidade_filtered, values='Frequência', names='Modalidade', title='Modalidade de Tratamento')
col6.plotly_chart(graf_modalidade_filtered, use_container_width=True)

fmc = df_filtered['modalidade_consulta_v2_66a4eb'].value_counts().reset_index()
fmc.columns = ['Classificação', 'Frequência']
graf_fmc = px.pie(fmc, values='Frequência', names='Classificação', title='Modalidade de Consulta')
col7.plotly_chart(graf_fmc, use_container_width=True)
