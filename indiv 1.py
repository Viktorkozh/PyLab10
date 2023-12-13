#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"b", "d", "l", "p"}
    b = {"b", "d", "e", "l", "p", "x"}
    c = {"k", "l", "p", "t"}
    d = {"d", "k", "o", "p", "q", "u", "v"}

    x = (a.difference(b)).intersection(c.union(d))
    y = ((u.difference(a)).intersection(d)).union(c.difference(b))

    if x:
        print(f"x = {x}")
    else:
        print("x is empty")

    if y:
        print(f"y = {y}")
    else:
        print(f"y is empty")
