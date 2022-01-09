#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import statistics as sts
import seaborn as srn

#Diretório onde se encontram os arquivos
path = 'C:/Users/Elvis/Documents/Estudo/UDEMY/Formação Cientista de Dados/12-2021/10.Prática em Python/dados/'

#nome do arquivo
file = 'tempo.csv'

#Lendo o arquivo
df = pd.read_csv(path + file, sep=';')

df


# In[16]:


#Aparencia
agrupado = df.groupby('Aparencia').size()
agrupado


# In[17]:


#Aparencia
agrupado.plot.bar()


# In[30]:


#Vento
agrupado = df.groupby(['Vento']).size()
agrupado


# In[31]:


#Vento
agrupado.plot.bar(color = 'gray')


# In[32]:


agrupado = df.groupby(['Jogar']).size()
agrupado


# In[33]:


agrupado.plot.bar(color = 'gray')


# In[34]:


df['Temperatura'].describe()


# In[35]:


srn.boxplot(df['Temperatura']).set_title('Temperatura')


# In[37]:


srn.distplot(df['Temperatura']).set_title('Temperatura')


# In[38]:


df['Umidade'].describe()


# In[40]:


srn.boxplot(df['Umidade']).set_title('Umidade')


# In[42]:


srn.distplot(df['Umidade']).set_title('Umidade')


# In[43]:


df.isnull().sum()


# In[44]:


#Aparencia Valor Inválido
agrupado = df.groupby('Aparencia').size()
agrupado


# In[45]:


df.loc[df['Aparencia'] == 'menos', 'Aparencia'] = "Sol"
#Validar
agrupado = df.groupby('Aparencia').size()
agrupado


# In[46]:


df['Temperatura'].describe()


# In[49]:


df.loc[ (df['Temperatura'] < -130) | (df['Temperatura'] > 130) ]


# In[50]:


mediana = sts.median(df['Temperatura'])
mediana


# In[51]:


df.loc[ (df['Temperatura'] < -130) | (df['Temperatura'] > 130), 'Temperatura' ] = mediana


# In[52]:


df.loc[ (df['Temperatura'] < -130) | (df['Temperatura'] > 130) ]


# In[54]:


agrupado = df.groupby('Umidade').size()
agrupado


# In[55]:


#Contando valores nulos
df['Umidade'].isnull().sum()


# In[57]:


mediana = sts.median(df['Umidade'])
mediana


# In[58]:


#Subistituindo valores nulos pela media
df['Umidade'].fillna(mediana, inplace=True)


# In[59]:


df['Umidade'].isnull().sum()


# In[61]:


df.loc[ (df['Umidade'] < 0) | (df['Umidade'] > 100) ]


# In[62]:


df.loc[ (df['Umidade'] < 0) | (df['Umidade'] > 100), 'Umidade' ] = mediana


# In[63]:


df.loc[ (df['Umidade'] < 0) | (df['Umidade'] > 100) ]


# In[64]:


agrupado = df.groupby('Vento').size()
agrupado


# In[66]:


df['Vento'].isnull().sum()


# In[68]:


df['Vento'].fillna('FALSO', inplace=True)


# In[69]:


df['Vento'].isnull().sum()


# In[ ]:




