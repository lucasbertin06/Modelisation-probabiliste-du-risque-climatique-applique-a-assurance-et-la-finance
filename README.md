# Projet Environment - Finance & Risk Analysis : ClimateRiskSim

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

## 1. Qu'est ce qui est fait/utilisé :

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

## 4. Conclusion de la simulation :

On finira par afficher les resultats avec :
- Perte moyenne
- Variance
- VaR 99 %
- Expected Shortfall
- Probabilité de ruine
- Capital recommandé

## 5. Objectif réel de ce projet :

Au-delà de la réalisation d'un simple simulateur, ce projet a pour objectif de développer une véritable démarche de modélisation scientifique appliquée à la gestion quantitative des risques.

L'ambition est de partir d'une problématique concrète : "comment le changement climatique influence-t-il le capital de solvabilité d'un assureur ?" puis de construire un modèle probabiliste capable d'y répondre à l'aide de simulations Monte-Carlo.

À travers ce projet, je souhaite démontrer ma capacité à concevoir un modèle mathématique cohérent, simuler des phénomènes aléatoires complexes, analyser statistiquement les résultats obtenus et interpréter les principales mesures de risque utilisées en actuariat, telles que la Value at Risk (VaR), l'Expected Shortfall ou encore la probabilité de ruine.

Le projet a également pour objectif de mettre en pratique plusieurs compétences complémentaires : probabilités, statistiques, programmation scientifique en Python, visualisation de données et développement logiciel. L'ensemble est conçu comme un projet de recherche appliquée, où chaque choix de modélisation est justifié et confronté à différents scénarios climatiques.