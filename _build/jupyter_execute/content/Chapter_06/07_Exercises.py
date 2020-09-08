## Exercises ##

**1.** A coin is tossed 12 times. Find the chance that

(a) there are six heads

(b) there are more than four tails

(c) one of the faces appears twice as many times as the other

**2.** If you bet on “red” at roulette, your chance of winning is 18/38. Successive bets are independent of each other. Suppose you keep betting on red and stop when you have won a total of six bets.

(a) What is the chance that you place exactly 10 bets?

(b) What is the chance that you place more than 10 bets?


**3.** Each move in the game Monopoly is based on the total number of spots showing on two rolls of a die. Let $X$ be the number of times I see a total of four spots in my next 10 moves in Monopoly. Find $P(X =2)$.

**4.** A class consists of 40 freshmen, 60 sophomores, 30 juniors, and 20 seniors. A simple random sample of 10 students is taken.

(a) Find the distribution of the number of sophomores in the sample.

(b) Find the joint distribution of the numbers of freshmen and sophomores in the sample.

(c) Find the conditional distribution of the number of freshmen in the sample given that there are 4 sophomores in the sample.


**5.** Suppose $X$ has the binomial $(48, 0.16)$ distribution. Define the probability histogram of $X$ to be *rising at $k$* if $P(X = k) > P(X = k-1)$.

(a) Without using `scipy` or any factorials or combinatorial terms, say whether or not the probability histogram of $X$ is rising at 8. 

(b) Is it rising at 7? What about at 9?

**6.** A die is rolled 10 times. Find the chance that the face that has six spots does not appear and every other face appears two times.

**7.** If you bet a dollar on a “split” at roulette, you have a 2/38 chance of winning. If you win the bet, your net gain is \$17. If you lose the bet, you lose your dollar.

Suppose you make 100 bets. Find the chance that you come out ahead, that is, the chance that you end up with more money than you had at the start.

**8.** A city has one million residents, of whom 48% have some college education. A simple random sample of 200 residents is taken.

(a) What is the chance that the majority (more than half) of the sampled residents have some college education?

(b) Find the binomial approximation to the chance in Part (a).

(c) Do you think the binomial approximation in Part (b) is justified? Why or why not?

**9.** Dibya and Jason are playing tennis. The game consists of a sequence of sets. The first player to win $s$ sets wins the match. Suppose the probability that Jason wins a set is $p$ independent of the result of any other set. What is the probability that Jason wins the match?

**10.** A test for a disease produces a correct result with chance 0.99. Suppose the test is run on 300 patients, independently of each other.

(a)  What is the chance that for at least 295 patients the result is correct? Find the numerical value.

(b)  Justify a Poisson approximation for the chance in (a) and find the value of the approximation.

**11.** Seven dice are rolled. Find the probabilities of each of the following events:

(a) exactly two sixes

(b) two fours, two fives, and three sixes

(c) three of one face and four of another

(d) each face appears

(e) three each of two different faces

**12.** The Early Start Denver Model (EDSM) is a developmental behavioral intervention for toddlers diagnosed with Autism Spectrum Disorder. In a [randomized controlled trial](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4951085/) to evaluate the efficacy of ESDM, 48 children were assigned randomly to an ESDM group and a control group. 

You can assume that a simple random sample of 24 children was chosen for the ESDM group and the remainder for the control group. In this exercise you will analyze some of the data from the study using [Fisher's Exact Test](http://prob140.org/textbook/content/Chapter_06/03_Hypergeometric_Distribution.html#fisher-s-exact-test), one of the primary tools used in the paper.

You will need Python to compute numerical values of the probabilities.

(a) As in all RCTs, researchers studied the compositions of the treatment and control groups before the start of the interventions, to see how similar or different the two groups were just due to the random assignment. 

Children in the study had two levels of Autistic Spectrum Disorder, one less severe than the other. Of the 48 children in the study, 9 had the less severe kind, and 3 of them were assigned to the treatment group.  

What is the chance that randomization would result in 3 or fewer of the 9 children with the less severe condition being assigned to the treatment group? Find the numerical value of the chance and say what it suggests about the randomization.

(b) The paper's report of the calculation in Part (a) says, "At baseline, the diagnoses in each group were not significantly different (Fisher’s exact test, P =.461)." What is the relation between the $P$-value reported in the paper and the answer you got in (a)? Explain where the difference comes from and show how the value of $0.461$ arises.

(c) After two years, 7 children in the ESDM group had improved outcomes compared with 1 child in the control group. Use these data and Fisher's exact test to draw a conclusion about whether or not the treatment was beneficial. 

[The authors of the paper performed a more complicated test but their conclusion is consistent with the conclusion here.]


