#!/usr/bin/env python

import sys
import os
import git


if len(sys.argv) < 2:
        print("please pass repo path")
        sys.exit(0)


repo_path = sys.argv[1]
dotgit = os.path.join(repo_path, ".git")


if not os.path.exists(dotgit) or not os.path.isdir(dotgit):
        print("no valid repo found")
        sys.exit(0)


repo = git.Repo(sys.argv[1])


commits_list = []
counter = 0

for commit in repo.iter_commits():
        commits_list.append(commit)
        counter += 1

        if counter == 2:
        	break

changed_files = []
 
for x in commits_list[0].diff(commits_list[-1]):
    if x.b_blob is not None and x.b_blob.path not in changed_files:
        changed_files.append(x.b_blob.path)


if 'CHANGELOG.md' not in changed_files:
        print('change the CHANGELOG.md, kid')
        sys.exit(1)
