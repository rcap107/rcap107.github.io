---
title: "A retrospective on the publication of Retrieve, Merge, Predict"
date: "2025-06-25"
categories: ["academia"]
draft: true
---
As I've already posted some time ago, the paper  paper "Retrieve, Merge, 
Predict - Augmenting tables with data lakes" has been published in 
[TMLR](https://jmlr.org/tmlr/index.html): you may find it 
[here](https://openreview.net/pdf?id=4uPJN6yfY1).

This post will be a retrospective recollection of all it took to get the paper out.
If you happen to read this as you struggle to get a paper published, I hope it'll
give you some confidence that, yes, if you push hard enough papers do get through. 

Of course, it could have been worse. The paper could have been rejected one more 
time... Still, the point of this post is to tie up the entire experience up, to 
get a sense of "closure". 

If it wasn't clear, there will be rambling. 

**September 2022**

I begin my contract as a post doc, working with the SODA team 
in Inria, and as part of the Lab team in Dataiku. The aim of the project at this 
point is still quite unclear: is it going to be about embedding relational data? 
Is it about performing information retrieval with corporate data? We still don't 
know. 

**December 2022**

After a questionable time over the previous few months, just before Christmas it
appears that the direction of my project will revolve around developing a new and 
improved version of Lazo, a hash-based information retrieval and indexing tool 
that is part of the Dataiku software. As hashing is almost entirely out of my 
wheelhouse, this leads to a pretty bad wake-up call, and to a not-so-enjoyable
Christmas vacation.

I also catch COVID, get very sick, and have to self-isolate in my room for two of 
the three weeks I spend home. 

**January to March 2023**

In this period, I spend my time looking at different data lakes that may help me
with benchmarking the new method, while working on the open source implementation
of the method itself. Somewhere in this period, we decide that the Open Data 
that was available to us was far too dirty to be used, and we decide to develop 
our own. Roughly, this is when we first came up with the YADL idea. 

**March to May 2023**

We start to mature the idea of employing YADL as part of a benchmark that would 
evaluate different methods for retrieving information coming from data lakes, and
combine it with a base table to add features and train a ML model. After designing
a (very messy, in retrospective) pipeline to evaluate a handful of different 
methods, we submit a very rough first version of our paper to the Benchmarks 
track of NeurIPS 2023. 

Some fun facts about this release: 
- the day before the deadline I get a panic attack as I realize a lof of the 
experiments are incorrect (the reason, I forgot). Not a big deal in the grand 
scheme of things, given I'll have to re-run all experiments at least three more 
times. 
- I end up submitting one of the final versions while on a trip on the Eiffel
Tower, connecting to the wifi of the tower and sitting on the seat of the guard. 
- As I try to submit another slightly modified version a few minutes before the
deadline, the proceedings servers go down, so I can't submit it. Soon after, we 
get an email telling us that the deadline was postponed by two hours because of 
the downtime. One of the authors sends us an email asking if we wanted to add
anythnig else in "the two extra hours we got".

Unsurprisingly, the paper was rejected. Considering that we didn't even have a 
clear idea of what problem we were trying to answer, the outcome was warranted
and definitely helped with producing a better paper. 

In this period, ChatGPT dropped, and everything on the Dataiku side went up in the
air because of it. I have some strong feelings about that period, and I can say
that at that time they did not help with either the paper, or my opinion of LLMs
and AI. Thankfully, over time both evolved. 

**May 2023 to early December 2023**

I keep on working on the paper, refining the pipeline and the ideas that come
with it. As time passes, we decide that the second submission should target VLDB
2024, a database-focused conference that would emphasise the retrieval side of the 
pipeline. For this submission, the experimental campaign involved tracking 
thousands of experimental runs, their configuration, their results, and the 
computational footprint of each. This involved a lot of jousting trying to make
the best use possible of the Inria clusters. 

**December 2023 to end of January 2024**

What a Christmas season. I still had all my experiments to run,
but this time I was at home with my family and in a period of supposed relaxation.
Some vacation that was. I had to run experiments, track results, put everything 
together, all while waiting for Santa to come home.

The kicker? Once I finally got back to work, I realized most of the runs were 
useless because of some bug I introduced in the code. Stellar. Result? I had to 
rush all the runs once again before the deadline of the paper (January 31st), and 
hope to get everything in before the paper was done. 

Result: I burn out, and get a massive bacterial infection I had to take 
antibiotics to get out of. Stellar x2. No COVID this time, thankfully. 

**February 2024 to March 2024**

I spend most of my time polishing the results, trying to come up with questions
that the reviewrs might ask, and answering those questions. 

We finally get the reviews. Two "weak accept" willing to change their mind, one 
"weak reject" not willing to change their mind. Ok then. 

Remember me preparing the questions? They ask exactly none of them.
In exchange, the reviewers require more experiments, more baselines, more results.

**April 2024 to May 2024**

I spend most of my time re-running all the experiments I had already run. Then, 
I run about twice as many on top of that. 

I am asked to add baselines, some of which have code that require specific 
versions of C to be compiled with, some of which requires massive restructuring to 
run on data other than what was used for the original paper. Of course, most of 
the baselines don't even have code to access.

Besides all of this, I am also rewriting a lot of the paper, while orchestrating
the entire experimental campaign. 

This is all during the months of April (during which we had a team retreat in 
the Alps, which I spent running experiments), and May (which in France is spent
mostly on bank holidays, and which I spent running experiments). 

**May 2024**

Finally, we submit the response to the reviewers, with some optimism as we thought
we addressed most of the points raised by the reviewers, and typically papers that
go through the rebuttal process tend to get accepted for the conference.

The paper gets rejected. Despite changing the mind of the one negative reviewer 
that also stated they would not change their mind, one of the two positive 
reviewers is not satisfied by our excuse that "we could not run a baseline because 
the code for it is not available", and rejects the paper. The area chair agrees
with the reviewer, and we're back to the drawing board.

I've already said my piece on this shitshow in [another post](academia_experience.md). 
I will be holding onto that particular grudge for a long time. 

I burn out again, spend another week or two out sick. I am fed up with 
everything and everyone in general. 

**May 2024 to July 2024**

We try to re-submit the paper with minimal changes to SIGMOD2025, another database
conference. 

The paper gets rejected immediately, with two rejects and one major revision. 
That's it for now, back to the drawing board.

At this point, I am _completely_ burnt out with everything and everyone. I did 
not recover from the previous burnout, and am in fact exuding a pretty obvious
"I want to murder every single one of you for just looking at me" energy.
I straight 
up get nauseous from watching the terminal window, and right before taking my 
summer days off it takes all I can to not crash out directly and start berating
all my coworkers for absolutely no reason. That was _not_ a good period. 

Looking back, that's probably some PTSD I developed over those months. 

I think it's around this moment where I stop caring about what happens to the 
paper. My attitude towards it is "I've already done everything I can, I am still
going to do what I have to get it out, but by now I do not care one bit it if
it gets accepted or if a black hole consumes any and all trace of its existence". 

To be fair, the fact I could think like that was just because by then I had already
given up on academia. If I had been a PhD student, then the added pressure of
having to publish a paper for the thesis would have made everything else worse. 
Good (?) thing I'd already had that experience during the PhD. 

**July 2024 to September 2024**

Thankfully, I was able to distract myself during the vacations, and thanks to the
promise to not resubmit anywhere until everyone is back I got to completely forget
about the paper and my work. I started playing with my collection of Raspberry Pi
boards instead. 

**September 2024 to December 2024**

Whew, we're close to the end, finally. The new decision is to submit to TMLR, a
journal that is supposed to accept any submitted papers, so long as the scientific
work is sound. By this point, I have recovered my wits (still suffering from 
shell PTSD (Linux shell, not artillery), however), and I can go back to working 
on the paper. 

At this point I am also working on skrub, as my post doc contract has ended. The 
good thing about this is that I am finally able to work on something other than
my experiments, freeing up my brain from being constantly haunted by them.

We decide to keep the paper "as-is" for the most part, and keep on improving the 
form, improving the plots, running some additional experiments. This is where I 
start tracking the total time required and run experiments with neural networks.

It's also when I start using the SLURM cluster at Inria, rather than using the 
regular cluster. Out of all the mistakes I made through the past two years, not
switching to the SLURM cluster ASAP was probably the biggest. As it turns out, 
being able to rely on high quality code for scheduling and handling parallel runs
helps, and helps a lot.

Thanks to the SLURM cluster I am able to re-run _all the experiments_ once again, 
and run twice as many _once again_. This would have been completely impossible 
had I kept using the regular cluster. 

**December 2024**

We decide to submit the paper right before Chrismas, to try to sneak in right 
before the moment _everyone_ in the field gets swept up by the NeurIPS + vacations 
period. 

The idea is to send the paper on a Tuesday. I do another mad dash putting together
the final version of the paper, and just as I am about to send the final version
I find out that the submissions had been closed just a day prior. Yep. Stellar x3.

As it turns out, this had been announced a couple weeks before, but I did not 
check on the website, so I did not find out about that until it was too late. 

Result? Weeks wasted, at least one more month until we'd resubmit. 

It's also burnout number 3, but at least this time it's already time for the 
vacations so it's not that bad. I catch a flu and proceed to spread it to my dad,
mom, sister, and niece in the matter of a week. 

**January 2025**

Yippee, yay, amazing. We submit the paper. It is in a pretty good shape, if I do
say so myself. We addressed most of the points that were still outstanding from 
the previous reviews, we added a lot more results, the plots and the text are 
tighter than before. Now it's time to wait for the reviews.

**March 2025** 

We finally get the reviews, and they're quite positive! More experiments to run,
but isn't that always the case? Thankfully, it's nothing too crazy, and by now
I am used to it. Kinda. Still have some of that PTSD. 

There was a bit of a mad rush trying to respond to the reviewers before the end 
of the first review period, but we manage to do it, and now the ball is in the 
reviewers' side of the field.

**April 2024** 

A long radio silence, sometimes interrupted by comments from the reviwers. They 
ask questions, we reply, they seem satisfied. We are still waiting for the 
recommendations from the reviewers. 

**Mid-April 2025** 

After another bout of radio silence, we finally ask the Editor what to do with 
our lives, and the Editor responds by saying they will be taking a decision by 
the end of the next week.

**May 2025**

The paper gets accepted! Now I have until the end of May to submit a camera ready 
version of the manuscript, so that it can finally be published. We did it! I feel 
nothing.

**First week of May 2025**

The paper is finally accepted. What a ride. I still feel nothing. I think I ran
out of things to feel at least two rejections ago. 

The important thing is that it has finally been accepted, and that I am done with 
it. Other than the blog post, of course.

## Where do I go from here? 
Not sure. After burning out in at least three separate occasions, I have now a 
much clearer idea of what I don't want to do for a living: something that puts me
in that condition on a regular basis. 

The paper has some citations, but I am not expecting to see that number increase, 
nor do I particularly care about it. 

However, all things considered it was worth it. Working on this paper taught me
a lot, both on the technical and human side. I also got to work with a lot of 
very, very smart and prepared folks, and I could move to Paris, a city I am 
loving. 

The final message is to not give up. Even if it can get _really_ bad at times,
that does not mean the situation won't improve, and so long as negative experiences
teach you something, it's not all that bad. 

