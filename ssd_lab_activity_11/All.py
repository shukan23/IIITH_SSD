import csv


#   Q1
result1 = []
with open('data.csv') as a:
    lines = csv.reader(a)
    for line in lines:
        x = len(line)
        y = line[:x-6]
        # print(y)
        result1.append(y)


#   Q2
Filtered = filter(lambda line : True if float(line[6]) > -3 else False,result1[1:])
result2 = [result1[0]]
result2.extend(Filtered)

#   Q3
open1 = [[]]
high1 = [[]]
low1 = [[]]
for x in result2[1:]:
    open1[0].append(float(x[1].replace(',','')))
    high1[0].append(float(x[2].replace(',','')))
    low1[0].append(float(x[3].replace(',','')))

avg_fun = lambda x : sum(x)/len(x) 
avg_open = list(map(avg_fun,open1))
avg_high =list(map(avg_fun,high1))
avg_low = list(map(avg_fun,low1))

with open('avg_output.txt', 'w') as out :
        out.write(str(avg_open[0])+ "\n")
        out.write(str(avg_high[0])+ "\n")
        out.write(str(avg_low[0])+ "\n")

#   Q4

a = input()

print(result2[0])
for row in result2[1:] :
    if row[0][0] == a :
        print(row)

#   Q5

with open('stock_out.txt', 'w') as out :
    for line in result2:
        ansstr = ""
        for x in line:
            ansstr+= x + " "
        ansstr += "\n"
        out.write(ansstr)