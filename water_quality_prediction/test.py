from preProcess import PreProcess


if __name__ == "__main__":
    file_name = './data/가평_2019.xlsx'
    p = PreProcess(
        input=file_name, 
        target=[2,3,4,5,6,7,8,9], # if target_all is True, this option ignore
        time=7*24,
        target_all=False,
        fill_cnt=10000
    )

    # sample (1)
    # output_np = p.getDataSet()
    # p.npToExcel(output_np, "./output/가평2019_23456789_168_fill_3_shape.xlsx")

    # output_np = p.getRawDataSet()
    # p.npToExcel(output_np, "./output/가평2019_raw_23456789_168_fill_0_shape.xlsx")

    # output_np = p.getDataSet()

    output_np = p.getRawDataSet()
    p.npToExcel(output_np, "./output/가평2019_raw_23456789_168_fill_10000_shape.xlsx")