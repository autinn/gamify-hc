# Using the GitHub Repo

## 1. Cloning the Repository (Setup Only)

To get started, clone the repository from GitHub:

`git clone https://github.com/autinn/gamify-hc.git`

`cd gamify-hc`

If you’re using SSH:

`git clone git@github.com:autinn/gamify-hc.git`

`cd gamify-hc`

## 2. Updating Your Local Copy

Keep your local repository up to date whenever interacting with main, by using the following command:

`git pull origin main`

Alternatively, if you’re working on a feature branch collaboratively, make sure your branch is up-to-date:

`git pull origin <branch-name>`

## 3. Making Changes Locally

Never code directly in the main branch. Before making changes, create a new branch to isolate your work:

`git checkout -b feature/your-feature-name`

Use descriptive branch names: (`feature/…` , `bugfix/…` , `chore/…` etc)

Commit your changes regularly::

Stage files (`.` is a placeholder for “select everything in this folder”):

`git add .`

Commit changes locally, commit messages can only be <= 80 characters long. If you cannot summarize what you have done in that few characters, split your work into multiple commits by staging files selectively:

`git commit -m "Describe your changes"`

## 4. Pushing to Remote

If your local main is up to date, and you are the only one working on your `feature/bugfix/chore` branch, you should be able to rebase your branch onto the latest copy of main as follows:

Make sure you are on the right branch:

`git checkout feature/your-feature-name`

Rebase your branch onto the most recent copy of main:

`git rebase main`

Push to remote:

`git push origin feature/your-feature-name`

Note that we set origin to our personal branch, NOT main. Pushing directly to main will not end well for us (it is bad practice).

Otherwise, if you are working with multiple people on the same branch, there are a few different approaches you can take. To be honest, I am not entirely sure what the best practice is in any given situation, but this seems to be good enough in many circumstances:

Make sure you are on the right branch:

`git checkout feature/your-feature-name`

Fetch and merge main into your current branch:

`git pull origin main`

You should also make sure you are up to date with the feature branch you are collaborating on.

`git pull origin feature/your-feature-name`

Finally, you can push to the feature branch, yipee! There will probably be a lot of manual merging along this process; it will not be fun.

`git push origin feature/your-feature-name`

Alternatively, you can create branches of branches, in which case your the former branch becomes like a mini main.

## 5. Creating a Pull Request (PR)

There comes a time when a branch is mostly ready to be merged into main, at which point you can make a PR. Likely, we will have a PR template very soon, but if not, this is what a PR should contain:
- At a high level, what changes were made?
- Why were these changes made?
- How were these changes made?
- What context, visual or otherwise, do reviewers need to understand or use this feature?
- How Was the Code Tested?
- Other Notes, Context, or Anything that Remains to be Addressed

Note how it is expected that the code has been tested before being put into a PR. This is absolutely necessary. As core Django dev Jacob Kaplan-Moss once said, “Code without tests is broken by design.”

## 6. Merging and Closing a PR

A PR needs to be reviewed at least once by someone other than the person who made the code. I would recommend assigning reviews to members of the same department (i.e. backend code is reviewed by backend engineers). If any changes need to be made, which they often do, comments should be added to the PR, all of which should be addressed before merging. It is important that the reviewer run the test suite designed for the new branch, and ideally the full test suite, before merging.

------------

This is a working document, feel free to suggest changes! The branch this was originally merged from is `documentation/github-usage-guidelines`