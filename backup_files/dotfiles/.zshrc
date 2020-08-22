# ~/.zshrc

# ----
# Path
# ----

export PATH="/usr/bin:$PATH";
export PATH="/usr/sbin:$PATH";
export PATH="$HOME/.local/bin:$PATH";
export PATH="/bin:$PATH";
export PATH="/sbin:$PATH";
export PATH="/usr/local/bin:$PATH";
export PATH="/usr/local/sbin:$PATH";
export PATH="$HOME/bin:$PATH";
export JAVA_HOME="/usr/lib/jvm/jdk-12.0.2";
export PATH="$JAVA_HOME/bin:$PATH";
export JAVA="/usr/lib/java/jre1.8.0_211";
export PATH="$JAVA/bin:$PATH";
export ZSH="$HOME/.oh-my-zsh"
export GEM_HOME="$HOME/gems"
export PATH="$HOME/gems/bin:$PATH"
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# ----------------
# Oh My Zsh Config
# ----------------

# Source to git-prompt
source $HOME/zsh-git-prompt
PROMPT='%B%m%~%b$(git_super_status) %# '

# Theme
ZSH_THEME="agnoster"

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion. Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to automatically update without prompting.
# DISABLE_UPDATE_PROMPT="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files under VCS as dirty.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time stamp shown in the history command output.
# You can set one of the optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd".
HIST_STAMPS="yyyy-mm-dd"

# -----------------
# Oh My Zsh Plugins
# -----------------

plugins=(git git-prompt zsh-syntax-highlighting zsh-autosuggestions zsh-256color)
source $ZSH/oh-my-zsh.sh

# -------
# ALIASES
# -------

# Nove de Julho
alias ndj-on='cd ~/Documents/Github/novedejulho && source bin/activate' # Activate Nove de Julho
alias ndj-off='cd ~/Documents/Github/novedejulho && deactivate $$ cd ~' # Deactivate Nove de Julho

# ls and grep (some with color support)
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

# Fixing debconf/config.dat error
alias fuserkill='sudo fuser -v -k /var/cache/debconf/config.dat'

# ---------
# FUNCTIONS
# ---------

# Mkenv: creates a folder with environment named .env
function mkenv() {
    cd ~/Documents/Github/ && mkdir $1 && cd $1 && python -m virtualenv .env
}
