#input関数を使って入力を受け取る
name = input('お名前は?')
print(name)

#len関数を使って文字列の長さを調べる
print(len(name))

#iter関数を使って順番に並んだオブジェクトを引数にとって出力する（返す）
name_iter = iter(name)
print(next(name_iter))
print(next(name_iter))
print(next(name_iter))
print(next(name_iter))
print(next(name_iter))

