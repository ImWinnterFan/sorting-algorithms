「マージ」:マージは２つのソート配列を小さい順に、１つの配列にまとめる操作(プリグラム)
def merge_arrays(left,right=[]):
  res = []
  i,j=0,0
  n,m = len(left),len(right)

  while i < n and j < m: #iとnの処理が終わったらループを抜ける

    if left[i] < right[j]: #left,rightで小さい方をresに追加
      res.append(left[i]) #resに小さい方を追加
      i += 1 #iの配列の要素を一つ進める

    else:
      res.append(right[j]) #resに小さい方を追加
      j +=1 #Jの配列の要素を一つ進める


  return res + left[i:] + right[j:] #left[i:]の意味は配列の要素の残り

  #片方の配列は先にwhileで終了するからleftかrightのどちらかにした入らない
  
