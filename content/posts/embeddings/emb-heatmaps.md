---
title: "Emb Heatmaps"
date: 2022-04-12T01:10:58+02:00


# weight: 1
# aliases: ["/first"]
tags: ["EmbDI", "embeddings"]
author: "Riccardo Cappuzzo"
# author: ["Me", "You"] # multiple authors
showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: false
description: "How I stopped worrying and learned to love projections. "
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
At this point, I have presented EmbDI quite a few times and for different audiences.
Besides all the observations on the experiments, one of my favorite parts is
showing how to plot EmbDI embeddings, and everything that can be gleamed from
those projections.

To be clear, the idea of projecting embeddings from their high dimension spaces
down to a more manageable 2, 3 or about a dozen dimensions is well established
and I did not invent anything. However, by employing the same techniques it
becomes possible to have a better idea of how embeddings encode information.

From what I have seen, there are two main approaches to the problem of "projecting"
embeddings, with the first being the use of a 2- or 3-d projection to have a
"simple" view on a plane or in a space, while the second is the use of heatmaps.
Both solutions rely on the use of projections such as PCA or t-SNE to compress
the vectors.

What I find to be the main advantage that heatmaps have over 3-d projections is
the fact that they allow to keep a larger number of dimensions while remaining
intelligible.

### Examples of heatmaps
The two heatmaps I will be presenting in this post are once again taken from the
IMDB-Movielens dataset, and contain information about movies (hey, out of all the
datasets I've used, they're the easiest to use as an example :P ).

The first heatmap shows the projection of a few pairs of columns, thus modeling
the task of schema matching: what we're trying to do is finding which columns
should be matched together.

From the heatmap, it's pretty clear that paired columns are very similar to each
other (although not in all dimensions), while being pretty different from those
in other pairs. This is a pretty good indication of why the final EmbDI algorithm
is actually selecting similar columns to be placed together. This is also why we
were looking into how to use these projections for adding explainability to our
models.  

Moving on to the second heatmap, in this case we're focusing on table values,
rather than vectors for attributes. In particular, here I have selected a few
movies in Italian, one movie in English and the respective vectors for the
language ("it" and "en").


### Building heatmaps starting from vectors
