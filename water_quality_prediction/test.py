from preProcess import preProcess


if __name__ == "__main__":
    p = preProcess('./data/expand_mini.xlsx', [2,3], 3)

    # sample (1)
    output_np = p.getDataSet(convert=False)
    print(output_np)
    '''
    [[ 4. 24.  5. 25.  6. 26.]
    [ 5. 25.  6. 26.  7. 27.]
    [ 6. 26.  7. 27.  8. 28.]
    [ 9. 29. 10. 30. 11. 31.]
    [10. 30. 11. 31. 12. 32.]
    [11. 31. 12. 32. 13. 33.]]
    '''

    # sample (2)
    output_np = p.getDataSet(convert=True)
    print(output_np)
    '''
    [[ 4.  5.  6. 24. 25. 26.]
    [ 5.  6.  7. 25. 26. 27.]
    [ 6.  7.  8. 26. 27. 28.]
    [ 9. 10. 11. 29. 30. 31.]
    [10. 11. 12. 30. 31. 32.]
    [11. 12. 13. 31. 32. 33.]]
    '''