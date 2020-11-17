import pandas as pd
import numpy as np


class PreProcess:
    def __init__(self, input, target, time):
        self.input = input
        self.target = target
        self.time = time
        self.group_cnt = time * len(target)
        self.df = pd.read_excel(input)
        
    def getInput(self):
        return self.input

    def getTarget(self):
        return self.target

    def getTime(self):
        return self.time

    def getDf(self):
        return self.df

    def getTargetDf(self, df):
        return df.iloc[:, self.target]

    def getLabelDf(self, target_df):
        x = self.df.iloc[:, self.target].isna().any(axis='columns').astype(int)
        y = self.df.iloc[:, self.target].isna().any(axis='columns').astype(int).shift(periods=1, fill_value=0)
        z = pd.concat([x, y], axis=1).any(axis='columns').astype(int).cumsum()
        raw_label_df = pd.concat([x, z], axis=1)
        raw_label_df.columns = ['is_nan', 'group']
        new_df = pd.concat([target_df, raw_label_df], axis=1)
        label_df = new_df.where(new_df['is_nan'] != 1).dropna()
        return label_df

    def getSizeSr(self, label_df):
        size_sr = label_df.groupby(label_df['group']).size()
        size_sr = size_sr.where(size_sr >= self.time+1).dropna()
        return size_sr

    def getDiscard(self, target_df):
        return ( len(target_df) * len(self.target) ) % ( self.group_cnt )

    def sliceDf(self, target_df, discard):
        return target_df[:len(target_df) - int(discard / len(self.target))]

    def shiftDf(self, label_df, size_sr):
        target_idx_list = size_sr.where(size_sr >= self.time+1).dropna().index.tolist()
        target_df_list = []
        concat_list = []
        for idx in target_idx_list:
            output_df = label_df.where(label_df['group'] == idx).dropna()
            total_cnt = len(label_df.where(label_df['group'] == idx).dropna())
            target_df_list.append({ 'total_cnt': total_cnt, 'output_df': output_df })
        for t in target_df_list:
            for n in range(0, t['total_cnt']-self.time+1):
                split_df = t['output_df'][n:self.time+n]
                concat_list.append(split_df)
        target_df = pd.concat(concat_list).drop('is_nan', axis=1).drop('group', axis=1)
        return target_df

    def getNp(self, output_df):
        output_np = output_df.to_numpy()
        output_np = output_np.reshape(-1, self.group_cnt)
        return output_np

    def getDataSet(self):
        df = self.getDf()
        target_df = self.getTargetDf(df)
        label_df = self.getLabelDf(target_df) # diff
        size_sr = self.getSizeSr(label_df) # diff
        target_df = self.shiftDf(label_df, size_sr) # diff
        discard = self.getDiscard(target_df)
        output_df = self.sliceDf(target_df, discard)
        output_np = self.getNp(output_df)
        return output_np

    def getRawDataSet(self):
        df = self.getDf()
        target_df = self.getTargetDf(df)
        discard = self.getDiscard(target_df)
        output_df = self.sliceDf(target_df, discard)
        output_np = self.getNp(output_df)
        return output_np

    def npToExcel(self, input_np, save_path):
        df = pd.DataFrame(data=input_np)
        df.to_excel(save_path, index=False)