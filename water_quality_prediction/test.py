from preProcess import PreProcess


if __name__ == "__main__":
    # file_name = './data/Gapyeong_2019.xlsx'
    file_name = './data/expand_mini.xlsx'
    p = PreProcess(input=file_name, target=[2,3,4], time=2, target_all=True)

    # sample (1)
    output_np = p.getDataSet()
    print(output_np)
    '''
    [[ 4. 24.  5. 25.  6. 26.]
    [ 5. 25.  6. 26.  7. 27.]
    [ 6. 26.  7. 27.  8. 28.]
    [ 9. 29. 10. 30. 11. 31.]
    [10. 30. 11. 31. 12. 32.]
    [11. 31. 12. 32. 13. 33.]]
    '''
    p.npToExcel(output_np, "./output/result_sample1.xlsx")