#! /bin/bash

CFGFILE="babel.cfg"
LOCALEDIR="../locale"
TEMPLATEFILE="$LOCALEDIR/messages.pot"
LANGUAGES=("de" "it" "es")

# -k extracts additionally strings marked by `lazy_gettext()` function from Flask-Babel
pybabel extract -F $CFGFILE -k lazy_gettext -o $TEMPLATEFILE ../

for language in "${LANGUAGES[@]}"
do
	pybabel init -i $TEMPLATEFILE -d $LOCALEDIR -l $language
done
