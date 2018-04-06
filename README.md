# Introduction

Abort finishing `hotfix` or `feature` if `CHANGELOG.md` (or any other file for that matter)
has not been changed in the last commit.

I am sure this can be done with just bash in lieu of python but my bash-fu is not that great.
I wrote this in a hurry because I used to keep forgetting to update the `CHANGELOG.md`
of a work project until I had pushed the changes.


## Usage


To check `git flow hotfix finish`, create a file named `pre-flow-hotfix-finish`
and put the following -- make necessary changes.


```bash
#!/usr/bin/env bash
python /<path/to/this/repo>/okay.py /full/path/to/project/directory
```


To apply this to `git flow feature finish` create another file named
`pre-flow-feature-finish` and put the same content.


In the beginning, when you do `git flow init`, it prompts for a
`hooks and filters` directory. If you've already initialized
the repo, run the following to set/change the hooks path.


```bash
git config gitflow.path.hooks /<path/to/this/repo>
```
