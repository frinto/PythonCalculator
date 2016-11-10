#README

How to use github in Pycharm or IntelliJ

---Initial setup----
1) Make sure you download git and install from https://git-scm.com/
2) Launch PyCharm and create a new project the location of the project doesnt matter as we going to clone and import the github project
3) Go to file > settings > Version Control > Github 
4) Enter your username and password of your github account into the fields. then hit apply and ok!
5) Next go to file > settings > Version Control > Git
6) specify the Path to Git executable that you installed earlier usually it is C:\Program Files\Git\cmd\git.exe
7) hit apply and ok

---Cloning---
cloning is the process of grabbing the git repository that contains the source code and everything else onto a local machine
Once it has been cloned a person can work on the cloned source code and push and pull changes to the server.

8)go to VCS> Checkout From Version Control> Github
9)Select folder to save to.

---Git commands---
10) after making changes to the source code right click then go to Git> Commit File
note that 'commit file' is basically applying those changes to the file, it doesnt mean that the file has been uploaded to github yet
in order to do that u will need to push the changes
11)in order to Push the changes go to VCS > Git > Push
12)now that u pushed the changes to the server we should all see it
13)now that its on the server the other person on the other end can "Pull" those changes down from the server and start working on it.
14)in order to pull go to VCS > Git > Pull

nows thats github in a nutshell there are some advance stuff like branches but thats kinda complicated xD



