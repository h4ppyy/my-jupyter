
import pandas as pd
import os

import matplotlib
import matplotlib.pyplot as plt
import math

import matplotlib.font_manager as fm  # 폰트 관련 용도

# matpotlib 에서 한글 깨짐 현상(mac)
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['font.family'] = "AppleGothic"

# font_path = '/System/Library/Fonts/AppleSDGothicNeo.ttc'
# # fontprop = fm.FontProperties(fname=font_path)
# font_name = fm.FontProperties(fname=font_path).get_name()
# matplotlib.rc('font', family=font_name)


path = "./excel/"
excelfiles = []
xlsx = []
rows = []
cols = []
columnlist = []
label_legend = []


for root, dirs, files in os.walk(path):
    for filename in files:
        # print(files)
        if filename == '.DS_Store':
            continue
        xlsx.append(pd.read_excel(path+filename))
        excelfiles.append(path+filename)
        label_legend.append(os.path.splitext(filename)[0])

        # columnlist.append(xlsx.columns.tolist())

        for i in range(0,1):
            rows.append(xlsx[i].shape[0])
            cols.append(xlsx[i].shape[1])

    for i in range(0, len(excelfiles)):
        columnlist.append(xlsx[i].columns.tolist())

# print(len(excelfiles))
# print(columnlist[1])
# print(math.ceil(len(excelfiles)/2))
# print(cols[0])
# print(columnlist[0][4])


for i in range(2, cols[0]):
    # fig.canvas.set_window_title(columnlist[0][i])
    # plt.subplot(math.ceil(len(excelfiles)/2),len(excelfiles)/2,1)
    # plt.title('1')
    # plt.plot(xlsx[0][columnlist[0][i]])
    fig = plt.gcf()
    if columnlist[0][i] == columnlist[1][i] :
        fig.canvas.set_window_title(columnlist[0][i])
    else :
        fig.canvas.set_window_title(columnlist[0][i] + " // "+ columnlist[1][i])

    for j in range(0, len(excelfiles)):
        # test = '가나다'
        # plt.plot(xlsx[j][columnlist[j][i]], label = test)
        plt.plot(xlsx[j][columnlist[j][i]], label = label_legend[j])
        # plt.plot(xlsx[j][columnlist[j][i]], label = "가나다")
        # plt.plot(xlsx[j][columnlist[j][i]], label = label_legend[j], fontproperties=fontprop)





    # plt.subplot(3,2,1)
    # plt.title('1')
    # plt.plot(xlsx[0][columnlist[0][i]])
    # # plt.subplot(3,2,2)
    # # # plt.title('2')
    # plt.plot(xlsx[1][columnlist[1][i]])
    # plt.subplot(3,2,3)
    # # plt.title('3')
    # plt.plot(xlsx[2][columnlist[2][i]])
    # plt.subplot(3,2,4)
    # plt.title('4')
    # plt.plot(xlsx[3][columnlist[3][i]])
    # plt.subplot(3,2,5)
    # # plt.title('5')
    # plt.plot(xlsx[4][columnlist[4][i]])
    # plt.subplot(3,2,6)
    # plt.plot(xlsx[5][columnlist[0][i]])


    plt.legend()
    plt.show()



# for i in range(len(excelfiles))

# fig = plt.gcf()
# fig.canvas.set_window_title("총유기탄소")
# plt.subplot(3,2,1)
# plt.title('1')
# plt.plot(xlsx[0]["총유기탄소"])
# plt.subplot(3,2,2)
# plt.plot(xlsx[1]["총유기탄소"])
# plt.subplot(3,2,3)
# plt.plot(xlsx[2]["총유기탄소"])
# plt.subplot(3,2,4)
# plt.plot(xlsx[3]["총유기탄소"])
# plt.subplot(3,2,5)
# plt.plot(xlsx[4]["총유기탄소"])
# plt.subplot(3,2,6)
# plt.plot(xlsx[5]["총유기탄소"])

# plt.show()



#
#
# print(excelfiles)
#
#
# for fname in excelfiles:
#     xlsx = pd.read_excel(fname)
#     print(fname)
#     print(xlsx.shape)
#     rows = xlsx.shape[0]
#     cols = xlsx.shape[1]
#     columnlist = xlsx.columns.tolist()
#     noncount = []
#     notnoncount = []
#
#
#     print("NaN")
#
#     for i in range(0, cols):
#         # print(xlsx[columnlist[i]])
#         noncount.append(xlsx[columnlist[i]].isna().astype(int).groupby(xlsx[columnlist[i]].notnull().astype(int).cumsum()).sum().tolist())
#         noncount[i] = list(filter(lambda num: num != 0, noncount[i]))
#         # print(columnlist[i], " : ", noncount[i])
#         if len(noncount[i]) != 0 :
#             print(columnlist[i] , "Total:", sum(noncount[i]), " Group:" , len(noncount[i]), "Max:", max(noncount[i]), "Min:", min(noncount[i]), "Ave:", sum(noncount[i]) / len(noncount[i]))
#
#
#     print()
#     print()
#     print()
#
#
#     print("notNaN")
#     for i in range(0, cols):
#         # print(xlsx[columnlist[i]])
#         notnoncount.append(xlsx[columnlist[i]].notna().astype(int).groupby(xlsx[columnlist[i]].isnull().astype(int).cumsum()).sum().tolist())
#         notnoncount[i] = list(filter(lambda num: num != 0, notnoncount[i]))
#         # print(columnlist[i] , "Total:", sum(notnoncount[i]), " Group:" , len(notnoncount[i]), "Max:", max(notnoncount[i]), "Min:", min(notnoncount[i]), "Ave:", sum(notnoncount[i]) / len(notnoncount[i]))
#         # print(columnlist[i], " : ", notnoncount[i])
#         if i > 3 :
#             print(columnlist[i] , "Total:", sum(notnoncount[i]), " Group:" , len(notnoncount[i]), "Max:", max(notnoncount[i]), "Min:", min(notnoncount[i]), "Ave:", sum(notnoncount[i]) / len(notnoncount[i]))
#         # if len(notnoncount[i]) != 0 :
#         #     print(columnlist[i] , "Total:", sum(notnoncount[i]), " Group:" , len(notnoncount[i]), "Max:", max(notnoncount[i]), "Min:", min(notnoncount[i]), "Ave:", sum(notnoncount[i]) / len(notnoncount[i]))
#
#
#     print()
#     print()
#     print()
#

# xlsx.append(pd.read_excel('./excel/가평2018.xlsx'))
# xlsx.append(pd.read_excel('./excel/화천2018.xlsx'))
# columnlist.append(xlsx[0].columns.tolist())
# columnlist.append(xlsx[1].columns.tolist())
# rows.append(xlsx[0].shape[0])
# cols.append(xlsx[0].shape[1])
#
#
# print(xlsx)
# print(columnlist)
# print(rows)
# print(cols)

# for i in range(4, cols):
#     # print(i-1)
#
#     fig = plt.gcf()
#     fig.canvas.set_window_title(columnlist[i])
#     plt.plot(xlsx[columnlist[i]])
#     # plt.xticks(xlsx[columnlist[0]])
#     plt.show()
#     # plt.show(block=True)
#     # input("Press Enter to continue...")
#
#
#
# xlsx = pd.read_excel('./excel/가평2018.xlsx')
# columnlist = xlsx.columns.tolist()
# rows = xlsx.shape[0]
# cols = xlsx.shape[1]
#
# for i in range(4, cols):
#     # print(i-1)
#
#     fig = plt.gcf()
#     fig.canvas.set_window_title(columnlist[i])
#     plt.plot(xlsx[columnlist[i]])
#     # plt.xticks(xlsx[columnlist[0]])
#     plt.show()
#     # plt.show(block=True)
#     # input("Press Enter to continue...")
