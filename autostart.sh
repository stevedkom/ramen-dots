#!/bin/sh

feh --bg-fill ~/Pictures/wallpapers/ramen-light.png

picom --experimental-backends & disown

dunst & disown

xss-lock --transfer-sleep-lock -- ~/.config/eww/scripts/lock.sh & disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME
