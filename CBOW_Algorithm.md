## A Note for Continuous Bag of Words (CBOW) Algorithm

* The following describe how the CBOW algorithm perform in LLM



" My dog sleeps all day on his cozy futon"



CBOW algorithm predicts the center word for a given set of context words within the window size. 
(Note that the skip-gram model predict the context words for a given set of center words)

For this exercise, the size of the sliding window is set to be 2. Given the size of the sliding window, one-hot vector will be generated as in the description below.

<code style = "color : red">My</code> in read dog sleeps all day on his cozy futon
My dog sleeps all day on his cozy futon
My dog sleeps all day on his cozy futon
My dog sleeps all day on his cozy futon
