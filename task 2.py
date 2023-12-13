#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = set(input("Введите строку а: "))
    b = set(input("Введите строку б: "))

    x = a.intersection(b)
    print(f"x = {x}")