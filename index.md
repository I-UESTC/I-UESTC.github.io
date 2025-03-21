---
---

# Research Statement

The ever accelerating process of urbanization enables modern people to live conveniently in a fully-connected world, urging for rich and real-time physiological and psychological healthcare services. To this end, Intelligent Interaction (I+) lab aims to integrate promising tools from diversified fields like Signal Processing (SP), Artificial Intelligence (AI), Machine Learning (ML) and Hardware Design (HD) to develop innovative technologies and systems for smart ambient sensing and context understanding with a focus on pervasive computing and affective computing.


{% include section.html %}

<!-- Two-column layout container -->
<div class="two-column-container">
  <!-- Left column: News -->
  <div class="column left-column">
    <h2>News</h2>
    {% include list.html data="posts" component="post-excerpt" %}
  </div>
  
  <!-- Right column: Open Resources -->
  <div class="column right-column">
    <h2>Open Resources</h2>
    <div class="resources">
      <!-- Gu-RRR-v1 Dataset -->
      {%
        include figure.html
        image="images/gu-rrr-v1-thumbnail.jpg"
        caption="Gu-RRR-v1: Dataset for Remote Respiration Rate Recognition"
        link="https://yibingweng.github.io/Gu-RRR-v1/"
        width="400px"
      %}
      
      <!-- EmoTake Dataset -->
      {%
        include figure.html
        image="images/emotake-thumbnail.jpg"
        caption="EmoTake: Emotion Recognition Dataset"
        link="https://github.com/yibingweng/EmoTake"
        width="400px"
      %}
    </div>
  </div>
</div>

<!-- CSS for the two-column layout -->
<style>
  .two-column-container {
    display: flex;
    flex-wrap: wrap;
    gap: 2rem;
  }
  
  .column {
    flex: 1;
    min-width: 300px;
  }
  
  .left-column {
    flex-basis: 55%;
  }
  
  .right-column {
    flex-basis: 35%;
  }
  
  .resources {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }
  
  /* Responsive adjustments */
  @media (max-width: 768px) {
    .two-column-container {
      flex-direction: column;
    }
    
    .column {
      width: 100%;
    }
  }
</style>
