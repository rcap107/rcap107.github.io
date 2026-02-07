---
title: "Introducing EmbDI"
date: 2022-04-12T14:07:48+02:00
categories: ["embdi"]
summary: "A short introduction to EmbDI."
---

Out of all the work I've carried out during my PhD, EmbDI is by far the most
important contribution. I've dedicated about half of PhD years working on
designing, developing and implementing the system, and I can say I have been
awarded with a lot of satisfaction from the result. Indeed, there is *a lot* to
talk about here, so I'll be writing a series of posts where I'll go into more
detail than it's reasonably needed to get into "the weeds" of what it was like
to work on EmbDI. This post will act as introduction and as index for later posts.

## What is EmbDI?
EmbDI stands for Embeddings for Data Integration, and is a system that generates
embeddings for tabular data (specifically, CSV tables) and then
uses said embeddings for performing Entity Resolution and Schema Matching. It was
developed during my PhD as a solution to the problem of automating those data
curation procedures and does so remarkably well, beating previous state of the
art systems by a pretty large margin.

While the ideas behind the implementation
of the code were developed together my supervisor (Prof. Paolo Papotti), and another
researcher from a different institution (Dr. Saravanan Thirumuruganathan), I wrote
the vast majority of the code alone. This, of course, means that the code was a
mess, then it got a bit better as I kept on hammering on it to clean up bugs
and make it available to other researchers. The code has its repository on
[github](https://github.com/rcap107/embdi), together with a very
in-depth readme and instructions on how to run it.

EmbDI is written in Python and relies on the usual data science libraries in
Pandas, Numpy and sklearn, as well as the gensim library for training the
embeddings themselves.

The code has been *thoroughly* tested to produce results for a paper that
made it to SIGMOD 2020, which can be
found [here](/static/pubs/sigmod-2020-embdi.pdf).
The slides used for the SIGMOD 2020 presentation are also available
[here](https://docs.google.com/presentation/d/e/2PACX-1vRqWYodB5N6J68WxohcnmxIIWMaac98TwNsM4K8fh15u5wKNQxUtlIpIa7_nebVEeedD8ZhJXgoizPf/pub?start=true&loop=true&delayms=3000).




## How does EmbDI work, in short?
EmbDI is a Python-based data integration system that takes as input relational
tables as CSV files, and returns as output a list of matches of tuples that
represent the same entity (a task I'll call Entity Resolution), or a list of
matches between columns that represent the same attribute (Schema Matching).

![png](/images/embdi/embdi_workflow.png)

The procedure followed by EmbDI is the following:

1. Take a pair of relational tables, then clean them to remove problematic strings and characters.
2. Convert the relational tables into a graph.
3. Traverse the graph by using random walks, then gather the random walks in a training corpus (that is, a text file that contains all the
random walks).
4. Feed the training corpus to the word2vec embeddings training algorithm.
5. Use the geometric properties of the embeddings to find related tuples and columns.

This is, of course, extremely summarized. I would like to explore how EmbDI
works more in depth over the course of a series of blog posts that will go into
far more detail than what I'll do here, so I'll make sure to link back to those
posts once they're ready.
