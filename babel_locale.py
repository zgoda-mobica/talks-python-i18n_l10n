from babel import Locale

from utils import _spacer


LOCALES = (
    ('Russian', 'ru_RU', ('ru', 'RU')),
    ('Hungarian', 'hu_HU', ('hu', 'HU')),
    ('Greek', 'el_GR', ('el', 'GR')),
    ('Hebrew', 'he_IL', ('he', 'IL')),
)


def locale_own_data():
    print('Locale data (pl - language only):')
    locale = Locale('pl')
    print('\tDisplay name: {0}'.format(locale.display_name))
    print('\tEnglish name: {0}'.format(locale.english_name))
    print('Locale data (pl_PL - language and territory):')
    locale = Locale('pl', 'PL')
    print('\tDisplay name: {0}'.format(locale.display_name))
    print('\tEnglish name: {0}'.format(locale.english_name))


def localized_locale_data():
    print('Localized locale data')
    for (name, symbol, params) in LOCALES:
        print('Now switch to {0} ({1})'.format(name, symbol))
        locale = Locale(*params)
        print('\tLocale display name: {0}'.format(locale.display_name))
        print('\tLocale English name: {0}'.format(locale.english_name))
        print('\tPoland (localized): {0}'.format(locale.territories['PL']))
        print('\tRomanian New Lei (localized): {0}'.format(locale.currencies['RON']))
        print('\tRomanian Old Lei (localized): {0}'.format(locale.currencies['ROL']))
        print('\t1st weekday (localized): {0}'.format(locale.days['format']['wide'][locale.first_week_day]))
        print('\tMay month name (localized): {0}'.format(locale.months['format']['wide'][5]))


def main():
    locale_own_data()
    _spacer()
    localized_locale_data()
    _spacer()

if __name__ == '__main__':
    main()
