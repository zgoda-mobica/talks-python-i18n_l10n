import os
import locale
import pprint

from utils import _spacer, _init_locale


def numeric_convention_information():
    print('Numeric conventions:')
    pprint.pprint(locale.localeconv())


def date_and_time_formatting_information():
    print('Date and time formatting:')
    names = ('datetime format (D_T_FMT)', 'date format (D_FMT)', 'time format (T_FMT)')
    for index, option in enumerate((locale.D_T_FMT, locale.D_FMT, locale.T_FMT)):
        print('\tOption: {0}, value: {1}'.format(names[index], locale.nl_langinfo(option)))


def day_names():
    print('Day names (full and abbreviated):')
    for i in range(7):
        day_num = i + 1
        day = getattr(locale, 'DAY_{0}'.format(day_num))
        ab_day = getattr(locale, 'ABDAY_{0}'.format(day_num))
        print('\tDay: {0}, name: {1}, abbreviated: {2}'.format(
            day_num, locale.nl_langinfo(day), locale.nl_langinfo(ab_day)
        ))


def month_names():
    print('Month names (full and abbreviated):')
    for i in range(12):
        mon_num = i + 1
        mon = getattr(locale, 'MON_{0}'.format(mon_num))
        ab_mon = getattr(locale, 'ABMON_{0}'.format(mon_num))
        print('\tMonth: {0}, name: {1}, abbreviated: {2}'.format(
            mon_num, locale.nl_langinfo(mon), locale.nl_langinfo(ab_mon)
        ))


def main():
    loc_name = os.environ.get('SET_LOCALE')
    _init_locale(loc_name)
    numeric_convention_information()
    _spacer()
    date_and_time_formatting_information()
    _spacer()
    day_names()
    _spacer()
    month_names()


if __name__ == '__main__':
    main()
