# git_assignment_HeroVired

## Q1
 You are part of a development team working on a Python application called "CalculatorPlus." The application provides basic arithmetic operations, such as addition, subtraction, multiplication, and division. Your task is to implement a new feature that adds support for calculating the square root of a number.

### a. Create a repository name: git_assignment_HeroVired --------- [Done] 
```
Completed and create branch from Github and clone the private Repository - https://github.com/Rakesh095-dvops/git_assignment_HeroVired.git
```
### b. Create a ‘dev’ branch .Added the code and push to dev branch --------- [Done]
```
PS ~\git_assignment_HeroVired> git branch dev 
PS ~\git_assignment_HeroVired> git branch 
  dev
* main
PS ~\git_assignment_HeroVired> git checkout dev    
Switched to branch 'dev'
```

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
#### C. Merge this branch with the main branch and make a release of version 1 of the ‘calculator plus app’. --------- [Done]
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
```
### d. Add any of your classmates as collaborators. -[Done]
### e. Implement a feature by creating a new branch called ‘feature/sqrt’. -[Done]
### f. Add the ‘sqrt’ code to it.- [Done]
  1. @ssptr007 added as collborator . As a collborator i have created a pull request and shared to @ssptr007 & vice Versa. 
  2. I have cloned @ssptr007 repo main branch.  
  3. create a feature branch and add the code ```git checkout -b feature/sqrt``
  4. Implement the Square Root Feature 
        1. ```git add   ```
        2. ```git commit -m {comment}```
### g. While you are working on this feature, imagine that one critical bug is reported in the main branch, and you need to switch back to the ‘dev’ branch, create fixes, and apply them while keeping your ‘feature/sqrt’ branch up-to-date.-[Done]

  1. cloned our own repository again ```git clone {url}```
  2.  ```git checkout dev```
  3.  ```git pull origin dev```to Ensure your local dev branch is up-to-date
  4. Make bug fix directly on the `dev` branch 
  5. once done commit the changes ,test the code.
### h. After completing the feature implementation and ensuring that the application works correctly, create a pull request targeting the main branch.-[Done]
```
Create a pull request using Github and UI and test the same.

```

### i. Request a code review from a team member and make any necessary improvements based on the review feedback.-[Done]
```
Create a pull request and share the details to @ssptr007 
```

### j. Once the code reviewer approves your pull request, merge the "feature/sqrt" branch into the ‘dev’ branch. -[Done]
```
Code reviewer approve the request and add necessary comments from github GUI.
```

### k. Finally, do the testing in the ‘dev’ branch itself and merge it into the ‘main’ branch and create a ‘version 2’ release.-[Done]
1. rechecking the merge between feqture/Sqrt and dev locally using VS code. 
2. test dev branch code. 
3. test main branch code. 
4. As exception was outputing the results. comment test scenarios to have clean output. 
5. Now merge dev and main branch 
6. create tags v2.0 
7. Also create release tags v2.0 from GUI.

#### below mentioned are the list of commands used for above h -k 
```
git checkout {branch}
git pull origin {branch}
git merge {branch}
git commit -m {comment}
git push origin main
git tag -a v2.0 -m "Release v2.0: Includes square root feature and bug fixes"
git push origin v2.0
git push origin --tags
```
![alt text](Images/ReleaseV2.0Q1.png)