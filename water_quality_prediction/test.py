from preProcess import PreProcess


if __name__ == "__main__":
    # file_name = './data/Gapyeong_2019.xlsx'
    file_name = './data/Gapyeong_2019.xlsx'
    p = PreProcess(
        input=file_name, 
        target=[2,3,4,5,6,7,8], 
        time=3*24, 
        target_all=False
        # fill_cnt=2
    )

    # sample (1)
    output_np = p.getDataSet()
    p.npToExcel(output_np, "./output/reshape_2345678_72_nofill.xlsx")

    # output_np = p.getRawDataSet()
    # p.npToExcel(output_np, "./output/result_sample2.xlsx")