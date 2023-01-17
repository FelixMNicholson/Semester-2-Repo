#!/usr/bin/env python
# coding: utf-8

# In[29]:


# Import pandas.
import pandas as pd


EmergencyProtocols = {'EmergencyProtocols':['Prevention', 'mitigation', 'preparedness', 'response', 'recovery']}

EmergencyProtocolsDF = pd.DataFrame(EmergencyProtocols)

#Hide Number Column ('Index') From Final DataFrame

EmergencyProtocolsDF = EmergencyProtocolsDF.style.hide_index()

#Print DataFrame

EmergencyProtocolsDF


# In[28]:


#Emergency Numbers List 

EmergencyNumbers = {'Service':['Law_Enforcement',
                               'FireRescue','Emergency Medical Services', 
                               'Emergency Management', 'Public Works'],
                    'Number':['123','224','101','999','900']}

EmergencyNumbersDF = pd.DataFrame(EmergencyNumbers)

#Hide Number Column('Index')From Final DataFrame

EmergencyNumbersDF = EmergencyNumbersDF.style.hide_index()

#Print DataFrame

EmergencyNumbersDF
        


# In[36]:


#Emergency Checklist

EmergencyCHK = {'check':['carotid pulse','breathing','obstructions','pupils','conciousness',
                             'contact details','allergies'],
                      'area':['neck','nose','nose, ears, mouth','responsive','','','']}
                            

EmergencyCHK_DF = pd.DataFrame(EmergencyCHK)

#Hide Number Column('Index')From Final DataFrame

EmergencyCHK_DF = EmergencyCHK_DF.style.hide_index()

#Print DataFrame

EmergencyCHK_DF
        


# In[ ]:




