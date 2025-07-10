---
marp: true
theme: esap_slides
# header: 'Welcome to ESAP!'
---

<!--- _class: lead --->

# Graphs!

---

## Agenda

1. Sets
2. Graphs as Vertices & Edges
3. Directedness & Undirectedness
4. Graph Problems
   1. Isomorphisms
   3. Colorings
   <!-- 2. Paths -->
---


<!--- _class: lead --->

# 1. Sets

---

## Sets, Defined

A **set** is a *collection of "things"*, where those "things" are the **elements** of the set.

By convention, we write a set as the grouping of its elements enclosed in curly braces: `{}`


$$S = \{25, 30, 35, 40, 45\}$$

$$T = \{\text{Harry}, \text{Joel}\}$$

$$U = \{\text{Mon, Tue, Wed, Thu, Fri}\}$$

What names could you give to describe each of these three sets?

---

## Inclusion / Exclusion

Every "thing" is either an element of the set or not an element of the set. 

We use this funny symbol to denote membership in a set: $\in$. We cross it out to denote absence from a set: $\not \in$

If we have a set $S = \{25, 30, 35, 40, 45\}$, then:

$$25 \in S$$
$$26 \not \in S$$
$$30 \in S$$
$$\text{💎}\ \not \in S$$

---

## Some Other Set Definitions

- Sets cannot have any repeated elements. In fact, we would say that $\{1, 1\}$ and $\{1\}$ are really the same set!
- The **cardinality** (or size) of a set is the number of (unique) elements contained in side of it.
  - We denote cardinality of a set $S$ as $|S|$. 
- Sets can be *finite* or *infinite!*
  - The set of days of the week is finite with cardinality of $7$.
  - The set of real numbers between $0$ and $1$ is infinite!

---

## Quick Activities

1. Take the names of the students at your table as a group of "things." *How many different sets can you make out of these names?*
2. What is the cardinality of the set of all possible four-digit phone passcodes?
3. What is the cardinality of the set of home countries for students in this course? (We'll do this one together.)

---


<!--- _class: lead --->

# 2. Graphs as Vertices and Edges

---

## Graphs

A **graph** is a combination of two sets:
1. a set of **vertices**, which are the "things" modeled by the graph.
2. a set of **edges**, which are the relationships or associations *between vertices.*

Graphs are used to model complex relationships between different elements of a problem we're trying to analyze. 


---

## Rock, Paper, Scissors

We can model *games* with graphs. Let's take the game of Rock, Paper, Scissors! 

(Do we all know how to play?)

1. Rock beats Scissors
2. Scissors beats Paper
3. Paper beats Rock


---

## Rock, Paper, Scissors

We can model *games* with graphs. Let's take the game of Rock, Paper, Scissors! 

There are three *gestures* you can make. These will be the vertices:

$$V = \{\text{Rock, Paper, Scissors}\}$$

---

## Rock, Paper, Scissors

We can model *games* with graphs. Let's take the game of Rock, Paper, Scissors! 

$$V = \{\text{Rock, Paper, Scissors}\}$$

```text
1. Rock beats Scissors
2. Scissors beats Paper
3. Paper beats Rock
```
We can model the "rules" of the game as our edges. *Edges always consist of pairs of vertices.*

$$E = \{\text{(Rock, Scissors), (Scissors, Paper), (Paper, Rock)}\}$$


---

## Rock, Paper, Scissors

So, what...?

We can visualize *vertices as circles* and *edges as lines connecting vertices.*

$$V = \{\text{Rock, Paper, Scissors}\}$$
$$E = \{\text{(Rock, Scissors)}, \text{(Scissors, Paper)}, \text{(Paper, Rock)}\}$$

![bg right:30% width:100%](img.svg)


---


## Rock, Paper, Scissors, Fire, Water

We can extend these games, actually! Here's a popular variant.

```text
1. Rock beats Scissors and Water
2. Scissors beats Water and Paper
3. Paper beats Rock and Water
4. Water beats Fire
5. Fire beats Rock, Paper, and Scissors
```

*What are the vertices and edges?* And can you draw the graph?


---


## Rock, Paper, Scissors, Fire, Water

We can extend these games, actually! Here's a popular variant.

```text
1. Rock beats Scissors and Water
2. Scissors beats Water and Paper
3. Paper beats Rock and Water
4. Water beats Fire
5. Fire beats Rock, Paper, and Scissors
```

![bg right:40% width:100%](image.png)

---


<!--- _class: lead --->

# 3. Directedness & Undirectedness

---

## Directed Edges

The edges that we saw in Rock, Paper, Scissors modeled the relationships in the forms of "X beats Y".
- Being assymetric, we say that the edges in this graph are **directed**.
- When it's true that "X beats Y", *it is not also true that Y beats X*!
- In our figure, we modeled this directedness by putting an arrow on the end of the edge, e.g. $Rock \rightarrow Scissors$

---
## Undirected Edges

The relationships between vertices in a graph can be **undirected**, or symmetric always.

For example:
- *Marriage* is a symmetric, undirected relationship: if $P_1$ is married to $P_2$, it's always also true that $P_2$ is married to $P_1$. 
- *Geographic adjacency* between buildings is undirected: the Moore Building and Levine Hall are connected, so Levine Hall and the Moore Building are connected.

---
## Undirected Edges as Double-Directed Edges

Undirected edges can be modeled with directed edges.
- If we have $(A, B) \in E$ and $(B, A) \in E$, then there is a symmetric & undirected relationship between $A$ and $B$ in the graph. 
- When drawing them, we could use two arrows (i.e. $A \leftrightarrow B$) or simply one line without arrows (i.e. $A — B$).


---

## Directedness Activities

If a graph consists of only undirected edges, we can call it an **undirected graph**. Otherwise, it is a **directed graph**. (All undirected graphs can be modeled as directed graphs.)

Consider a graph with vertices $V = \{A, B, C, D\}$


1. If $E = \{(A,B), (B, C), (C, D)\}$, is the graph directed or undirected?
1. If $E = \{(A,B), (B, A), (B, C), (C, D)\}$, is the graph directed or undirected?
1. If $E = \{(A,B), (B, A), (B, C), (C, B)\}$, is the graph directed or undirected?

---

## Being Lazy is Important

*Sometimes, we just call a graph "undirected" and then assume that (A, B) is an undirected edge always between A and B.*


(This is, like, a little imprecise but in practice it saves a lot of time and writing when we're working with undirected graphs and life is precious and short so let's just run with it shall we?)


---

## Thinking About Symmetry

Can you come up with...
1. two directed graphs that model two different assymmetric relationships?
2. two undirected graphs that model two different symmetric relationships?

---

## Edges Activity

![bg right width:100%](radial.svg)

How many *undirected* edges can we draw in a graph that looks like this?

$$V = \{A, B, C, D, E, F\}$$
$$E = ???$$

---

## Edges

![bg right width:100%](edges_radial.svg)

How many *undirected* edges can we draw in a graph that looks like this?

$$V = \{A, B, C, D, E, F\}$$
$$E = \text{i'm not writing it all out, it's in the picture over there}$$
$$|E| = 15$$


---

## Edges

How many *undirected* edges can we draw in a graph with $n$ edges? 

| $n$ | max # of edges |
| --- | -------------- |
| 4   |                |
| 5   |                |
| 6   | 15             |
| n   |                |


---

## Edges

How many *undirected* edges can we draw in a graph with $n$ edges? 

| $n$ | max # of edges     |
| --- | ------------------ |
| 4   | 6                  |
| 5   | 10                 |
| 6   | 15                 |
| n   | $\frac{n(n-1)}{2}$ |

---

## "Combinatorial" Proof for Max Edge Count

1. From any of our $n$ nodes, we could make a pair from that one and any of the $n - 1$ others. 
2. There are therefore $n(n-1)$ possible vertex pairs that we could describe among our $n$ different nodes.
3. In these possible vertex pairs, for any two arbitrary vertices $A$ and $B$, we would always have both $(A, B)$ and $(B, A)$. However, since we're talking about *undirected* graphs, these both count as the same edge!
4. So, $n(n-1)$ is exactly *twice* the number of possible edges, and the correct total is $\frac{n(n-1)}{2}$.

---

In an undirected graph, the **degree** of a vertex is the number of edges that include that vertex.

What are the degrees in this graph?

| Vertex | Degree |
| ------ | ------ |
| A      |        |
| B      |        |
| C      |        |
| D      |        |
| E      |        |

![bg right width:100%](count_degrees.svg)

---

In an undirected graph, the **degree** of a vertex is the number of edges that include that vertex.

What are the degrees in this graph?

| Vertex | Degree |
| ------ | ------ |
| A      | 2      |
| B      | 3      |
| C      | 1      |
| D      | 2      |
| E      | 0      |

![bg right width:100%](count_degrees.svg)

---

<!--- _class: lead --->


# 4.1 Graph Problems: Isomorphisms

---

## Graph Isomorphism

Two graphs $G$ and $G'$ are **isomorphic** if there exists a **mapping** from vertices in $G$ to vertices in $G'$ such that the edges are preserved under that mapping.

![](isomorphism.svg)

---


![](labeled_isomorphism.svg)

If we map $(A, B, C, D) \rightarrow (1, 2, 3, 4)$, then the edges in the left graph go from:

$$E = \{(A, B), (B, C), (C, D), (D, A)\}$$

to $E' = \{(1, 2), (2, 3), (3, 4), (4, 1)\}$, which are exactly the edges in the right graph!


---

## Find the mapping

![](challenge_isomorphism.svg)

How can you map A-E to 1-5 in order to prove that the graphs are isomorphic?

---

## Find the mapping

![](challenge_isomorphism.svg)

$(A, B, C, D, E) \rightarrow (2, 4, 1, 5, 3)$ gets us there!

---

## Counting Graphs

How many different (non-isomorphic) ways are there to create a graph with $n$ vertices?

| $n$ | # ways |
| --- | ------ |
| 1   |        |
| 2   |        |
| 3   |        |
| 4   |        |


---


![bg](image-1.png)

---

<!--- _class: lead --->


# 4.2 Graph Problems: Colorings

---

## Graph Coloring

A valid **graph coloring** is an assignment of one color to each vertex such that *adjacent vertices have different colors.*

![height:380px](image-2.png)

---

## Graph Coloring: Setting

A valid **graph coloring** is an assignment of one color to each vertex such that *adjacent vertices have different colors.*

---

## Coloring Isn't Always About Colors

The concept of a "color" is really just some label that we use for each vertices. We can use the same kind of thinking to figure out room assignments for classes!

1. If two classes occur at the same time, they can't be held in the same room.
2. Classes are the vertices
3. Time conflicts are the edges
4. A valid coloring is an assignment of rooms to classes such that no two adjacent vertices share the same color.

---

## Color it in

| Class    | Time        | Room |
| -------- | ----------- | ---- |
| CIS 4500 | 12-1:30     |      |
| CIS 4510 | 10:15-11:45 |      |
| CIS 4550 | 10:15-11:45 |      |
| CIS 1100 | 12-1        |      |
| CIS 3333 | 10-11       |      |

Can you draw the graph for this schedule and find the *minimum number of rooms required?* Try starting from 1, 2, ... and find the first one that works.