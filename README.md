# Real World Data Storytelling: Cyber Security Attacks

## Group 6 – CIS4930

## Team Members
- Vanessa Campoe – VAC23A – Data Wrangler
- Max Siska – MMS24I – Analyst
- Mateo Linares Figueroa – ML22BZ – Visualization Designer
- Vivianna Loredo – VL22J – Documentation/README Lead

## Project Overview:
Cybersecurity attacks have become one of the most pressing issues in the modern world. They can take down entire systems, leak sensitive data, and
cause real damage to both everyday people and large organizations. Our group decided to dig into a real cybersecurity attack dataset to see what
stories the data could tell us. We wanted to understand how these attacks behave, what patterns show up in network traffic, and what tends to make
certain incidents more severe than others. Using Python, we looked at things like which protocols get targeted most, how packet size plays a role,
and what ports seem to attract the most activity. More than anything, we wanted to make sense of the data and share our findings in a clear,
approachable way regardless of how much someone knows about cybersecurity.

## Why This Dataset Fits:
We chose this dataset because it offered exactly the kind of depth and variety we needed to do a thorough analysis. It is pulled from real network
traffic logs, so there is genuine context behind the numbers rather than just made up data. On the numerical side, it includes things like source
port, destination port, and packet length, which give us plenty to work with when it comes to stats and correlations. It also has strong categorical
columns like protocol, attack type, and severity level, which are perfect for grouping and comparing across different slices of the data. Overall it
gave us a solid foundation to build a meaningful analysis around.

## Research Questions
1. Which attack types show up most frequently and how are they spread across different network protocols like TCP, UDP, and ICMP?
2. Do incidents with higher anomaly scores tend to have a higher severity level, or is there little connection between the two?
3. Is there a pattern in how actions are taken (blocked, logged, ignored) depending on the attack type or severity level?

## Dataset Source
[Kaggle - Cyber Security Attacks](https://www.kaggle.com/datasets/teamincribo/cyber-security-attacks)

## Team Organization Note:
The work was split up by role so everything had a clear owner. The data wrangler handled loading and cleaning the dataset, the analyst took on the 
groupby operations, aggregations, and EDA side of things, the visualization designer is handling the plots and styling, and the documentation lead
took on the markdown, README structure, and overall project narrative. Branches and pull requests were also used to keep work organized on GitHub,
which can be seen in the commit history.
