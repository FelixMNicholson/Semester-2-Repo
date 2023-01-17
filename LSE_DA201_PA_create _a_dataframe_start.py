#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics using Python

# ## Practical activity: Create a DataFrame from the dictionary

# **This is the start to the activity.**
# 
# A peer has come to you for help. They have started building a dictionary using Jupyter Notebook. Below you will find their incomplete code. Now that you have learned to add values and keys using a DataFrame, make changes to the code to complete the following:
# - Import the dictionary into a DataFrame and add two more rows to the state and capital columns.
# - Sense-check the code that was presented to you is accurate and free from errors.

# ### Raw data
# - states = ["Acre", "Alogoas", "Amapa", "Amazonas", "Bahia", "Ceara", "Distrito Federal", 
#             "Espirito Santo", "Goiás", "Maranhao", "Mato grosso", "Mato grosso do sul", 
#             "Minas gerais", "Para", "Paraiba", "Parana", "Pernambuco", "Piaui", "Rio de Janeiro", 
#             "Rio Grande do norte", "Rio Grande do Sul", "Rondonia", "Roraima", "Santa Catarina", 
#             "Sao Paulo", "Sergipe", "Tocantins"]
# 
# - capitals = ["Rio Branco", "Maceió" "Macapá", "Manaus", "Salvador", "Fortaleza", "Brasília", 
#               "Vitória", "Goiânia", "São Luís", "Cuiabá", "Campo Grande","Belo Horizonte","Belém",
#               "João Pessoa", "Curitiba", "Recife", "Teresina", "Rio de Janeiro", "Natal", "Porto Alegre", 
#               "Porto Velho", "Boa Vista", "Florianópolis", "São Paulo", "Aracaju", "Palmas"]

# ### Incomplete Dictionary

# In[44]:


# Import pandas.
import pandas as pd


#Add a Comma to List so States and Capitals ('Array') is same length 

brazil = {'states': ["Acre", "Alogoas", "Amapa", "Amazonas", 
                    "Bahia", "Ceara", "Distrito Federal", 
"Espirito Santo", "Goiás", "Maranhao", "Mato grosso", "Mato grosso do sul", "Minas gerais",
 "Para", "Paraiba", "Parana", 
 "Pernambuco", "Piaui", "Rio de Janeiro", 
 "Rio Grande do norte", "Rio Grande do Sul", "Rondonia", "Roraima", 
          "Santa Catarina", "Sao Paulo", "Sergipe", "Tocantins"],
'Capitals': ["Rio Branco", "Maceió", "Macapá", "Manaus", "Salvador", "Fortaleza", "Brasília",
  "Vitória", "Goiânia", "São Luís", "Cuiabá", "Campo Grande","Belo Horizonte","Belém",
        "João Pessoa", "Curitiba", "Recife", "Teresina", "Rio de Janeiro", "Natal", "Porto Alegre", 
        "Porto Velho", "Boa Vista", "Florianópolis", "São Paulo", "Aracaju", "Palmas"]}
    


brazilfires = pd.DataFrame(brazil)

#Two steps to make second second DataFrame. Step 1 makes a dictionary. Step 2 makes it into a DataFrame. 

brazil2 = {'states':['newstate_1', 'newstate_2'],'Capitals':['newcap1', 'newcap2']} 

brazilfires2 = pd.DataFrame(brazil2)
  
    
#Append Adds both DataFrames Together. 


brazilfinal = brazilfires.append(brazilfires2, ignore_index=True)


#Print Appended List 

brazilfinal




# In[ ]:





# In[ ]:




