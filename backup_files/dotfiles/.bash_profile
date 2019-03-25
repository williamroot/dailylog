# ~/.bash_profile

# -------------
# PROMPT SETUP
# -------------

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
txtblk="$(tput setaf 0 2>/dev/null || echo '\e[0;30m')"  # Black
txtred="$(tput setaf 1 2>/dev/null || echo '\e[0;31m')"  # Red
txtgrn="$(tput setaf 2 2>/dev/null || echo '\e[0;32m')"  # Green
txtylw="$(tput setaf 3 2>/dev/null || echo '\e[0;33m')"  # Yellow
txtblu="$(tput setaf 4 2>/dev/null || echo '\e[0;34m')"  # Blue
txtpur="$(tput setaf 5 2>/dev/null || echo '\e[0;35m')"  # Purple
txtcyn="$(tput setaf 6 2>/dev/null || echo '\e[0;36m')"  # Cyan
txtwht="$(tput setaf 7 2>/dev/null || echo '\e[0;37m')"  # White
bldblk="$(tput setaf 0 2>/dev/null)$(tput bold 2>/dev/null || echo '\e[1;30m')"  # Black
bldred="$(tput setaf 1 2>/dev/null)$(tput bold 2>/dev/null || echo '\e[1;31m')"  # Red
bldgrn="$(tput setaf 2 2>/dev/null)$(tput bold 2>/dev/null || echo '\e[1;32m')"  # Green
bldylw="$(tput setaf 3 2>/dev/null)$(tput bold 2>/dev/null || echo '\e[1;33m')"  # Yellow
bldblu="$(tput setaf 4 2>/dev/null)$(tput bold 2>/dev/null || echo '\e[1;34m')"  # Blue
bldpur="$(tput setaf 5 2>/dev/null)$(tput bold 2>/dev/null || echo '\e[1;35m')"  # Purple
bldcyn="$(tput setaf 6 2>/dev/null)$(tput bold 2>/dev/null || echo '\e[1;36m')"  # Cyan
bldwht="$(tput setaf 7 2>/dev/null)$(tput bold 2>/dev/null || echo '\e[1;37m')"  # White
undblk="$(tput setaf 0 2>/dev/null)$(tput smul 2>/dev/null || echo '\e[4;30m')"  # Black
undred="$(tput setaf 1 2>/dev/null)$(tput smul 2>/dev/null || echo '\e[4;31m')"  # Red
undgrn="$(tput setaf 2 2>/dev/null)$(tput smul 2>/dev/null || echo '\e[4;32m')"  # Green
undylw="$(tput setaf 3 2>/dev/null)$(tput smul 2>/dev/null || echo '\e[4;33m')"  # Yellow
undblu="$(tput setaf 4 2>/dev/null)$(tput smul 2>/dev/null || echo '\e[4;34m')"  # Blue
undpur="$(tput setaf 5 2>/dev/null)$(tput smul 2>/dev/null || echo '\e[4;35m')"  # Purple
undcyn="$(tput setaf 6 2>/dev/null)$(tput smul 2>/dev/null || echo '\e[4;36m')"  # Cyan
undwht="$(tput setaf 7 2>/dev/null)$(tput smul 2>/dev/null || echo '\e[4;37m')"  # White
bakblk="$(tput setab 0 2>/dev/null || echo '\e[40m')"  # Black
bakred="$(tput setab 1 2>/dev/null || echo '\e[41m')"  # Red
bakgrn="$(tput setab 2 2>/dev/null || echo '\e[42m')"  # Green
bakylw="$(tput setab 3 2>/dev/null || echo '\e[43m')"  # Yellow
bakblu="$(tput setab 4 2>/dev/null || echo '\e[44m')"  # Blue
bakpur="$(tput setab 5 2>/dev/null || echo '\e[45m')"  # Purple
bakcyn="$(tput setab 6 2>/dev/null || echo '\e[46m')"  # Cyan
bakwht="$(tput setab 7 2>/dev/null || echo '\e[47m')"  # White
txtrst="$(tput sgr 0 2>/dev/null || echo '\e[0m')" # Text Reset
cusgrn="$(tput setaf 36)$(tput bold)"
cuscyn="$(tput setaf 42)$(tput bold)"
cusblu="$(tput setaf 48)$(tput bold)"

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

# Initial info lines
echo ${cusgrn}"Operating system"${txtrst} ${bldwht}$(uname -o)${txtrst}
echo ${cusgrn}"Distribution"${txtrst} ${bldwht}$(lsb_release -d -s)${txtrst}
echo ${cusgrn}"Kernel"${txtrst} ${bldwht}$(uname -s -r)${txtrst}
echo ${cusgrn}"Processor arch"${txtrst} ${bldwht}$(uname -p)${txtrst}
echo ${cusgrn}"Uptime"${txtrst} ${bldwht}$(uptime -p)${txtrst}
echo ${cusgrn}"Date"${txtrst} ${bldwht}$(date "+%A, %d de %B de %Y, %R")${txtrst}

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

# Aliases for Python
alias python=python3
alias pip=pip3

# Aliases for Nove de Julho
alias ndj-on='cd ~/Documents/Github/novedejulho && source bin/activate' # Activate Nove de Julho
alias ndj-off='cd ~/Documents/Github/novedejulho && deactivate $$ cd ~' # Deactivate Nove de Julho

# Makeenv: function to create a folder with .env env
function mkenv() {
    cd ~/Documents/Github/
    mkdir $1
    cd $1
    virtualenv .env
}

# Color support of ls and grep
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# Some other aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Alert for long running commands.  Use like: $ sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Programmable completion features
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi
