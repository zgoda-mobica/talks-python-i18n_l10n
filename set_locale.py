import os
import locale

from utils import _print_locale_info, _spacer


def set_locale_system_default():
    print('Setting locale using defaults only')
    print('1. Reset locale to default')
    locale.resetlocale()
    _print_locale_info()
    print('2. Set locale to system default')
    locale.setlocale(locale.LC_ALL, '')
    _print_locale_info()


def set_locale_with_env_reset():
    print('Setting locale with environment set to "C"')
    os.environ['LANG'] = 'C'
    print('1. Reset locale to default')
    locale.resetlocale()
    _print_locale_info()
    print('2. Set locale to system default')
    locale.setlocale(locale.LC_ALL, '')
    _print_locale_info()
    print('3. Set locale to one of supported locales')
    locale.resetlocale()
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    _print_locale_info()
    print('4. Set locale to one of unsupported locales')
    locale.resetlocale()
    locale.setlocale(locale.LC_ALL, 'de_AT.UTF-8')
    _print_locale_info()


def main():
    set_locale_system_default()
    _spacer()
    set_locale_with_env_reset()

if __name__ == '__main__':
    main()
