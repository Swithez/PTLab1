# -*- coding: utf-8 -*-
import numpy as np
from Types import RatingsType


class CalcThirdQuartile:

    def __init__(self, ratings: RatingsType) -> None:
        self.ratings: RatingsType = ratings
        self.third_quartile_students: list[str] = []

    def calc(self) -> list[str]:
        # Достаём рейтинг и выполняем вычисления
        rating_values = np.array(list(self.ratings.values()))
        q3 = np.percentile(rating_values, 75)

        # Находим студентов, попадающих в третью квартиль.
        self.third_quartile_students = [
            student for student, rating in self.ratings.items()
            if q3 < rating
        ]

        return self.third_quartile_students
