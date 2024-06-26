import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

planilha = r'C:\Users\moesios\Desktop\gráficos - pesquisas\MATRIZES AMOSTRAIS -.xlsx'
df_viagens = pd.read_excel(planilha, sheet_name='VIAGENS VÁLIDAS')

sns.set_theme(style="darkgrid", palette="deep")

gender_percentages = df_viagens['Gênero'].value_counts(normalize=True) * 100
plt.figure(figsize=(8, 6))
plt.pie(gender_percentages, labels=gender_percentages.index, autopct='%1.1f%%', startangle=140, colors=['#8E9AAF', '#EFD3D7', '#DEE2FF'])
plt.title('Percentual de Gênero Pesquisados')
plt.show()

#ensino_percentages = df_viagens['Escola pública/particular'].value_counts(normalize=True) * 100
#plt.figure(figsize=(8, 6))
#plt.pie(ensino_percentages, labels=ensino_percentages.index, autopct='%1.1f%%', startangle=140, colors=['#8dd3c7', '#fb8072'])
#plt.title('Percentual de Ensino Matriculado (Escola Pública/Particular)')
#plt.show()

viagens_por_morador = df_viagens.groupby('ID_MORADOR')['NUM_VIAGEM'].sum()
plt.figure(figsize=(10, 6))
sns.histplot(viagens_por_morador, bins=20, kde=True, edgecolor='black')
plt.xlabel('Número de Viagens')
plt.ylabel('Quantidade de Moradores')
plt.title('Quantidade de Viagens por Morador')
plt.show()

tipo_viagem_percentages = df_viagens['TIPO_VIAGEM'].value_counts(normalize=True) * 100
plt.figure(figsize=(8, 6))
plt.pie(tipo_viagem_percentages, labels=tipo_viagem_percentages.index, autopct='%1.1f%%', startangle=140, colors=['#bebada', '#fdb462'])
plt.title('Percentual de Viagens por Tipo')
plt.show()

escolha_modal_percentages = df_viagens['ESCOLHA MODAL'].value_counts(normalize=True) * 100
plt.figure(figsize=(8, 6))
plt.pie(escolha_modal_percentages, labels=escolha_modal_percentages.index, autopct='%1.1f%%', startangle=140, colors=['#b3de69', '#fccde5', '#ffffb3'])
plt.title('Percentual de Escolha Modal')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df_viagens['Tempo_total'], bins=20, kde=True, edgecolor='black')
plt.xlabel('Tempo Total de Viagem (minutos)')
plt.ylabel('Número de Viagens')
plt.title('Distribuição do Tempo de Viagem')
plt.show()

viagens_semana = df_viagens[df_viagens['FINAL DE SEMANA'] == 'N']['ID_MORADOR'].value_counts()
plt.figure(figsize=(10, 6))
sns.histplot(viagens_semana, bins=20, kde=True, edgecolor='black')
plt.xlabel('Número de Viagens')
plt.ylabel('Quantidade de Moradores')
plt.title('Quantidade de Viagens por Pessoa durante a Semana')
plt.show()

viagens_fim_de_semana = df_viagens[df_viagens['FINAL DE SEMANA'] == 'S']['ID_MORADOR'].value_counts()
plt.figure(figsize=(10, 6))
sns.histplot(viagens_fim_de_semana, bins=20, kde=True, edgecolor='black')
plt.xlabel('Número de Viagens')
plt.ylabel('Quantidade de Moradores')
plt.title('Quantidade de Viagens por Pessoa no Final de Semana')
plt.show()

modo_principal_percentages = df_viagens['MODO PRINCIPAL'].value_counts(normalize=True) * 100
plt.figure(figsize=(8, 6))
plt.pie(modo_principal_percentages, labels=modo_principal_percentages.index, autopct='%1.1f%%', startangle=140, colors=['#ccebc5', '#ffed6f', '#8dd3c7'])
plt.title('Percentual de Modo de Transporte Principal')
plt.show()

#escolha_modal_por_horario = df_viagens.groupby('Faixa_horaria')['ESCOLHA MODAL'].value_counts(normalize=True).unstack()
#escolha_modal_por_horario.plot(kind='bar', stacked=True, figsize=(12, 8), color=['#bebada', '#b3de69', '#fccde5'])
#plt.title('Percentual de Escolha Modal por Faixa Horária')
#plt.xlabel('Faixa Horária')
#plt.ylabel('Percentual de Escolha Modal')
#plt.legend(title='Escolha Modal')
#plt.show()

escolha_modal_por_faixa_etaria = df_viagens.groupby('Faixa etária')['ESCOLHA MODAL'].value_counts(normalize=True).unstack()
escolha_modal_por_faixa_etaria.plot(kind='bar', stacked=True, figsize=(12, 8), color=['#ccebc5', '#ffed6f', '#8dd3c7'])
plt.title('Percentual de Escolha Modal por Faixa Etária')
plt.xlabel('Faixa Etária')
plt.ylabel('Percentual de Escolha Modal')
plt.legend(title='Escolha Modal')
plt.show()

motivo_deslocamento_percentages = df_viagens['MOTIVO VIAGEM'].value_counts(normalize=True) * 100
plt.figure(figsize=(10, 6))
sns.barplot(x=motivo_deslocamento_percentages.values, y=motivo_deslocamento_percentages.index, palette="pastel")
plt.xlabel('Percentual de Viagens')
plt.ylabel('Motivo de Viagem')
plt.title('Percentual de Motivo de Deslocamento')
plt.show()

escolha_modal_por_motivo = df_viagens.groupby('MOTIVO VIAGEM')['ESCOLHA MODAL'].value_counts(normalize=True).unstack()
escolha_modal_por_motivo.plot(kind='bar', stacked=True, figsize=(12, 8), color=['#bebada', '#b3de69', '#fccde5'])
plt.title('Escolha Modal para Cada Motivo de Viagem')
plt.xlabel('Motivo de Viagem')
plt.ylabel('Percentual de Escolha Modal')
plt.legend(title='Escolha Modal')
plt.show()

plt.figure(figsize=(12, 8))
sns.boxplot(x='MOTIVO VIAGEM', y='Tempo_total', data=df_viagens, palette="pastel")
plt.xlabel('Motivo de Viagem')
plt.ylabel('Tempo Total de Viagem (minutos)')
plt.title('Duração de Viagens por Motivo')
plt.xticks(rotation=45)
plt.show()

viagens_diarias_por_genero = df_viagens.groupby(['ID_MORADOR', 'Gênero']).size().unstack().sum()
plt.figure(figsize=(10, 6))
sns.barplot(x=viagens_diarias_por_genero.index, y=viagens_diarias_por_genero.values, palette="pastel")
plt.xlabel('Gênero')
plt.ylabel('Quantidade de Viagens Diárias')
plt.title('Quantidade de Viagens Diárias por Gênero')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=df_viagens, x='Tempo_total', hue='Gênero', kde=True, bins=20, palette=["#8dd3c7", "#fb8072"])
plt.xlabel('Tempo Total de Viagem (minutos)')
plt.ylabel('Número de Viagens')
plt.title('Duração de Viagens por Gênero')
plt.legend(title='Gênero')
plt.show()

escolha_modal_por_genero = df_viagens.groupby('Gênero')['ESCOLHA MODAL'].value_counts(normalize=True).unstack()
escolha_modal_por_genero.plot(kind='bar', stacked=True, figsize=(12, 8), color=['#8dd3c7', '#fb8072', '#bebada'])
plt.title('Percentual de Escolha Modal por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Percentual de Escolha Modal')
plt.legend(title='Escolha Modal')
plt.show()

plt.figure(figsize=(12, 8))
sns.countplot(x='Classe', hue='MOTIVO VIAGEM', data=df_viagens[df_viagens['MOTIVO VIAGEM'] == 'Domiciliar'], palette="pastel")
plt.xlabel('Classe de Renda')
plt.ylabel('Contagem de Viagens Domiciliares')
plt.title('Motivo das Viagens Domiciliares por Classe de Renda')
plt.legend(title='Motivo de Viagem')
plt.show()

escolha_modal_por_renda = df_viagens.groupby('Classe')['ESCOLHA MODAL'].value_counts(normalize=True).unstack()
escolha_modal_por_renda.plot(kind='bar', stacked=True, figsize=(12, 8), color=['#ccebc5', '#ffed6f', '#8dd3c7'])
plt.title('Escolha Modal por Faixa de Renda')
plt.xlabel('Faixa de Renda')
plt.ylabel('Percentual de Escolha Modal')
plt.legend(title='Escolha Modal')
plt.show()
