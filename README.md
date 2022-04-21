# homework_otus
_Домашние задания по курсу "Автоматизация тестирования на Python"_
___
## homework_1_oop
Цель:
Научиться писать код в ООП стиле и покрывать его тестами.

Описание/Пошаговая инструкция выполнения домашнего задания:

- [ ] Создать базовый класс геометрической фигуры (Figure).
- [ ] Реализовать классы геометрических фигур Треугольник, Прямоугольник, Квадрат, Круг (Triangle, Rectangle, Square, Circle). Каждый класс должен располагаться в отдельном файле с соответствующим названием (например class Triangle => Triangle.py).
- [ ] Все файлы с классами должны находиться в папке src/
- [ ] Треугольник должен задаваться тремя сторонами, если треугольник создать нельзя то выбрасывать ошибку raise ValueError.

### 1 Часть
- [ ] Каждая фигура должна иметь атрибуты: name - название фигуры, area (вычисляемое!) - площадь, perimeter (вычисляемое!) - периметр (сумма длин сторон или длину окружности)
- [ ] Все вычисляемые свойства должны вычисляться по формулам для соответствующих геометрических фигур (никакого хардкода значений).
- [ ] Каждая фигура должна реализовать метод add_area(figure) который должен принимать другую геометрическую фигуру и возвращать сумму площадей этих фигур. Если метод передана не геометрическая фигура, то нужно выбрасывать ошибку (raise ValueError).
###Пример работы с одним из классов фигуры:

square = Square(10) # Так создаем квадрат со стороной 10

square.area

100

triangle = Triangle(13, 14, 15) # Так создаем треугольник со сторонами 13, 14, 15

triangle.area

84

triangle.add_area(square)

184

### 2 Часть. 
- [ ] Написать тесты с использованием pytest на эти классы. Глубину покрытия и объем определить самостоятельно, но минимум проверить реализацию всех указанных требований для каждого класса.
Все тесты должны располагаться в папке tests/
___