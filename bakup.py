# Alabama data
one_percent_alabama = 'states/alabama/revisedpums1_alabama_01.txt'
df_alabama = DataFrameWrapper(ci_states)
df_alabama.fill_frame ([], ci_states.person_record, one_percent_alabama, ci_states.one_percent_file,'race','education','income','gender','age','relationship')
# df_alabama.save_frame('states/alabama/alabama_pums_extract.csv',header=True) creating csv commented
dt_dict_alabama ={'serial_no':object,'race':object,'gender':object,'relationship':object}
p_df_alabama = pd.read_csv('states/alabama/alabama_pums_extract.csv',dtype=dt_dict_alabama)
# print p_df_alabama
# alabama data ends
# texas data
one_percent_texas = 'states/texas/revisedpums1_48.txt'
df_texas = DataFrameWrapper(ci_states)
df_texas.fill_frame ([], ci_states.person_record, one_percent_texas, ci_states.one_percent_file,'race','education','income','gender','age','relationship')
df_texas.save_frame('states/texas/texas_pums_extract.csv',header=True)
dt_dict_texas ={'serial_no':object,'race':object,'gender':object,'relationship':object}
p_df_texas = pd.read_csv('states/texas/texas_pums_extract.csv',dtype=dt_dict_texas)
print p_df_texas
# texas data ends
#california data
one_percent_texas = 'states/california/revisedpums1_06.txt'
df_texas = DataFrameWrapper(ci_states)
df_texas.fill_frame ([], ci_states.person_record, one_percent_texas, ci_states.one_percent_file,'race','education','income','gender','age','relationship')
df_texas.save_frame('states/texas/texas_pums_extract.csv',header=True)
dt_dict_texas ={'serial_no':object,'race':object,'gender':object,'relationship':object}
p_df_texas = pd.read_csv('states/texas/texas_pums_extract.csv',dtype=dt_dict_texas)
print p_df_texas
#california data ends