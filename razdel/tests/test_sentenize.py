
import pytest

from razdel import sentenize

from .partition import parse_partitions
from .common import (
    run,
    data_path,
    data_lines,
    load_lines
)


UNIT = parse_partitions([
    'фонетических правил языка; в случае, если',
    '(Прилепин — очень хороший писатель, лучше, чем Лимонов.| |Но враг)',
    'Петров - 176!| |Михайлов - 180!',
    'если бы… не тот широко',
    'Георгий Иванов.| |На грани музыки и сна',
    'исполняется 150 лет.| |31 мая 1859 года после неоднократных',

    # SOKR
    'И т. д. и т. п.| |В общем, вся газета',
    'специалистом, к.п.н. И. П. Карташовым.',
    'основании п. 2, ст. 5 УПК',
    'Вблизи оз. Селяха',
    'уменьшить с 20 до 18 проц. (при сохранении',
    '6 июля 2007 г. "в связи с совершением',
    'на 500 тыс. машин',
    'Влияние взглядов Л. В. Щербы',
    'директор фирмы Чарльз Дж. Филлипс',
    'Т.е. ОБЯЗАТЕЛЬНО письменно',
    'была утечка т.н. Таблицы боевых действий',
    'В 1996-1999гг. теффт',
    'России, т. е. 55 % опрошенных',
    'я ощущал в 1990-е.| |Славное было время',

    # BOUND
    'словам, "не будет точно".| |"Возможно, у нас',
    'Брось!.."| |Связываться не хотелось',
    'Peter Goldreich,Scott Tremaine (1979).| |«Относительно теории колец Урана».',
    'Это чудовищные риски.| |"Яндекс" попал под удар',
    'кто они такие… »',

    # DASH
    '- "Так в чем же дело?"| |- "Не ра-ду-ют".',
    '— Ты ей скажи, что я ей гостинца дам.| |— А мне дашь?',

    '4. Я присутствовал во время встречи',
    'IV. Гестационный сахарный диабет',
    '§2. Нахождение оптимального объекта.',
    '8.1. Зачем нужны эти классы?',
    'в данной квартире;| |2) отчуждать свою долю',

    'пастухов - тоже ;)| |Я вспомнила',
    'распределённой жабы :))| |А платить мне будут аж 1200 рублей'
])


@pytest.mark.parametrize('test', UNIT)
def test_unit(test):
    run(sentenize, test)


def test_che_sample():
    path = data_path('che_sents_sample.txt')
    lines = load_lines(path)
    for partition in parse_partitions(lines):
        run(sentenize, partition)


def int_tests(count):
    path = data_path('sents.txt')
    lines = data_lines(path, count)
    return parse_partitions(lines)


def test_int(int_test):
    run(sentenize, int_test)
