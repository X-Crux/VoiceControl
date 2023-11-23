import re


def words_to_number(text):
    words_to_numbers = {
        'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5,
        'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9, 'десять': 10,
        'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14,
        'пятнадцать': 15, 'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18,
        'девятнадцать': 19, 'двадцать': 20, 'тридцать': 30, 'сорок': 40,
        'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят': 80,
        'девяносто': 90, 'сто': 100, 'двести': 200, 'триста': 300, 'четыреста': 400,
        'пятьсот': 500, 'шестьсот': 600, 'семьсот': 700, 'восемьсот': 800,
        'девятьсот': 900, 'тысяча': 1000, 'тысячи': 1000, 'миллион': 1000000,
        'миллиона': 1000000, 'миллиард': 1000000000, 'миллиарда': 1000000000
    }

    result = 0
    partial_result = 0
    for word in re.findall(r'\w+', text):
        number = words_to_numbers.get(word.lower())
        if number is not None:
            if number >= 1000:
                result += partial_result * number
                partial_result = 0
            else:
                partial_result += number

    return result + partial_result


class DataAnalysis:
    data = dict()

    def __init__(self, data):
        self.data = data

    def analyze(self) -> dict:
        analysis_result = {
            'adj': 'txt',
            'num': 1
        }

        if 'txt' in self.data['adjs'] or 'текстовый' in self.data['adjs'] or 'текстовых' in self.data['adjs']:
            analysis_result['adj'] = 'txt'

        if 'все' in self.data['dets']:
            analysis_result['num'] = 'all'
        elif len(self.data['nums']):
            status = True

            for num in self.data['nums']:
                try:
                    analysis_result['num'] = int(num)
                    status = False
                    break
                except ValueError:
                    pass

            if status:
                num_str = ' '.join([str(num) for num in self.data['nums']])
                num_int = words_to_number(num_str)
                analysis_result['num'] = int(num_int)

        return analysis_result
