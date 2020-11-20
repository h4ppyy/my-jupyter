from preProcess import PreProcess


if __name__ == "__main__":
    # file_name = './data/Gapyeong_2019.xlsx'
    file_name = './data/의암호_2019.xlsx'
    p = PreProcess(
        input=file_name, 
        target=[2,3,4,5,6,7,8,9,10], # if target_all is True, this option ignore
        time=7*24, 
        target_all=False,
        fill_cnt=1000
    )

    # sample (1)
    output_np = p.getDataSet()
    # p.npToExcel(output_np, "./output/reshape_all_168_fill_2.xlsx")

    # output_np = p.getRawDataSet()
    # p.npToExcel(output_np, "./output/의암호2019_raw_all_168_fill_2.xlsx")