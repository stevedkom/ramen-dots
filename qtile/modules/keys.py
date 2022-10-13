from libqtile.lazy import lazy
from libqtile.config import Key
import os

mod = "mod4"
terminal = "alacritty"


## Helpers ##
def change_group(ws):
    return [lazy.spawn("eww close-all"),
            lazy.spawn("eww update WS_CURRENT=" + ws),
            lazy.group["scratch"].hide_all(),
            lazy.group[ws].toscreen(),
            lazy.spawn(os.path.expanduser("~/.config/eww/scripts/ws-notify.sh"))]

@lazy.function
def eww_group(qtile, dir):
    groups = {"a": {"prev": "f", "next": "s"},
              "s":  {"prev": "a", "next": "d"},
              "d":  {"prev": "s", "next": "f"},
              "f":  {"prev": "d", "next": "a"}}
    for k, v in qtile.cmd_groups().items():
        if v['screen'] == 0:
            qtile.cmd_spawn("eww close-all")
            qtile.cmd_spawn("eww update WS_CURRENT=" + groups[k][dir])

def dropdown(name):
    return [lazy.group['scratch'].hide_all(),
            lazy.group["scratch"].dropdown_toggle(name),
            lazy.spawn(os.path.expanduser("~/.config/eww/scripts/dropdown-status.sh"))]

## Bindings ##
keys = [
    # Direct switch groups
    Key([mod], "a", *change_group("a")),
    Key([mod], "s", *change_group("s")),
    Key([mod], "d", *change_group("d")),
    Key([mod], "f", *change_group("f")),
    # Move window to group
    # Add widget closing code here
    Key([mod, "shift"], "a",
        lazy.window.togroup("a"), *change_group("a")),
    Key([mod, "shift"], "s",
        lazy.window.togroup("s"), *change_group("s")),
    Key([mod, "shift"], "d",
        lazy.window.togroup("d"), *change_group("d")),
    Key([mod, "shift"], "f",
        lazy.window.togroup("f"), *change_group("f")),
    # Switch windows
    Key([mod], "h", lazy.layout.previous()),
    Key([mod], "l", lazy.layout.next()),
    # Switch workspaces
    Key([mod], "k", eww_group("prev"),
        lazy.screen.prev_group(), lazy.group['scratch'].hide_all(),
        lazy.spawn(os.path.expanduser("~/.config/eww/scripts/ws-notify.sh"))),
    Key([mod], "j", eww_group("next"),
        lazy.screen.next_group(), lazy.group['scratch'].hide_all(),
        lazy.spawn(os.path.expanduser("~/.config/eww/scripts/ws-notify.sh"))),
    # Shuffle windows
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "semicolon", lazy.layout.swap_main()),
    # Grow windows
    Key([mod, "control"], "j", lazy.layout.grow()),
    Key([mod, "control"], "k", lazy.layout.shrink()),
    Key([mod, "control"], "h", lazy.layout.shrink_main()),
    Key([mod, "control"], "l", lazy.layout.grow_main()),
    Key([mod, "control"], "semicolon", lazy.layout.normalize()),
    # Toggle layouts
    Key([mod], "Tab", lazy.next_layout()),
    # Kill window
    Key([mod], "Escape", lazy.window.kill()),
    # Qtile
    Key([mod, "shift", "control"], "r", lazy.restart()),
    Key([mod, "shift", "control"], "q", lazy.shutdown()),
    # Media and Brightness
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("amixer -D pulse set Master 5%+ unmute")),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("amixer -D pulse set Master 5%- unmute")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -D pulse set Master toggle")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight +10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -10")),
    # Dedicated app keys and dropdowns
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "space", lazy.spawn(os.path.expanduser("~/.config/rofi/launcher.sh"))),
    Key([mod, "shift"], "space",
        lazy.spawn("rofi -show combi -modes combi,ssh")),
    Key([mod], "t", *dropdown("term")),
    Key([mod], "r", *dropdown("ranger")),
    Key([mod], "p", *dropdown("sysmon")),
    Key([mod], "i",
        lazy.group['scratch'].hide_all(),
        lazy.group["scratch"].dropdown_toggle("wifi"),
        lazy.spawn(os.path.expanduser("~/.config/eww/scripts/wifi-bg.sh"))),
    # Eww should have a script that would make it easy to toggle with 1 key
    Key([mod], "w", lazy.spawn(os.path.expanduser("~/.config/eww/scripts/launch-control.sh"))),
    Key([mod], "q", lazy.group['scratch'].hide_all(), lazy.spawn("eww close-all")),
    # Extra keys to deal with floating windows, in case the mouse move and
    # resize are not enough. The center will get called both times, but if the
    # window was toggled to tile it will do nothing. Better to have an if, but
    # then I would need a hook and not sure yet how I would want to set that up
    Key([mod], "m", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "m", lazy.window.toggle_floating(), lazy.window.center()),
    # Logout
    Key([mod], "backslash",
        lazy.spawn(os.path.expanduser("~/.config/eww/scripts/lock.sh"))),
    Key([], "F11",
        lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/screenshot.sh"))),
]
