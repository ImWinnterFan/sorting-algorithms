import random 

def Visual_selection_sort(arr):
  for i in range(len(arr)):
    min_index = i 
    print(f"Loop-{i}")  #※Iは配列の長さ分繰り返す回数
    print(f"i = {i}, arr[i] = {arr[i]}") #arr[i]は配列arrの要素を取り出すための方法
   


    for j in range(i+1,len(arr)): #range(開始地点,終了地点) ※Jは配列の現在地 
    #前回の処理で最小値を見つけてすでに配置してるから、i+1することで次の最小値を探す動作に移る
    
      print(f"j={j} Comparing place[{j}] = {arr[j]} with Now Min-index place[{min_index}]={arr[min_index]}")

      if arr[j]<arr[min_index]:#現在のJと最小値minを比較 ※arrは全体、arr[]は配列中の一つの要素
        min_index=j#最小値を入れ替える ※arr[]を外したら変数はただの値であることを忘れずに！
      
    arr[i],arr[min_index]=arr[min_index],arr[i] #arr[i]は必ず最小値の場所にあるから、見つけたminと場所入れ替える
    print(f"now sort is {arr}\n")
    
  return arr

if __name__ == "__main__":
    arr = [random.randint(0,20) for _ in range(10)]
    print(f"before sort is {arr}")
    Visual_selection_sort(arr)

#RESULT
before sort is [14, 18, 13, 3, 13, 14, 12, 18, 6, 4]
Loop-0
i = 0, arr[i] = 14
j=1 Comparing place[1] = 18 with Now Min-index place[0]=14
j=2 Comparing place[2] = 13 with Now Min-index place[0]=14
j=3 Comparing place[3] = 3 with Now Min-index place[2]=13
j=4 Comparing place[4] = 13 with Now Min-index place[3]=3
j=5 Comparing place[5] = 14 with Now Min-index place[3]=3
j=6 Comparing place[6] = 12 with Now Min-index place[3]=3
j=7 Comparing place[7] = 18 with Now Min-index place[3]=3
j=8 Comparing place[8] = 6 with Now Min-index place[3]=3
j=9 Comparing place[9] = 4 with Now Min-index place[3]=3
now sort is [3, 18, 13, 14, 13, 14, 12, 18, 6, 4]

Loop-1
i = 1, arr[i] = 18
j=2 Comparing place[2] = 13 with Now Min-index place[1]=18
j=3 Comparing place[3] = 14 with Now Min-index place[2]=13
j=4 Comparing place[4] = 13 with Now Min-index place[2]=13
j=5 Comparing place[5] = 14 with Now Min-index place[2]=13
j=6 Comparing place[6] = 12 with Now Min-index place[2]=13
j=7 Comparing place[7] = 18 with Now Min-index place[6]=12
j=8 Comparing place[8] = 6 with Now Min-index place[6]=12
j=9 Comparing place[9] = 4 with Now Min-index place[8]=6
now sort is [3, 4, 13, 14, 13, 14, 12, 18, 6, 18]

Loop-2
i = 2, arr[i] = 13
j=3 Comparing place[3] = 14 with Now Min-index place[2]=13
j=4 Comparing place[4] = 13 with Now Min-index place[2]=13
j=5 Comparing place[5] = 14 with Now Min-index place[2]=13
j=6 Comparing place[6] = 12 with Now Min-index place[2]=13
j=7 Comparing place[7] = 18 with Now Min-index place[6]=12
j=8 Comparing place[8] = 6 with Now Min-index place[6]=12
j=9 Comparing place[9] = 18 with Now Min-index place[8]=6
now sort is [3, 4, 6, 14, 13, 14, 12, 18, 13, 18]

Loop-3
i = 3, arr[i] = 14
j=4 Comparing place[4] = 13 with Now Min-index place[3]=14
j=5 Comparing place[5] = 14 with Now Min-index place[4]=13
j=6 Comparing place[6] = 12 with Now Min-index place[4]=13
j=7 Comparing place[7] = 18 with Now Min-index place[6]=12
j=8 Comparing place[8] = 13 with Now Min-index place[6]=12
j=9 Comparing place[9] = 18 with Now Min-index place[6]=12
now sort is [3, 4, 6, 12, 13, 14, 14, 18, 13, 18]

Loop-4
i = 4, arr[i] = 13
j=5 Comparing place[5] = 14 with Now Min-index place[4]=13
j=6 Comparing place[6] = 14 with Now Min-index place[4]=13
j=7 Comparing place[7] = 18 with Now Min-index place[4]=13
j=8 Comparing place[8] = 13 with Now Min-index place[4]=13
j=9 Comparing place[9] = 18 with Now Min-index place[4]=13
now sort is [3, 4, 6, 12, 13, 14, 14, 18, 13, 18]

Loop-5
i = 5, arr[i] = 14
j=6 Comparing place[6] = 14 with Now Min-index place[5]=14
j=7 Comparing place[7] = 18 with Now Min-index place[5]=14
j=8 Comparing place[8] = 13 with Now Min-index place[5]=14
j=9 Comparing place[9] = 18 with Now Min-index place[8]=13
now sort is [3, 4, 6, 12, 13, 13, 14, 18, 14, 18]

Loop-6
i = 6, arr[i] = 14
j=7 Comparing place[7] = 18 with Now Min-index place[6]=14
j=8 Comparing place[8] = 14 with Now Min-index place[6]=14
j=9 Comparing place[9] = 18 with Now Min-index place[6]=14
now sort is [3, 4, 6, 12, 13, 13, 14, 18, 14, 18]

Loop-7
i = 7, arr[i] = 18
j=8 Comparing place[8] = 14 with Now Min-index place[7]=18
j=9 Comparing place[9] = 18 with Now Min-index place[8]=14
now sort is [3, 4, 6, 12, 13, 13, 14, 14, 18, 18]

Loop-8
i = 8, arr[i] = 18
j=9 Comparing place[9] = 18 with Now Min-index place[8]=18
now sort is [3, 4, 6, 12, 13, 13, 14, 14, 18, 18]

Loop-9
i = 9, arr[i] = 18
now sort is [3, 4, 6, 12, 13, 13, 14, 14, 18, 18]
