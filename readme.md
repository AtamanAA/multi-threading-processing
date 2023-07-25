# Практика з конкурентності

## Multithreading та multiprocessing

### Тести для завдання № 2

Час виконання програми в секундах в залежності від кількості потоків(процесів) для швидкої задачі

| Кіл-ть | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 9   |
| ------ |------|------|------|------|------|------|------|------|------|-----|
| Thread | 0.27 | 0.41 | 0.6  | 0.79 | 0.99 | 1228 | 1.4  | 1.45 | 1.6  | 1.8 |
| Process | 0.34 | 0.52 | 0.45 | 0.5  | 0.58 | 0.65 | 0.74 | 0.82 | 0.96 | 1  |


Час виконання програми в секундах в залежності від кількості потоків(процесів) для довгої задачі

| Кіл-ть | 1  | 2  | 3  | 10  |
| ------ |----|----|----|-----|
| Thread | 21 | 45 | 65 | 220 |
| Process | 22 | 23 | 34 | 86  |

Висновок:

* Для простих обчислювальних задач (менше 0.2 секунд для одного обчислювання) multithreading показує значний приріст в швидкості обчислювань.

* Для більш скадних обчислювань (більше 0.2 секунд для одного обчислювання) multiprocessing починає вигравити за сумарним часом виконання прграми де є більше 3 обчислень.


### Тести для завдання № 5

Час виконання програми в секундах в залежності від кількості запитів

| Кіл-ть запитів     | 5   | 50  | 100 | 500 |
|--------------------|-----|-----|-----|-----|
| Послідовний виклик | 1.5 | 12  | 22  | 105 |
| Thread             | 0.5 | 2.7 | 5.5 | 30  |



Висновок:

* Час виконання 500-та запитів для послідовних викликів 105 секунд, при використанні concurrent.futures - 30 секунд