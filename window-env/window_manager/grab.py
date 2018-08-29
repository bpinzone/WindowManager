"""
Get the window settings and push them into the json file.
"""

import sys
from shell import shell
from os import remove
from os import system
from os.path import isfile
import json
from tools import *


def grab_apple(app, preset_number):

    # read  file
    apps_pos_d = get_pos_dict()
    commands = [
        "tell application \"{}\"".format(app),
        "get bounds of the front window",
        "end tell"
    ]

    # generate command
    apple_script_cmd = generate_apple_script(commands)

    # run get command
    get_cmd_out = "{" + shell(apple_script_cmd).output()[0] + "}"

    key = "{}_{}".format(app, preset_number)
    apps_pos_d[key] = get_cmd_out

    # override position file.
    write_pos_file(apps_pos_d)


def grab_Wunderlist(preset_number):
    apps_pos_d = get_pos_dict()

    # get position
    commands = [
        "tell application \"Wunderlist\" to activate",
        "tell application \"System Events\" to tell process \"Wunderlist\"",
        "get position of window 1",
        "end tell"
    ]
    apple_script_cmd = generate_apple_script(commands)
    get_cmd_out = shell(apple_script_cmd).output()[0]

    x_y = [int(dim) for dim in get_cmd_out.split(",")]

    # get size
    commands = [
        "tell application \"Wunderlist\" to activate",
        "tell application \"System Events\" to tell process \"Wunderlist\"",
        "get size of window 1",
        "end tell"
    ]
    apple_script_cmd = generate_apple_script(commands)
    get_cmd_out = shell(apple_script_cmd).output()[0]

    w_h = [int(dim) for dim in get_cmd_out.split(",")]

    # export data
    wunderlist_data = {
        "x": x_y[0],
        "y": x_y[1],
        "w": w_h[0],
        "h": w_h[1]
    }

    key = "Wunderlist_{}".format(preset_number)
    apps_pos_d[key] = wunderlist_data

    write_pos_file(apps_pos_d)


def grab_Discord(preset_number):
    apps_pos_d = get_pos_dict()

    # get position
    commands = [
        "tell application \"Discord\" to activate",
        "tell application \"System Events\" to tell process \"Discord\"",
        "get position of window 1",
        "end tell"
    ]
    apple_script_cmd = generate_apple_script(commands)
    get_cmd_out = shell(apple_script_cmd).output()[0]

    x_y = [int(dim) for dim in get_cmd_out.split(",")]

    # get size
    commands = [
        "tell application \"Discord\" to activate",
        "tell application \"System Events\" to tell process \"Discord\"",
        "get size of window 1",
        "end tell"
    ]
    apple_script_cmd = generate_apple_script(commands)
    get_cmd_out = shell(apple_script_cmd).output()[0]

    w_h = [int(dim) for dim in get_cmd_out.split(",")]

    # export data
    wunderlist_data = {
        "x": x_y[0],
        "y": x_y[1],
        "w": w_h[0],
        "h": w_h[1]
    }

    key = "Discord_{}".format(preset_number)
    apps_pos_d[key] = wunderlist_data
    write_pos_file(apps_pos_d)


def grab_Spotify(preset_number):
    apps_pos_d = get_pos_dict()

    # Get position
    commands = [
        "tell application \"Spotify\" to activate",
        "tell application \"System Events\"",
        "tell process \"Spotify\" to get first window",
        "set spotify_window to result",
        "get position of spotify_window",
        "end tell"
    ]
    apple_script_cmd = generate_apple_script(commands)
    get_cmd_out = shell(apple_script_cmd).output()[0]

    x_y = [int(dim) for dim in get_cmd_out.split(",")]

    #  Get Size
    commands = [
        "tell application \"Spotify\" to activate",
        "tell application \"System Events\"",
        "tell process \"Spotify\" to get first window",
        "set spotify_window to result",
        "get size of spotify_window",
        "end tell"
    ]
    apple_script_cmd = generate_apple_script(commands)
    get_cmd_out = shell(apple_script_cmd).output()[0]

    w_h = [int(dim) for dim in get_cmd_out.split(",")]

    # export data
    spotify_data = {
        "x": x_y[0],
        "y": x_y[1],
        "w": w_h[0],
        "h": w_h[1]
    }

    key = "Spotify_{}".format(preset_number)
    apps_pos_d[key] = spotify_data

    write_pos_file(apps_pos_d)


def main(preset_number):

    #load config from file
    app_config_d = {}
    load_dict_from_file(CONFIG_FILE, app_config_d)

    running_apps = get_running_apps()

    # get each app.
    for app in app_config_d:

        if app not in running_apps:
            continue
        if app_config_d[app]['isApple']:
            grab_apple(app, preset_number)
        else:
            # get the local symbole table, get the function by its name, and call it.
            globals()['grab_' + app](preset_number)


if __name__ == "__main__":
    assert(len(sys.argv) == 2)
    main(sys.argv[1])
