from preProcess import PreProcess


if __name__ == "__main__":
    p = PreProcess('./data/expand_mini.xlsx', [2,3], 3)

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

    output_np = p.getRawDataSet()
    print(output_np)
    '''
    [[ 2.8  6.8  2.8  6.8  nan  nan]
    [ 2.7  6.8  nan  nan  1.  21. ]
    [ 2.  22.   3.  23.   nan  nan]
    [ 4.  24.   5.  25.   6.  26. ]
    [ 7.  27.   8.  28.   nan  nan]
    [ 9.  29.  10.  30.  11.  31. ]]
    '''