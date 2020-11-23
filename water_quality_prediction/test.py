from preProcess import PreProcess


if __name__ == "__main__":
    input = './data/mini_sample/서상_2019.xlsx'
    # input = './data/mini_sample'
    p = PreProcess(
        input=input, # file or directory
        target=[0,2,4,5], # if target_all is True, this option ignore
        time=3,
        target_all=False,
        fill_cnt=0
    )

    # make train data
    output_np = p.getDataSet()
    p.npToExcel(output_np, "./output/merge.xlsx")

    # make raw data (directory)
    '''
    output_np_list = p.getRawDataSet()
    idx = 1
    for output_np in output_np_list:
        p.npToExcel(output_np, "./output/raw_{idx}.xlsx".format(idx=idx))
        idx += 1
    '''

    # make raw data (file)
    '''
    output_np = p.getRawDataSet()
    p.npToExcel(output_np, "./output/raw.xlsx")
    '''