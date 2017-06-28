import datetime

from babel import Locale
from babel.dates import format_date, get_timezone, get_timezone_location, format_timedelta

from utils import _spacer


LOCALES = (
    ('Russian', 'ru_RU', ('ru', 'RU')),
    ('Hungarian', 'hu_HU', ('hu', 'HU')),
    ('Greek', 'el_GR', ('el', 'GR')),
    ('French', 'fr_FR', ('fr', 'FR')),
)


def my_birthday():
    print('My birthday in different locales')
    bday = datetime.date(1971, 5, 4)
    for (name, symbol, params) in LOCALES:
        locale = Locale(*params)
        for fmt in ('full', 'medium', 'short'):
            print('\t{0} ({1}): {2}'.format(name, fmt, format_date(bday, fmt, locale)))


def timezone_names():
    print('Timezone data')
    tznames = ('Europe/Athens', 'US/Alaska', 'Africa/Johannesburg')
    for (name, symbol, params) in LOCALES:
        locale = Locale(*params)
        for tzname in tznames:
            tz = get_timezone(tzname)
            loc_name = get_timezone_location(tz, locale, False)
            city = get_timezone_location(tz, locale, True)
            print('\tTZ location for {0}: {1}, city: {2}'.format(tzname, loc_name, city))


def time_deltas():
    print('Periods of time (timedelta)')
    deltas = (
        datetime.timedelta(minutes=15),
        datetime.timedelta(hours=3),
        datetime.timedelta(days=8),
        datetime.timedelta(weeks=5),
    )
    for (name, symbol, params) in LOCALES:
        locale = Locale(*params)
        args = [name]
        for delta in deltas:
            args.append(format_timedelta(delta, locale=locale))
        print('\tbasic {0}: {1} - {2} - {3} - {4}'.format(*args))
        args = [name]
        for delta in deltas:
            args.append(format_timedelta(delta, granularity='day', locale=locale))
        print('\tday granularity {0}: {1} - {2} - {3} - {4}'.format(*args))


def main():
    my_birthday()
    _spacer()
    timezone_names()
    _spacer()
    time_deltas()

if __name__ == '__main__':
    main()
