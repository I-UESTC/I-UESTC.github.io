---
---

# Research Statement

The ever accelerating process of urbanization enables modern people to live conveniently in a fully-connected world, urging for rich and real-time physiological and psychological healthcare services. To this end, Intelligent Interaction (I+) lab aims to integrate promising tools from diversified fields like Signal Processing (SP), Artificial Intelligence (AI), Machine Learning (ML) and Hardware Design (HD) to develop innovative technologies and systems for smart ambient sensing and context understanding with a focus on pervasive computing and affective computing.


{% include section.html %}

<div class="row">
  <div class="column left-column">
    <h2>News</h2>
    {% include news-simple-list.html limit=15 prefix="home-" %}
    <div class="view-all-link">
      <a href="{{ '/blog' | relative_url }}" class="view-more">
        View all news <span class="arrow">→</span>
      </a>
    </div>
  </div>
  
  <div class="column right-column">
    <h2>Open Resources</h2>
    {% include figure.html
      image="images/EmoTake.png"
      caption="EmoTake: A dataset exploring drivers' emotional states and their impact on takeover behavior prediction in semi-automated vehicles, using camera-based detection to interpret facial expressions and body movements."
      link="https://github.com/yibingweng/EmoTake"
      width="400px"
    %}
    
    {% include figure.html
      image="images/Gu_RRR_v1.png"
      caption="Gu-RRR-v1: A comprehensive dataset containing 81 dashcam videos of potential road rage scenarios, with detailed frame-by-frame annotations of environmental conditions, ego vehicle movements, and critical objects that trigger driver anger in various traffic situations."
      link="https://yibingweng.github.io/Gu-RRR-v1/"
      width="400px"
    %}
  </div>
</div>

<style>
  .row {
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
  
  .view-all-link {
    margin-top: 0.75rem;
    text-align: right;
  }
  
  .view-more {
    font-size: 0.9rem;
    color: #666;
    text-decoration: none;
    transition: color 0.2s ease;
  }
  
  .view-more:hover {
    color: #557A95;
  }
  
  .arrow {
    display: inline-block;
    transition: transform 0.2s ease;
  }
  
  .view-more:hover .arrow {
    transform: translateX(3px);
  }
  
  /* Improved mobile responsiveness */
  @media (max-width: 768px) {
    .row {
      flex-direction: column;
    }
    
    .column {
      width: 100%;
    }
    
    .left-column {
      overflow: visible;
      width: 100%;
      margin-bottom: 2rem;
    }
  }
</style>
