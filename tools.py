from os import system
from os import popen
from os.path import isfile
from shell import shell
import json


CONFIG_FILE = './app_config.json'
POS_FILE = './apps_pos.json'


def get_running_apps():
    command = generate_grep_app_search_cmd()
    open_apps = set(popen(command).read().replace(".app", "").split("\n"))
    return open_apps


def get_pos_dict():
    apps_pos_d = {}
    try:
        load_dict_from_file('apps_pos.json', apps_pos_d)
    except json.JSONDecodeError:
        print("No settings")
    return apps_pos_d


def write_pos_file(dict):
    pos_file = open(POS_FILE, 'w')
    pos_file.truncate()
    pos_file.write(json.dumps(dict))
    pos_file.close()


def generate_grep_app_search_cmd():

    app_config_d = {}
    load_dict_from_file(CONFIG_FILE, app_config_d)

    #  list processes
    command = "ps aux | grep "

    # find app processes
    for app in app_config_d.keys():
        command += "-e \"{}.app\" ".format(app)

    # filter forbidden
    command += "| grep -e \"grep\" "
    for app in app_config_d.keys():
        if "forbidden_apps" in app_config_d[app]:
            for f_app in app_config_d[app]["forbidden_apps"]:
                command += "-e \"{}.app\" ".format(f_app)
    command += " -v "
    command += "| grep '[A-Za-z]*\.app' -o"

    # Well that was fun.
    return command


def load_dict_from_file(file_name, dict):
    """
    file_name must be a relative path from the WindowManager folder.
    Loads the file into the dict.
    If the file doesn't exist, does nothing.
    """
    if isfile(file_name):
        file = open(file_name, 'r')
        dict.clear()
        dict.update(json.load(file))
        file.close()


def generate_apple_script(commands):
    """Commands is a list of strings"""
    script = "osascript "
    for command in commands:
        script += "-e '{}' ".format(command)
    return script


def app_is_running(app):
    commands=[
        "set targetApp to \"{}\"".format(app),
        "tell application \"System Events\"",
        "set appExists to exists process targetApp",
        "end tell"
    ]

    script = generate_apple_script(commands)
    print(script)
