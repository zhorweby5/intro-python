# 2025-04-20

## Beege Rule 1# Errors are our friend!

## Getting Started

* 1. ls: Check existing library
* 2. cd projects/
* 3. intro-python-to see what is inside type( vim ./intro-python)
* 4. vim ./intro-python/README.md
  or if already in vim
* 5. :e ./intro-python/README.md

## Coding Terms/Concepts

* .  = current folder (don't edit yet)
* .. = parent directory (don't edit yet either)
* project
* dependencies
* python=programming language that uses code shorthand words & symbols  to interpret code
* uva=virtual environment to experiment with code that could potentially harm other computer files.
## Keyboard shortcuts

* command tab: switch programs
* command c: copy
* command q: quit running program
* command v:  paste
* command t: new tab chrome/terminal only
* command w: closes current tab chrome/terminal only

## Vim

* I: Insert Mode (--Insert on bottom)
* O: O in Command mode= Insert + add new line
* Escape Key (Leave Insert Mode and Enter Command Mode)
* Save and Quit (In Command Mode, Type :wq)

## First Python File

* Bash-Shell Program (Helps User operate the computer safely)
* Shell is Command Line Interface
* How to tell Bash to run Python Program
  * Use Shebang Line (#!/..)
    * For Python programs, you generally want to use this: `#!/usr/bin/env python`
  * Run File with another Program installed
  * /usr/bin/env Searches for another program somewhere on the computer (python)
  * Env finds the file for user

## Running Python Program

* in your Python file:
  * Make sure the very first line is your shebang
  * Add some newlines for cleanliness/readability (read as, not really required)
  * To print "hello world" to the screen, write the Python code: `print("hello world")`
* back in the Terminal:
  * `chmod u+x file.py`:  add execute permissions for the owning user on file.py
  * `./file.py` ---- run the file, where the file is named file.py
* Change code: return to vim file, click insert, change written code,
 and then enter code again in bash

##  Git

* Source Control-Avoid the headache of final version mixups, Multiple versions of the same file management, experiment with different versions, accountability of the file (who, what, when, where)
collaboration, safety reasons
Safety-storage on multiple computers
*  One tool 
*  Most popular Git
*  One database, easily duplicated and command line utility
*  Git allows commits of data, so that you can commit a file to history-repository
*  Branches-join, experiment, and change stored files from any point in committed history
*  Remotes-different copies of the same repository making changes to each other
*  Tags: The labels for a commit you create
*  git status
*  git add
*  gitignore
*  git reset
 ##  How to make a git file

 *  start with git init
 *  then git status
 *  after checking git status, type in required git config to set up email, name
 *  git add
 *  git commit -m [commit message]
 *  git status to check master branch

 ##  Create a branch

 *  Type in git branch to see existing commands
 *  Type git checkout -b (enter branch name) to create a new branch

# 2025-04-24

## LESSON 1 

## docs.astral.sh##

## Python Basics

* project-configure
* dependencies-install someone else's code, make your own project using someone else's code
* a-pip=old, slow
* uv=reliable way to make dependencies

## Getting started with uv
* installing uv
* curl= is dangerous
* download, then look first
* uv init .

## pyproject.toml

* track dependencies=makes transferring from computers better

* uv add <package name> (minus the <>s)

-for entire python package

* python: virtual environment

## install dependencies to virtual environment first

##.venv

* ls -a to see .venv
* dont't touch the lock file
* lock file: requests 2.32.3-used for security functions
* lock file should be in git
* Do not include uv in git
* Do not commit .venv

## .gitignore (then commit)

* Have git ignore your virtual environment folder.
* 1. touch .gitignore
* 2. vim gitignore
* 3. uv init (projectname) = creates folder git repository to gitignore

## .gitignore

* type  .venv
* gitignore will ignore that folder
* ls  
* 1. .gitignore
* 2.  .venv
* 3.  :wq 

## check git status

do not use this in vsc all the time
familiarize yourself with vim

##  vsc sidebar
*  staged shortcut: add these 
*  .gitignore
*  python-version
*  pyproject.toml
*  uv.

* if you dont have vsc
* git add (manually)
* 1.  git add (type all the names with spaces) and press enter
* 2. commit -m "uv config"
* 3. git push

git push-adds dependency

##vim hello.py##

##  Purpose: Activate Virtual Environment

* To activate your virtual environment, run `source .venv/bin/activate`
* if your virtual environment is active, you'll see "(intro-python)" at the beginning of your line on Terminal
* personal virtual is active which python to check

* type ./hello.py ,and enter
* Success!... you succesfully downloaded google home page in html code but

## Beege Rule 1# Errors are our Friend
*  You learn from errors, bad results doing it right  are worse than doing something wrong and reading fatal!

* Now Make an Error
* Enter vim hello.py
* in the vim delete or modify google.com 
* :wq 
* then enter ./ hello.py in command terminal
* fatal error will occur

## Google homepage code (Web Development Concepts)

*  Why does it look like that?
*  Uglification= makes the code longer and obfuscates for readibility/security  concerns
*  Minification= reduce code to the fewest characters possible

## Coding Git Sequence Start
*  git status
*  git init
*  git status
*  git add
*  git push
*  git log

## April 27 Homework:
Coding Start
Friday Homework
add cowsay dependency
 and make the cow say something
and import to python
send through github

Process
1. Attempted to Install Cowsay using pip install cowsay
2. Attempted to us git, uv init but went down wrong pathway
3. Created a folder known as cowsay
4. Almost git added cowsay
5. Realized efforts in wrong direction
6. Used Chatgpt to find out
7. brew install cowsay
8. cowsay Moo, BaaBaa, quam lavatio fecit
9. Save, git added, and committed changes to my progress
10. Created a New Repository on Github =Cowsay Numba 1


Correct Method of Installing Cowsay 2025-04-26- Beege

1. Be in the project folder, type ls 
2. type cd intro-python
3. uv add (package name) = package is using other people's code
4. uv add cowsay (add the package into the existing project) 
5. import cowsay
6. cowsay.cow('Hello World')
7. print(cowsay.get_output_string('cow', 'Hello World))

cd=change directory =makes an argument to open a file
Arguments=add new information to an existing file
When one file "talks" to another file, it is an argument
TO find certain files you need to write cd (file name) 
suc as cd intro-python
