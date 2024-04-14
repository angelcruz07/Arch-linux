# Qtile Config File
# http://www.qtile.org/

from libqtile import  hook
from libqtile.lazy import lazy

#Configs
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.widgets import widget_defaults, extension_defaults
from settings.screens import screens
from settings.keys import mod, keys, terminal
from settings.mouse import mouse
from settings.path import qtile_path

from os import path
import subprocess


@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])


main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = 'urgent'
wmname = 'LG3D'

# dgroups_key_binder = None
# dgroups_app_rules = []  # type: list
# follow_mouse_focus = True
# bring_front_click = False
# floats_kept_above = True
# cursor_warp = False
# auto_fullscreen = True
# focus_on_window_activation = 'urgent'
# reconfigure_screens = True
# # If things like steam games want to auto-minimize themselves when losing
# auto_minimize = True
# # When using the Wayland backend, this can be used to configure input devices.
# wl_input_rules = None
# # java that happens to be on java's whitelist.
# wmname = "LG3D"
