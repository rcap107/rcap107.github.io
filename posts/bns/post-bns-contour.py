# %% [markdown]
# ---
# title: Learning contour plots for theorycrafting
# date: 2025/04/06
# draft: true
# categories:
#   - code
#   - games
#   - "blade and soul"
#   - plotting
# ---
# Today's blog post will be another entry in my collection of "using games as excuse
# to learn stuff that might be useful at work". Specifically, I will be trying to
# learn how [contour plots](https://en.wikipedia.org/wiki/Contour_line) work by
# applying formulas that are used in games.
#
# In this case, it'll be again about Blade and Soul and its damage formula, which
# I explained in more detail in a [previous blog post](/posts/bns/post-bns-intro.qmd),
# which you might want to read before continuing here. Don't worry, I'll wait!
#
# ## The objective: figure out which stats should be upgraded first
# After figuring out how damage works, my next step is then deciding how to plan
# my upgrades to prioritize specific attributes. In this case, I was interested
# in finding out what's more important between **Critical Rate** (Crit%) and
# **Critical Damage** (CDmg). Having a higher critical rate means that more attacks are
# critical hits in general, while having a higher critical damage means that critical
# attacks hit harder.
#
# What's important to note is that, past a certain point, AP is by far the hardest
# attribute to increase, and critical rate is easier to come by than critical damage.
# AP sources are more limited than other stats (soulshields do not give AP, at
# least for the time being), and it is normal to hover around the same AP value
# for a long time.
# On the other hand, the two critical stats can be found on most equipment, although
# a specific amount of critical rate (say, 100) will correspond to a lower
# amount of critical damage by a lower amount (say 60).
#
# As a result (and at the time of writing), most characters will have an AP value
# between 600 and 800, and a Critical rate and Critical damage in the
# 500 to 2500 range.
#
# Given all this, I had two questions I wanted to answer: what's the impact of
# CDmg over my final Damage value?
# Should I sacrifice Crit% on purpose in order to have more CDmg, or should I
# keep both attributes somewhat balanced?
#
# A way of doing this could be plotting the damage formula as a function of two
# of the three variables, and try to draw some conclusions from there.
# As a reminder, the main "Damage" formula is this:
# $$
# Damage = AP \times (Crit\% \times CDmg + (1-Crit\%))
# $$
# Then, in order to get from the attributes shown on the character page to those
# in the formula, I need to use the other two equations:
# $$
# Crit\% = \frac{Crit \times 96.98979}{Crit + 1124.069}
# $$
# where $Crit$ is the _Critical rate_ attribute.
# $$
# CDmg = \frac{CD \times 290.8}{CD + 2102.36} + 125
# $$
# where $CD$ is the _Critical damage_ attribute.
#
# Given all this, we can use contour plots to get some indicative answers.
#
# ## What are contour plots, and why do I want to use them?
# Contour plots are a type of plot that is typically used to represent functions
# of two variables on a flat plane. The function may be a mathematical function
# (like in the case I will consider), but also a geographical representation of
# a region.
#
# In this case, I was inspired to use contour plots by a different blogger, who
# used contour plots for a different videogame (see
# [here](https://big-stupid-jellyfish.github.io/GFMath/pages/newerquip)).
# I found contour plots to be quite interesting and fairly easy to understand and
# show to people. An added bonus was that I have never used them anywhere, so this
# could be another "learning experience" to then bring back to my daily job.
# After writing some code using matplotlib, I thought it could be interesting
# to try out the plotly library, for added interactivity and because I have never
# given it a good try.
#
# Introduction out of the way, it's time to write some code.

# %%
# First off, the mandatory imports
import numpy as np
import plotly.graph_objects as go


# %%
# Now I will define some utility functions based on the equations described above.
def fun_crit(crit_attr):
    return (96.98979 * crit_attr) / (1124.069 + crit_attr)


def fun_cdmg(cdmg_attr):
    return (290.8 * cdmg_attr) / (2102.36 + cdmg_attr) + 125


def damage_formula(ap, crit_attr, cdmg_attr):
    crit = fun_crit(crit_attr)
    cdmg = fun_cdmg(cdmg_attr)
    # Dividing by 100 to convert to probability
    return ap * (crit / 100 * cdmg / 100 + (1 - crit / 100))


# %%
# x = crit rate
# y = crit damage
# z = damage
AP = 700
x = np.linspace(700, 2500, 100)
y = np.linspace(500, 2500, 100)

z = AP * (fun_crit(y) / 100 * (fun_cdmg(x) / 100 - 1) + 1)

fig = go.Figure(
    data=[
        go.Contour(
            x=x,
            y=y,
            z=z,
            contours=dict(showlabels=True, labelfont=dict(size=12, color="white")),
        ),
    ],
    layout=dict(
        width=800,
        height=600,
        xaxis_title="Critical Damage",
        yaxis_title="Critical rate",
    ),
)
fig.show()

# %%
y = np.linspace(650, 720, 50)
x = np.linspace(1500, 1700, 50)
# y = np.linspace(500, 2500, 100)

crit = 1500

z = y * (fun_crit(crit) / 100 * (fun_cdmg(x) / 100 - 1) + 1)

fig = go.Figure(
    data=[
        go.Contour(
            x=x,
            y=y,
            z=z,
            contours=dict(showlabels=True, labelfont=dict(size=12, color="white")),
            hovertemplate="CDmg: %{x:.0f} - AP: %{y:.0f} - Damage: %{z:.0f}",
            colorbar=dict(nticks=20, tickmode="auto"),
            ncontours=20
        ),
    ],
    layout=dict(
        width=640,
        height=600,
        xaxis_title="Critical damage",
        yaxis_title="AP",
        title_text="Critical damage vs AP - 1500 crit",
    ),
)
fig.show()
# %%
