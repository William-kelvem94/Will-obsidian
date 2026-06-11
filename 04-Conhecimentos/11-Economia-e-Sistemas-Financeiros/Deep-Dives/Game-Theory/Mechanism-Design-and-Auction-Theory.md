---
type: deep-dive
topic: Game Theory
domain: Economics
links: ["[[03-Sistemas-Formais-e-Exatas]]"]
tags: [mechanism-design, auction-theory, incentive-compatibility]
---

# Mechanism Design and Auction Theory

## Incentive Compatibility and Revelation Principle
A mechanism is a pair $(f, \pi)$ where $f$ is an outcome function and $\pi$ is a payment rule. A mechanism is **Incentive Compatible (IC)** if for every player $i$, reporting their true type $\theta_i$ maximizes their utility:
$$u_i(\theta_i, \theta_{-i}) \geq u_i(\hat{\theta}_i, \theta_{-i}), \quad \forall \hat{\theta}_i \in \Theta_i$$
The **Revelation Principle** states that any equilibrium of any mechanism can be replicated by a direct-revelation mechanism where truth-telling is a Nash equilibrium.

## Vickrey-Clarke-Groves (VCG) Mechanisms
The VCG mechanism ensures efficiency and strategy-proofness. The outcome $x^*$ maximizes social welfare:
$$x^* = \arg \max_{x \in X} \sum_{i=1}^n v_i(x, \theta_i)$$
The payment $p_i$ for player $i$ is the externality they impose on others:
$$p_i = \left( \max_{x \in X} \sum_{j \neq i} v_j(x, \theta_j) \right) - \sum_{j \neq i} v_j(x^*, \theta_j)$$

## Auction Theory and Revenue Maximization
In a first-price sealed-bid auction, bidders submit $b_i$. The highest bidder wins and pays $b_i$. In a second-price (Vickrey) auction, the highest bidder wins but pays the second-highest bid $b_{(2)}$.

### Revenue Equivalence Theorem
Under certain conditions (risk-neutral bidders, independent private values), any mechanism that assigns the object to the bidder with the highest value and yields zero utility to a bidder with the lowest possible value will result in the same expected revenue for the seller.

### Optimal Auction Design (Myerson's Lemma)
To maximize revenue, the seller implements a mechanism based on **virtual valuations** $\psi(\theta)$:
$$\psi(\theta) = \theta - \frac{1 - F(\theta)}{f(\theta)}$$
where $F$ is the CDF and $f$ is the PDF of the valuations. The seller awards the item to the bidder with the highest positive virtual valuation.
