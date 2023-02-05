---
title: "Intro Embeddings"
date: 2022-04-12T02:02:56+02:00


# weight: 1
# aliases: ["/first"]
tags: ["Embeddings"]
author: "Riccardo Cappuzzo"
# author: ["Me", "You"] # multiple authors
showToc: true
TocOpen: false
draft: true
hidemeta: false
comments: false
description: "Desc Text."
canonicalURL: "https://canonical.url/to/page"
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
I've mentioned "embeddings" in a number of posts so far, but what do I mean by
"embeddings"?
Embeddings are a way of representing "things" in space in such a way that their
position in space reflects the "degree of relatedness" between these things. For
example, the word "king" and the word "queen" should be closer to each other than
the words "king" and "banana", for example. Embeddings can be used to this end:
by using an embedding algorithm such as word2vec or fastText we can obtain a
vector (a list of real numbers) for each of these words. Then, we can measure
the distance in space between these vectors to find how similar these words are.

In fact, let's do just that by using the gensim library (in fact, I'll be
following some of the steps defined in the [gensim tutorial for word2vec](https://radimrehurek.com/gensim/auto_examples/tutorials/run_word2vec.html#sphx-glr-auto-examples-tutorials-run-word2vec-py) ).

First, we need to install the library:

```py
pip install --upgrade gensim
```

Then, load a pretrained model from the gensim-data repository. Note that this
will download the entire corpus of vectors in your `~` folder (in my case, my
Windows user folder on Windows), and this corpus can be quite large.
The `word2vec-google-news-300` corpus used here has size 1662.8 MB, so be careful
with that if you have a limited connection! This corpus has been pretrained over
the Google News corpus, and is free to use for stuff like this, or maybe a bit
more serious than what I'm showing.

```py
>>> import gensim.downloader as
>>> wv = api.load('word2vec-google-news-300')
```

The "wv" variable contains a vector for each word in the vocabulary of the model.
This does not mean that all possible words are present in the model! Indeed,
out-of-vocabulary terms are a big problem especially for earlier models such as
word2vec, and are one of the main reasons why I developed EmbDI  in the first
place.

We can use the `wv` variable to access the vectors for "king" and "queen" and
find out if they're actually close to each other.
```py
>>> wv.similarity('king', 'queen')
0.6510957
>>> wv.similarity('king', 'banana')
0.13649082
```
Here we're asking the model to measure the cosine similarity between the vector
for "king" and those of "queen" and "banana". As we expected, the first two words
are closer to each other than the first and the second.

These vectors are pretty large with 300 dimensions, which explains why the
corpus is so big:
```py
>>> len(wv)
300000
>>> len(wv['king'])
300
```





But, "what are these embeddings?" I (figuratively) hear you ask. Embeddings are
vectors, that is sequences of real numbers that describe coordinates in a space.
While we'used to 2-D or 3-D spaces, the spaces embeddings live in tend to be
*high-dimensional*,
which means that rather than three dimensions, we're talking about hundreds of
dimensions. This is where I always lose people when I explain what I work on,
and it's hard to blame someone for having a hard time imagining a space with
300 dimensions!

Indeed, it's impossible to directly "see" these embeddings and their positioning
in space. This does not mean that these vectors are impossible to visualize in
any way. Indeed, a number of methods are available to this end, ranging from the
usual [PCA]() or [t-SNE]()  projections, to alternative methods such as heatmaps.
