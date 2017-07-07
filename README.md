# Let Your App Speak User's Language (i18n/l10n)

Python Talks: Let Your App Speak User's Language (i18n/l10n)

Introductory talk on i18n/l10n support in Python.

Python has built-in support for both translation and localization provided by [`gettext`](https://www.gnu.org/software/gettext/) package. To be able to use any of these features, gettext support has to be enabled during compilation. All linux distributions have this feature enabled in default system Python instance but it depends on actual presence of shared libraries from gettext package. On Windows these features are always present.

## `gettext`

Gettext translations are grouped into so-called "catalogs" that provide complete set of translated messages for particular language. The structure of message catalog allow for overriding parts of message set for different territories supported by application, for example one can have basic `de` translations for German language as spoken in Germany, with some messages overriden for `de_AT` (territory: Austria). This allows to be as specific as developer needs.

### Plurals

Polish is not the most complicated language when it comes to plurals, although clearly stands out of the crowd by providing 3 forms when most languages have only 2. Russian for example has 3 forms too, but take a look and compare complexity of the formula.

Polish:
```
nplurals=3; plural=(n==1 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2);
```

Russian:
```
nplurals=3; plural=(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2);
```

Out of Slavic languages, only Slovenian has 4 forms:
```
nplurals=4; plural=(n%100==1 ? 0 : n%100==2 ? 1 : n%100==3 || n%100==4 ? 2 : 3);
```

Apart of Slovenian and Bulgarian which has only 2 forms all other Slavic languages have 3 forms but the complexity of formula varies slightly. Other European languages that have 3 forms are eg. Romanian, Latvian and Lithuanian.

Cornish and other Gaelic languages have 4 forms:
```
nplurals=4; plural=(n==1) ? 0 : (n==2) ? 1 : (n == 3) ? 2 : 3;  # Cornish
nplurals=4; plural=(n==1) ? 0 : (n==2) ? 1 : (n != 8 && n != 11) ? 2 : 3;  # Welsh
nplurals=4; plural=(n==1 || n==11) ? 0 : (n==2 || n==12) ? 1 : (n > 2 && n < 20) ? 2 : 3;  # Scottish Gaelic
```

Other European language that has 4 forms is Maltese:
```
nplurals=4; plural=(n==1 ? 0 : n==0 || ( n%100>1 && n%100<11) ? 1 : (n%100>10 && n%100<20 ) ? 2 : 3);
```

From European languages Irish has most forms (5):
```
nplurals=5; plural=n==1 ? 0 : n==2 ? 1 : (n>2 && n<7) ? 2 :(n>6 && n<11) ? 3 : 4;
```

The only language that has more forms is Arabic (6):
```
nplurals=6; plural=(n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : n%100>=3 && n%100<=10 ? 3 : n%100>=11 ? 4 : 5);
```

And of couse languages that do not have plural forms exist, eg. Georgian, native North Asian (Yakut, Uyghur) and almost all of East Asian languages. Chinese is specific in that it generally does not have plural form except when it comes to personal pronouns (eg. "We" vs. "I").

### Examples

1. [Getting system information](sysinfo.py)
2. [Setting locale](set_locale.py)
3. [Locale L10N functions](locale_settings.py)
4. [Basic gettext translations](basic_gettext.py)

## Babel

[Babel](http://babel.pocoo.org/) is the most comprehensive and featureful i18n and l10n library for Python. It is based on [CLDR database](http://cldr.unicode.org/) of locale data, providing wider range of localization options than basic `gettext` that ships with linux systems, eg. in addition to country/territory names, the locale data also provides access to names of languages, scripts, variants, time zones, and more. Some of the data is closely related to number and date formatting. Availability of provided data is independent of system language support.

### Language data

While CLDR contains language data for territories, this data can not be trated as scientific because it is only as accurate as possible at the time of CLDR publication. Current Babel version (2.4.0) uses data from CLDR v29 which was released Mar. 16 2016 while current CLDR is at v31 released Apr. 7 2017 (v31.0.1).

### Translations with Babel

Babel uses `gettext` to provide i18n support but its power is in tools that simplify message extraction from source files.

### Examples

1. [Localized locale data](babel_locale.py)
2. [Date related functions](babel_dates.py)
3. [Number formats](babel_numbers.py)
4. [Miscellaneous data from CLDR](babel_misc.py)
5. [Localizing measures](babel_measures.py)
