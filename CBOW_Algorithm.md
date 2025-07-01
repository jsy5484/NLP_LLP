# A Note for Continuous Bag of Words (CBOW) Algorithm

; The following notes describe how the CBOW algorithm perform in a natural language processing model.

CBOW algorithm predicts the center word for a given set of context words within the window size. 
(Note that the skip-gram model predict the context words for a given set of center words)


Example sentence is:

" My dog sleeps all day on his cozy futon"


For this exercise, the size of the sliding window is set to be 2. Given the size of the sliding window, one-hot vector will be generated as in the description below.





| Location of center words  | Description of sliding window |
| ------------- | ------------- |
| 0  | $${\color{red}My}$$ $${\color{aqua}dog}$$ $${\color{aqua}sleeps}$$ all day on his cozy futon  |
| 1  | $${\color{aqua}My}$$ $${\color{red}dog}$$ $${\color{aqua}sleeps}$$ $${\color{aqua}all}$$ day on his cozy futon   |
| 2  | $${\color{aqua}My}$$ $${\color{aqua}dog}$$ $${\color{red}sleeps}$$ $${\color{aqua}all}$$ $${\color{aqua}day}$$ on his cozy futon   |
| 3  | My $${\color{aqua}dog}$$ $${\color{aqua}sleeps}$$ $${\color{red}all}$$ $${\color{aqua}day}$$ $${\color{aqua}on}$$ his cozy futon   |
| 4  | My dog $${\color{aqua}sleeps}$$ $${\color{aqua}all}$$ $${\color{red}day}$$ $${\color{aqua}on}$$ $${\color{aqua}his}$$ cozy futon   |
| 5  | My dog sleeps $${\color{aqua}all}$$ $${\color{aqua}day}$$ $${\color{red}on}$$ $${\color{aqua}his}$$ $${\color{aqua}cozy}$$ futon  |
| 6  | My dog sleeps all $${\color{aqua}day}$$ $${\color{aqua}on}$$ $${\color{red}his}$$ $${\color{aqua}cozy}$$ $${\color{aqua}futon}$$      |
| 7  | My dog sleeps all day $${\color{aqua}on}$$ $${\color{aqua}his}$$ $${\color{red}cozy}$$ $${\color{aqua}futon}$$      |
| 8  | My dog sleeps all day on $${\color{aqua}his}$$ $${\color{aqua}cozy}$$ $${\color{red}futon}$$      |

Above structure can be expressed as one-hot vector which is an input of the CBOW Algorithm.

| One-hot vector for center word  | One-hot vector for context words |
| ------------- | ------------- |
| [1, 0, 0, 0, 0, 0, 0, 0, 0]  | [0, 1, 0, 0, 0, 0, 0, 0, 0]  |
|                              | [0, 0, 1, 0, 0, 0, 0, 0, 0]  |
| [0, 1, 0, 0, 0, 0, 0, 0, 0]  | [1, 0, 0, 0, 0, 0, 0, 0, 0]  |
|                              | [0, 0, 1, 0, 0, 0, 0, 0, 0]  |
|                              | [0, 0, 0, 1, 0, 0, 0, 0, 0]  |
| [0, 0, 1, 0, 0, 0, 0, 0, 0]  | [1, 0, 0, 0, 0, 0, 0, 0, 0]  |
|                              | [0, 1, 0, 0, 0, 0, 0, 0, 0]  |
|                              | [0, 0, 0, 1, 0, 0, 0, 0, 0]  |
|                              | [0, 0, 0, 0, 1, 0, 0, 0, 0]  |
| [0, 0, 0, 1, 0, 0, 0, 0, 0]  | [0, 1, 0, 0, 0, 0, 0, 0, 0]  |
|                              | [0, 0, 1, 0, 0, 0, 0, 0, 0]  |
|                              | [0, 0, 0, 0, 1, 0, 0, 0, 0]  |
|                              | [0, 0, 0, 0, 0, 1, 0, 0, 0]  |
| [0, 0, 0, 0, 1, 0, 0, 0, 0]  | [0, 0, 1, 0, 0, 0, 0, 0, 0]  |
|                              | [0, 0, 0, 1, 0, 0, 0, 0, 0]  |
|                              | [0, 0, 0, 0, 0, 1, 0, 0, 0]  |
|                              | [0, 0, 0, 0, 0, 0, 1, 0, 0]  |
| [0, 0, 0, 0, 0, 1, 0, 0, 0]  | [0, 0, 0, 1, 0, 0, 0, 0, 0]  |
|                              | [0, 0, 0, 0, 1, 0, 0, 0, 0]  |
|                              | [0, 0, 0, 0, 0, 0, 1, 0, 0]  |
|                              | [0, 0, 0, 0, 0, 0, 0, 1, 0]  |
| [0, 0, 0, 0, 0, 0, 1, 0, 0]  | [0, 0, 0, 0, 1, 0, 0, 0, 0]  |
|                              | [0, 0, 0, 0, 0, 1, 0, 0, 0]  |
|                              | [0, 0, 0, 0, 0, 0, 0, 1, 0]  |
|                              | [0, 0, 0, 0, 0, 0, 0, 0, 1]  |
| [0, 0, 0, 0, 0, 0, 0, 1, 0]  | [0, 0, 0, 0, 0, 1, 0, 0, 0]  |
|                              | [0, 0, 0, 0, 0, 0, 1, 0, 0]  |
|                              | [0, 0, 0, 0, 0, 0, 0, 0, 1]  |
| [0, 0, 0, 0, 0, 0, 0, 0, 1]  | [0, 0, 0, 0, 0, 0, 1, 0, 0]  |
|                              | [0, 0, 0, 0, 0, 0, 0, 1, 0]  |



## Description of CBOW Algorithm

![image](https://github.com/user-attachments/assets/174a4012-6f6c-4f31-9d07-83f1c31e2198)

CBOW Algorithm can be summarized as above diagram. 

Based on the one-hot vectors in the center words, input layers are

| Input layers | Input vector  | 
| -------------| ------------- | 
| _x_<sub>my</sub> | [1, 0, 0, 0, 0, 0, 0, 0, 0]  | 
| _x_<sub>dog</sub>| [0, 1, 0, 0, 0, 0, 0, 0, 0]  | 
| _x_<sub>sleeps</sub>| [0, 0, 1, 0, 0, 0, 0, 0, 0]  | 
| _x_<sub>all</sub>| [0, 0, 0, 1, 0, 0, 0, 0, 0]  | 
| _x_<sub>day</sub>| [0, 0, 0, 0, 1, 0, 0, 0, 0]  | 
| _x_<sub>on</sub>| [0, 0, 0, 0, 0, 1, 0, 0, 0]  | 
| _x_<sub>his</sub>| [0, 0, 0, 0, 0, 0, 1, 0, 0]  | 
| _x_<sub>cozy</sub>| [0, 0, 0, 0, 0, 0, 0, 1, 0]  | 
| _x_<sub>futon</sub>| [0, 0, 0, 0, 0, 0, 0, 0, 1]  | 

