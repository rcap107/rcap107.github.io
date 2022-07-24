---
title: "The setup"
date: 2022-07-11T00:54:30+02:00


# weight: 1
# aliases: ["/first"]"
tags: ["raspberry", "arduino"]
author: "Riccardo Cappuzzo"
# author: ["Me", "You"] # multiple authors
showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: true
description: "The device, and the accessories."
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
To begin with, let's consider the material I am working with, to have an idea of what 
can be done with it and what might be needed to build something clever. 

First off, my board is a Raspberry Pi 2 Model B (2015), which features neither a Wifi
nor a Bluetooth connection. This did cause me quite a few headaches, since connecting
wireless turned out to be more complex than I thought.

I am running the Pi using a completely unofficial power supply, which regularly leads
the board to print a very ominous "Undervoltage detected" message on the CLI. 

I also own an Arduino Uno board, with which I am far less familiar as I cannot use 
Python to wrestle results out of it. I will still try to get it to work, and report
it here. 

For the Uno, I got an adapter for MicroSD cards, so that it would be possible to use
the microcontroller to log sensor data. I also need to get a fairly small MicroSD card
because the Uno cannot handle more than 5-ish GBs of storage. 

In my plans, I wanted to access the Pi remotely via wifi using SSH, which is 
problematic as the model I am working with does not have an integrated Wifi antenna. 
For this reason, I went to an electronics store and bought the first USB Wifi 
antenna, without checking whether it would work on Linux devices. Turns out, it didn't. 
Which means that I had to look for a different model, and ended up purchasing a 
(model-name)[model-link]. 

Since the first idea I got was using the Pi as a thermometer, the first sensor I 
purchased was a DHT22 temperature-humidity sensor. The version I purchased is slightly
different from what I have seen on online guides, but the functionality is the same.

I am looking to purchase another Pi, but since I am still going to use it as a sensor 
base, I will be getting either a Pi Zero (whenever they become available again!), or 
a Pico. 