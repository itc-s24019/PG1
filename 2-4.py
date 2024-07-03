#データの型を調べる
print(type(3))
print(type(3.1))

#変数に格納されているデータの方を調べる
a = 3
print(type(a))

#上のプログラムを活用してデータか整数型かを確認
print(type(a) is int)
print(type(a) is float)
print(isinstance(a, int))

#数値演算（pow関数を使って冪乗の計算をする）
print(pow(2, 10))
print(pow(16, 0.5))

#pow関数を使って前の２つの因数で計算された値を割って、余りをかえす
print(pow(9, 22, 23))
print(divmod(13, 5))

#少数を少数に丸める
print(round(2.672, 2))
print(round(2.679, 2))
print(round(1.5))
print(round(2.5))
print(round(2.675, 2))


