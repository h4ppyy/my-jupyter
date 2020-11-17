import pandas as pd
import numpy as np


class PreProcess:
    def __init__(self, input, target, time):
        self.input = input
        self.target = target
        self.time = time

    def getDataSet(self):
        # 1. read excel
        df = pd.read_excel(self.input)

        # 2. search target column
        origin_df = df.iloc[:, self.target]

        # 3. labeling for group
        x = df.iloc[:, self.target].isna().any(axis='columns').astype(int)
        y = df.iloc[:, self.target].isna().any(axis='columns').astype(int).shift(periods=1, fill_value=0)
        z = pd.concat([x, y], axis=1).any(axis='columns').astype(int).cumsum()
        label_df = pd.concat([x, z], axis=1)
        label_df.columns = ['is_nan', 'group']
        new_df = pd.concat([origin_df, label_df], axis=1)
        result_df = new_df.where(new_df['is_nan'] != 1).dropna()

        # 4. get count of group
        size_sr = result_df.groupby(result_df['group']).size()
        size_sr.where(size_sr >= self.time+1).dropna()

        # 5. use the input time for expand data 
        target_idx_list = size_sr.where(size_sr >= self.time+1).dropna().index.tolist()
        target_df_list = []
        concat_list = []
        for idx in target_idx_list:
            output_df = result_df.where(result_df['group'] == idx).dropna()
            total_cnt = len(result_df.where(result_df['group'] == idx).dropna())
            target_df_list.append({ 'total_cnt': total_cnt, 'output_df': output_df })
        for t in target_df_list:
            for n in range(0, t['total_cnt']-self.time+1):
                split_df = t['output_df'][n:self.time+n]
                concat_list.append(split_df)
        origin_df = pd.concat(concat_list).drop('is_nan', axis=1).drop('group', axis=1)

        # 6. slice
        v = ( len(origin_df) * len(self.target) ) % ( len(self.target) * self.time )
        output_df = origin_df[:len(origin_df) - int(v / len(self.target))]

        # 7. dataframe to numpy  
        output_np = output_df.to_numpy()
        group_cnt = self.time * len(self.target)
        output_np = output_np.reshape(-1, group_cnt)

        return output_np

    def getRawDataSet(self):
        # 1. read excel
        df = pd.read_excel(self.input)

        # 2. search target column
        origin_df = df.iloc[:, self.target]

        # 3. slice
        v = ( len(origin_df) * len(self.target) ) % ( len(self.target) * self.time )
        output_df = origin_df[:len(origin_df) - int(v / len(self.target))]

        # 6. dataframe to numpy  
        output_np = output_df.to_numpy()
        group_cnt = self.time * len(self.target)
        output_np = output_np.reshape(-1, group_cnt)

        return output_np
