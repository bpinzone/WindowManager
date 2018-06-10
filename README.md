# WindowManager
Save the position and size of your application windows to restore them later. <br />

TODO:<br />
Change grab->save<br />
Change set->move<br />

One might put the following in their bash_profile<br />

alias sw="grab_windows $1"<br />
alias mw="set_windows $1"<br />
alias swe="grab_windows_e $1"<br />
alias mwe="set_windows_e $1"<br />

function grab_windows {<br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cd <path to python files><br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python ./grab.py $1<br />

}<br />

function grab_windows_e {<br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;grab_windows $1<br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exit<br />
}<br />

function set_windows {<br />
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cd <path to python files><br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python ./set.py $1<br />
}<br />
function set_windows_e {<br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set_windows $1<br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exit<br />
}<br />