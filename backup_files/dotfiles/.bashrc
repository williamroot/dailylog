# ~/.bashrc

# Third-party codes:
# - The Fuck (https://github.com/nvbn/thefuck)
# - Git Aware Prompt (https://github.com/jimeh/git-aware-prompt)

# ------------
# PROMPT SETUP
# ------------

# Update path
export PATH="/usr/bin:$PATH";
export PATH="/usr/sbin:$PATH";
export PATH="$HOME/.local/bin:$PATH";
export PATH="/bin:$PATH";
export PATH="/sbin:$PATH";
export PATH="/usr/local/bin:$PATH";
export PATH="/usr/local/sbin:$PATH";
export PATH="$HOME/bin:$PATH";

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# Avoid duplicate lines or lines starting with space in the history
HISTCONTROL=ignoreboth

# Append to the history file instead of overwriting it
shopt -s histappend

# Number of lines or commands stored in memory in a history list while your bash session is ongoing
HISTSIZE=10000

# Ignore the maximum number of lines contained in the history file
HISTFILESIZE=

# Case-insensitive globbing (used in pathname expansion)
shopt -s nocaseglob

# Check the window size after each command and, if necessary, update the values of lines and columns
shopt -s checkwinsize

# Make less more friendly for non-text input files
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# Set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# Set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
    color_prompt=yes
    else
    color_prompt=
    fi
fi

# Colors (some cloned from Git Aware Prompt, some customized ones)
txtblk="$(tput setaf 0 2>/dev/null || echo '\e[0;30m')"
txtred="$(tput setaf 1 2>/dev/null || echo '\e[0;31m')"
txtgrn="$(tput setaf 2 2>/dev/null || echo '\e[0;32m')"
txtylw="$(tput setaf 3 2>/dev/null || echo '\e[0;33m')"
txtblu="$(tput setaf 4 2>/dev/null || echo '\e[0;34m')"
txtpur="$(tput setaf 5 2>/dev/null || echo '\e[0;35m')"
txtcyn="$(tput setaf 6 2>/dev/null || echo '\e[0;36m')"
txtwht="$(tput setaf 7 2>/dev/null || echo '\e[0;37m')"
bldblk="$(tput setaf 0 2>/dev/null)$(tput bold 2>/dev/null || echo '\e[1;30m')"
bldred="$(tput setaf 1 2>/dev/null)$(tput bold 2>/dev/null || echo '\e[1;31m')"
bldgrn="$(tput setaf 2 2>/dev/null)$(tput bold 2>/dev/null || echo '\e[1;32m')"
bldylw="$(tput setaf 3 2>/dev/null)$(tput bold 2>/dev/null || echo '\e[1;33m')"
bldblu="$(tput setaf 4 2>/dev/null)$(tput bold 2>/dev/null || echo '\e[1;34m')"
bldpur="$(tput setaf 5 2>/dev/null)$(tput bold 2>/dev/null || echo '\e[1;35m')"
bldcyn="$(tput setaf 6 2>/dev/null)$(tput bold 2>/dev/null || echo '\e[1;36m')"
bldwht="$(tput setaf 7 2>/dev/null)$(tput bold 2>/dev/null || echo '\e[1;37m')"
undblk="$(tput setaf 0 2>/dev/null)$(tput smul 2>/dev/null || echo '\e[4;30m')"
undred="$(tput setaf 1 2>/dev/null)$(tput smul 2>/dev/null || echo '\e[4;31m')"
undgrn="$(tput setaf 2 2>/dev/null)$(tput smul 2>/dev/null || echo '\e[4;32m')"
undylw="$(tput setaf 3 2>/dev/null)$(tput smul 2>/dev/null || echo '\e[4;33m')"
undblu="$(tput setaf 4 2>/dev/null)$(tput smul 2>/dev/null || echo '\e[4;34m')"
undpur="$(tput setaf 5 2>/dev/null)$(tput smul 2>/dev/null || echo '\e[4;35m')"
undcyn="$(tput setaf 6 2>/dev/null)$(tput smul 2>/dev/null || echo '\e[4;36m')"
undwht="$(tput setaf 7 2>/dev/null)$(tput smul 2>/dev/null || echo '\e[4;37m')"
bakblk="$(tput setab 0 2>/dev/null || echo '\e[40m')"
bakred="$(tput setab 1 2>/dev/null || echo '\e[41m')"
bakgrn="$(tput setab 2 2>/dev/null || echo '\e[42m')"
bakylw="$(tput setab 3 2>/dev/null || echo '\e[43m')"
bakblu="$(tput setab 4 2>/dev/null || echo '\e[44m')"
bakpur="$(tput setab 5 2>/dev/null || echo '\e[45m')"
bakcyn="$(tput setab 6 2>/dev/null || echo '\e[46m')"
bakwht="$(tput setab 7 2>/dev/null || echo '\e[47m')"
txtrst="$(tput sgr 0 2>/dev/null || echo '\e[0m')"
cusgrn="$(tput setaf 36)$(tput bold)"
cuscyn="$(tput setaf 42)$(tput bold)"
cusblu="$(tput setaf 48)$(tput bold)"

# Date and time
echo ${bldwht}$(date "+%A, %d de %B de %Y, %R")${txtrst}

# Function: Git Aware Prompt (for avoiding remote GAP file)
find_git_branch() {
  local branch
  if branch=$(git rev-parse --abbrev-ref HEAD 2> /dev/null); then
    if [[ "$branch" == "HEAD" ]]; then
      branch='detached*'
    fi
    git_branch="(working on ${bldblu}$branch${txtrst})"
  else
    git_branch=""
  fi
}

find_git_dirty() {
  local status=$(git status --porcelain 2> /dev/null)
  if [[ "$status" != "" ]]; then
    git_dirty="${bldblu}*${txtrst}"
  else
    git_dirty=""
  fi
}

PROMPT_COMMAND="find_git_branch; find_git_dirty; $PROMPT_COMMAND"

# Command prompt
if [ "$color_prompt" = yes ]; then
    PS1="${debian_chroot:+($debian_chroot)}\n\[${cusgrn}\]\u\[${txtrst}\] \[${txtwht}\]at\[${txtrst}\] \[${cuscyn}\]\h\[${txtrst}\] \[${txtwht}\]in\[${txtrst}\] \[${cusblu}\]\W\[${txtrst}\] \$git_branch\$git_dirty\n\[${txtwht}\]\$\[${txtrst}\] "
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# Use this if it is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# ---------------------
# FUNCTIONS AND ALIASES
# ---------------------

# The Fuck
eval $(thefuck --alias)

# Aliases for Python
alias python=python3
alias pip=pip3

# Aliases for Nove de Julho
alias ndj-on='cd ~/Documents/Github/novedejulho && source bin/activate' # Activate Nove de Julho
alias ndj-off='cd ~/Documents/Github/novedejulho && deactivate $$ cd ~' # Deactivate Nove de Julho

# Alias for Major Tom
alias majortom='ssh -i "majortom.pem" ubuntu@ec2-3-17-152-28.us-east-2.compute.amazonaws.com'

# Aliases for Privoxy
alias proxy-on='/etc/init.d/privoxy start'
alias proxy-off='/etc/init.d/privoxy stop'
alias proxy-restart='/etc/init.d/privoxy restart'
alias proxy-status='/etc/init.d/privoxy status'

# Mkenv: function to create a folder with environment named .env
function mkenv() {
    cd ~/Documents/Github/ && mkdir $1 && cd $1 && virtualenv .env
}

# Aliases for ls and grep (some with color support)
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Alert for long running commands.  Use like: $ sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# ---------------
# BASH COMPLETION
# ---------------

if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi
if [ $TILIX_ID ] || [ $VTE_VERSION ] ; then source /etc/profile.d/vte.sh; fi # Ubuntu Budgie END

