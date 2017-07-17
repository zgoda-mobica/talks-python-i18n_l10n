# Let Your App Speak User's Language (i18n/l10n)

Python Talks: Let Your App Speak User's Language (i18n/l10n)

Introductory talk on i18n/l10n support in Python.

## `locale`

Basic localication support is provided by [locale module](https://docs.python.org/3/library/locale.html) which wraps ANSI C locale implementation. Actual support for various locale items depends on what is provided by operating system, the most complete and usually valid support is provided on Linux. Both Windows and OS X have long history of "embrace and extend" practices but support in latest versions is generally good (OS X > 10.5, Windows 10).

Changing locale can have side effects that should not be surprising, eg. changing `LC_CTYPE` affects formatting of floating point numbers in string objects, and changing `LC_TIME` affects date and time formatting operations with `strftime()`.

On Linux systems, locale information is limited to installed language support. To list installed locales run `locale -a`:

```shell
$ locale -a
C
C.UTF-8
en_AG
en_AG.utf8
en_AU.utf8
en_BW.utf8
en_CA.utf8
en_DK.utf8
en_GB.utf8
en_HK.utf8
en_IE.utf8
en_IN
en_IN.utf8
en_NG
en_NG.utf8
en_NZ.utf8
en_PH.utf8
en_SG.utf8
en_US.utf8
en_ZA.utf8
en_ZM
en_ZM.utf8
en_ZW.utf8
fr_BE.utf8
fr_CA.utf8
fr_CH.utf8
fr_FR.utf8
fr_LU.utf8
pl_PL.utf8
POSIX
ru_RU.utf8
ru_UA.utf8
```

In the above example I have installed complete sets of locales for English, French, Polish and Russian languages in UTF-8 script. `C` and `POSIX` are default fallback locales and are always available, when applying translation untranslated messages are returned. Full locale name consists of ISO 639-1 language name (eg. `en`), ISO 3166-1 territory specification (eg. `ZA`) and optionally script. Some territories have default script so the script name may be omitted from full locale name.

## `gettext`

Python has built-in support for translation provided by [`gettext`](https://www.gnu.org/software/gettext/) package. To be able to use any of these features, gettext support has to be enabled during compilation. All linux distributions have this feature enabled in default system Python instance but it depends on actual presence of shared libraries from gettext package which is not installed by default on most server instances. On Windows these features are always present but require independent installation of gettext.

Gettext translations are grouped into so-called "catalogs" that provide complete set of translated messages for particular language. The structure of message catalog allow for overriding parts of message set for different territories supported by application, for example one can have basic `de` translations for German language, with some messages overriden for `de_AT` (territory: Austria) or `de_DE` (territory: Germany). This allows to be as specific as developer needs, eg. when making localized application versions for different German-speaking countries. In my example I could make localized French versions for Belgium, Canada, Switzerland, France and Luxembourg or Russian for Russia and Ukraine.

### Plurals

Polish is not the most complicated language when it comes to plurals, although clearly stands out of the crowd by providing 3 forms when most languages have only 2. Russian for example has 3 forms too, but take a look and compare complexity of the formula.

Polish:

```javascript
nplurals=3; plural=(n==1 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2);
```

Russian:

```javascript
nplurals=3; plural=(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2);
```

Out of Slavic languages, only Slovenian has 4 forms:

```javascript
nplurals=4; plural=(n%100==1 ? 0 : n%100==2 ? 1 : n%100==3 || n%100==4 ? 2 : 3);
```

Apart of Slovenian and Bulgarian which has only 2 forms all other Slavic languages have 3 forms but the complexity of formula varies slightly. Other European languages that have 3 forms are eg. Romanian, Latvian and Lithuanian.

Cornish and other Gaelic languages have 4 forms:

```javascript
nplurals=4; plural=(n==1) ? 0 : (n==2) ? 1 : (n == 3) ? 2 : 3;  # Cornish
nplurals=4; plural=(n==1) ? 0 : (n==2) ? 1 : (n != 8 && n != 11) ? 2 : 3;  # Welsh
nplurals=4; plural=(n==1 || n==11) ? 0 : (n==2 || n==12) ? 1 : (n > 2 && n < 20) ? 2 : 3;  # Scottish Gaelic
```

Other European language that has 4 forms is Maltese:

```javascript
nplurals=4; plural=(n==1 ? 0 : n==0 || ( n%100>1 && n%100<11) ? 1 : (n%100>10 && n%100<20 ) ? 2 : 3);
```

From European languages Irish has most forms (5):

```javascript
nplurals=5; plural=n==1 ? 0 : n==2 ? 1 : (n>2 && n<7) ? 2 :(n>6 && n<11) ? 3 : 4;
```

This translates to human: "I have 5 forms numbered 0 to 4, for singular use form 0, for n == 2 use form 1, for n between 2 and 7 use form 2, for n between 7 and 11 use form 3 and for all other use form 4". In translation source file this looks as follows:

```text
#: /home/jazg/projects/talks-python-i18n_l10n/basic_gettext.py:25
#, python-format
msgid "Value %(num)d means singular"
msgid_plural "Value %(num)d means plural"
msgstr[0] ""
msgstr[1] ""
msgstr[2] ""
msgstr[3] ""
msgstr[4] ""
```

The only language that has more forms is Arabic (6):

```javascript
nplurals=6; plural=(n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : n%100>=3 && n%100<=10 ? 3 : n%100>=11 ? 4 : 5);
```

And of couse languages that do not have plural forms exist, eg. Georgian, native North Asian (Yakut, Uyghur) and almost all of East Asian languages. Chinese is specific in that it generally does not have plural form except when it comes to personal pronouns (eg. "We" vs. "I").

### Gettext examples

1. [Getting system information](sysinfo.py)
1. [Setting locale](set_locale.py)
1. [Locale L10N functions](locale_settings.py)
1. [Basic gettext translations](basic_gettext.py)

## Babel

[Babel](http://babel.pocoo.org/) is the most comprehensive and featureful i18n and l10n library for Python. It is based on [CLDR database](http://cldr.unicode.org/) of locale data, providing wider range of localization options than basic locale system that ships with linux systems, eg. in addition to country/territory names, the locale data also provides access to names of languages, scripts, variants, time zones, and more. Some of the data is closely related to number and date formatting. The availability of locale data provided by Babel is independent of system language support whereas `locale` provides only localization data for system-supported languages. This is specifically handy in case of web applications that at some point may provide l10n support for languages that are not installed in server environment.

### Spoken language stats

While CLDR contains some spoken language statistics for territories, this data can not be trated as scientific because it is only as accurate as possible at the time of CLDR publication. Current Babel version (2.4.0) uses data from CLDR v29 which was released Mar. 16 2016 while current CLDR is at v31 released Apr. 7 2017 (v31.0.1).

### Translations with Babel

Babel uses `gettext` to provide i18n support but its power is in tools that simplify working with message catalogs. Original `gettext` tools like `xgettext` or `msgfmt` work on file basis, which is perfect in Makefile-based projects, but it's real PITA when one has to manually compile list of files that contain translatable strings. Here `pybabel` program comes with great help:

```text
$ pybabel --help
Usage: pybabel command [options] [args]

Options:
  --version       show program's version number and exit
  -h, --help      show this help message and exit
  --list-locales  print all known locales and exit
  -v, --verbose   print as much as possible
  -q, --quiet     print as little as possible

commands:
  compile  compile message catalogs to MO files
  extract  extract messages from source files and generate a POT file
  init     create new message catalogs from a POT file
  update   update existing message catalogs from a POT file
```

Initialization workflow when using `pybabel`:

1. create `pybabel` configuration file that specifies mapping of message extractors and file types ([see example](scripts/babel.cfg))
1. `extract` messages into template file
1. `init` - initialize message catalog for specific locale from messages in template

Update workflow:

1. `extract` messages into template file
1. `update` message catalog applying any changes introduced in template
1. `compile` message catalog source into machine objects

Example workflow scripts are provided in [`scripts` directory of this project](scripts/).

### Babel examples

1. [Localized locale data](babel_locale.py)
1. [Date related functions](babel_dates.py)
1. [Number formats](babel_numbers.py)
1. [Miscellaneous data from CLDR](babel_misc.py)
1. [Localizing measurement units](babel_measures.py)
