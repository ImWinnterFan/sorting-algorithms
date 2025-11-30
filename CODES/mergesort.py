「問題を分割」：配列を小さい単位に分割して分けて処理する(マージソート)
import random

# --- マージ関数の定義 ---
def merge_arrays(left, right):
    res = []
    i, j = 0, 0
    n, m = len(left), len(right)
    while i < n and j < m:
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    return res + left[i:] + right[j:]

# --- step関数の定義 ---
def step(array):
    res = []
    for i in range(0, len(array), 2):
        # 2個ずつ取り出してマージ
        if i+1 < len(array):  # ペアが揃っている場合
            res.append(merge_arrays(*array[i:i+2]))
        else:                 # 最後に1個だけ余った場合
            res.append(array[i])
    return res

# --- 実行部分 ---
random.seed(3)
my_array = [random.randint(0,1000) for i in range(15)]
my_array = [[v] for v in my_array]

print("初期配列:", my_array)

step1 = step(my_array)
print("一回目の操作:", step1)

step2 = step(step1)
print("二回目の操作:", step2)
