from babel import Locale
from babel.numbers import format_currency

LOCALES = (
    ('Russian', 'ru_RU', ('ru', 'RU')),
    ('Hungarian', 'hu_HU', ('hu', 'HU')),
    ('Greek', 'el_GR', ('el', 'GR')),
    ('French', 'fr_FR', ('fr', 'FR')),
    ('Brasil', 'pt_BR', ('pt', 'BR')),
)


def currency_formatting():
    print('Formatting of currency values')
    amounts = (
        (27.95, 'GBP'),
        (114, 'PLN'),
        (1241, 'HUF'),
        (221.4, 'AUD'),
        (4.24, 'EUR'),
    )
    for (name, symbol, params) in LOCALES:
        locale = Locale(*params)
        args = [name]
        for amt, cur in amounts:
            args.append(format_currency(amt, cur, locale=locale))
        print('\tlump sum in {0}: {1} - {2} - {3} - {4} - {5}'.format(*args))


def main():
    currency_formatting()

if __name__ == '__main__':
    main()
