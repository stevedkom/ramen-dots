from libqtile import hook, qtile
import subprocess
import os


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([home])


@hook.subscribe.layout_change
def toggle_term_opacity(layout, group):
    config = os.path.expanduser("~/.config/alacritty/alacritty.yml")

    if layout.name == "max":
        subprocess.call(["sed", "-i", "s/opacity:.*/opacity: 0/", config])
        subprocess.call(["sed", "-i", "s/size: 10/size: 12/", config])

    else:
        subprocess.call(["sed", "-i", "s/opacity:.*/opacity: 1/", config])
        subprocess.call(["sed", "-i", "s/size: 12/size: 10/", config])

