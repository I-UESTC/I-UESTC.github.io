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

    <div class="resource-item">
      {% include figure.html
        image="images/IMG_Scene.png" 
        caption="围绕智能驾舱中的情感认知与调节，本项目致力于构建“感知-认知-调节”闭环系统，推动智能驾舱向更安全、更舒适、更人性化的方向发展"
        link="http://118.24.143.121/"
        width="400px"
      %}
      <div class="resource-link">
        <a href="http://118.24.143.121/" class="resource-more">
          查看更多细节 <span class="resource-icon">↗</span>
        </a>
      </div>
    </div>
    
    <div class="resource-item">
      {% include figure.html
        image="images/EmoTake.png"
        caption="EmoTake: A dataset exploring drivers' emotional states and their impact on takeover behavior prediction in semi-automated vehicles, using camera-based detection to interpret facial expressions and body movements."
        link="https://github.com/yibingweng/EmoTake"
        width="400px"
      %}
      <div class="resource-link">
        <a href="https://github.com/yibingweng/EmoTake" class="resource-more">
          Explore dataset <span class="resource-icon">↗</span>
        </a>
      </div>
    </div>
    
    <div class="resource-item">
      {% include figure.html
        image="images/Gu_RRR_v1.png"
        caption="Gu-RRR-v1: A comprehensive dataset containing 81 dashcam videos of potential road rage scenarios, with detailed frame-by-frame annotations of environmental conditions, ego vehicle movements, and critical objects that trigger driver anger in various traffic situations."
        link="https://yibingweng.github.io/Gu-RRR-v1/"
        width="400px"
      %}
      <div class="resource-link">
        <a href="https://yibingweng.github.io/Gu-RRR-v1/" class="resource-more">
          Explore dataset <span class="resource-icon">↗</span>
        </a>
      </div>
    </div>
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
  
  /* Resource styling */
  .resource-item {
    margin-bottom: 2rem;
  }
  
  .resource-link {
    margin-top: 0.5rem;
    text-align: right;
  }
  
  .resource-more {
    font-size: 0.9rem;
    color: #557A95;
    text-decoration: none;
    transition: all 0.2s ease;
    padding: 0.25rem 0.5rem;
    border-radius: 3px;
  }
  
  .resource-more:hover {
    background-color: rgba(85, 122, 149, 0.1);
  }
  
  .resource-icon {
    display: inline-block;
    margin-left: 3px;
    transition: transform 0.2s ease;
  }
  
  .resource-more:hover .resource-icon {
    transform: translate(2px, -2px);
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
