---
title: "My 2024 (so far) in academia"
date: 2024-10-08T22:06:34+02:00
categories: [""]
---
Disclaimer: this post will mostly be a rant. The reasons for it should become
sufficiently clear as I go over my experience in the past few months. 

For context, I have been working on a paper for the past year or so. Said paper 
involved running a few thousands experimental configurations over different 
baselines, then reporting said experiments in a paper that was initially [submitted
to VLDB2024]({{< relref "posts/news/vldb_2024.md" >}}) (end of 
January this year). Said paper was rejected at VLDB 2024, submitted to SIGMOD2025, 
and was rejected again.

Over the course of only a few months, I had the privilege of experiencing (very 
courteous) academic blackmailing, extremely negative reviews, burnout, overtime, 
and possibly the most bullshit rejection I have heard of. 

Let's start from top, with the academic blackmail. So, VLDB is a single blind 
conference, which means that the authors are not aware of who the reviewers are,
while the reviewers can instead see the names and affiliations of the authors. 

This is less annoying to manage than double blind (which instead involve anonymizing
everything), but has the fun side effect of receiving emails from the reviewers, 
who might _nicely_ ask to _please_ add their recent papers to yours in a 
_completely non-threatening way_ by _reaching out in private to one of the authors_. 
Bonus points for asking to add references to papers whose code is not available 
to run and test. 

This leads me directly into the rejection. I have my fair share of rejected papers 
-- though by this point, most of my rejections are from this singular paper --, 
and I am keenly aware of how much of an impact "rolling the right reviewers" has
on the final outcome. This rejection was especially fun, however,
because it came _only after_ a revision period during which I had to re-run
most of the experiments (hence the burnout). But as a man once said, "I'm not 
done yet": the reasoning for the rejection was that "we did not test a specific 
baseline, and said baseline works on my machine" (paraphrased). The kicker? _The 
code for the baseline was not available online, and the reviewer did not provide 
it to us so that we could test it_. As a result, the area chair agreed with it, 
and the paper was rejected after the revision step. 

What was even more of a kick in the nether regions was that we even managed to 
change the mind of the one reviewer that had marked his review as "weak reject,
and I am not going to change my mind". Unfortunately, we also managed to change
the mind of one of the "weak accept" reviews to "reject", and that somehow stuck. 

Something interesting to note is that, soon after the paper was rejected, the arXiv 
version received a new citation. This citation was by one of the authors of the baseline. 
While I am not one to engage in conspirationsm, the coincidence was a bit too 
perfect for me to ignore.  

While I only briefly mentioned the burnout, it was _bad_. I got sick after every 
deadline, and I think I developed some degree of PTSD from looking at terminal 
screens waiting for experimental runs to end. Not the best, especially considering
it did not result in success (yet, at least). That's not good for morale either. 

### Lessons learned
What is the summary of these experiences? 1) The current reviewing system is broken
(which is something literally anyone in the field will confirm); 2) academia is 
rife with politics just like everything else; 3) effort is not likely to be 
rewarded, and your fate lies less in your hands and in your results, than in 
the ethereal roll of the dice that will assign a reviewer rather than another 
in any given round of paper submission. 

The result? I will be looking for my next position in industry, rather than 
academia. Stay tuned for when I will write the equivalent post on my industry
misgivings once I have enough experience in that. 