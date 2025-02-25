# git_assignment_HeroVired

## Q2 
For a project that deals with large binary files, integrate Git LFS (Large File Storage) to handle these files efficiently. Demonstrate how to add, commit, and push binary files to the repository, ensuring they are tracked by Git LFS correctly. Clone the repository on another machine to verify that the binary files are downloaded correctly.

In the repository ‘git_assignment_HeroVired’, create a branch ‘lfs’. Upload any large file whose size is over ‘200mb’ and try to push this file into the repository

### a. upload large file whose >‘200mb’ , Push to Repo --------- [Done] 
  - install git lfs
  - create the repo lfs
  - run BinaryFileCreation.py to generate file > 200 mb 
  - track the file using ```git track```
  - stage, commit, and push the `.gitattributes` file and the binary files 
```
PS ~git_assignment_HeroVired> git lfs install
Updated Git hooks.
Git LFS initialized.
 
PS ~git_assignment_HeroVired> git branch lfs
PS ~git_assignment_HeroVired> git branch 
  dev
* feature/sqrt
  lfs
  main
PS ~git_assignment_HeroVired> git checkout lfs
Switched to branch 'lfs'

PS ~git_assignment_HeroVired> python .\BinaryFileCreation.py
Successfully created file: my_large_file.dat (300 MB)

PS ~git_assignment_HeroVired> git lfs track "my_large_file.dat"  
Tracking "my_large_file.dat"
PS ~git_assignment_HeroVired>  git lfs track "*.bin"
Tracking "*.bin"
PS ~git_assignment_HeroVired>  git lfs track "*.bin"
Tracking "*.bin"
PS ~git_assignment_HeroVired>  git lfs track "*.dat"
Tracking "*.dat"
PS ~git_assignment_HeroVired> git add .gitattributes
PS ~git_assignment_HeroVired> git add  .\BinaryFileCreation.py
PS ~git_assignment_HeroVired> git add .\my_large_file.dat

PS ~git_assignment_HeroVired> git commit -m "Add large binary file (my_large_file.dat) and Git LFS configuration"
[lfs 237f872] Add large binary file (my_large_file.dat) and Git LFS configuration
 3 files changed, 44 insertions(+)
 create mode 100644 .gitattributes
 create mode 100644 BinaryFileCreation.py
 create mode 100644 my_large_file.dat

PS ~git_assignment_HeroVired> git push origin lfs
Uploading LFS objects: 100% (1/1), 315 MB | 11 MB/s, done.
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 8 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 1.25 KiB | 640.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
remote: 
remote: Create a pull request for 'lfs' on GitHub by visiting:
remote:      https://github.com/Rakesh095-dvops/git_assignment_HeroVired/pull/new/lfs
remote:
To https://github.com/Rakesh095-dvops/git_assignment_HeroVired.git
 * [new branch]      lfs -> lfs

```
### b. Clone the repository on another machine to verify that the binary files are downloaded correctly.----[Done]
  - clone the Git Repository ```git clone <repository_url>```
  - install Git LFS ``` git lfs install ```
  - checkout the Relevant Branch i.e lfs```git checkout <branch_name> ```
  - Verify the File Size 
    ```
    PS ~> Get-ChildItem .\my_large_file.dat | ForEach-Object {$_.Length / (1MB)}
    300
    ```