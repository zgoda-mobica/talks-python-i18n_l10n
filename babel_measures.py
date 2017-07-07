from babel import Locale
from babel.units import format_unit, get_unit_name

from utils import _spacer

LOCALES = (
    ('Polish', 'pl_PL', ('pl', 'PL')),
    ('Russian', 'ru_RU', ('ru', 'RU')),
    ('Hungarian', 'hu_HU', ('hu', 'HU')),
    ('Greek', 'el_GR', ('el', 'GR')),
    ('French', 'fr_FR', ('fr', 'FR')),
    ('Hebrew', 'he_IL', ('he', 'IL')),
)


def localized_measures():
    print('Localized measurement units')
    units = (
        'area-square-meter',
        'consumption-liter-per-100kilometers',
        'pressure-hectopascal',
        'duration-century',
        'energy-kilowatt-hour',
        'volume-pint',
    )
    for (name, symbol, params) in LOCALES:
        locale = Locale(*params)
        args = [name]
        for unit in units:
            unit_name = get_unit_name(unit, locale=locale)
            if unit_name is None:
                unit_name = 'N/A ({0})'.format(unit)
            args.append(unit_name)
        print('\nin {0}: {1} - {2} - {3} - {4} - {5} - {6}'.format(*args))


def units_formating():
    print('Formating values in units')
    values = (
        (12.4, 'area-square-meter'),
        (7.7, 'consumption-liter-per-100kilometers'),
        (1017, 'pressure-hectopascal'),
        (9, 'duration-century'),
        (11, 'energy-kilowatt-hour'),
        (2, 'volume-pint'),
    )
    for (name, symbol, params) in LOCALES:
        locale = Locale(*params)
        args = [name]
        for (value, unit) in values:
            val_long = format_unit(value, unit, 'long', locale=locale)
            short_name = get_unit_name(unit, 'short', locale=locale) 
            args.append('{0} ({1})'.format(val_long, short_name))
        print('\nin {0}: {1} - {2} - {3} - {4} - {5} - {6}'.format(*args))


def main():
    localized_measures()
    _spacer()
    units_formating()

if __name__ == '__main__':
    main()
