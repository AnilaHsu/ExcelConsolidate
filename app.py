import pandas as pd
from os import walk
import os
import glob

path = ''
df_empty = pd.DataFrame(columns=['經銷商','保卡號碼','小  計'])
# print(df_empty)

for root, dirs, files in walk('consolidate_finder'):
    for file in files:
        if not file.endswith("xls"):
            continue
        # file_name = glob.glob(os.path.join(root,file))
        print(os.path.join(root,file))
        df = pd.concat(pd.read_excel(os.path.join(root,file),header=[9], sheet_name=None,engine='xlrd'))
        # df.to_csv('test.csv')
        print(df)

        new_df = df[['經銷商','保卡號碼','小  計']]
        print(new_df)
        df_empty=df_empty.append(new_df,ignore_index=True)
        print(df_empty)

df_empty.rename(columns={'保卡號碼':'保單編號/保卡號碼'},inplace=True)
print(df_empty)

# df_empty.to_excel('concat_file.xls')

