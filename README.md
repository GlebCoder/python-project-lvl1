### Hexlet tests and linter status:
[![Actions Status](https://github.com/GlebCoder/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/GlebCoder/python-project-lvl1/actions)
[![Lint check workflow](https://github.com/GlebCoder/python-project-lvl1/actions/workflows/lint-check.yml/badge.svg)]()
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)


## Общее описание и примеры

«Игры разума» — набор из пяти консольных игр, построенных по принципу популярных мобильных приложений для прокачки мозга. Каждая игра задает вопросы, на которые нужно дать правильные ответы. После трех правильных ответов считается, что игра пройдена. Неправильные ответы завершают игру и предлагают пройти ее заново. Игры:  

Калькулятор. Арифметические выражения, которые необходимо вычислить.

https://asciinema.org/a/NmU2lPrYfI2goWiaCNUEfw0qV -a video example of the brain-calc game  


Прогрессия. Поиск пропущенных чисел в последовательности чисел.  

https://asciinema.org/a/EGYwSn4ypjm8G5u0qiKNGBchU - a video example of the brain-progression game  


Определение четного числа.  

https://asciinema.org/a/0z95rvcKEHCMSiFM4jaYn7WMP - a video example of the brain-even game 


Определение наибольшего общего делителя. 

https://asciinema.org/a/BYyX0iDvE0iy7xBuiCkovRCO1 - a video example of the brain-gcd game  

Определение простого числа. 

https://asciinema.org/a/flhu4JGfyiZUEkxLfHJN8gn0e a video example of the brain-prime game 

Пример игры:  

$ brain-progression  
Welcome to the Brain Game!  
What number is missing in this progression?  
May I have your name? Roman  
Hello, Roman!  
Question: 14 .. 18 20 22 24 26 28  
Your answer: 16 # Пользователь вводит ответ  
Correct!  
Question: 5 6 7 8 9 .. 11 12  
Your answer: 10 # Пользователь вводит ответ  
Correct!  
Question: 12 15 18 21 .. 27 30 33  
Your answer: 24 # Пользователь вводит ответ  
Correct!  
Congratulations, Roman!  

## Установка пакета

Пакет устанавливается напрямую из git-репозитария.  
в командной строке нужно ввести:  


python3 -m pip install --user git+https://github.com/GlebCoder/python-project-lvl1.git


Внимание: этот пакет установится, только если у вас pip будет версии 20 и выше. Если вы увидите ошибку при установке пакета, попробуйте обновить сам pip (python3 -m pip install --user --upgrade pip).


## Запуск игр

После установки игры должны запускаться следующими командами:

Для игры калькулятор: brain-calc

Для игры прогрессия: brain-progression

Для игры определения четного числа: brain-even

Для игры НОД (наибольший общий делитель): brain-gcd

Для игры определения простого числа: brain-prime

