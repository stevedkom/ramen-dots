#! /bin/bash

eww close-all
firefox --new-tab $1
qtile cmd-obj -o group a -f toscreen
