# Introduction to Git and GitHub
Git is a distributed version control system for tracking changes in source code during software development with speed and efficiency.

## How to install Git on Ubuntu/Linux/Debian
```script
$ sudo apt update
$ sudo apt install git or 
$ sudo add-apt-repository ppa:git-core/ppa
$ sudo apt update
$ sudo apt install git
```

## Introduction to GitHub
GitHub is an American multinational corporation that provides hosting for software development and version control using Git. It offers the distributed version control and source code management (SCM) functionality of Git, plus its own features. It provides access control and several collaboration features such as bug tracking, feature requests, task management, continuous integration and wikis for every project.

## Tutorial: Getting started with Git and GitHub

Create a new repository  ("my-first-python-project") on GitHub and on local. Open the terminal and type the following commands:

```git
$ mkdir my-first-python-project
$ cd my-first-python-project
$ echo "# my-first-python-project" >> README.md
$ git init
$ git add README.md
$ git commit -m "first commit"
$ git remote add origin git@github.com:username/my-first-python-project.git or 
$ git remote add origin https://github.com/username/my-first-python-project.git	$ git push -u origin master 
Or push an existing repository from the command line
$ git remote add origin git@github.com:username/my-first-python-project.git or 
$ git remote add origin https://github.com/username/my-first-python-project.git
$ git push -u origin master
```

# References:
- [https://github.com/](https://github.com/)
- [https://en.wikipedia.org/wiki/GitHub](https://en.wikipedia.org/wiki/GitHub)
- [https://git-scm.com/docs/gittutorial](https://git-scm.com/docs/gittutorial)
- [https://git-scm.com/download/linux](https://git-scm.com/download/linux)
- [https://en.wikipedia.org/wiki/Git](https://en.wikipedia.org/wiki/Git)
- [https://www.cyberciti.biz/faq/what-does-sudo-apt-get-update-command-do-on-ubuntu-debian/](https://www.cyberciti.biz/faq/what-does-sudo-apt-get-update-command-do-on-ubuntu-debian/)
