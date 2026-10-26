---
title: "Competitive Programming"
description: "Kattis, Codeforeces and more"
pubDate: 2026-10-04
tags: ["CP"]
draft: false
---

Some random notes about competitive programming.

Some of my old blogs (mainly solutions, in Chinese) can be found in [Luogu](https://www.luogu.com.cn/user/217300/article)

### Oct-04:

##### Finding the ring of a pseudotree

```cpp
void dfs(int o){
    for(int to: e[o]){
        if(fr[to] && to!=fr[o]){
            //[...]
        }
    }
}
```

Say u-v is the additional non-tree edge, both u-v and v-u reaches ``//[...]`` part.

Instead, start with leaves and repeatedly remove nodes with degree 1 instead.

##### Using std::unordered_map and std::unordered_set

Their reallocation is exceptionally slow, especially when hashing is expensive. 

Use ``.reserve()`` to provide extra space when possible. 

### Oct-18

Always do background research on your teammates in icpc-styled competitions.

Whats their favourite IDE, what compiler / environment?

What about keyboard layout? Are they using Russian keyboard?

How do we adjust?

--- 

Also, always think twice on ``<`` vs ``<=``.

