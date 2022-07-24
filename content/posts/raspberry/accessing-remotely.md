---
title: "Accessing the Pi remotely"
date: 2022-07-10T01:14:44+02:00


# weight: 1
# aliases: ["/first"]
tags: ["raspberry"]
author: "Riccardo Cappuzzo"
# author: ["Me", "You"] # multiple authors
showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: true
description: ""
# canonicalURL: ""
disableHLJS: true # to disable highlightjs
disableShare: false
disableHLJS: false
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
cover:
    image: "<image path/url>" # image path/url
    alt: "<alt text>" # alt text
    caption: "<text>" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: true # only hide on current single page
editPost:
    URL: "https://github.com/rcap107.github.io/content"
    Text: "Suggest Changes" # edit text
    appendFilePath: true # to append file path to Edit link
---
I'll start my trip in the development with my Pi by explaining what I did
to access it remotely, which normally is pretty straightforwards. I will 
also add a section on some absolutely not-straightforwards things that 
happened randomly one day, then stopped. 

For most of the setup, I had direct access to the Pi with keyboard and 
a screen (it was not headless). I also relied a lot on a bunch of guides 
and tutorials I found online, which I will try to link in the post. I 
won't be able to remember all of them, however. 

## Enabling SSH
Alternative sources:
- ()[]
- ()[] 
- ()[]

Enabling SSH on the Pi is pretty easy, if you actually have access to the
board with keyboard and a screen. 

Begin with typing:
```
sudo raspi-config
```
If you haven't, remember to set a strong password before enabling SSH by 
selecting the `System Options` entry, then `Password`. After doing that, go back 
to the starting window and select `Interface Options`, then `SSH`. Select `Yes`,
then close the configuration tool.

Reboot the Pi with
```
sudo reboot
```







## Setting a static IP

## Accessing the board 


## Bonus section: when none of it works


