#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    vowels = set("aeiouAEIOU")  # Определение множества гласных

    input_string = input("Введите строку: ")  # Ввод строки с клавиатуры

    # Подсчет количества гласных
    vowel_count = sum(char in vowels for char in input_string)

    print(f"Количество гласных: {vowel_count}")
