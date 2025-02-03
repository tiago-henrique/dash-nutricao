import streamlit as st
import pandas as pd
import plotly.express as px

url = 'https://lmu.famerp.br/tiago/indicadores.csv'

df = pd.read_csv(url)

pc = df['data'].count()
rt = df['data_v2'].count()

st.set_page_config(layout='wide')

st.title("Dashboard - Primeira Consulta Nutrição")

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

#st.set_page_config(layout='wide')

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)
col7, col8 = st.columns(2)
col9, col10 = st.columns(2)
col11, col12 = st.columns(2)
col13, col14 = st.columns(2)
col15, col16 = st.columns(2)

col1.header('Primeira Consulta')
col1.subheader(pc)
#col2.header('Retorno')
#col2.subheader(rt)


df['topografia'] = df['topografia'].map(topografias)
freq_topografias = df['topografia'].value_counts().reset_index()
freq_topografias.columns = ['Topografia', 'Frequência']

topo = st.sidebar.selectbox('Selecione a Topografia', df['topografia'].unique())
df_filtered = df[df['topografia'] == topo]

graf_topografia = px.bar(freq_topografias, x='Frequência', y='Topografia', color='Frequência', title='Topografias - Primeira consulta', text_auto=True, orientation='h')
col3.plotly_chart(graf_topografia, use_container_width=True)
#st.write(freq_topografias)

df_filtered['modalidade_tratamento'] = df_filtered['modalidade_tratamento'].map(modalidade_tratamento)
freq_modalidade_filtrada = df_filtered['modalidade_tratamento'].value_counts().reset_index()
freq_modalidade_filtrada.columns = ['Modalidade', 'Frequência']
graf_modalidade_filtrada = px.pie(freq_modalidade_filtrada, values='Frequência', names='Modalidade', title='Modalidade de Tratamento')
col4.plotly_chart(graf_modalidade_filtrada, use_container_width=True)

#df['modalidade_tratamento'] = df['modalidade_tratamento'].map(modalidade_tratamento)
#freq_modalidade = df['modalidade_tratamento'].value_counts().reset_index()
#freq_modalidade.columns = ['Modalidade', 'Frequência']
#graf_modalidade = px.pie(freq_modalidade, values='Frequência', names='Modalidade', title='Modalidade de tratamento - Primeira consulta')
#col4.plotly_chart(graf_modalidade, use_container_width=True)

freq_imc_adulto = df['classificacao_imc_adulto'].value_counts().reset_index()
freq_imc_adulto.columns = ['Classificação', 'Frequência']
graf_imc_adulto = px.pie(freq_imc_adulto, values='Frequência', names='Classificação', title='Classificação por IMC - Adulto')
col5.plotly_chart(graf_imc_adulto, use_container_width=True)

freq_imc_idoso = df['classificacao_imc_idosos'].value_counts().reset_index()
freq_imc_idoso.columns = ['Classificação', 'Frequência']
graf_imc_idoso = px.pie(freq_imc_idoso, values='Frequência', names='Classificação', title='Classificação por IMC - Idosos')
col6.plotly_chart(graf_imc_idoso, use_container_width=True)

df['se_ganho_ponderal'] = df['se_ganho_ponderal'].map(ganho_ponderal)
freq_ganho_ponderal = df['se_ganho_ponderal'].value_counts().reset_index()
freq_ganho_ponderal.columns = ['Classificação', 'Frequência']
graf_ganho_ponderal = px.pie(freq_ganho_ponderal, values='Frequência', names='Classificação', title='Ganho Ponderal')
col7.plotly_chart(graf_ganho_ponderal, use_container_width=True)

df['se_perda_ponderal'] = df['se_perda_ponderal'].map(perda_ponderal)
freq_perda_ponderal = df['se_perda_ponderal'].value_counts().reset_index()
freq_perda_ponderal.columns = ['Classificação', 'Frequência']
graf_perda_ponderal = px.pie(freq_perda_ponderal, values='Frequência', names='Classificação', title='Perda Ponderal')
col8.plotly_chart(graf_perda_ponderal, use_container_width=True)

freq_cp_cm_homens = df['classificacao_cp_homens'].value_counts().reset_index()
freq_cp_cm_homens.columns = ['Classificação', 'Frequência']
graf_cp_cm_homens = px.pie(freq_cp_cm_homens, values='Frequência', names='Classificação', title='Classificação Circunferência Panturrilha - Homens')
col9.plotly_chart(graf_cp_cm_homens, use_container_width=True)

freq_cp_cm_mulheres = df['classificacao_cp_mulheres'].value_counts().reset_index()
freq_cp_cm_mulheres.columns = ['Classificação', 'Frequência']
graf_cp_cm_mulheres = px.pie(freq_cp_cm_mulheres, values='Frequência', names='Classificação', title='Classificação Circunferência Panturrilha - Mulheres')
col10.plotly_chart(graf_cp_cm_mulheres, use_container_width=True)

df['asg'] = df['asg'].map(asg)
freq_asg = df['asg'].value_counts().reset_index()
freq_asg.columns = ['Classificação', 'Frequência']
freq_asg = px.pie(freq_asg, values='Frequência', names='Classificação', title='Avaliação Subjetiva Global do Estado Nutricional')
col11.plotly_chart(freq_asg, use_container_width=True)

df['modalidade_consulta'] = df['modalidade_consulta'].map(modalidade)
freq_modalidade = df['modalidade_consulta'].value_counts().reset_index()
freq_modalidade.columns = ['Classificação', 'Frequência']
freq_modalidade = px.pie(freq_modalidade, values='Frequência', names='Classificação', title='Modalidade de Atendimento')
col12.plotly_chart(freq_modalidade, use_container_width=True)

df['via_alimentar'] = df['via_alimentar'].map(via_alimentar)
freq_via_alimentar = df['via_alimentar'].value_counts().reset_index()
freq_via_alimentar.columns = ['Classificação', 'Frequência']
freq_via_alimentar = px.pie(freq_via_alimentar, values='Frequência', names='Classificação', title='Via Alimentar')
col13.plotly_chart(freq_via_alimentar, use_container_width=True)

df['tipo_via_alimentar'] = df['tipo_via_alimentar'].map(tipo_via)
freq_tipo_via = df['tipo_via_alimentar'].value_counts().reset_index()
freq_tipo_via.columns = ['Classificação', 'Frequência']
freq_tipo_via = px.bar(freq_tipo_via, x='Frequência', y='Classificação', color='Frequência', title='Tipo de Via Alimentar', text_auto=True, orientation='h')
col14.plotly_chart(freq_tipo_via, use_container_width=True)
