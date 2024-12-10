# -*- coding: utf-8 -*-
import json
from Types import DataType
from DataReader import DataReader


class JsonDataReader(DataReader):

    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        # Открытие и загрузка данных из JSON файла
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Преобразуем JSON-данные в нужный формат
        self.students = {
            name: [(subject, score) for subject, score in subjects.items()]
            for name, subjects in data.items()
        }

        return self.students
