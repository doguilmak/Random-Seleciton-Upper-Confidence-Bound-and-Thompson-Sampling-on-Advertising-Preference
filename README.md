
# Random Seleciton, Upper Confidence Bound and Thompson Sampling on Advertising Preference

## Problem Statement

The purpose of this study is to predict which ad will be the most preferred by the customers over the fictitious ads clicked by the users. In this study, there are 3 various type of methods exist. You can find methods as function in **Libraries** file.

## Dataset

Data set is created by myself. Values ​​are generated to be completely random. The dataset has ***9 columns*** and ***2000 rows with a header.***

## Methodology

In this project, as stated in the title, results were obtained through three different methods. These methods are as respectively listed below:

 ***1. Random Selection***
 ***2. Upper Confidence Bound (UCB)***
 ***3. Thompson Sampling***

Three methods were evaluated based on how many times preferred advertisements were actually preferred and these values.

## Analysis

| # | Column | Non-Null Count | Dtype |
|--|--|--|--|
| 0 | ad_1 | 1999 non-null | int64
| 1 | ad_2 | 1999 non-null | int64
| 2 | ad_3 | 1999 non-null | int64
| 3 | ad_4 | 1999 non-null | int64
| 4 | ad_5 | 1999 non-null | int64
| 5 | ad_6 | 1999 non-null | int64
| 6 | ad_7 | 1999 non-null | int64
| 7 | ad_8 | 1999 non-null | int64
| 8 | ad_9 | 1999 non-null | int64

 1. **Random Selection** 
 > Process took 0.4174320697784424 seconds.
 2. **Upper Confidence Bound** 
 > Process took 0.3849928379058838 seconds.
 3. **Thompson Sampling** 
 > Process took 0.5694751739501953 seconds.

### Rewards

| # | Column | Summation
|--|--|--|
| 0 | ad_1 | 615 
| 1 | ad_2 | 647
| 2 | ad_3 | 644
| 3 | ad_4 | 591
| 4 | ad_5 | 794
| 5 | ad_6 | 631
| 6 | ad_7 | 633
| 7 | ad_8 | 653
| 8 | ad_9 | 625

| Model Name | Reward |
|--|--|
| **Random Selection**  | 648 |
| **Upper Confidence Bound**  | 724 |
| **Thompson Sampling**  | 755 |


## How to Run Code

Before running the code make sure that you have these libraries:

 - pandas 
 - matplotlib
 - seaborn
 - time
    
## Contact Me

If you have something to say to me please contact me: 

 - Twitter: [Doguilmak](https://twitter.com/Doguilmak).  
 - Mail address: doguilmak@gmail.com
