import os
import locale
import gettext

from utils import _init_locale, _spacer


def basic_translated_text():
    lang, _ = locale.getlocale()
    print('Basic translated text for language {0}:'.format(lang))
    t = gettext.translation('basic_gettext', 'locale', languages=[lang], fallback=True)
    _ = t.gettext
    print(_('This text will be translated'))


def plurals():
    lang, _ = locale.getlocale()
    print('Translating plural values for language {0}:'.format(lang))
    t = gettext.translation('basic_gettext', 'locale', languages=[lang], fallback=True)
    ngettext = t.ngettext
    for num in (1, 2, 5, 10, 22, 100, 212):
        message = ngettext('Value %(num)d means singular', 'Value %(num)d means plural', num)
        print(message % {'num': num})


def main():
    loc_name = os.environ.get('SET_LOCALE')
    _init_locale(loc_name)
    basic_translated_text()
    _spacer()
    plurals()

if __name__ == '__main__':
    main()
