from preProcess import preProcess


if __name__ == "__main__":
    p = preProcess('./data/expand_mini.xlsx', [2,3], 3)
    output_np = p.getDataSet()
    print(output_np)