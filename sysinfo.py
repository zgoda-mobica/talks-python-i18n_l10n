import os

from utils import _print_locale_info, _spacer


def bare_system_info():
    print('Bare (unitialized) system information:')
    _print_locale_info()


def clean_system_info():
    print('Locale explicitly set to "C" in environment:')
    os.environ['LANG'] = 'C'
    _print_locale_info()


def main():
    bare_system_info()
    _spacer()
    clean_system_info()

if __name__ == '__main__':
    main()
