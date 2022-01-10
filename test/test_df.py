from os import walk
import os
import pandas as pd


# 指定要列出所有檔案的目錄
mypath = ''

for root, dirs, files in walk('test'):
  print("路徑：", root)
  print("目錄：", dirs)
  print("檔案：", files)
  for file in files:
    print(os.path.join(root,file))
    df=pd.read_excel(os.path.join(root,file),header=[9])
print(df[['經銷商','保戶名稱','小  計']])

test_df = pd.read_excel('A010.xls',header=[9])
df = test_df[['經銷商','保戶名稱','小  計']]
# test_df.to_csv('test.csv')

