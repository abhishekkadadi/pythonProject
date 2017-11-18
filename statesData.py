import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from read_in_census_data import CensusInfo, DataFrameWrapper


# imports done
data_dictionary = '5%_PUMS_record_layout.xls'
ci_states = CensusInfo(data_dictionary)
states=['alabama','texas','california','florida','illnois','virginia','ohio','alaska','new_york','district_of_colombia']
textFiles=['revisedpums1_alabama_01','revisedpums1_48','revisedpums1_06','revisedpums1_12','revisedpums1_17','revisedpums1_51','revisedpums1_39','revisedpums1_02','revisedpums1_36','revisedpums1_11']

# Creating CSV looping 10 states then commenting out the code
# textFilesCounter=0
# for loopingState in states:
#     one_percent = 'states/'+loopingState+'/'+textFiles[textFilesCounter]+'.txt'
#     df = DataFrameWrapper(ci_states)
#     df.fill_frame ([], ci_states.person_record, one_percent, ci_states.one_percent_file,'race','education','income','gender','age','relationship')
#     df.save_frame('states/'+loopingState+'/'+textFiles[textFilesCounter]+'_extract.csv',header=True)
#     textFilesCounter+=1
# Creating Csv ends here...!

# Average Incomes in 10 states
dt_dict ={'serial_no':object,'race':object,'gender':object,'relationship':object}
avgIncomeDict={}
stateDict={}
# Lets store states objects to variable.
p_df_alabama = pd.read_csv('states/'+states[0]+'/'+textFiles[0]+'_extract.csv',dtype=dt_dict)
p_df_texas = pd.read_csv('states/'+states[1]+'/'+textFiles[1]+'_extract.csv',dtype=dt_dict)
p_df_california = pd.read_csv('states/'+states[2]+'/'+textFiles[2]+'_extract.csv',dtype=dt_dict)
p_df_florida = pd.read_csv('states/'+states[3]+'/'+textFiles[3]+'_extract.csv',dtype=dt_dict)
p_df_illnois = pd.read_csv('states/'+states[4]+'/'+textFiles[4]+'_extract.csv',dtype=dt_dict)
p_df_virginia = pd.read_csv('states/'+states[5]+'/'+textFiles[5]+'_extract.csv',dtype=dt_dict)
p_df_ohio = pd.read_csv('states/'+states[6]+'/'+textFiles[6]+'_extract.csv',dtype=dt_dict)
p_df_alaska = pd.read_csv('states/'+states[7]+'/'+textFiles[7]+'_extract.csv',dtype=dt_dict)
p_df_new_york = pd.read_csv('states/'+states[8]+'/'+textFiles[8]+'_extract.csv',dtype=dt_dict)
p_df_district_of_colombia = pd.read_csv('states/'+states[9]+'/'+textFiles[9]+'_extract.csv',dtype=dt_dict)
stateDict={'alabama':p_df_alabama,'texas':p_df_texas,'california':p_df_california,'florida':p_df_florida,'illnois':p_df_illnois,'virginia':p_df_virginia,\
           'ohio':p_df_ohio,'alaska':p_df_alaska,'new_york':p_df_new_york,'district_of_colombia':p_df_district_of_colombia}

for loopingState in states:
    incomeOf=stateDict[loopingState]
    stateIncomeIs=incomeOf[incomeOf['income']>0]['income']
    mean=round(stateIncomeIs.mean(),2)
    avgIncomeDict[loopingState]=mean
print avgIncomeDict

plt.suptitle('Average income in 10 states', fontsize=20)
plt.bar(range(len(avgIncomeDict)), avgIncomeDict.values(), align='center')
plt.xticks(range(len(avgIncomeDict)), avgIncomeDict.keys(),rotation=90)
plt.show()
# Average income ends
