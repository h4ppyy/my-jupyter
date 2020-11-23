import glob
import pandas as pd
import numpy as np


class PreProcess:
    def __init__(self, input, target, time, target_all, fill_cnt=0):
        self.fill_cnt = fill_cnt
        self.time = time
        self.df_raw_list = []

        file_list = glob.glob(input + "/*.xlsx")
        print('[debug] len(file_list) = ', len(file_list))
        
        # file
        if len(file_list) == 0:
            df = pd.read_excel(input)
            fill_df = self.getFillDf(df)
            min_size = fill_df.columns.size

        # directory
        else:
            dn = pd.DataFrame(data={'line': ['0']}) # null padding
            df_list = []
            min_size = 999
            for f in file_list:
                df = pd.read_excel(f)
                self.df_raw_list.append(self.getFillDf(df))
                df_list.append(self.getFillDf(df))
                df_list.append(dn)
                if min_size > df.columns.size:
                    min_size = df.columns.size
            fill_df = pd.concat(df_list).drop('line', axis=1)

        # get all column name list (except 0, 1)
        target_all_list = [n for n in range(2, min_size)]
        print('[debug] target_all_list = ', target_all_list)
        print('[debug] min_size = ', min_size)
             
        if target_all:
            self.target = target_all_list
            self.target_name = fill_df.columns.tolist()[2:min_size]
        else:
            self.target = target
            self.target_name = []
            for t in target:
                self.target_name.append(fill_df.columns.tolist()[t])

        print('[debug] self.target = ', self.target)

        self.group_cnt = self.time * len(self.target)
        print('[debug] self.group_cnt = ', self.group_cnt)

        self.target_df = self.getTargetDf(fill_df)
        print('[debug] self.target_df = ', self.target_df)

    def getFillDf(self, df):
        if self.fill_cnt != 0:
            mask = df.copy()
            for i in df.columns: 
                dfx = pd.DataFrame( df[i] )
                dfx['new'] = ((dfx.notnull() != dfx.shift().notnull()).cumsum())
                dfx['ones'] = 1
                mask[i] = (dfx.groupby('new')['ones'].transform('count') < self.fill_cnt + 1) | df[i].notnull()
            df = df.interpolate().bfill()[mask]
        return df 

    def getTargetDf(self, df):
        return df.iloc[:, self.target]

    def getRelTargetDf(self, df):
        return df.loc[:, self.target_name]

    def getLabelDf(self, target_df):
        x = target_df.isna().any(axis='columns').astype(int)
        y = target_df.isna().any(axis='columns').astype(int).shift(periods=1, fill_value=0)
        z = pd.concat([x, y], axis=1).any(axis='columns').astype(int).cumsum()
        raw_label_df = pd.concat([x, z], axis=1)
        raw_label_df.columns = ['is_nan', 'group']
        new_df = pd.concat([target_df, raw_label_df], axis=1)
        label_df = new_df.where(new_df['is_nan'] != 1).dropna()
        return label_df

    def getSizeSr(self, label_df):
        size_sr = label_df.groupby(label_df['group']).size()
        return size_sr

    def getDiscard(self, target_df):
        return ( len(target_df) * len(self.target) ) % ( self.group_cnt )

    def sliceDf(self, target_df, discard):
        return target_df[:len(target_df) - int(discard / len(self.target))]

    def shiftDf(self, label_df, size_sr):
        target_idx_list = size_sr.where(size_sr >= self.time).dropna().index.tolist()
        target_df_list = []
        concat_list = []

        # debug
        print('group_cnt -> ', len(target_idx_list))
        
        for idx in target_idx_list:
            output_df = label_df.where(label_df['group'] == idx).dropna()
            total_cnt = len(label_df.where(label_df['group'] == idx).dropna())

            # debug
            print('total_cnt -> ', total_cnt)

            target_df_list.append({ 'total_cnt': total_cnt, 'output_df': output_df })
        for t in target_df_list:
            for n in range(0, t['total_cnt']-self.time+1):
                split_df = t['output_df'][n:self.time+n]
                concat_list.append(split_df)
                
        # validate
        if len(concat_list) == 0:
            print('[fail] no groups were created. reduce the time option')
            exit(0)

        target_df = pd.concat(concat_list).drop('is_nan', axis=1).drop('group', axis=1)
        return target_df

    def getNp(self, output_df):
        output_np = output_df.to_numpy()
        output_np = output_np.reshape(-1, self.group_cnt)
        return output_np

    def getDataSet(self):
        label_df = self.getLabelDf(self.target_df) # diff
        size_sr = self.getSizeSr(label_df) # diff
        target_df = self.shiftDf(label_df, size_sr) # diff
        discard = self.getDiscard(target_df)
        output_df = self.sliceDf(target_df, discard)
        output_np = self.getNp(output_df)
        return output_np

    def getRawDataSet(self):
        # file
        if len(self.df_raw_list) == 0:
            target_df = self.target_df
            discard = self.getDiscard(target_df)
            output_df = self.sliceDf(target_df, discard)
            output_np = self.getNp(output_df)
            return output_np

        # directory
        else:
            output_np_list = []
            for fill_df in self.df_raw_list:
                target_df = self.getRelTargetDf(fill_df)
                discard = self.getDiscard(target_df)
                output_df = self.sliceDf(target_df, discard)
                output_np = self.getNp(output_df)
                output_np_list.append(output_np)
            return output_np_list
        

    def npToExcel(self, input_np, save_path):
        df = pd.DataFrame(data=input_np)
        df.to_excel(save_path, index=False)