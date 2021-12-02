import pandas as pd
from os import walk
import os
import glob
import sys
from pandas.core.reshape.concat import concat

def grab_and_concat_files():
    print("Start proccessing...")

    ROOT_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
    df_append = pd.DataFrame(columns=['經銷商', '經銷商', '保卡號碼', '小  計'])
    # print(df_empty)

    target_dir = os.path.join(ROOT_DIR, 'consolidate_finder')
    print(target_dir)
    for root, dirs, files in walk(target_dir):
        for file in files:
            if not file.endswith("xls"):
                continue

            # print(os.path.join(root, file))
            data_df = pd.concat(pd.read_excel(os.path.join(root, file),
                                            header=[9], sheet_name=None, engine='xlrd'))
            # df.to_csv('test.csv')
            # print(df)

            # 選取需要的資料至目前的 DF
            need_df = data_df[['經銷商', '保卡號碼', '小  計']]
            # need_df.to_excel('need.xls')
            # print(need_df)

            # 新建一欄經銷商(下移資料)
            dealer_df = need_df['經銷商'].shift()
            # print('dealer_df',dealer_df)

            # concat 新的經銷商至目前的 DF
            shift_df = concat([dealer_df, need_df], axis=1)
            # shift_df.to_excel('concat.xls')
            # print(shift_df.columns)
            # print(df_empty)

            # 刪掉多層 index 中的第一層 index
            shift_df.index = shift_df.index.droplevel()
            # print('shift_df',shift_df)
            # shift_df.to_excel('shift_df.xls')

            odd_df = shift_df[shift_df.index % 2 == 1]
            # odd_df.to_excel('odd.xls')

            # 彙整 Excel
            df_append = df_append.append(odd_df, ignore_index=True)
            # df_append.to_excel('df.xls')
            # print(df_append)
        return df_append,ROOT_DIR


# 嘗試先彙整再清理
# dealer_df = need_df['經銷商'].shift()
# test_df = concat([dealer_df,df_append],axis=1)
# test_df.to_excel('test_df.csv')
# # print(df_empty)

# df = df_concat[df_concat.index%2==1]

def clean_unnecessary_data(df_append,ROOT_DIR):
    df_distinct = df_append.loc[:, ~df_append.columns.duplicated()]
    # print(df_distinct)
    # df_distinct.to_excel('df_distinct.xls')
    df = df_distinct[~df_distinct['經銷商'].isin(['經銷商總計'])]
    # print(df)
    df.to_excel(os.path.join(ROOT_DIR, 'df.xls'))

    print("Successed :)")

def main():
    df_append,ROOT_DIR = grab_and_concat_files()
    clean_unnecessary_data(df_append,ROOT_DIR)

if __name__ =="__main__":
    main()