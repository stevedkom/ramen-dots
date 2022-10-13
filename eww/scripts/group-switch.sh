#! /usr/bin/bash

eww close-all
GROUP=`qtile cmd-obj -o screen -f items -a group | awk '{print $2}' | tr -d "[]'()"`
eww update WS_CURRENT=$GROUP
#qtile cmd-obj -o group scratch -f hide_all
