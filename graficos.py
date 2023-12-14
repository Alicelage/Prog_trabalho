#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def faz_porcentagem(a,b):
      calculo=(a/b)*100
      formatando="{0:.2f}"
      return float(formatando.format(calculo))

def arquivo_log(nome_arquivo,analise_nome, dados_x, dados_y,eixo_x,eixo_y):
      arquivo=open((nome_arquivo + '.log'), 'a')
      print('Arquivo de log referente a análise:', analise_nome,'intitulado:', nome_arquivo, file=arquivo)
      print('Os dados da análise são:', file=arquivo)
      print('Para eixo X (',eixo_x,'): dados =', dados_x, file=arquivo)
      print('Para eixo Y (',eixo_y,'): dados =', dados_y, file=arquivo)
      arquivo.close()


df=pd.read_csv('Vitimas_DadosAbertos_20230912.csv', encoding='utf-8', header=0, sep=';')
colunas_analise1=['uf_acidente']
analise_1=pd.DataFrame(data=df, columns=colunas_analise1, index=range(7835129))
analise_1['ocorrencia'] = '1'

# contando quantos acidentes houveram por estado brasileiro entre os anos 2018 e 2023
por_estado=analise_1.groupby(['uf_acidente']).count().reset_index()
print(por_estado)
print(list(por_estado.index))

# plotando primeiro gráfico que faz referência ao numero de acidentes por estado brasileiro
estados= ["AC","AL","AM","AP","BA","CE","DF","ES","GO","MA","MG","MS","MT","PA","PB","PE","PI","PR","RJ","RN","RO","RR","RS","SC","SE","SP","TO"]
valores_estados=[]
for column in por_estado['ocorrencia']: 
      valores_estados.append(column)

plt.figure(figsize = (20,5))
plt.bar(estados, valores_estados, color = "pink", label = "Ocorrencia de acidentes / Estado brasileiro")
plt.grid(False)
plt.box(True)
plt.xlabel('ESTADOS')
plt.ylabel('ACIDENTES')
plt.title("Número de ocorrência de acidentes de trânsito por ESTADO brasileiro de 2018 a maio de 2023")
plt.legend(fontsize=20)

f_arquivo_1=arquivo_log('resultados_analise_dados','Número de acidentes por UF no Brasil',estados,valores_estados,'ESTADOS BRASILEIROS','ACIDENTES DE TRÂNSITO')


# media de acidentes por regiao de 2018 a 2023
norte_br=pd.DataFrame(data=por_estado.iloc[[0,2,3,13,20,21,26]], columns=['ocorrencia'])
print("Média de acidentes na região norte do Brasil:",norte_br['ocorrencia'].mean())

nordeste_br=pd.DataFrame(data=por_estado.iloc[[1,4,5,9,14,15,16,19]], columns=['ocorrencia'])
print("Média de acidentes na região nordeste do Brasil:",nordeste_br['ocorrencia'].mean())

centro_o_br=pd.DataFrame(data=por_estado.iloc[[6,8,11,12]], columns=['ocorrencia'])
print("Média de acidentes na região centro-oeste do Brasil:",centro_o_br['ocorrencia'].mean())

sudeste_br=pd.DataFrame(data=por_estado.iloc[[7,10,18,25]], columns=['ocorrencia'])
print("Média de acidentes na região sudeste do Brasil:",sudeste_br['ocorrencia'].mean())

sul_br=pd.DataFrame(data=por_estado.iloc[[17,22,23,]], columns=['ocorrencia'])
print("Média de acidentes na região sul do Brasil:",sul_br['ocorrencia'].mean())

#plotando segundo gráfico sobre média de acidentes por região do Brasil
regioes=["NORTE","NORDESTE","CENTRO-OESTE","SUDESTE","SUL"]
acidentes_regioes=[norte_br['ocorrencia'].mean(),nordeste_br['ocorrencia'].mean(),centro_o_br['ocorrencia'].mean(),sudeste_br['ocorrencia'].mean(),sul_br['ocorrencia'].mean()]
plt.figure(figsize = (20,15))
plt.bar(regioes, acidentes_regioes, color = "green",label = "Ocorrencia de acidentes / Regiões do Brasil")
plt.grid(False)
plt.box(True)
plt.xlabel('DIVISÃO REGIONAL DO BRASIL')
plt.ylabel('ACIDENTES')
plt.title("Média de ocorrência de acidentes de trânsito por REGIÃO do Brasil de 2018 a maio de 2023")

f_arquivo_2=arquivo_log('resultados_analise_dados','Média de acidentes por REGIÃO no Brasil',regioes,acidentes_regioes,'DIVISÃO REGIONAL DO BRASIL','MÉDIA DE ACIDENTES DE TRÂNSITO')

plt.legend(fontsize=20)

# calculando numero de acidentes por anos compreendido entre 2018 e 2023
coluna=['ano_acidente']
analise_2=pd.DataFrame(data=df, columns=coluna)
analise_2['ocorrencia'] = '1'
acidente_anual = analise_2.groupby(['ano_acidente']).count().reset_index()
print(acidente_anual)

#plotando terceiro gráfico sobre acidentes anualmente de 2018 a 2023
anos=["2018","2019","2020","2021","2022","2023"]
anos_acidente=[]
for column in acidente_anual['ocorrencia']:
      anos_acidente.append(column)
plt.figure(figsize=(20,10))
plt.plot(anos, anos_acidente, marker="o", linestyle="-", color = "red", label = "Acidentes/Ano")
plt.title("Gráfico indica a ocorrência de acidentes de trânsito por ANO (2018/maio 2023)")
plt.grid(True)
plt.box(True)
plt.legend(fontsize=20)
plt.xlabel("Anos")
plt.ylabel("Acidentes por milhão de ocorrência")

f_arquivo_3=arquivo_log('resultados_analise_dados','Número de acidentes por ANO no Brasil',anos,anos_acidente,'ANOS DE 2018 A 2023','ACIDENTES DE TRÂNSITO')


# Calculo faixa etaria das vitimas
coluna_a=['faixa_idade']
analise_3=pd.DataFrame(data=df, columns=coluna_a)
analise_3['ocorrencia'] = '1'
idade_agrupada=analise_3.groupby(['faixa_idade']).count().reset_index()
print("Faixa etária dos indivíduos envolvidos em acidentes:", idade_agrupada)
print("A menor faixa etária está entre vítimas maiores que 80 anos:", idade_agrupada['ocorrencia'].min(),"acidentes")
# removendo os dados não informados
idade_agrupada.iloc[14]=0
print("A maior faixa etária vítima de acidentes está entre 30 e 34 anos de idade:", idade_agrupada['ocorrencia'].max(),"acidentes")
# Plotando quarto gráfico sobre faixa etária das vitimas
idade_=[]
idade_agrupada.drop([14])
for column in idade_agrupada['faixa_idade']:
      idade_.append(column)
acidente_idade=[]
for column in idade_agrupada['ocorrencia']:
      acidente_idade.append(column)
plt.figure(figsize = (35,20))
plt.plot(idade_, acidente_idade, marker="o", linestyle="-", color = "blue", label = "Acidentes/Idade")
plt.title("Gráfico indica a ocorrência de acidentes de trânsito por FAIXA ETÁRIA (2018/maio 2023)", fontsize=25)
plt.grid(True)
plt.box(True)
plt.legend(fontsize=20)
plt.xlabel("IDADE", fontsize=20)
plt.ylabel("ACIDENTES por milhão de ocorrência", fontsize=20)

f_arquivo_4=arquivo_log('resultados_analise_dados','Número de acidentes por FAIXA ETÁRIA no Brasil',idade_,idade_agrupada,'FAIXA ETÁRIA DAS VÍTIMAS','ACIDENTES DE TRÂNSITO')

# Calcular vítimas mulheres x vitimas homens
coluna_b=['genero','tp_envolvido']
analise_4=pd.DataFrame(data=df, columns=coluna_b)
analise_4['ocorrencia'] = '1'
agrupa_genero_tipo=analise_4.groupby(['genero','tp_envolvido']).count().reset_index()
print(agrupa_genero_tipo)
agrupa_genero=analise_4.groupby(['genero']).count().reset_index()
agrupa_tipo=analise_4.groupby(['tp_envolvido']).count().reset_index()
print(agrupa_genero)
print(agrupa_tipo)
# Indices femininos
todo_f=np.array([[agrupa_genero_tipo['ocorrencia'][7],agrupa_genero_tipo['ocorrencia'][10],agrupa_genero_tipo['ocorrencia'][11],agrupa_genero['ocorrencia'][1]],[agrupa_genero_tipo['ocorrencia'][13],agrupa_genero_tipo['ocorrencia'][16], agrupa_genero_tipo['ocorrencia'][17], agrupa_genero['ocorrencia'][2]],[agrupa_tipo['ocorrencia'][1],agrupa_tipo['ocorrencia'][4], agrupa_tipo['ocorrencia'][5],7835129]])
print("Matriz que expressa valorez por genero e tipos:",todo_f)
fem_motorista= faz_porcentagem(todo_f[0, 0],todo_f[2, 0]) 
fem_passageiro= faz_porcentagem(todo_f[0, 1],todo_f[2, 1])
fem_pedestre= faz_porcentagem(todo_f[0, 2],todo_f[2, 2])
fem_total= faz_porcentagem(todo_f[0 ,3],todo_f[2, 3])
print("Porcentagem de mulheres motoristas:", fem_motorista)
print("Porcentagem de mulheres passageiro:", fem_passageiro)
print("Porcentagem de mulheres pedestres:", fem_pedestre)
print("Porcentagem de mulheres sob total:", fem_total)
# Indices masculinos
masc_motorista= faz_porcentagem(todo_f[1, 0],todo_f[2, 0])
masc_passageiro= faz_porcentagem(todo_f[1, 1],todo_f[2, 1])
masc_pedestre= faz_porcentagem(todo_f[1, 2],todo_f[2, 2])
masc_total= faz_porcentagem(todo_f[1, 3],todo_f[2, 3])
print("Porcentagem de homens motoristas:", masc_motorista)
print("Porcentagem de homens passageiro:", masc_passageiro)
print("Porcentagem de homens pedestres:", masc_pedestre)
print("Porcentagem de homens sob total:", masc_total)

# Plotando quinto gráfico para gêneros e categorias
genero=["Feminino Motorista","Feminino Passageiro","Feminino Pedestre","Masculino Motorista","Masculino Passageiro","Masculino Pedestre"]
acidente_genero=[fem_motorista,fem_passageiro,fem_pedestre,masc_motorista,masc_passageiro,masc_pedestre]
plt.figure(figsize = (20,10))
plt.pie(acidente_genero, labels = genero, autopct = '%1.1f%%', shadow = True, startangle = 90)
plt.title("Percentual por categoria de GÊNERO em acidentes de trânsito")
plt.legend(fontsize=10)

f_arquivo_5=arquivo_log('resultados_analise_dados','Número de acidentes por CATEGORIA DE TRÁFEGO E GÊNERO ',genero,acidente_genero,'CATEGORIAS','PERCENTUAL DE ACIDENTES DE TRÂNSITO')

# Plotando sexto gráfico sobre total de gêneros
genero_2=["FEMININO","MASCULINO"]
valores_genero2=[fem_total,masc_total]
plt.figure(figsize = (20,10))
plt.pie(valores_genero2, labels = genero_2, autopct = '%1.1f%%', shadow = True, startangle = 90)
plt.title("Percentual por GÊNERO em acidentes de trânsito")
plt.legend(fontsize=25)

f_arquivo_6=arquivo_log('resultados_analise_dados','Número de acidentes por GÊNERO no Brasil',genero_2,valores_genero2,'GÊNERO','PERCENTUAL DE ACIDENTES DE TRÂNSITO')

# Calcular vitimas supeitas do uso de alcool
coluna_c=['susp_alcool']
analise_5=pd.DataFrame(data=df, columns=coluna_c)
analise_5['ocorrencia'] = '1'
dados_alcool=analise_5.groupby(['susp_alcool']).count().reset_index()
print(dados_alcool)
dados_alcool_1=dados_alcool.copy()
# Eliminar valores dos dados "desconhecido","nao aplicavel" e "nao informado"
dados_alcool_1.iat[0, 1]=0
dados_alcool_1.iat[2, 1]=0
dados_alcool_1.iat[3, 1]=0
dados_alcool.drop([0])
dados_alcool.drop([2])
dados_alcool.drop([3])
total_alcool=dados_alcool_1['ocorrencia'].sum()
prob_nao_alcool=faz_porcentagem(dados_alcool_1.iat[1, 1],total_alcool)
prob_alcool=faz_porcentagem(dados_alcool_1.iat[4, 1],total_alcool)
print("A porcentagem que indica que a vitima esteve alcoolizada em um acidente de trânsito é:",prob_alcool)
print("A porcentagem que indica que a vitima não esteve alcoolizada em um acidente de transito é:",prob_nao_alcool)

# Plotando sétimo gráfico sobre influência do alcool nos acidentes
coluna_h=['ano_acidente','susp_alcool']
analise_10=pd.DataFrame(data=df,columns=coluna_h)
analise_10['ocorrencia']= '1'
analise_10=analise_10.groupby(['ano_acidente','susp_alcool']).count().reset_index()
print(analise_10)
print(analise_10)
anos_alcool=["2018","2019","2020","2021","2022","2023"]
alcool=[analise_10.iat[4,2],analise_10.iat[9, 2],analise_10.iat[14, 2],analise_10.iat[19, 2],analise_10.iat[24, 2],analise_10.iat[29, 2]]
not_alcool=[analise_10.iat[1, 2],analise_10.iat[6, 2],analise_10.iat[11, 2],analise_10.iat[16, 2],analise_10.iat[21, 2],analise_10.iat[26, 2]]
plt.figure(figsize=(20,15) )
plt.bar(anos_alcool,alcool, color='pink',label='Acidententes com a presença de álcool')
plt.bar(anos_alcool,not_alcool,bottom=alcool, color='yellow', label='Acidentes com a ausência de álcool')
plt.title('Acidentes de trânsito causados pela presença de ÁLCOOL (2018/maio 2023)')
plt.grid(False)
plt.box(True)
plt.xlabel("ANOS")
plt.ylabel("NÚMERO ACIDENTES")
plt.legend(fontsize=20)

f_arquivo_7=arquivo_log('resultados_analise_dados','Número de acidentes pelo envolvimento com ÁLCOOL por ano no Brasil',anos_alcool,alcool,'ANOS','ACIDENTES DE TRÂNSITO PELA PRESENÇA DE ÁLCOOL')

# Calcular óbitos por ano
coluna_d=['qtde_obitos','ano_acidente']
analise_6=pd.DataFrame(data=df, columns=coluna_d)
analise_6['ocorrencia'] = '1'
agrupa_quant_obt=analise_6.groupby(['qtde_obitos','ano_acidente']).count().reset_index()
print(agrupa_quant_obt)
obt_calc=agrupa_quant_obt.copy()
# Calculo da quantidade de acidentes - qntd de acidentes com 0 obitos
obt_2018=acidente_anual.iat[0, 1] - obt_calc.iat[0, 2]
obt_2019=acidente_anual.iat[1, 1] - obt_calc.iat[1, 2]
obt_2020=acidente_anual.iat[2, 1] - obt_calc.iat[2, 2]
obt_2021=acidente_anual.iat[3, 1] - obt_calc.iat[3, 2]
obt_2022=acidente_anual.iat[4, 1] - obt_calc.iat[4, 2]
obt_2023=acidente_anual.iat[5, 1] - obt_calc.iat[5, 2]
print("Morreram", obt_2018, "pessoas em 2018")
print("Morreram", obt_2019, "pessoas em 2019")
print("Morreram", obt_2020, "pessoas em 2020") 
print("Morreram", obt_2021, "pessoas em 2021")
print("Morreram", obt_2022, "pessoas em 2022") 
print("Morreram", obt_2023, "pessoas em 2023")
# Calculo da porcentagem de obitos por ano
porc_2018=faz_porcentagem(obt_2018,acidente_anual.iat[0, 1])
porc_2019=faz_porcentagem(obt_2019,acidente_anual.iat[1, 1])
porc_2020=faz_porcentagem(obt_2020,acidente_anual.iat[2, 1])
porc_2021=faz_porcentagem(obt_2021,acidente_anual.iat[3, 1])
porc_2022=faz_porcentagem(obt_2022,acidente_anual.iat[4, 1])
porc_2023=faz_porcentagem(obt_2023,acidente_anual.iat[5, 1])
print("Isso corresponde a:")
print("2018 =",porc_2018,"por cento")
print("2019 =",porc_2019,"por cento")
print("2020 =", porc_2020,"por cento")
print("2021 =",porc_2021, "por cento")
print("2022 =", porc_2022,"por cento")
print("2023 =",porc_2023, "por cento")

# Plotando oitavo gráfico da análise de óbitos por ano 
obitos_anos=['2018','2019','2020','2021','2022','2023']
obitos_quant=[obt_2018,obt_2019,obt_2020,obt_2021,obt_2022,obt_2023]
obt_porc=[porc_2018,porc_2019,porc_2020,porc_2021,porc_2022,porc_2023]
anos_acidente=[]

for column in acidente_anual['ocorrencia']:
      anos_acidente.append(column)
dado_obitos=[[obitos_quant],[anos_acidente]]

plt.figure(figsize=(25,10))
bp_dict = plt.bar(obitos_anos, list(map(float, obitos_quant)), align='edge', width=-0.4, label='Quantidade de óbitos por acidentes')
bp_dict = plt.bar(obitos_anos, list(map(float, anos_acidente)), align='edge', width=0.4, label='Quantidade de acidentes por ano')
plt.title('ÓBITOS por acidentes de trânsito (2018/maio 2023)')
plt.box(True)
plt.legend(fontsize=20)
plt.xlabel("ANO")
plt.ylabel("ÓBITOS em acidentes de trânsito")
plt.show()

f_arquivo_8=arquivo_log('resultados_analise_dados','Número de óbitos por número de acidentes no Brasil',obitos_anos,obitos_quant,'ANOS','ÓBITOS POR ACIDENTES DE TRÂNSITO')
f_arquivo_alt=arquivo_log('resultados_analise_dados','Percentual de óbitos por ano de acidente de trânsito no Brasil',obitos_anos,obt_porc,'ANOS','PERCENTUAL DE ACIDENTES DE TRÂNSITO')

# Importando próxima base de dados 
df_2=pd.read_csv('TipoVeiculo_DadosAbertos_20230912.csv', encoding='utf-8', header=0, sep=';')

# Calculo de tipos de veiculo envolvido nos acidentes de trânsito
coluna_e=['tipo_veiculo']
analise_7=pd.DataFrame(data=df_2, columns=coluna_e)
analise_7['contador']='1'
contabiliza_veiculo=analise_7.groupby(['tipo_veiculo']).count().reset_index()
print("Base de dados veiculos envolvidos em acidentes:")
print(contabiliza_veiculo)
# Desconsiderando valores "desconhecido" e "nao informado"
contabiliza_veiculo.iat[12, 1]=0
contabiliza_veiculo.iat[18, 1]=0
# Calculando qual o veículo menos acidentado e qual o mais acidentado
minimo=contabiliza_veiculo['contador'].min()
maximo=contabiliza_veiculo['contador'].max()
print("O veículo menos acidentado possui:", minimo, "acidentes")
print("O veículo mais acidentado possui:", maximo, "acidentes")

# Plotando nono gráfico sobre veículos 
veiculo_nome=['AUTOMOVEL','MOTOCICLETA','CAMINHAO','ONIBUS','BICICLETA','DESCONHECIDO']
veiculo_num=[2762951,1074240,82403,205847,285564,554233]
veiculos_={'AUTOMOVEL':2762951,'MOTOCICLETA':1074240,'CAMINHAO':285564,'ONIBUS':205847,'BICICLETA':82403,'DESCONHECIDO': 554233}
nome_veiculo = list(veiculos_.keys()) 
valores_veiculo = list(veiculos_.values())  

plt.figure(figsize=(15,10))
plt.barh(nome_veiculo,valores_veiculo, color='blue', label='Ocorrência de acidentes por categoria')
plt.title('Ocorrência de acidentes de trânsito por categoria de VEÍCULOS (2018/maio 2023)')
plt.xlabel=('Categoria de veículos')
plt.ylabel=('Acidentes em ocorrências')
plt.grid(True)
plt.legend(fontsize=15)
plt.show

f_arquivo_9=arquivo_log('resultados_analise_dados','Número de acidentes por CATEGORIA DE VEÍCULO no Brasil',veiculo_nome,veiculo_num,'CATEGORIA DE VEÍCULO','ACIDENTES DE TRÂNSITO')

# Calculando a probabilidade de ocorrência de cada (automóvel, motocicleta, bicileta, caminhão, Ônibus) veículo 
todo_veiculo=contabiliza_veiculo['contador'].sum()
# Calculando a probabilidade de ocorrência de cada (automóvel, motocicleta, bicileta, caminhão, Ônibus) veículo 
todo_veiculo=contabiliza_veiculo['contador'].sum()

prob_automovel=faz_porcentagem(contabiliza_veiculo.iat[0, 1],todo_veiculo)
print("Porcentagem que corresponde a acidentes envolvendo carro:", prob_automovel)
prob_motocicleta=faz_porcentagem(contabiliza_veiculo.iat[15, 1],todo_veiculo)
print("Porcentagem que corresponde a acidentes envolvendo motocicleta:", prob_motocicleta)
prob_bicicleta=faz_porcentagem(contabiliza_veiculo.iat[1, 1],todo_veiculo)
print("Porcentagem que corresponde a acidentes envolvendo bicicleta:", prob_bicicleta)
prob_caminhao=faz_porcentagem(contabiliza_veiculo.iat[3, 1],todo_veiculo)
print("Porcentagem que corresponde a acidentes envolvendo caminhão:", prob_caminhao)
prob_onibus=faz_porcentagem(contabiliza_veiculo.iat[19, 1],todo_veiculo)
print("Porcentagem que corresponde a acidentes envolvendo ônibus:", prob_onibus)
prob_desc=faz_porcentagem(554233,todo_veiculo)

# Plotando nono gráfico sobre as porcentagens
prob_veic=[prob_automovel,prob_motocicleta,prob_bicicleta,prob_onibus,prob_caminhao,prob_desc]
veiculos_=['AUTOMOVEL','MOTOCICLETA','BICICLETA','ONIBUS','CAMINHAO','DESCONHECIDO']
plt.figure(figsize = (18,10))
plt.pie(prob_veic, labels = veiculos_, autopct = '%1.1f%%', shadow = True, startangle = 90)
plt.title("Percentual por categoria de VEÍCULOS em acidentes de trânsito")
plt.legend(fontsize=8)

f_arquivo_10=arquivo_log('resultados_analise_dados','Percentual de acidentes por CATEGORIA DE VEÍCULO no Brasil',veiculos_,prob_veic,'CATEGORIA DE VEÍCULO','PERCENTUAL DE ACIDENTES DE TRÂNSITO')

# Importando próxima base de dados
df_3=pd.read_csv('Acidentes_DadosAbertos_20230912.csv', encoding='utf-8', header=0, sep=';')

# Calculo de analise por dia de acidente
coluna_f=['dia_semana']
analise_8=pd.DataFrame(data=df_3, columns=coluna_f)
analise_8['num_acidentes'] = '1'
contador_semanal=analise_8.groupby(['dia_semana']).count().reset_index()
print(contador_semanal)
# Contabilizando o dia da semana que mais ocorreu acidente de trânsito
dia_maior=contador_semanal['num_acidentes'].max()
print("Posição do maior número de acidentes na semana: \n {contador_semanal.isin([dia_maior])}")
print('O dia que mais ocorreu acidente é: {contador_semanal.iat[5, 0]} somando {contador_semanal.iat[5, 1]} acidentes \n')
# Contabilizando o dia da semana que menos ocorreu acidente de trânsito
dia_menor=contador_semanal['num_acidentes'].min()
print("Posição do menor número de acidentes na semana: \n {contador_semanal.isin([dia_menor])}")
print('O dia que menos ocorreu acidente é: {contador_semanal.iat[0, 0]} somando {contador_semanal.iat[0, 1]} acidentes \n')
# Contagem da porcentagem por dia de acidentes
total=contador_semanal['num_acidentes'].sum()
domingo=faz_porcentagem(contador_semanal.iat[0, 1],total)
print("O dia DOMINGO possui:", domingo, "dos acidentes.\n")
segunda= faz_porcentagem(contador_semanal.iat[4, 1],total)
print("O dia SEGUNDA-FEIRA possui:", segunda, "dos acidentes.\n")
terça=faz_porcentagem(contador_semanal.iat[6, 1],total)
print("O dia TERÇA-FEIRA possui:", terça, "dos acidentes.\n")
quarta=faz_porcentagem(contador_semanal.iat[1, 1],total)
print("O dia QUARTA-FEIRA possui:", quarta,"dos acidentes.\n")
quinta=faz_porcentagem(contador_semanal.iat[2, 1],total)
print("O dia QUINTA-FEIRA possui:", quinta, "dos acidentes.\n")
sexta=faz_porcentagem(contador_semanal.iat[5, 1],total)
print("O dia SEXTA-FEIRA possui:", sexta,"dos acidentes.\n")
sabado=faz_porcentagem(contador_semanal.iat[3, 1],total)
print("O dia SABADO possui:", sabado,"dos acidentes.\n")

#Plotando décimo gráfico sobre dias da semana que ocorreram acidentes
dias=['DOMINGO','SEGUNDA-FEIRA','TERÇA-FEIRA','QUARTA-FEIRA','QUINTA-FEIRA','SEXTA-FEIRA','SÁBADO']
porc_dias=[domingo,segunda,terça,quarta,quinta,sexta,sabado]
plt.figure(figsize=(20,10))
plt.plot(dias, porc_dias, marker="o", linestyle="-", color = "green", label = "Acidentes/Dias da semana")
plt.title("Gráfico indica o percentual de acidentes de trânsito por DIAS DA SEMANA (2018/maio 2023)")
plt.grid(True)
plt.box(True)
plt.legend(fontsize=20)
plt.xlabel=("Dia semanal")
plt.ylabel=("Acidentes por milhão de ocorrência")

f_arquivo_11=arquivo_log('resultados_analise_dados','Percentual de acidentes por DIA DA SEMANA no Brasil',dias,porc_dias,'DIAS DA SEMANA','PERCENTUAL DE ACIDENTES DE TRÂNSITO')
  
# Fase do dia que mais ocorreu acidente
coluna_g=['fase_dia']
analise_9=pd.DataFrame(data=df_3, columns=coluna_g)
analise_9['ocorrencias'] = '1'
agrupa_acid_fase=analise_9.groupby(['fase_dia']).count().reset_index()
print(agrupa_acid_fase)
# Desconsiderando dados "desconhecidos" e "nao informado"
agrupa_acid_fase.drop(agrupa_acid_fase.index[0])
todo=agrupa_acid_fase['ocorrencias'].sum()
fase_menor=agrupa_acid_fase['ocorrencias'].min()
fase_maior=agrupa_acid_fase['ocorrencias'].max()
print("A fase do dia:", agrupa_acid_fase.iat[5, 0], "possui o maior número de acidentes, com:", fase_maior, "ocorrências.")
print("A fase do dia:", agrupa_acid_fase.iat[1, 0], "possui o menor número de acidentes, com:", fase_menor, "ocorrências.")
# Calculando porcentagem dos dias
manha=faz_porcentagem(agrupa_acid_fase.iat[2, 1],todo)
noite=faz_porcentagem(agrupa_acid_fase.iat[4, 1],todo)
tarde=faz_porcentagem(agrupa_acid_fase.iat[5, 1],todo)
madruga=faz_porcentagem(agrupa_acid_fase.iat[1, 1],todo)
print("Manhã:", manha, "por cento dos acidentes.")
print("Tarde:", tarde, "por cento dos acidentes.")
print("Noite:", noite, "por cento dos acidentes.")
print("Madrugada:", madruga, "por cento dos acidentes.")

# Plotando último gráfico sobre a ocorrência de acidentes de trânsito por fases do dia
fases_=['MANHÃ','TARDE','NOITE','MADRUGADA']
quant_fases=[manha,tarde,noite,madruga]
plt.figure(figsize=(15,10))
plt.barh(fases_,quant_fases, color='yellow', label='Acidentes de trânsito')
plt.title('Ocorrência de acidentes de trânsito por FASES DO DIA (2018/maio 2023)')
plt.xlabel=('Fases do dia')
plt.ylabel=('Acidentes por ocorrências')
plt.legend(fontsize=15)
plt.show

f_arquivo_12=arquivo_log('resultados_analise_dados','Percentual de acidentes por FASES DO DIA no Brasil',fases_,quant_fases,'FASES DO DIA','PERCENTUAL DE ACIDENTES DE TRÂNSITO')


# %%
