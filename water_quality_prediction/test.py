from preProcess import PreProcess


if __name__ == "__main__":
    file_name = './data/가평_2019.xlsx'
    p = PreProcess(
        input=file_name, 
        target=[2], # if target_all is True, this option ignore
        time=5,
        target_all=False,
        fill_cnt=10000
    )

    # sample (1)
    # output_np = p.getDataSet()
    # p.npToExcel(output_np, "./output/가평2019_2_5_fill_3_shape.xlsx")

    # output_np = p.getRawDataSet()
    # p.npToExcel(output_np, "./output/가평2019_raw_2_5_fill_0_shape.xlsx")

    # output_np = p.getDataSet()
    # line 44

    # output_np = p.getRawDataSet()
    # line 120
    # p.npToExcel(output_np, "./output/가평2019_raw_2_5_fill_10000_shape.xlsx")