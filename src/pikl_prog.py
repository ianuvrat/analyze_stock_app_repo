import pandas as pd
file_path = '../pickl_files/'

astral_df = pd.read_pickle(file_path + 'astrl_df.pkl')
gmm_df = pd.read_pickle(file_path + 'gmm_df.pkl')
lal_df = pd.read_pickle(file_path + 'lal_df.pkl')
amrut_df = pd.read_pickle(file_path + 'amrut_df.pkl')

alkyl_df = pd.read_pickle(file_path + 'alkyl_df.pkl')
ap_df = pd.read_pickle(file_path + 'ap_df.pkl')
divis_df = pd.read_pickle(file_path + 'divis_df.pkl')
titan_df = pd.read_pickle(file_path + 'titan_df.pkl')

tcs_df = pd.read_pickle(file_path + 'tcs_df.pkl')
tata_elxsi_df = pd.read_pickle(file_path + 'tata_elxsi_df.pkl')
