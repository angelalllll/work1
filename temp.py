# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cmath

def solve_quadratic(a, b, c):
    # 計算判別式
    delta = b**2 - 4*a*c

    # 根據判別式的值求解根
    if delta > 0:
        x1 = (-b + cmath.sqrt(delta)) / (2*a)
        x2 = (-b - cmath.sqrt(delta)) / (2*a)
        return x1, x2
    elif delta == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + cmath.sqrt(-delta)*1j) / (2*a)
        x2 = (-b - cmath.sqrt(-delta)*1j) / (2*a)
        return x1, x2

# 設定方程式的係數        
a = float(input("請輸入a的值："))
b = float(input("請輸入b的值："))
c = float(input("請輸入c的值："))

# 解方程式
roots = solve_quadratic(a, b, c)

# 輸出結果
print("方程式的根為：", roots)
