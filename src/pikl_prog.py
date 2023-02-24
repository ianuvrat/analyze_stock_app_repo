import pandas as pd
file_path = '../pickl_files/'

astral_df = pd.read_pickle(file_path + 'astrl_df.pkl')
gmm_df = pd.read_pickle(file_path + 'gmm_df.pkl')
lal_df = pd.read_pickle(file_path + 'lal_df.pkl')
amrut_df = pd.read_pickle(file_path + 'amrut_df.pkl')
