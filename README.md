# Viagogo Front-Page AB Test Results

## Part I

### Experiment

Our app's home page features 10 event categories to our users.  Which 10 categories we pick has an impact on how many users ultimately buy tickets.

We performed an AB test to compare two category-picking strategies:

  * Strategy A: 'control' -- display the 10 most popular categories.  This is the current behavior of our app.
  * Startegy B: 'variant' -- display the 10 categories nearest to the user's location with events this week.

We are using two metrics to quantify the efficacy of a strategy:

  * 'conversion rate' -- the percentage of home page visitors who buy a ticket
  * 'bounce rate' -- the percentage of home page visitors who left our website immediately

So ideally we want a high conversion rate and a low bounce rate.

### Results

Comparing the 'control' and 'variant' strategies using the conversion rate,

![](img/conversion-rate.png)

we have that the 'control' strategy outperforms the 'variant' strategy every day except for October 18th.  Looking at the total for the entire month, the conversion rate for the control is 5.6% while for the variant it is 5.3%.  Switching our app to the variant strategy could decrease ticket purchases by about 4.6%.

Comparing our strategies using the bounce rate,

![](img/conversion-rate.png)

we have that the 'control' strategy outperforms the 'variant' strategy every single day.  Looking at the total for the entire month, the bounce rate for the control is 39.7% while for the variant it is 41.2%.  Switching our app to the variant strategy could increase visitors abandoning our website by 4.0% (relative change).

DISCUSS NOTABLE TRENDS IN THE METRICS

You can see that there is a spike in the conversion rate on October 18th.  This probably indicates that there was a big event coming up, and users were arriving at the app already decided on buying tickets for that event.

You can see from the conversion and bounce rate graphs that they are negatively correlated.  That is, when the conversion rate is high, the bounce rate is low, and vice-versa.


MENTION any supplementary analysis



### Conclusion

The results show that the 'variant' strategy is worse than our current 'control' strategy.  But is the difference statistically significant?

We have two separate groups (the 'A' and 'B' groups of visitors), and we are measuring the same proportion (conversion rate) for each.  This means that we must use a Two Proportion Z-Test to determine the statistical significance.

## Two Proportion Z-Test

(assuming there is no overlap between A and B groups.  assuming the same person is not recorded twice)

Our null hypothesis is that the conversion rate is equal for the A and B group.  Our alternative hypothesis is that the 'control' population conversion rate is greater than that of the 'variant'.  This is a right-tailed distribution.  The test statistic `z` is:

    z = (p1 - p2) / sqrt(p * (1-p) * (1/n1 + 1/n2))

where

p1 = 0.05558219919855477
p2 = 0.05305114856166729
p = 0.05430630284714648
n1 = 2996337
n2 = 3045853

so that

   z = 13.726287068516598

so that the p-value is less than 0.00001 (due to our very high n), and thus the result IS statistically significant!  We should therefore revert to the control strategy.



IS THERE more data you would like to consider before deciding?





---

## Part II

Having just run the experiment described in Part 1, you are now tasked with coming up with the
next experiment to run on the mobile homepage.

  1. List five potential improvements you would make to the current page. Explain your reasoning.
  2. What additional data would you like to know to help you assess which idea to prioritize?
  3. How would you measure the success or failure of each of these chang



---

## Developer README notes

This repo contains the viagogo case study code.

### Install

To install deps:

	pip3 install -r requirements.txt


### Run

Look at the `main()` function inside `main.py` and modify it according to what information you want to generate.  Then open the terminal and run:

	python3 main.py

