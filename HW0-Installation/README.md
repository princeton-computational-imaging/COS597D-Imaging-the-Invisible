# HW0: Environment setup for COS597

In this initial assignment, the goals are:

1. to set up a working programming environment using either conda environments.
2. to get acclimated to the "pull, commit, push" development cycle for git. This course's programming assignments will be submitted via Github (all free-response questions will be submitted via Canvas).
3. to get acclimated with Jupyter Lab, which is required for all assignments in this course.
4. to get familiar with Latex homework template, which will be used throughout the quarter.

**Please read through readme.md carefully**

**After setting up the assignment environment, please look into the Jupyter notebook (*.ipynb)**

**At the end, prepare a small report on Overleaf and submit the pdf to Canvas. Don't forget to PUSH your repository**

## Anaconda/Miniconda Environment Setup (Python Environment)

### Installation
This course uses **Python 3**. Python 2 will not work for these assignments, and all assignments will be graded with Python 3 on our end. Python 2 is [leaving the data science programming stack](https://pythonclock.org/) on Jan 1, 2020.

The easiest way to get set up is to use [**miniconda**](https://docs.conda.io/en/latest/miniconda.html). However, the full version of Anaconda is totally fine as well [**Anaconda**](https://docs.anaconda.com/anaconda/install/). I personally use Anaconda since it comes with a lot of functionality. Still, miniconda is the right environment for you if you have limited disk space.

Install the appropriate version of anaconda/miniconda for your operating system (select the Python 3 version). After miniconda is installed, you should be able to run `conda`. If you get an error (e.g. `-bash: conda: command not found`), make sure to source your bash file afterward (`source ~/.bash_profile` worked for Prem) or if on Windows, restart your terminal. For Windows you might need to use the "Anaconda prompt" to navigate with conda. 
It is not unheard of that people are experiencing problems installing conda on your platform. In that case, you might want to look in the system paths and replace the standard Python version with the anaconda path. Google (and stackoverflow) is also a great resource to get these problems sorted out.

### cos597 Environment
Now let's create a virtual environment. Virtual environments are a simple way to isolate all the dependencies for a particular project. They make it easy to work on multiple projects without them interfering with each other (e.g., conflicting versions of libraries between tasks). 

If you are new to CONDA please read through this article. It should really help you get started and understand better what this is all about
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

Now, let's get started setting everything up for 331. Here's the command:

``conda create -n COS597 python``

`COS597` is the name for the environment, and it can be used for all assignments. Its name can be whatever you want, just make sure to remember it! You can even use your *base* environment. However, we recommend using separate environments for different classes, projects, etc. 

Once the environment is created, you should activate it with:

``conda activate COS597``

Your shell/cmd/bash might look something like `(COS597) your folder/name`. The environment name is in parenthesis, indicating that it is active. If this is not the case, something likely went wrong. 

Now let's install a few packages that might come in useful throughout the course. Note that you might need to install more packages during the class. This is just a selection of packages we consider essential. You are free to install whatever package you might consider useful.

Do this by navigating to this folder's top root on the terminal and running, with your activated COS597 conda environment:

``pip install -r requirements.txt``

Note that we are installing many packages. This can take a while since all of those packages need to be downloaded first. If a package cannot be installed, you google to figure out what went wrong and install it manually.

Great! Your environment is all set up. You can check if those environments are correctly installed, by simply open an "ipython"-console and trying to import several of the packages in requirements.txt

## Git (Version Control)
We will use `git` for all code submissions in this class. New to `git`? Not to worry, it's quite easy! Here's a [helpful guide](https://guides.github.com/activities/hello-world/) or go through this more comprehensive [tutorial](https://git-scm.com/docs/gittutorial)

If you haven't installed GIT on your computer, please install it from [this link](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

To clone this repository, install GIT on your computer and copy the link of your assignment repository. Next, you might want to create a folder called `COS597` to download all future assignments in this quarter. Next, `cd` into this environment where you now should find an empty folder, if nothing is downloaded yet.

Now, you have to find the link to your assignment repository above on the github page in your browser at "Clone or Download". This link might be either an SSH or HTTPS link. I recommend setting up SSH keys on your computer, which should facilitate pushing and pulling your repositories using SSH ([Link 1](https://docs.github.com/en/enterprise/2.15/user/articles/adding-a-new-ssh-key-to-your-github-account),[Link 2](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh))

Once you've copied the link to your keyboard, enter the following into your command-line tool (for windows, this might be the Git Bash):

``git clone INSERT-YOUR-LINK-HERE``

Once cloned, `cd` into the cloned repository. Every assignment has some files that you edit to complete it.
The problems.md gives concise instructions on what do do, so please read this first. However, the most important part is the assignment.ipynb, the Jupyter Notebook will guide you through complete homework.

## Github development cycle

All assignments are submitted via Github in this class. Once you've accepted this assignment via the Github classroom link, it made a repository of the form `https://github.com/COS597/HW-LINK-\[your github username\]`. In the first part of this README, you cloned the repository to your local machine to develop on.

To make changes, simply open or create some file in your local version. If you created a file, you have to do:

``git add [new_file_name]`` 
you can also use
``git add .``
to add all changes in your repository; however, make sure not to include large files etc. or unnecessary files (like OS-specific files) in there. To avoid pushing these files, you can edit the .gitignore.

Git add will make `git` track the file. If you have edited an already tracked file, you don't have to add it. Then:

``git commit -m [commit_message]``

will commit the change. `commit_message` is something that describes the type of change you made. Good commit messages are descriptive, easy to understand and correspond well with the actual changes made. Finally:

```
git pull origin master
git push origin master
```

will pull the remote code and then push the commit to the repository on Github. 

**The code on the Github server (not the version on your local machine) is the code we will evaluate if you pass the assignment. If you don't push a commit, we won't see it, and we won't grade it **

## Jupyter Lab

We installed our required libraries from the requirements.txt for our environment 'COS597'.

Make sure that you have activated the conda environment of `COS597`; otherwise the packages might not be visible to you:

`conda activate COS597`

We will be using Jupyter Lab throughout the quarter.
Note that you can also use Jupyter Notebook and a different IDE for completing the python files.
However, we highly recommend sticking with Jupyter Lab since it provides the complete IDE experience since we have designed this course this way.

To start Jupyter Lab, the easiest way is to `cd` into the specific homework assignment (here it will be in the directory where assignment0.ipynb is present) and simply enter:

`jupyter lab`

If some problem persists after this command, the jupyter libraries might not have been installed correctly.
In that case, just run these commands and any missing components will be installed:

```
pip install ipykernel
pip install jupyter
pip install jupyterlab
```

Once you can open jupyter lab, try a simple import and see if there is no compilation issue once you execute it (using ctrl + Enter). Example:

`import numpy as np`

To use all the packages and libraries we installed in our COS597 conda environment, we need to create a corresponding Jupyter "environment".
(Make sure that you have activated the conda environment of `COS597`):

`python -m ipykernel install --name=COS597 --user`

To check if this was successful:
Go to Jupyter Lab (or notebook) -> Go To "Change Kernel" option -> you should now see "COS597" as an option. Select that and you are good to start your assignment!

Each assignment will consist of a coding and writing task. In the initial homework, the coding and writing tasks are straightforward. They should help you get started with everything.


# Coding Task

1. Open the Jupyter Notebook (*.ipynb)
2. Implement the missing functions ( that show a `NotImplementedError` when running) in the `src` folder as indicated inside the jupyter notebook
3. Add, commit, and push your implementations to your GitHub repository. 
4. Ensure that the commits are updated on your GitHub repository **on Time before the due date**. Graders have access to your commit history and will judge according to this. The graders will check if you have an implementation in your repository, and if you fail this, this will count as a direct fail.