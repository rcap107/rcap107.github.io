---
title: "EuroSciPy 2025: thinking back on the event and my tutorial"
date: 2025-08-26
tags: [EuroSciPy, conference, Python, OSS]
---

The week of EuroSciPy 2025 has just ended, and now it's time to take stock of all
the various talks I attended, those that I missed out on, and some other personal
observations.

In this post, I will be going over my personal experience with the trip and the 
talk I gave on the first day. 

# The city, the venue, and the organization
This year, the conference was held in the AGH University of Kraków, Poland.
This being my very first time in Poland, I had no idea what to expect. What I 
found was a beautiful city, great and well maintained infrastructure, and everyone 
speaking in English. At least the last part was a surprise and a nice change of 
pace, given my typical experience in France 🙈.

At the university we were spoiled with coffee, tea and snacks all day long. I must
admit I did not love the food, but I believe that's mostly to do with my own
personal tastes rather than the actual quality. 

I was travelling with three other scikit-learn maintainers: Olivier Grisel, Guillaume
Lemaitre and Loic Esteve. I'm thankful they had me tag along: it's always
interesting to listen in to their conversations, and I always learn a lot from 
just discussing with them. 

Overall, the organizers and volunteers were incredibly helpful, and I think
everything went according to plan. At least, from what I could tell.

My main gripe with the whole event was that it was held in the week starting on the
18th of August, meaning that we had to travel right on the weekend where _everyone_
goes back from vacation. Being on vacation myself, I did not have the time to 
prepare my talk as well as I wanted. I really hope that the dates for next year's
event will be better. 

# The social side
It was a great time! I met a lot of interesting and clever people. It was just the
kind of geek collection that I'd expect from such a conference, and in general 
everyone was nice and fun to hang out with. I'm sure I'll meet a lot of the same
people at PyData Paris in a month, looking forwards to that. 

Also, the social event was a blast and I ate way more pizza (and good pizza) than
I had expected. Full marks on that too!

# My tutorial: "Timeseries forecasting with skrub" 
Yes, that's right. I was a speaker this time! My first time doing a tutorial in a
public conference, at that. Indeed, I was _very_ nervous about it, and while I 
had a lot of people come and tell me it was great, I still felt it was not as good
as it could have been, and I've been mulling over how to make it better for the 
next time. At least, I can say that I am thinking of the next time! 

The material we used for the tutorial is available in
[this repository](https://github.com/skrub-data/EuroSciPy2025). It was adapted
from the masterclass that Olivier and Guillaume prepared for Probabl.
(the masterclass is available [here](https://github.com/probabl-ai/forecasting)),
cutting down on a lot of material, and adding a few exercises for the tutorial. 

I feel like the main problem with this tutorial is that it had _two_ complicated
parts to it: preparing data for forecasting, and using the skrub Data Ops. In a 
tutorial like the one we did, this made the 90 minutes extremely dense and hard 
to follow. I even had the same problem when I followed the masterclass, and _I knew_
what Data Ops were! 

I'm already planning to address that in the next version by just _removing the 
forecasting altogether_, and instead using a simpler example to force the audience
to deal only with the Data Ops. 

Another problem was with the exercises: they were too few and far inbetween, and 
they were _way too complicated_ for the audience to actually solve in the limited
time we gave them. A lot of complex operations that would require a bunch of 
digging in the examples and the documentation.

I absolutely have to come up with simpler examples, and in general with things that
anyone can do given the information provided up to that point. In most of the other
tutorials the speakers let us play around with the software for much longer, which
I think was a far better strategy than what we ended up doing. 

Finally, and this is entirely due to my nervousness and not having a clue what to
say in a tutorial, I completely forgot to introduce myself, which was funny, but
also not good. Thankfully, Guillaume covered for me when he did the second
section of the tutorial. 

I'm still fairly happy with the outcome, but I still think we could have done better,
and I'll make sure the next version _will_ be better. 

Oh, and if you want to judge for yourself whether I'm being too harsh on myself, 
you can find the full thing on [Youtube](https://www.youtube.com/watch?v=hbmfiBX5zZc).

# Conclusions
Overall, it was a very positive experience: there were a lot of interesting talks,
interesting people, and interesting packages. The trip went well and the city was 
very nice (I still hate travelling, but that's just me). I finally presented my 
first tutorial, with somewhat mixed results (at least in my head...), so now I know
what to do for the next. I'm really happy I went. 

Stay tuned for the next post, where I'll go over the talks I liked the most and 
share pointers and links to the material. 

Cheers! 