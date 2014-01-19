#!/bin/bash
#
# simple console util for translation text to any language using Yandex Translate API
# use: Translate.sh ru 'call me, baby'
# will return translation of a phrase to ru language
# more example at http://api.yandex.ru/translate/
#

to=$1
text=$2

link='https://translate.yandex.net/api/v1.5/tr.json/translate?key='
key='-- key from http://api.yandex.ru/key/keyslist.xml --'

curl -s "$link$key&lang=$to&text=$text" | awk -F'"' {' print $10 '}
