import datetime
import operator

from babel import Locale
from babel.languages import get_official_languages, get_territory_language_info
from babel.lists import format_list
from babel.support import Format

from utils import _spacer

LOCALES = (
    ('Russian', 'ru_RU', ('ru', 'RU')),
    ('Hungarian', 'hu_HU', ('hu', 'HU')),
    ('Greek', 'el_GR', ('el', 'GR')),
    ('French', 'fr_FR', ('fr', 'FR')),
    ('Hebrew', 'he_IL', ('he', 'IL')),
)


def list_format():
    print('Formating lists')
    items = (
        'one',
        'two',
        'three',
        'four',
        'five'
    )
    for (name, symbol, params) in LOCALES:
        locale = Locale(*params)
        result = format_list(items, locale=locale)
        print('\tlist in {0} - {1}'.format(name, result))


def format_class():
    print('Utility class that holds all formating functionality for single locale')
    date = datetime.date(1874, 5, 29)
    amount = (284.55, 'CNY')
    for (name, symbol, params) in LOCALES:
        locale = Locale(*params)
        fmt = Format(locale=locale)
        args = [name]
        args.append(fmt.date(date, format='full'))
        args.append(fmt.currency(*amount))
        print('\tFormats for {0} - date: {1}, currency: {2}'.format(*args))


def languages():
    print('Known languages')
    locale = Locale('en', 'US')
    for (_, _, params) in LOCALES:
        territory = params[1]
        official_languages = format_list(get_official_languages(territory), locale=locale)
        all_languages = format_list(get_official_languages(territory, regional=True, de_facto=True), locale=locale)
        print('\tterritory: {0}'.format(locale.territories[territory]))
        print('\t\tofficial: {0}\n\t\tall: {1}'.format(official_languages, all_languages))


def language_info():
    print('Language information for specific territory')
    locale = Locale('en', 'US')
    for (_, _, params) in LOCALES:
        territory = params[1]
        print('\tterritory: {0}'.format(locale.territories[territory]))
        lang_info = get_territory_language_info(territory)
        language_data = []
        for k, v in lang_info.items():
            pcnt = v.get('population_percent', 0)
            status = v.get('official_status')
            if status is None:
                status = 'unofficial'
            if '_' in status:
                status = status.split('_', 1)[-1]
            language_data.append((pcnt, locale.languages.get(k, k), status))
            sorted_languages = reversed(sorted(language_data, key=operator.itemgetter(0)))
        for (pcnt, name, status) in sorted_languages:
            print('\t\tlanguage: {0}, population: {1}%, status: {2}'.format(name, pcnt, status))


def main():
    list_format()
    _spacer()
    format_class()
    _spacer()
    languages()
    _spacer()
    language_info()

if __name__ == '__main__':
    main()
