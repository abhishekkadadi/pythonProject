import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from read_in_census_data import CensusInfo, DataFrameWrapper
from collections import Counter
# All def
# Combining education together
def education(x):
    if 9 <= x <= 11:
        return 'HS'
    elif x == 12:
        return 'AA'
    elif x == 13:
        return 'BE'
    elif x == 14:
        return 'MS' #masters
    elif x > 14:
        return 'HD' #Doctor or professional
    else:
        return 'ND'
# combinig enducation together ends


# all def ends

# imports done
data_dictionary = '5%_PUMS_record_layout.xls'
ci_states = CensusInfo(data_dictionary)
states=['alabama','texas','california','florida','illnois','virginia','ohio','alaska','new_york','district_of_colombia']
textFiles=['revisedpums1_alabama_01','revisedpums1_48','revisedpums1_06','revisedpums1_12','revisedpums1_17','revisedpums1_51','revisedpums1_39','revisedpums1_02','revisedpums1_36','revisedpums1_11']
df = DataFrameWrapper(ci_states)
df.is_copy = False
# Creating CSV looping 10 states then commenting out the code
# textFilesCounter=0
# for loopingState in states:
#     one_percent = 'states/'+loopingState+'/'+textFiles[textFilesCounter]+'.txt'
#     df.fill_frame ([], ci_states.person_record, one_percent, ci_states.one_percent_file,'race','education','income','gender','age','relationship')
#     df.save_frame('states/'+loopingState+'/'+textFiles[textFilesCounter]+'_extract.csv',header=True)
#     textFilesCounter+=1
# Creating Csv ends here...!

# Average Incomes in 10 states
dt_dict ={'serial_no':object,'race':object,'gender':object,'relationship':object}
avgIncomeDict={}
stateDict={}
educationDict={}
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
# plt.show()
# Average income ends
#Education degree VS INCOME of 10 states
for loopingState in states:
    incomeOf=stateDict[loopingState]
    stateIncomeIs=incomeOf[incomeOf['income']>0]['income']
    mean=round(stateIncomeIs.mean(),2)
    avgIncomeDict[loopingState]=mean
#Lets compare mean income and max education of multiple groups overall in 10 states
#logic- get numbers of education and its corresponding income for every state then average it
p_df_inc2 = pd.DataFrame()
for loopingState in states:
    stateName=stateDict[loopingState]
    p_df_inc = stateName[stateName['income']>0]
    p_df_inc.is_copy=None
    # print p_df_inc['education'].map(education)
    p_df_inc.loc[:,'Degrees']=p_df_inc['education'].map(education)
    # print p_df_district_of_colombia
    dataFrame=p_df_inc.loc[:,['Degrees','income']]
    p_df_inc2=p_df_inc2.append(dataFrame,ignore_index=True)
# has all degrees and income of ten states
# plt.show(p_df_inc2.groupby('Degrees').mean().plot(y='income', kind='bar',title='Income Vs Education'))

######################whites only income##########################################################################
#whites n non white only income in 10 states
whiteIncome=[]
nonWhiteIncome=[]
for loopingState in states:
    stateName = stateDict[loopingState]
    stateName['white_only'] = stateName['race'].map(lambda x: x == '47')
    income=stateName['income'].groupby(stateName['white_only']).mean()
    whiteIncome.append(income[True])
    nonWhiteIncome.append(income[False])
meanWhiteIncome=round(np.mean(whiteIncome),2)
meanNonWhiteIncome=round(np.mean(nonWhiteIncome),2)
fig, ax  = plt.subplots()
ax.set_title('Mean White income vs Mean Non White income of 10 states')
ax.bar([1,2], [meanWhiteIncome,meanNonWhiteIncome,], width=1,
       tick_label=['Mean White Income', 'Mean Non White Income'], align='center')
# plt.show()
#whites n non white only income ends

#whites max education vs non whites max education
p_df_inc3 = pd.DataFrame()
whiteOnlyDF=pd.DataFrame()
nonWhiteOnlyDF=pd.DataFrame()
for loopingState in states:
    stateName=stateDict[loopingState]
    p_df_inc.loc[:, 'Degrees'] = p_df_inc['education'].map(education)
    dataFrame=p_df_inc.loc[:,['Degrees','race']]
    p_df_inc3=p_df_inc3.append(dataFrame,ignore_index=True)

whiteOnlyDF=p_df_inc3[p_df_inc3['race'].map(lambda x: x == '47')]
nonWhiteOnlyDF=p_df_inc3[p_df_inc3['race'].map(lambda x: x != '47')]
# groupby('Degrees').count()
df1 = whiteOnlyDF['Degrees'].value_counts()
df2 = nonWhiteOnlyDF['Degrees'].value_counts()
df1 = pd.DataFrame({'Degrees':df1.index, 'count':df1.values})
df2 = pd.DataFrame({'Degrees':df2.index, 'count':df2.values})
df1['Key'] = 'White'
df2['Key'] = 'NonWhite'

DF = pd.concat([df1,df2],keys=['White','NonWhite'])

DFGroup = DF.groupby(['Degrees','Key'])

DFGPlot = DFGroup.sum().unstack('Key').plot(kind='bar')
plt.show()
# print nonWhiteOnlyDF
#whites max education vs non whites max education ends

