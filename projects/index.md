---
title: Research
nav:
  order: 2
  tooltip: works, datasets, and more
---

# {% include icon.html icon="fa-solid fa-wrench" %}Research

This page highlights the main research directions of our laboratory. We focus on cutting-edge advancements in artificial intelligence, machine learning, and data science, with applications across various domains including computer vision, natural language processing, and smart technologies. Our team is dedicated to pushing the boundaries of innovation and solving real-world challenges through interdisciplinary research.

{% include section.html %}

## Affect Analysis

<b>EmoTake: Exploring Drivers’ Emotion for Takeover Behavior Prediction</b>
{:.center}
{%
  include figure.html
  image="images/EmoTake.png"
  caption="Overview of EmoTake"
  link="research/#highlighted"
  width="800px"
%}

The blossoming semi-automated vehicles allow drivers to engage in various non-driving-related tasks, which may stimulate diverse emotions, thus affecting takeover safety. Though the effects of emotion on takeover behavior have recently been examined, how to effectively obtain and utilize drivers’ emotions for predicting takeover behavior remains largely unexplored. We propose EmoTake, a deep learning-empowered system that explores drivers’ emotional and physical states to predict takeover readiness, reaction time, and quality. The key enabler is a deep neural framework that extracts drivers’ fine-grained body movements from a camera and interprets them into drivers’ multi-channel emotional and physical information (e.g., facial expression, and head pose) for prediction. Our study (N = 26) verifies the efficiency of EmoTake and shows that: 1) facial expression benefits prediction; 2) emotions have diverse impacts on takeovers. Our findings provide insights into takeover prediction and in-vehicle emotion regulation.

{%
  include button.html
  type="source"
  link="https://github.com/yibingweng/EmoTake"
  icon="fa-brands fa-github"
  text="Source"
  tooltip="Follow us on GitHub"
  flip=true
  style="bare"
%}
[1] Gu Y, Weng Y, Wang Y, et al. EmoTake: Exploring Drivers' Emotion for Takeover Behavior Prediction[J]. IEEE Transactions on Affective Computing, 2024.[PDF](https://github.com/I-UESTC/I-UESTC.github.io/raw/main/assets/EmoTake_Exploring_Drivers_Emotion_for_Takeover_Behavior_Prediction.pdf)
