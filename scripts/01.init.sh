#! /bin/bash

CFGFILE="babel.cfg"
LOCALEDIR="../locale"
TEMPLATEFILE="$LOCALEDIR/messages.pot"
CODEDIR="$HOME/projects/talks-python-i18n_l10n"
LANGUAGES=("de" "it" "es" "ga")

# -k extracts additionally strings marked by `lazy_gettext()` function from Flask-Babel
pybabel extract -F $CFGFILE -k lazy_gettext -o $TEMPLATEFILE $CODEDIR

for language in "${LANGUAGES[@]}"
do
	pybabel init -i $TEMPLATEFILE -d $LOCALEDIR -l $language
done
