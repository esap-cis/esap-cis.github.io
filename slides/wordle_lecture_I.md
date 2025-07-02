---
marp: true
theme: esap_slides
--------------------------

<!-- _class: lead -->

# Probability in Practice


---

## Recap: Core Ideas from Wednesday

<table style="border-collapse: collapse; width: 100%; font-size: 0.9em;">
  <thead>
    <tr>
      <th style="text-align: left; border-bottom: 1px solid #ccc; padding: 4px 0;">Concept</th>
      <th style="text-align: left; border-bottom: 1px solid #ccc; padding: 4px 0;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding: 2px 0;">Experiment</td><td style="padding: 2px 0;">Repeatable action with uncertain outcome</td></tr>
    <tr><td style="padding: 2px 0;">Sample Space</td><td style="padding: 2px 0;">All possible outcomes of an experiment</td></tr>
    <tr><td style="padding: 2px 0;">Event</td><td style="padding: 2px 0;">Subset of the sample space with shared features</td></tr>
    <tr><td style="padding: 2px 0;">Probability</td><td style="padding: 2px 0;">Long-run frequency of an event occurring</td></tr>
    <tr><td style="padding: 2px 0;">Expected Value</td><td style="padding: 2px 0;">Average outcome over many trials</td></tr>
    <tr><td style="padding: 2px 0;">Bernoulli Trials</td><td style="padding: 2px 0;">Binary outcomes (Success/Failure), each with its own probability</td></tr>
    <tr><td style="padding: 2px 0;">Law of Large Numbers</td><td style="padding: 2px 0;">With enough trials, experimental ≈ theoretical probability</td></tr>
  </tbody>
</table>

---

## Practice Activity: Revisiting Trials

You're rolling two 15-sided dice that have values 1-15, 1,000 times. 

**Write psuedocode that could estimate the probability that the sum of each dice is between 10 - 20.** We'll code it together after!

Here are functions that could prove useful!
<table style="border-collapse: collapse; width: 100%; font-size: 0.9em;">
  <thead>
    <tr>
      <th style="text-align: left; border-bottom: 1px solid #ccc; padding: 4px 0;">Function</th>
      <th style="text-align: left; border-bottom: 1px solid #ccc; padding: 4px 0;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 2px 0;">random.randint(a, b)</td>
      <td style="padding: 2px 0;">Returns a random integer N such that a ≤ N ≤ b</td>
    </tr>
    <tr>
      <td style="padding: 2px 0;">random.choice(seq)</td>
      <td style="padding: 2px 0;">Chooses a random element from a sequence</td>
    </tr>
    <tr>
      <td style="padding: 2px 0;">random.choices(seq, k=n)</td>
      <td style="padding: 2px 0;">Returns a list of n random elements (with replacement)</td>
    </tr>
    <tr>
      <td style="padding: 2px 0;">random.sample(seq, k=n)</td>
      <td style="padding: 2px 0;">Returns n unique random elements (without replacement)</td>
    </tr>
  </tbody>
</table>

---

## Interpreting Conditional Probability

Conditional probability tells us how likely one event is, given another has occurred.

$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$

**Example:** What’s the probability a card is a Queen **given** it’s a face card?

* $P(Queen \cap Face) = \frac{4}{52}$
* $P(Face) = \frac{12}{52}$

$P(Queen \mid Face) = \frac{4/52}{12/52} = \frac{4}{12} = 0.333$

---

## Practice: Conditional Reasoning

You're told a student got an A in a course.

* 80% of students who studied got an A: $P(A | Studied)$
* 30% of all students studied: $P(Studied)$
* 50% of students got an A: $P(A)$

What is the probability that a student **studied**, given that they got an A?

Use:

$$
P(Studied | A) = \frac{P(A \text{ and } Studied)}{P(A)}
$$

---

## Solution Explanation

Plug in values:

* $P(A | Studied) = 0.8$
* $P(Studied) = 0.3$
* $P(A) = 0.5$

Then:

$$
P(Studied | A) = \frac{0.8 \cdot 0.3}{0.5} = \frac{0.24}{0.5} = 0.48
$$

So there's a 48% chance the student studied.

---

# Reducing Uncertainty

<!-- _class: lead -->

---
## Motivation: Why We Guess

In many problems, we don’t observe the answer directly — we **probe** to gather evidence.

* Diagnosing illness from symptoms
* Debugging code by printing values
* Choosing a password based on failed attempts

**Cryptography** relies on the opposite: it tries to make these deductions practically **impossible**. 

This is why your password is *so secure*. 

---

## From Events to Partitions

Each guess we make splits the sample space:

* Some outcomes ruled out
* Others remain possible

The goal is to **make the partition as informative as possible** — ideally splitting the space evenly.

---

## What Exactly Is a Partition?

When we make a guess, we don’t just check if it's right — we **divide** the space of all possible answers.

<div style="margin-top: 10px;"></div>

* A **partition** breaks up the sample space into **disjoint** subsets
  (i.e. every outcome fits exactly one group, it either could be an answer or it is not)

* Each group corresponds to a possible **feedback** result

---


### Why is this helpful?

* Guesses that create **balanced partitions** (with evenly sized groups) give more information
* Guesses that create **unbalanced partitions** (e.g. one big group, many small) are less helpful


---
## Practice: Binary Search Game

You're trying to guess a number from 1 to 64.

What sequence of **yes/no questions** lets you find the number **as fast as possible**?

> Imagine you had an **oracle** who instantly answers your yes/no questions.

Which questions would you ask first? How many would you need?

*hint: There's a way to solve this by asking in at most 6 questions.*

---

# Representing Language
<!-- _class: lead -->

---

## Transition: From Randomness to Language

Earlier, we saw probability in coin flips and dice rolls, but how can this apply to language?

Thankfully, *natural language* has **structure** — some letters follow others more often.

We can model this using **n-grams**.

---

Here’s a clear, introductory slide to define key terms around language modeling:

---

## Language Definitions

To talk about words and structure, we need to define:

* **Vocabulary**:
  A set of all valid words in our system (e.g., from a dictionary or word list)

* **Character**:
  A single letter (e.g., `A`, `B`, `Z`)

* **Frequency**:
  How often something occurs (e.g., how many times `TH` appears across all words)

These concepts help us reason about language *probabilistically*.

---


## What is an N-Gram?

An **n-gram** is a sequence of `n` characters from a word or sentence.

Examples:

* Unigrams: `T`, `H`, `E`
* Bigrams: `TH`, `HE`, `EN`
* Trigrams: `THE`, `HEN`

After finding the frequency of these **n-grams**, we can start calculating probabilities!

---

## Counting N-Grams

From the vocabulary, count how often sequences occur.

Words: `[THE, THEN, THEM]`

Bi-grams:
- `TH`: 3 times
- `HE`: 3 times
- `EN`: 1 time
- `EM`: 1 time

---

## Counting N-Grams

To build an n-gram model, follow these steps:

1. **Choose a vocabulary**:
   Example: `["THE", "THEN", "THEM"]`

2. **Extract n-grams** from each word:
   From `"THEN"` we get:

   * Bigrams: `TH`, `HE`, `EN`

3. **Tally occurrences**:
   Count how many times each character and each pair appears.

---

### Conditional Probabilities

Once you have counts, compute:

* $P(H \mid T) = \frac{count(TH)}{count(T)}$
  - What's the probability of an H coming after given there's a T?

* $P(E \mid H) = \frac{count(HE)}{count(H)}$
  - What's the probability of an E coming after given there's a H?

These let us **estimate the probability of one letter following another**.

---
## Building Frequency Tables

<pre>
from collections import defaultdict

data = ["THE", "THEN", "THEM"]
bigram_counts = defaultdict(int)
unigram_counts = defaultdict(int)

for word in data:
    for i in range(len(word) - 1):
        unigram_counts[word[i]] += 1
        bigram_counts[word[i:i+2]] += 1
    unigram_counts[word[-1]] += 1

print(bigram_counts)
print(unigram_counts)
</pre>

---

## Using N-Grams to Score Words

We can estimate the likelihood of a word by multiplying its n-gram probabilities.

For `THEME`:

$$
P(THEME) = P(T) \cdot P(H \mid T) \cdot P(E \mid H) \cdot P(M \mid E) \cdot P(E \mid M)
$$

This gives a numeric score. Higher = more natural.

**Why multiply?**

Each step **depends** on the last — a chain of events.

---

## Assumptions in this Model 

For bigrams:

$$
P(word) = P(x_1) \cdot P(x_2|x_1) \cdot P(x_3|x_2) \cdot P(x_4|x_3) \dots
$$

Where $x_i$ is a specific character in the word. 

This is a simplification — we assume only the **previous character** matters. 

*This is called a markov assumption. We don't need to look to far in the past.*

---

## Lecture Activity: Score Some Words

**Bigram Counts:** `TH`:10, `HE`:6, `EN`:4, `HA`:3, `AT`:5, `TE`:2
**Unigram Counts:** `T`:12, `H`:8, `E`:10, `A`:4

Estimate:

* $P(\text{THEN}) = P(T) \cdot P(H|T) \cdot P(E|H) \cdot P(N|E)$
* $P(\text{HATE}) = P(H) \cdot P(A|H) \cdot P(T|A) \cdot P(E|T)$

Which is more likely?

---

## Final Thoughts

Each concept today helps us narrow uncertainty:

* Conditional reasoning tells us how evidence updates belief
* N-grams model structure in language
* Partitioning helps us ask better questions

Your solver should use **probability + structure + strategy**.

---

## Lab Goals

Today, you'll:

* Compute n-gram frequency tables
* Use those to score word likelihoods
* Simulate guessing and feedback
* Write a basic solver that uses information to choose words

We’ll continue refining strategies tomorrow.
