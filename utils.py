import locale


def _print_locale_info():
    loc = locale.getdefaultlocale()
    print('\tDefault locale: {0}, encoding: {1}'.format(*loc))
    loc = locale.getlocale()
    print('\tCurrent locale: {0}, encoding: {1}'.format(*loc))


def _spacer(length=80):
    print('=' * length)


def _init_locale(locale_name=None):
    if locale_name is None:
        locale_name = ''
    locale.resetlocale()
    locale.setlocale(locale.LC_ALL, locale_name)
