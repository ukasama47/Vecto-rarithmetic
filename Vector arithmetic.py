

# ベクトルの和を計算する関数
def v_sum(x, y):
    z = [a + b for a, b in zip(x, y)]
    return z

# ベクトルの差を計算する関数
def v_diff(x, y):
    z = [a - b for a, b in zip(x, y)]
    return z

# ベクトルの内積を計算する関数
def v_ip(x, y):
    z = sum([a * b for a, b in zip(x, y)])
    return z

# 確認用スクリプト
if __name__ == '__main__':
    a = [1, 2, 3]
    b = [4, 5, 6]

    # ベクトルの和の計算と出力
    sum_ab = v_sum(a, b)
    print("ベクトルの和:", sum_ab)

    # ベクトルの差の計算と出力
    diff_ab = v_diff(a, b)
    print("ベクトルの差:", diff_ab)

    # ベクトルの内積の計算と出力
    ip_ab = v_ip(a, b)
    print("ベクトルの内積:", ip_ab)
