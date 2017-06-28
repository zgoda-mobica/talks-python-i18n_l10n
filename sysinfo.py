import os
import locale


def _print_locale_info():
    loc = locale.getdefaultlocale()
    print('\tDefault locale: {0}, encoding: {1}'.format(*loc))
    loc = locale.getlocale()
    print('\tCurrent locale: {0}, encoding: {1}'.format(*loc))    


def bare_system_info():
    print('Bare (unitialized) system information:')
    _print_locale_info()


def clean_system_info():
    print('Locale explicitly set to "C" in environment:')
    os.environ['LANG'] = 'C'
    _print_locale_info()


def main():
    bare_system_info()
    clean_system_info()

if __name__ == '__main__':
    main()
