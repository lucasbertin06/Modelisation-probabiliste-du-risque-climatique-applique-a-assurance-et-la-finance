# Projet Environment - Finance & Risk Analysis : ClimateRiskSim

# Version Francaise / French Version :

Face au changement climatique, les aléas naturels ne sont plus une exception mais une norme de plus en plus coûteuse. Avec ClimateRiskSim, l'objectif est de mesurer l'incertitude financière qui pèse sur les portefeuilles d'assurance pour repondre à : quel capital un assureur doit-il immobiliser aujourd'hui pour survivre aux crises climatiques extrêmes de demain ? 

Grâce à la modélisation stochastique, cette plateforme évalue la vulnérabilité des acteurs financiers face au réchauffement global et offre un cadre d'analyse décisionnel pour anticiper la ruine.

Pour cela, j'ai muni le projet des bibliotheques suivantes :

- numpy : calcul numérique
- scipy : lois de probabilité et optimisation
- pandas : manipulation de données
- matplotlib : graphiques
- plotly : visualisations interactives (optionnel)
- statsmodels : statistiques
- scikit-learn : pour la partie prédictive
- jupyter : pour les expérimentations
- pytest : pour tester le code

## 1. Qu'est ce qui est fait / utilisé :

Ici, on fait intervenir des domaines tel que :

- la theorie des risques
- les probabilités
- les statistiques
- les simulations de Monte-Carlo
- l'actuariat

<br>

Avec ces outils, on ca essayer de modeliser une compagnie d'assurance fictive spécialisée dans les catastrophes naturelles.

<br>

Pour modéliser cela, nous allons prendre comme catastrophes les :
- inondations
- incendies de forets
- tempetes

<br>

Et nous allons ensuite les associés à différentes caractéristiques :
- fréquence
- coût
- précision d'étude
- gravité

<br>

## 2. Modele mathématique utilisé :

Nous utilisons le : Modele de risque collectif (CRM)

Ce modele est utilisé puisqu'il est classique en actuariat, relativement simple et suffisament realiste pour ce projet !

Nous allons alors simuler sur une année un ensemble de catastrophes ainsi que le coût associé et enfin on additionnera les pertes.

<br>

## 3. Representation du changement climatique :

Pour cela, il se va de le representer par deux facteurs :
- La fréquence des catastrophes naturelles en hausse
- La gravité de ces dernieres qui augmentent aussi

<br>

Pour permettre une simulation qui montre différentes conclusions, l'utilisateur du simulateur pourra alors choisir au début différentes fréquences et taux de gravité, et plus important, choisir la catastrophe de son choix. <br>
L'utilisateur pourra alors apres différentes simulations comparer les différents scénarios entre eux.  

<br>

## 4. Conclusion de la simulation :

On finira par afficher les resultats avec :
- Perte moyenne
- Variance
- VaR 99 %
- Expected Shortfall
- Probabilité de ruine
- Capital recommandé

<br>

## 5. Objectif réel de ce projet :

Au-delà de la réalisation d'un simple simulateur, ce projet a pour objectif de développer une véritable démarche de modélisation scientifique appliquée à la gestion quantitative des risques.

L'ambition est de partir d'une problématique concrète : "comment le changement climatique influence-t-il le capital de solvabilité d'un assureur ?" puis de construire un modèle probabiliste capable d'y répondre à l'aide de simulations Monte-Carlo.

À travers ce projet, je souhaite démontrer ma capacité à concevoir un modèle mathématique cohérent, simuler des phénomènes aléatoires complexes, analyser statistiquement les résultats obtenus et interpréter les principales mesures de risque utilisées en actuariat, telles que la Value at Risk (VaR), l'Expected Shortfall ou encore la probabilité de ruine.

Le projet a également pour objectif de mettre en pratique plusieurs compétences complémentaires : probabilités, statistiques, programmation scientifique en Python, visualisation de données et développement logiciel. L'ensemble est conçu comme un projet de recherche appliquée, où chaque choix de modélisation est justifié et confronté à différents scénarios climatiques.

<br>

# Version Anglaise / English Version : 

Faced with climate change, natural hazards are no longer an anomaly, but a increasingly costly new norm. With **ClimateRiskSim**, the objective is to measure the financial uncertainty weighing on insurance portfolios to answer a critical question: **How much capital must an insurer set aside today to survive tomorrow’s extreme climate crises?**

Through stochastic modeling, this platform evaluates the vulnerability of financial actors facing global warming and offers a decision-making framework to anticipate ruin.

For this purpose, the project is equipped with the following libraries:

- numpy : numerical computation
- scipy : probability distributions and optimization
- pandas : data manipulation
- matplotlib : graphics and visual rendering
- plotly : interactive visualizations (optional)
- statsmodels : statistical modeling
- scikit-learn : predictive algorithms
- jupyter : experimentation and prototyping
- pytest : code testing and validation

<br>

## 1. What is Done / Used:

This project involves fields such as:

- Risk theory
- Probability
- Statistics
- Monte Carlo simulations
- Actuarial science

<br>

Using these tools, we try to model a fictitious insurance company specializing in natural disasters.

<br>

To model this, we consider the following natural disasters:
- Floods
- Forest fires
- Storms

<br>

And we associate them with different characteristics:
- Frequency
- Cost
- Study precision
- Severity

<br>

## 2. Mathematical Model Used:

We use the **Collective Risk Model (CRM)**.

This model is used because it is a classic in actuarial science, relatively simple, and realistic enough for this project!

We will simulate over a one-year period a set of disasters as well as the associated costs, and finally, we will aggregate total losses.

<br>

## 3. Representation of Climate Change:

Climate change is represented by two main factors:
- The increasing frequency of natural disasters
- The rising severity of these events

<br>

To enable simulations that demonstrate different conclusions, users can select initial frequencies, severity rates, and, most importantly, choose the disaster of their choice. <br>
After running various simulations, users will be able to compare different scenarios with one another.

<br>

## 4. Simulation Conclusion:

We conclude by displaying the results with:
- Average Loss
- VaR 99%
- Expected Shortfall
- Probability of Ruin
- Recommended Capital

<br>

## 5. Main Objective of This Project:

Beyond creating a simple simulator, the main goal of this project is to develop a true scientific modeling approach applied to quantitative risk management.

The ambition is to start from a concrete problem: *"How does climate change influence an insurer's solvency capital?"* and then build a probabilistic model capable of answering it using Monte Carlo simulations.

Through this project, I aim to demonstrate my ability to design a coherent mathematical model, simulate complex random phenomena, statistically analyze the results obtained, and interpret key risk metrics used in actuarial science, such as Value at Risk (VaR), Expected Shortfall, and the probability of ruin.

The project also aims to put into practice several complementary skills: probability, statistics, scientific programming in Python, data visualization, and software development. The whole project is designed as applied research, where every modeling choice is justified and tested against different climate scenarios.