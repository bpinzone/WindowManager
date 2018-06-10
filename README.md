# WindowManager
Save the position and size of your application windows to restore them later. 

TODO:
Change grab->save
Change set->move

One might put the following in their bash_profile

alias sw="grab_windows $1"
alias mw="set_windows $1"
alias swe="grab_windows_e $1"
alias mwe="set_windows_e $1"

function grab_windows {
        cd <path to python files>
        python ./grab.py $1

}

function grab_windows_e {
        grab_windows $1
        exit
}

function set_windows {
        cd <path to python files>
        python ./set.py $1
}
function set_windows_e {
        set_windows $1
        exit
}