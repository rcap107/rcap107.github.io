---
title: "Learning optimization by minmaxing Blade and Soul soulshields"
format: html
date: "2025/04/08"
categories:
    - code
    - games
    - "blade_and_soul"
draft: true
reading-time: true
---

It belongs to the _Soulshield set_ 
"Horror's Oath", along with 4 more other pieces; since I have equipped 5 pieces,
I also gain the additional _Set effects_, which further increase the statistics. 
In Blade and Soul, shields are always equipped as a set of 3, 5, or 8 pieces. 

## Soulshields and how stats are gained in BnS
To help understanding the rest of the post, I need to explain how character stats
are assigned in BnS. Like in many other games, you gain statistics by wearing 
better equipment, as equipment carries stats that add to the base stats your 
character has. 

A particularity of BnS is that a lot of the statistics are given by items called 
"Soulshields". Each character has exactly 8 soulshield slots that can be filled
by one soulshield piece per slot. Soulshield pieces always provide health, as well
as one or two additional stats. Moreover, soulshield pieces belong to "sets", and
"wearing" multiple pieces from the same set in different slots may bring additional
benefits (usually more stats on top of what the pieces already give). Soulshield
sets are extremely important in the game, and it's normally more beneficial to wear
suboptimal pieces if they unlock the full set. 

more on how to get shields and the fact that some have bad stats and that stats
are rng anyway

## What I want to optimize: my requirements
Now that I gave a brief introduction of how stats are assigned, the problem becomes
figuring out how to choose the best sets among all the copies that I have gathered.

There are a few requirements that I need to keep in mind: 

- A combination of shield pieces must have exactly one piece per slot. 
- All soulshield sets must be optimal: only combinations of 3, 5, or 8 pieces 
are valid. 
- While I want to optimize my shield set, I am not interested in a perfect solution. 
- I am not sure what the "best" combination looks like.
- I am interested in maximizing the stats of *Critical hit*, *Critical damage*, and 
keep my *Accuracy* above a certain amount to make sure that all my hits land. 
- Pretty much all other stats are useless, including any value of Accuracy above
the threshold I decided (about 700). 
- I am interested in the final amount of stats a set can provide, including the 
base stats provided by all other sources. This means that, for example, I may not
need any Accuracy if I can get it from other equipment.

As I was thinking how to implement this, a number of problems came up, some of
which will be covered in other posts:

- How do I define "the best combination"?
- How do I get the stats of all my slices from the game to something like a 
spreadsheet, without an API? 
- How do I generate all the possible combinations? 
- How do I validate combinations, so that I keep only those that satisfy my 
requirements? 
- How do I present the results in a way that clearly lists the pieces I need to 
build a specific combination? 

## Coda: why am I doing all this? 
1. Because it was an interesting problem with an application I (may) find useful.
2. Because I found an excuse to learn some Google Sheets scripting.
3. Because it's not the kind of problem I encounter often.
4. Because, by using very few external libraries it's a way to practice plain python.
5. Because I might use this as an excuse to re-write everything in Rust and learn 
some of that too. 

So, plenty of reasons! I have a lot to write, so I will be breaking this project
in a few more posts and share them all here. Stay tuned for more! 