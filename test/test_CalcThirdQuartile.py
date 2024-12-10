# -*- coding: utf-8 -*-
import pytest
import numpy as np
from src.Types import RatingsType
from src.CalcThirdQuartile import CalcThirdQuartile


class TestCalcThirdQuartile:

    @pytest.fixture()
    def input_ratings(self) -> RatingsType:
        return {
            "Новиков": 68.0,
            "Фёдоров": 88.0,
            "Морозов": 78.0,
            "Волков": 92.0,
            "Соловьёв": 55.0,
            "Васильев": 72.0,
            "Зайцев": 81.0
        }

    def test_calc(self, input_ratings: RatingsType) -> None:
        calc_quartile = CalcThirdQuartile(input_ratings)
        result = calc_quartile.calc()

        # Вычисление квартили для вывода
        rating_values = np.array(list(input_ratings.values()))
        q3 = np.percentile(rating_values, 75)

        expected = {"Фёдоров", "Волков"}  # Ожидаемые студенты
        assert sorted(result) == sorted(expected)
