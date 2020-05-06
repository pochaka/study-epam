# Модель файла:
# | Страна | Категория Товара | Количество проданных | Цена за штуку |

import csv

class CsvParser:
    def __init__(self, file_name):
        pass

    def sell_over(self, item_type: str, threshhold: int):
        '''Список стран, где продано item_type больше, чем threshhold'''
        pass

    def get_country_profit(self, country):
        '''Общая прибыть по стране'''
        pass

    def save_as(self, new_file_name, delimiter):
        '''Сохранение с другим разделителем'''
        pass


