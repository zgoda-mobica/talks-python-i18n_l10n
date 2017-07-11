name: title
class: center, middle

# Let your App Speak User's Language

## Python l10n/i18n primer

.left[
```text
Jarek Zgoda
<jaroslaw.zgoda@mobica.com>
```
]

---

name: intro

.center[# Localization and Internationalization]

Names coined by DEC in late 70's

<dl>
    <dt>Internationalization (i18n)</dt>
    <dd>The process of designing a software application so that it can potentially be adapted to various languages and regions without engineering changes.</dd>

    <dt>Localization (l10n)</dt>
    <dd>The process of adapting internationalized software for a specific region or language by adding locale-specific components and translating text.</dd>
</dl>

.center[## Other names]

* globalization (g11n) - IBM, Sun Microsystems
* localizability (l12y) - Microsoft
* national/native language support (NLS) - Hewlett-Packard

---

name: base-tools

.center[# Basic tools for l10n and i18n]

* `locale` to work with system localization settings
  - locale can be set to any that is installed in the system
  - in program change of locale is limited to process scope
* `gettext` to provide translated texts

---

name: locale

.center[# Locale support]

* built in
* locale data has to be provided by OS
* most of basic data is localized, eg. month and day names or numeric formats

---

name: gettext

.center[# Gettext support]

* built in
* requires external support library (already present on all Linux desktop systems)
* use external tools to extract and compile messages into _machine objects_

---

name: babel

.center[# Babel library]

* installed from PyPI
* independent of system provided locale data
* based on Unicode Constortium's Common Language Data Repository (CLDR)
* full range of localization data and functions:
  - numeric formats
  - date formats
  - currency, territory, language, measurement unit names

---

name: babel-tools

.center[# Babel translation tools]

* greatly simplify work with message catalogs
* project oriented, full Python support
* message extraction functions for web template systems
* support libraries for popular web frameworks (Flask, Django, Pylons)
