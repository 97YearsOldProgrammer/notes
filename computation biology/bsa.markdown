  # biological sequence analysis #

- [Probability related](#probability-basis)
- [chatper1](#statistic-model)
  - [random sequence model](#random-sequence-model) 
- [chapter2]

----------------------------------------------------------------------------------------------------------------------------

## probability basis ##

| probability concept                                | what it means 
|:--------------------------------------------------:|:--------------- 
| condition probability/ posterior probability       | $P( A \mid B)$
| Bayes' theorem                                     | $P(X, Y) = P( X \mid Y)P(Y)$
| Marginal Probability                               | $P(X) = \sum_{y}P(X, Y) = \sum_{y}P(X \mid Y)P(Y)$ 
| binomial distribution                              | $P(k (1s out of N) ) = \binom{N}{k} p^{k} (1 - p)^{N - k}$
| the gaussian distribution/ aka normal distribution | $f(x) = \frac{1}{σ \sqrt{2\pi } } e^{\frac{-1}{2} { \frac{x - u}{σ} }^{2} }$
| multinomial distribution                           | $P( n \mid \theta) = M^{-1}(n)\sum_{i=1}^{K} \theta i^{ni}$

### condition probability ###

$$P(A \cap B) = P(A)*P(B \mid A)$$

this is some events happening given condition that some events have already happend ,for example, for event A as something might not works, given that event B as something has already set up, the probability of the whole thing could be represented by such probability notation here $P(A \mid B)$, and I still remember $P(A \mid B)$ is not equal to $P(B \mid A)$  

$$\frac{P(A \cap B)}{P(A)} = P(B \mid A)$$

- a real probability question to ponder
  - if we wanna if event $P(A \cup B)$; it's the union notation ; it just means probability of event A and B  
  - we can use formula $P(A \cup B ) = P(A) + P(B) + P(A \cap B)$
    - $P(A \cap B)$ it's the intersection notation ; means probability of event A and B happens

### binomial distribution ###

- **bernoulli distribution** 
- $$P(X = x) = \begin{cases} p & \text{if } x = 1, \\1 - p & \text{if } x = 0.\end{cases}$$
  - this state that every possible trail have a discrete outcome
  - is studied the single trail out there
  - which is either 0(false) and 1(true)
  - binary outcome

- generalizing the bernoulli distribution --> allow multiple trails
  - we would have the **binomial distribution**
 
$$P(k '1's out of N) = \binom{N}{k} p^{k} (1 - p)^{N - k}$$  
- given a finite set
  - consisting of all the possible results of N tries of an experiment
  - it has to be a binary outcome ; either true or false
  - if it's true   ; we give p += 1
  - if it's false  ; we give (p - 1) += 1  

$$\binom{N}{k}$$
- this represent the number of ways of choosing k objectgs from N
  - this is equal to $\frac{N!}{( (N - k)!k! )}$ 

- mean of the overall set distribution
  - $m = \sum_{k P(k)}$

- variance of the overall distribution P
  - $σ^{2} = \sum_{k=1}^{N} {(k-m)}^{2} \binom{N}{k} p^{k} (1-p)^{N-k}$

- there is something that we could use differentiation to count the variance

### the gaussian distribution/normal ###

after we learned the binominal distribution ; given a set of experiment N with given binary trails ; either 1(true) or 0(false) as result , as N --> ∞ , the binominal distribution become the `gaussian distribution` ; and we could rescale the mean and variance to fixed

- rescaled mean and variance ; with given a new variable u 
  - $u = (k - m)$
  - $σ = \frac{ (k - Np) }{ \sqrt{ Np(1 - p) } }$ 

- $f(u) = \frac{1}{2\pi} e^{ \frac{ -u^{2} }{2} }$
  - this said with a limit of a large number of events
  - a binomial distribution become a Guassian 
  - the formula above is the density of that 

### the multinomial distribution ###

this is the generalization form of binomial distribution, this multinomial distribution have to satisfied one condition that `each trail shall be independent to each other` otherwise it don't satisfied the condition for this

- The probability of getting ni occurrences of outcome i is given by
$$P( n \mid \theta) = M^{-1}(n)\sum_{i=1}^{K} \theta i^{ni}$$

- The normalising constant depends on the total number of outcomes observed
$$M(n) = \frac{\prod_{i}ni!}{(\sum_{k}nk)!}$$

whenever k = 2, it turns into the binominal distribution

### beta distribution ###

compared to normal distribution and bernulli distribution
### The dirichlet distribution ###

$\mathcal{D}(\theta \mid \alpha) = Z^{-1}(\alpha) \prod_{i=1}^K \theta_i^{\alpha_i - 1} \delta \left( \sum_{i=1}^K \theta_i - 1 \right)$

------------------------------------------------------------------------------------------

## chatper1 ##

in this chapter, it go overs overall material and some general examples of Bayesian model and it's traditional example for probability analyzation and bayesian statistic, how to pick proper parameter for Bayesian model

### bayesian model ###

this is an easy one out here 

| given condition | value 
|:---------------:|:-------
| P(D) fair dice  | 99%   
| P(d) dishonest  | 1%    
| $P(six \mid d)$ | 50%   

we wanna find more information about this scenario, like $P(six \mid D)$ or $P(six d)$ or $P(six D)$, we can use the baysian theorem to calculate more information with current information

- if we wannt find $P(d \mid 3sixes)$ ; given having three sixes in a roll, what's the probability the dice are all dishonest dice
  - we can apply the baye's theorem out there
  - $P(d \mid 3sixes) = \frac{P( 3sixes \mid d)P(d)}{P(3sixes)}$
  - then we plgu in those values, we would get the values out there 

well it looks like it's easy to calculate, btw it's kinda hard for making a good parameterzation, the whole bayesian model could be work in such formula, there are different strategy for selecting such parameter
$$P(\theta \mid D) = \frac{P(\theta)P(D\mid \theta)}{\int_{\theta'}P(\theta')P(D\mid\theta')}$$
$$P(D) = \int_{\theta'}P(\theta')P(D\mid\theta')$$

- `Bayesian statistic`
  - about which parameter to choose for analyzation in Bayesian model   
- `MAP estimation`
  - strategy that take whatever parameter to make $P(\theta \mid \D)$ largestest 
- mean approximation
  - approach to make parameter as the mean of the posteirior distribution from an estimate perspective 

### a pseudo-counts into bayesian model ###

give observed data with 1, 3, 4, 2, 4, 6, 2, 1, 2, 2, we know that the dice we are using have some sort of loaded dice, which is dishonest for the output, we want to analyze the probability here, make analyzation, so what we are gonna to do, is adding a pseudocount/an additional trail into this data to make everything works, since if we wanna make p5 as a parameter, there is no case of rolling a dice and get 5 back

### random sequence model ###

$$ \prod_{i=1}^{n} qxi = qx1*qx2*qx3....qxn$$

###

----------------------------------------------------------------------------------------------------------------------------

## Chapter2 ##

### introduction ###

- question: whether if two sequences are related
  - 1 use alignment to decide
  - 2 scroing system to rank alignment
  - 3 algorithm for find good scoring alignments
  - 4 statistical methods for evaluation those alignment score

  