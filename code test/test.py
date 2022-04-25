'''

Question Description: 
* A backpack, load something into it, the item weight w(weight) corresponds to [2,3,4,7], the value va(value) corresponds to [1,4,7,12], if your maximum load is 20 and each item can be loaded an unlimited number of times, find the maximum value you can load into the backpack.
* If the number of times the item can be loaded corresponds to [4,3,2,1], find the maximum value you can load into the backpack.
* If the volume of the item vo(volume) corresponds to [3,5,8,17], and the maximum capacity is 35, find the maximum value you can put in your backpack.

the code below statify three above constraint.

'''

import pandas as pd
import time

def Knapsack(w, vo, va, times, total_weight, total_volume):

    total_value = 0
    result = [{
                'weight': 0,
                'volume': 0,
                'value': 0,
                'total_value': total_value,  #increasing
                'rest_weight': total_weight,  #decreasing
                'rest_volume':total_volume  #decreasing
            }]

    y = [0] * len(w)  #Used to count the number of times items are loaded
    for i in range(1000):  #Set the number of loading attempts
        k = 0
        for j in range(len(w)):
            if w[k] > total_weight or vo[k] > total_volume or y[k] == times[k]:  #Remove items whose weight exceeds the remaining load capacity or whose volume is greater than the remaining capacity or whose loading times have reached the upper limit
                print("weight%dvolume%d：total%dtimes" %(w[k], vo[k], y[k]))
                del w[k], vo[k], va[k], times[k], y[k]
            else:
                k += 1

        if len(w) > 0:
            u = [[], []]
            for j in range(len(w)):
                u[0].append(min(times[j] - y[j], (total_weight // w[j]), (total_volume // vo[j])))
                u[1].append(u[0][j] * va[j])  #First rounding to calculate the maximum loadable value of the item (first tier)

                s = [[], []]
                for k in range(len(w)):
                    if k == j:
                        s[0].append(0)
                    else:
                        s[0].append(min(times[k] - y[k], (total_weight - (w[j] * u[0][j]))// w[k], (total_volume - (vo[j] * u[0][j])) // vo[k]))
                    s[1].append(s[0][k] * va[k])  #Calculate the maximum loadable value of the item by rounding again for the remaining weight, volume, and number of times after rounding (second level)

                    t = [[], []]
                    for l in range(len(w)):
                        if l == j or l == k:
                            t[0].append(0)
                        else:
                            t[0].append(min(times[l] - y[l], (total_weight - (w[j] * u[0][j]) - (w[k] * s[0][k])) // w[l],(total_volume - (vo[j] * u[0][j]) - (vo[k] * s[0][k])) // vo[l]))
                        t[1].append(t[0][l] * va[l])  # The remaining weight, volume, and number of times after rounding are rounded again to calculate the highest loadable value of the item (the third layer), the more layers, the more accurate the calculation, for the time being, only three layers are calculated
                    s[1][k] += max(t[1])  #Add the maximum value of the highest loadable value of the third rounded item to the result of the second
                u[1][j] += max(s[1])  #Add the maximum value of the highest loadable value of the second rounded item to the first result

            if max(u[1]) > 0:   #Select the items with the highest assessed value to be loaded first
                y[u[1].index(max(u[1]))] += 1  #Record the number of times items are loaded
                weight, volume, value = w[u[1].index(max(u[1]))], vo[u[1].index(max(u[1]))], va[u[1].index(max(u[1]))]
                total_weight = total_weight - weight  #Calculate the remaining load-bearing capacity
                total_volume = total_volume - volume  #Calculate remaining capacity
                total_value += value  #Calculate the total value of loaded items
                result.append({
                    'weight': weight,
                    'volume': volume,
                    'value': value,
                    'total_value': total_value,
                    'rest_weight': total_weight,
                    'rest_volume':total_volume
                })
            else:  #Stop loading once there are no more items to load that meet the constraints
                break

    return pd.DataFrame(result,columns = ['weight', 'volume', 'value', 'total_value', 'rest_weight', 'rest_volume'])


data = pd.read_csv("data.csv")  
data['unitw_value'] = data['value'] / data['weight']
data = data.sort_values(by = 'unitw_value', ascending = False)

weight = data['weight'].tolist()
volume = data['volume'].tolist()
value = data['value'].tolist()
times = data['times'].tolist()
total_weight = 20
total_volume = 35

if __name__ == "__main__":
    start_time = time.time()
    print("total %d kinds of item" %(len(weight)))
    print(Knapsack(weight, volume, value, times, total_weight, total_volume))
    end_time = time.time()
    print(end_time - start_time)
