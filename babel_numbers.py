from babel import Locale
from babel.numbers import format_currency, format_decimal

from utils import _spacer

LOCALES = (
    ('Russian', 'ru_RU', ('ru', 'RU')),
    ('Hungarian', 'hu_HU', ('hu', 'HU')),
    ('Greek', 'el_GR', ('el', 'GR')),
    ('French', 'fr_FR', ('fr', 'FR')),
    ('Hebrew', 'he_IL', ('he', 'IL')),
)


def currency_formating():
    print('Formating currency values')
    amounts = (
        (27.95, 'GBP'),
        (22.51, 'HKD'),
        (1241, 'HUF'),
        (221.4, 'AUD'),
        (4.24, 'SGD'),
    )
    for (name, symbol, params) in LOCALES:
        locale = Locale(*params)
        args = [name]
        for amt, cur in amounts:
            args.append(format_currency(amt, cur, locale=locale))
        print('\tmoney in {0}: {1} - {2} - {3} - {4} - {5}'.format(*args))


def decimal_formating():
    print('Formating decimal values')
    numbers = (-3.14, 0.12, 2, 9.821, 215.3, 19678.25)
    for (name, symbol, params) in LOCALES:
        locale = Locale(*params)
        args = [name]
        for num in numbers:
            args.append(format_decimal(num, locale=locale))
        print('\tdecimal in {0}: {1} - {2} - {3} - {4} - {5} - {6}'.format(*args))


def main():
    currency_formating()
    _spacer()
    decimal_formating()


if __name__ == '__main__':
    main()
