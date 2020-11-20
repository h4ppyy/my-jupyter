import matplotlib.pyplot as plt

f = open("./data/MSE_loss_curr.txt", 'r')
idx = 0
idx_list = []
data_list = []
while True:
    line = f.readline()
    if not line: break
    if idx % 2 == 0:
        idx_list.append(int(line.strip()))
    else:
        data_list.append(float(line.strip()))
    idx += 1
f.close()

plt.plot(idx_list, data_list)
plt.legend()
plt.show()