# Using Github

  Hi there. I've designed this guide to teach and instruct team members on using [Github](https://github.com) to organize our project and tasks. Although we may not fully move to this yet, I'll try my best to break down the fundamentals. 
  
  Github is a website which uses technology called 'Git' to organize projects, normally large programming projects which can have thousands of contributors. For instance, Linus Torvalds, creator of both Linux and Git, has the [source code for Linux](https://github.com/torvalds/linux) here, with 5375 contributors in total.
  
  Projects are stored as repositories. Our repository does not simply store the project in the state it is in now. The project is a timeline of 'commits', which you can think about as an instance where something is changed in the project. Being able to document all the changes is both useful in being able to track progress, but it is also useful in reversing changes if necessary. For us, we'll use it to track progress.
  
This guide will cover:
+ Creating new issues
+ Using [Github for Windows](http://desktop.github.com/), because the command line is scary-looking
  + Committing (adding, modifying, and removing files)
  + 'Push' and 'Pull' - pushing changes into the central repository, and pulling changes from the repository to your computer
+ Markdown - to make your text pretty if you need it to be

## Creating New Issues
1. Go to our [repository](https://github.com/TwelveNights/borderline
2. Select the Issues tab on the right side.
3. Write up a title and comment on the issue we need to address.
4. Attach a label, milestone, and assignee(optional). If the issue doesn't need to be resolved immediately, set the milestone for **Product Backlog**.
5. Press 'submit' and away it goes!
*Note that it is possible to reference other issues and commits. Simply type '#' followed by the number for the issue to link it. Also, people are linkable too!* @TwelveNights

## Using Github for Windows
1. Open up Github for Windows.
2. Make sure to set up your options so Github for Windows is linked to your account. Also, include your alias and e-mail so that each commit is tied to your name.
3. Click on the plus-sign to add a repository.
4. Clone the repository 'borderline' to your computer.
5. Now you'll see a screen featuring the repository on the client.

### Push & Pull
  Thankfully, Github for Windows makes this very clean. Github for Windows offers a timeline to check through the history of the project. You can update your local files by pressing 'sync'.

### Committing (adding, modifying, and removing files)
1. Click on the farthest right circle on the timeline.
2. Here, you can view changes to each file by clicking on them. Note that this is usually for code, so this feature may not be applicable to you.
3. Type a nice commit title. Use present tense.
4. Add some description if you would like. This can be anything you'd like to talk about for your commit. If it's straight-forward, feel free to not include any description.
5. Press 'Commit to Master'
6. Once you'd like to add the file to the repository, press 'sync'.
**Note: please do not spam commits. Try to commit when you have many changes, or when you have important ones.**