# git_assignment_HeroVired

## Q1
 You are part of a development team working on a Python application called "CalculatorPlus." The application provides basic arithmetic operations, such as addition, subtraction, multiplication, and division. Your task is to implement a new feature that adds support for calculating the square root of a number.

### a. Create a repository name: git_assignment_HeroVired --------- [Done] 
```
Completed and create branch from Github and clone the private Repository - https://github.com/Rakesh095-dvops/git_assignment_HeroVired.git
```
### b. Create a ‘dev’ branch --------- [Done]
```
PS ~\git_assignment_HeroVired> git branch dev 
PS ~\git_assignment_HeroVired> git branch 
  dev
* main
PS ~\git_assignment_HeroVired> git checkout dev    
Switched to branch 'dev'
```
#### b.1. Added the code and push to dev branch --------- [Done]
```
PS ~\git_assignment_HeroVired> git ls-files
.gitignore
README.md
PS ~\git_assignment_HeroVired> git add .
PS ~\git_assignment_HeroVired> git commit -m "initial push for dev branch with README.MD and CalculatorPlus.py files"
[dev 62753ba] initial push for dev branch with README.MD and CalculatorPlus.py files
 2 files changed, 52 insertions(+), 1 deletion(-)
 create mode 100644 CalculatorPlus.py

PS ~\git_assignment_HeroVired> git push origin dev   
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 1.18 KiB | 1.18 MiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
remote: 
remote: Create a pull request for 'dev' on GitHub by visiting:
remote:      https://github.com/Rakesh095-dvops/git_assignment_HeroVired/pull/new/dev
remote:
To https://github.com/Rakesh095-dvops/git_assignment_HeroVired.git
 * [new branch]      dev -> dev

```
##### SnapShot 
![alt text](Images/dev_branch_push.png)

```
push commit and updated the dev branch 
PS ~\git_assignment_HeroVired git status
On branch dev
nothing to commit, working tree clean

```
### C. Merge this branch with the main branch and make a release of version 1 of the ‘calculator plus app’. --------- [Done]
1. Switch to the main branch:
2. Make sure your main branch is up-to-date
3. Merge the 'dev' branch into 'main'
4. Check for merge conflicts and resolve them.
    - git status will show you files with conflicts
    - Edit the conflicting files, then:
    - git add <conflicting_file>
    - git commit
5. Commit the change to Main
6. Create the release tag
7. Push everything to main.
```
PS ~git_assignment_HeroVired> git push origin dev
PS ~git_assignment_HeroVired> git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
PS ~git_assignment_HeroVired> git pull origin main
From https://github.com/Rakesh095-dvops/git_assignment_HeroVired
 * branch            main       -> FETCH_HEAD
Already up to date.
PS ~git_assignment_HeroVired> git merge dev
Updating 41768b9..457a03a
Fast-forward
 CalculatorPlus.py          |  31 +++++++++++++++++++++++++
 Images/dev_branch_push.png | Bin 0 -> 129564 bytes
 README.md                  |  55 ++++++++++++++++++++++++++++++++++++++++++++-
 3 files changed, 85 insertions(+), 1 deletion(-)
 create mode 100644 CalculatorPlus.py
 create mode 100644 Images/dev_branch_push.png
PS ~git_assignment_HeroVired> git commit -m "Merge dev branch into main, incorporating latest changes"
On branch main
Your branch is ahead of 'origin/main' by 3 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
PS ~git_assignment_HeroVired> git status
On branch main
Your branch is ahead of 'origin/main' by 3 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
PS ~git_assignment_HeroVired> git add .
PS ~git_assignment_HeroVired> git tag -a v1.0 -m "Release v1.0: Initial release after merging dev branch."
PS ~git_assignment_HeroVired> git push origin main --tags
Enumerating objects: 1, done.
Counting objects: 100% (1/1), done.
Writing objects: 100% (1/1), 195 bytes | 195.00 KiB/s, done.
Total 1 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/Rakesh095-dvops/git_assignment_HeroVired.git
   41768b9..457a03a  main -> main
 * [new tag]         v1.0 -> v1.0
PS ~git_assignment_HeroVired> git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

```
### d. Implement a feature by creating a new branch called ‘feature/sqrt’. --------- [Done]

```
PS ~git_assignment_HeroVired> git checkout -b feature/sqrt
Switched to a new branch 'feature/sqrt'
PS ~git_assignment_HeroVired> git branch
  dev
* feature/sqrt
  main
PS ~git_assignment_HeroVired> git add .     
PS ~git_assignment_HeroVired> git status
On branch feature/sqrt
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   CalculatorPlus.py
        modified:   README.md

PS ~git_assignment_HeroVired> git commit -m "feat: Add sqrt function to calculator"              
[feature/sqrt f5db45d] feat: Add sqrt function to calculator
 2 files changed, 15 insertions(+), 15 deletions(-)

PS ~ git push origin feature/sqrt
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 483 bytes | 483.00 KiB/s, done.
Total 4 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
remote:
remote: Create a pull request for 'feature/sqrt' on GitHub by visiting:
remote:      https://github.com/Rakesh095-dvops/git_assignment_HeroVired/pull/new/feature/sqrt
remote:
To https://github.com/Rakesh095-dvops/git_assignment_HeroVired.git
 * [new branch]      feature/sqrt -> feature/sqrt

```
































## Q2 