## A Note for Continuous Bag of Words (CBOW) Algorithm

* The following describe how the CBOW algorithm perform in LLM



" My dog sleeps all day on his cozy futon"



CBOW algorithm predicts the center word for a given set of context words within the window size. 
(Note that the skip-gram model predict the context words for a given set of center words)

For this exercise, the size of the sliding window is set to be 2. Given the size of the sliding window, one-hot vector will be generated as in the description below.





| Location of center words  | Description of sliding window |
| ------------- | ------------- |
| 0  | $${\color{red}My}$$ $${\color{aqua}dog}$$ $${\color{aqua}sleeps}$$ all day on his cozy futon  |
| 1  | $${\color{aqua}My}$$ $${\color{red}dog}$$ $${\color{aqua}sleeps}$$ $${\color{aqua}all}$$ day on his cozy futon   |
| 2  | $${\color{aqua}My}$$ $${\color{aqua}dog}$$ $${\color{red}sleeps}$$ $${\color{aqua}all}$$ $${\color{aqua}day}$$ on his cozy futon   |
| 3  | My $${\color{aqua}dog}$$ $${\color{aqua}sleeps}$$ $${\color{red}all}$$ $${\color{aqua}day}$$ $${\color{aqua}on}$$ his cozy futon   |
| 4  | My dog $${\color{aqua}sleeps}$$ $${\color{aqua}all}$$ $${\color{red}day}$$ $${\color{aqua}on}$$ $${\color{aqua}his}$$ cozy futon   |
| 5  | My dog sleeps $${\color{aqua}all}$$ $${\color{aqua}day}$$ $${\color{red}on}$$ $${\color{aqua}his}$$ $${\color{aqua}on}$$ futon  |
| 6  | My dog sleeps all $${\color{aqua}day}$$ $${\color{aqua}on}$$ $${\color{red}his}$$ $${\color{aqua}on}$$ $${\color{aqua}futon}$$      |
| 7  | My dog sleeps all day $${\color{aqua}on}$$ $${\color{aqua}his}$$ $${\color{red}on}$$ $${\color{aqua}futon}$$      |
| 8  | My dog sleeps all day on $${\color{aqua}his}$$ $${\color{aqua}on}$$ $${\color{red}futon}$$      |

Above structure can be expressed as one-hot vector which is input of the CBOW Algorithm.

| One-hot vector for center word  | One-hot vector for context words |
| ------------- | ------------- |
| [1, 0, 0, 0, 0, 0, 0, 0, 0]  | [0, 1, 0, 0, 0, 0, 0, 0, 0]  |
|                              | [0, 0, 1, 0, 0, 0, 0, 0, 0]  |
| 1  | $${\color{aqua}My}$$ $${\color{red}dog}$$ $${\color{aqua}sleeps}$$ $${\color{aqua}all}$$ day on his cozy futon   |
| 2  | $${\color{aqua}My}$$ $${\color{aqua}dog}$$ $${\color{red}sleeps}$$ $${\color{aqua}all}$$ $${\color{aqua}day}$$ on his cozy futon   |
| 3  | My $${\color{aqua}dog}$$ $${\color{aqua}sleeps}$$ $${\color{red}all}$$ $${\color{aqua}day}$$ $${\color{aqua}on}$$ his cozy futon   |
| 4  | My dog $${\color{aqua}sleeps}$$ $${\color{aqua}all}$$ $${\color{red}day}$$ $${\color{aqua}on}$$ $${\color{aqua}his}$$ cozy futon   |
| 5  | My dog sleeps $${\color{aqua}all}$$ $${\color{aqua}day}$$ $${\color{red}on}$$ $${\color{aqua}his}$$ $${\color{aqua}on}$$ futon  |
| 6  | My dog sleeps all $${\color{aqua}day}$$ $${\color{aqua}on}$$ $${\color{red}his}$$ $${\color{aqua}on}$$ $${\color{aqua}futon}$$      |
| 7  | My dog sleeps all day $${\color{aqua}on}$$ $${\color{aqua}his}$$ $${\color{red}on}$$ $${\color{aqua}futon}$$      |
| 8  | My dog sleeps all day on $${\color{aqua}his}$$ $${\color{aqua}on}$$ $${\color{red}futon}$$      |



