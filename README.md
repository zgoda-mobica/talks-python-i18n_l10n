# Let Your App Speak User's Language (i18n/l10n)

Python Talks: Let Your App Speak User's Language (i18n/l10n)

Introductory talk on i18n/l10n support in Python.

## gettext

### Plurals

Polish is not the most complicated language when it comes to plurals, although clearly stands out of the crowd by providing 3 forms when most languages has only 2. Russian for example has 3 forms too, but take a look and compare complexity of the formula.

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

## Babel

[Babel](http://babel.pocoo.org/) is the most comprehensive and featureful i18n and l10n library for Python. It is based on [CLDR database](http://cldr.unicode.org/) of locale data, providing wider range of localization options than basic `gettext` that ships with linux systems, eg. in addition to country/territory names, the locale data also provides access to names of languages, scripts, variants, time zones, and more. Some of the data is closely related to number and date formatting. Availability of provided data is independent of system language catalogs.
