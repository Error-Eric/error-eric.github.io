---
title: "CoDices Devlog"
description: "A little wish to empower TTRPG using technology"
pubDate: 2026-11-06
tags: ["Dev", "TTRPG"]
draft: false
---

This is written on Nov 6, about 23 PM. I did codeforces early this morning and I'm sleepy as hell. But I plan to release v0.0.1 this weekend and I spent like a hour chatting with AI to think of a name.

In fact, the project didn't go as smooth as I thought. I was initially too ambitious trying to renovate everything from chats to dicebots. I attempted to play with p2p using rust, but it turned out to be too challenging. 

I also tried different strategies. AI one-shot H5 is practically impossible and a waste of tokens. I tried LaTeX templates, worked well until it went super long. I tried static json to H5, and it turns out human could hardly read. And I think MD to H5 is the best comprimise.

Designing the syntax is hard. I want the source MD readable in raw text or vanilla MD, which is basically the idea of MD itself. But that means I can't be too flexible with the gramma syntax. Also, different authors in TTRPG have different habits. It's still uncertain if a work can be converted to MD easily.

People say that front-end dev is dead, and I think so. I practically let AI generate everything, and it worked pretty well. However, I still find some knowledge, although basic, pretty useful. For instance, I know I'm making web app, so I'd want to use JS or TS. To refer to a widget clearly, I'll need to know selectors like `class = "", id = ""` so that I can communicate with AI more efficiently. Having a webpage that looks okay in one-shot is one thing, making AI understand the change is another. And sometimes, AI just don't find where's wrong with a series of buttons, one of which highlighted, having the same gap between them. But a human with eye should tell the imbalance immediately -- in this case, one'd better now how to find which css entry determined its margin or padding. 

Some challenge still lies ahead. What if external resources, like images and musics, are needed to be incoporated into the writting? What about some weird rich texts?
 
