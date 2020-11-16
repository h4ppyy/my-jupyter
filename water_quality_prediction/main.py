import argparse
import pandas as pd
import numpy as np

# usage
'''
python main.py --input ./data/expand_mini.xlsx --target 2,3 --time 3
'''

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--input", help="Please enter file")
  parser.add_argument("--target", default='2,3', help="Please enter string array of type (default: 2,3)")
  parser.add_argument("--time", type=int, default=3, help="Please enter number of time (default: 3)")
  args = parser.parse_args()

  target_col = list(map(int, args.target.split(','))) # [2, 3]
  input_unit_time = args.time # min 2

  # 1. read excel
  df = pd.read_excel(args.input)

  # 2. search target column
  origin_df = df.iloc[:, target_col]

  # 3. labeling for group
  x = df.iloc[:, target_col].isna().any(axis='columns').astype(int)
  y = df.iloc[:, target_col].isna().any(axis='columns').astype(int).shift(periods=1, fill_value=0)
  z = pd.concat([x, y], axis=1).any(axis='columns').astype(int).cumsum()
  label_df = pd.concat([x, z], axis=1)
  label_df.columns = ['is_nan', 'group']
  new_df = pd.concat([origin_df, label_df], axis=1)
  result_df = new_df.where(new_df['is_nan'] != 1).dropna()

  # 4. get count of group
  size_sr = result_df.groupby(result_df['group']).size()
  size_sr.where(size_sr >= input_unit_time+1).dropna()

  # 5. use the input time for expand data 
  target_idx_list = size_sr.where(size_sr >= input_unit_time+1).dropna().index.tolist()
  target_df_list = []
  concat_list = []
  for idx in target_idx_list:
      output_df = result_df.where(result_df['group'] == idx).dropna()
      total_cnt = len(result_df.where(result_df['group'] == idx).dropna())
      target_df_list.append({ 'total_cnt': total_cnt, 'output_df': output_df })
  for t in target_df_list:
      for n in range(0, t['total_cnt']-input_unit_time+1):
          split_df = t['output_df'][n:input_unit_time+n]
          concat_list.append(split_df)
  output_df = pd.concat(concat_list).drop('is_nan', axis=1).drop('group', axis=1)

  # 6. dataframe to numpy  
  output_np = output_df.to_numpy()
  group_cnt = input_unit_time * len(target_col)
  output_np = output_np.reshape(group_cnt, -1)

  # 7. result
  print(output_np)

  # optional (exchange odd, even)
  '''
  new_np = []
  for n in range(0, len(output_np)):
      new = np.concatenate((output_np[n][::2], output_np[n][1::2]), axis=0)
      new_np.append(new)
  new_np = np.array(new_np)
  print(new_np)
  '''