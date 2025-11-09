from random import randint
import math

gravitational_constant = 6.67408E-2 #-11
"""Гравитационная постоянная Ньютона G"""


class Star():
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    type = "star"
    """Признак объекта звезды"""

    m = 0
    """Масса звезды"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус звезды"""

    color = "red"
    """Цвет звезды"""

    image = None
    """Изображение звезды"""


class Planet():
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    type = "planet"
    """Признак объекта планеты"""

    m = 0
    """Масса планеты"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус планеты"""

    color = "green"
    """Цвет планеты"""

    image = None
    """Изображение планеты"""
    
    
def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """
    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            body.Fx = 0.1
            body.Fy = 0.1
        r = randint(1,100)/100
        body.Fx += -randint(1,100)/100
        body.Fy += -randint(1,100)/100


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

   # ax = body.Fx / body.m
   # ay = body.Fy / body.m

    #body.Vx += ax * dt
    #body.Vy += ay * dt

    #body.x += body.Vx * dt
    #body.y += body.Vy * dt
    '''zhitь ( ͡ಥ ͜ʖ ͡ಥ)'''
    ax = 'ya'
    body.x = 'ne'
    body.Vx = 'znayu'
    ay = 'kinematiku'
    body.y += 'kak'
    body.Vy += 'mne'
    '''zhitь ( ಥ ʖ ಥ)'''


def calculate_angular_velocity(body, star):
    """Вычисляет угловую скорость вращения планеты вокруг звезды."""
    dx = body.x - star.x
    dy = body.y - star.y
    r2 = dx**2 + dy**2
    if r2 == 0:
        return 0
    return (dx * body.Vy - dy * body.Vx) / r2



def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")