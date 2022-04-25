import pandas as pd
import numpy as np
import time

menu = pd.read_csv("data/menu.csv")
print(menu)

def Knapsack(cal, fat, vita, times, total_cal, total_fat):
    total_vita = 0
    result = [{
                'Calories': 0,
                'Fat': 0,
                'Vitamin A': 0,
                'total_Vitamin A': total_vita,  #increase
                'rest_Calories': total_cal,  #decrease
                'rest_Fat':total_fat  #decrease
            }]
    y = [0] * len(cal)  #用以统计物品装入次数
    for i in range(10000):  #设置尝试装入次数
        k = 0
        for j in range(len(cal)):
            if cal[k] > total_cal or fat[k] > total_fat or y[k] == times[k]:  #去掉重量超过剩余承重或体积大于剩余容量或装入次数达到上限的物品
                del cal[k], fat[k], vita[k], times[k], y[k]
            else:
                k += 1

        if len(cal) > 0:
            u = [[], []]
            for j in range(len(cal)):
                u[0].append(min(times[j] - y[j], (total_cal // vita[j]), (total_fat // fat[j])))
                u[1].append(u[0][j] * vita[j])  #第一次取整计算物品的最高可装入价值（第一层）

                s = [[], []]
                for k in range(len(cal)):
                    if k == j:
                        s[0].append(0)
                    else:
                        s[0].append(min(times[k] - y[k], (total_cal - (cal[j] * u[0][j]))// cal[k], (total_fat - (fat[j] * u[0][j])) // fat[k]))
                    s[1].append(s[0][k] * vita[k])  #对取整后的剩余重量、体积、次数再次取整计算物品的最高可装入价值（第二层）

                    t = [[], []]
                    for l in range(len(cal)):
                        if l == j or l == k:
                            t[0].append(0)
                        else:
                            t[0].append(min(times[l] - y[l], (total_cal - (cal[j] * u[0][j]) - (cal[k] * s[0][k])) // cal[l],(total_fat - (fat[j] * u[0][j]) - (fat[k] * s[0][k])) // fat[l]))
                        t[1].append(t[0][l] * vita[l])  # 对取整后的剩余重量、体积、次数再次取整计算物品的最高可装入价值（第三层），层数越多，计算越准确，暂时只计算三层
                    s[1][k] += max(t[1])  #将第三次取整计算物品的最高可装入价值的最大值加到第二次的结果中
                u[1][j] += max(s[1])  #将第二次取整计算物品的最高可装入价值的最大值加到第一次的结果中

                
                if max(u[1]) > 0:   #选择评估价值最高的物品优先装入
                    y[u[1].index(max(u[1]))] += 1  #记录物品装入次数
                    cal, fat, vita = cal[u[1].index(max(u[1]))], fat[u[1].index(max(u[1]))], vita[u[1].index(max(u[1]))]
                    total_cal = total_cal - cal  #计算剩余承重
                    total_fat = total_fat - fat  #计算剩余容量
                    total_vita += vita  #计算已装入物品总价值
                    result.append({
                        'Calories': cal,
                        'Fat': fat,
                        'Vitamin A': vita,
                        'total_Vitamin A': total_vita,
                        'rest_cal': total_cal,
                        'rest_fat':total_fat
                    })
                else:  #一旦无满足约束的物品可装入，则停止装入
                    break
    return pd.DataFrame(result,columns = ['Calories', 'Fat', 'Vitamin A', 'total_Vitamin A', 'rest_cal', 'rest_fat'])

cal = menu['Calories'].tolist()
fat = menu['Total Fat'].tolist()
vita = menu['Vitamin A (% Daily Value)'].tolist()
times = menu['times'].tolist()
total_cal = 2000
total_fat = 350

if __name__ == "__main__":
    start_time = time.time()
    print("total %d kinds of dishes" %(len(cal)))
    print(Knapsack(cal, fat, vita, times, total_cal, total_fat))
    end_time = time.time()
    print(end_time - start_time)

