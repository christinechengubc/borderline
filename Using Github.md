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
1. Go to our [repository](https://github.com/TwelveNights/borderline).
2. Select the Issues tab on the right side.
![Issues](https://github.com/TwelveNights/borderline/blob/master/Using%20Github/1.png?raw=true)
3. Here, you'll find all existing issues. Click on 'New Issue'.
![New Issue](https://github.com/TwelveNights/borderline/blob/master/Using%20Github/2.png?raw=true)
4. Write up a title and comment on the issue we need to address.
5. Attach a label, milestone, and assignee(optional). If the issue doesn't need to be resolved immediately, set the milestone for **Product Backlog**.
![Making a New Issue](https://github.com/TwelveNights/borderline/blob/master/Using%20Github/6.png?raw=true)
**If the label you need doesn't exist, you can create new labels under the 'Labels' tab!**
![Labels](https://github.com/TwelveNights/borderline/blob/master/Using%20Github/4.png?raw=true)
6. Press 'submit' and away it goes!  
**Note that it is possible to reference other issues and commits. Simply type '#' followed by the number for the issue to link it. Also, people are linkable too with @!**

## Using Github for Windows
1. Open up Github for Windows.
2. Make sure to set up your options so Github for Windows is linked to your account. Also, include your alias and e-mail so that each commit is tied to your name.
![Options](https://github.com/TwelveNights/borderline/blob/master/Using%20Github/9.png?raw=true)
![Name and Email](https://github.com/TwelveNights/borderline/blob/master/Using%20Github/10.png?raw=true)
3. Click on the plus-sign to add a repository.
![Adding a Repository](https://github.com/TwelveNights/borderline/blob/master/Using%20Github/7.png?raw=true)
4. Clone the repository 'borderline' to your computer.
![Cloning a Repository](https://github.com/TwelveNights/borderline/blob/master/Using%20Github/8.png?raw=true)

#### Push & Pull
  Thankfully, Github for Windows makes this very clean. Github for Windows offers a timeline to check through the history of the project. You can update your local files by pressing 'sync'.
![Sync](https://github.com/TwelveNights/borderline/blob/master/Using%20Github/14.png?raw=true)

#### Committing (adding, modifying, and removing files)
1. Click on the farthest right circle on the timeline. These are the changes you've made.
![Recent Changes](https://github.com/TwelveNights/borderline/blob/master/Using%20Github/11.png?raw=true)
2. Here, you can view changes to each file by clicking on them. Note that this is usually for code, so this feature may not be applicable to you.
3. Type a nice commit title. Use present tense. Add some description if you would like. This can be anything you'd like to talk about for your commit. However, a description is not mandatory.
![Commit](https://github.com/TwelveNights/borderline/blob/master/Using%20Github/12.png?raw=true)
4. Press 'Commit to Master'
5. Once you'd like to add the file from your computer to the repository, press 'sync'.
![Sync](https://github.com/TwelveNights/borderline/blob/master/Using%20Github/14.png?raw=true)
**Note: please do not spam commits. Try to commit when you have many changes, or when you have important ones.**

Congratulations, now you've successfully added to the project! Make sure to 'sync' regularly, because this not only updates your local files with commits other members have made, but also allows other members to have the changes you've made.


## Markdown
  If you're interested on how to make text pretty, like this document, follow the [Mastering Markdown Guide](https://guides.github.com/features/mastering-markdown). Basically, it's text formatting you can do when you comment on issues and such on the Github site. I wrote this document with some Markdown elements, such as
- [x] Images
- [x] Headers
- [x] Bold
- [x] Links
- [x] This Checkboard
- [ ] Emoji

## Conclusion
  I've left out some details, like viewing issues specifically and more technical things that probably don't belong in this guide. Anyways, I recommend you try it out yourselves and contribute to the repository.
  
  If there are any questions you have, don't hesitate to ask me about it. I actually really love Git, and Github just makes it more accessible to people.
  
Eddie, @TwelveNights


![Thank You](http://i.imgur.com/SSLjSgB.png)
