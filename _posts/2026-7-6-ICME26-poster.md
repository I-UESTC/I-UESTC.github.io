---
title: 团队路怒推理研究成果在IEEE ICME 2026作海报展示
image: images/2026_ICME_poster_01.png
author: gu_yu
tags: ICME
last_modified_at: ""
---

<!-- excerpt start -->
2026年7月5日至9日，IEEE International Conference on Multimedia and Expo（ICME 2026）在泰国曼谷举行。作为多媒体领域的重要国际学术会议，ICME汇聚了来自世界各地高校、科研机构及产业界的研究人员，围绕多媒体分析、视觉理解、多模态智能、生成式人工智能等方向的最新研究成果展开交流。团队路怒推理研究工作《Road Rage Reasoning: Task Definition and a Vision-Language Model (VLM)-Based Framework》入选本届大会，并在“Multimodal LLMs and Vision-Language Reasoning”专题海报环节进行展示与交流。
<!-- excerpt end -->

该研究面向真实驾驶环境中的路怒问题，探索视觉语言模型（Vision-Language Models，VLMs）对潜在路怒诱发事件进行感知、理解与推理的能力。不同于传统情感计算主要关注驾驶员已经产生的情绪状态，研究进一步将关注点前移至可能诱发路怒情绪的外部驾驶事件，希望通过及时理解交通环境中的情绪诱因，为后续主动情感调节提供信息基础。

{:.center}
{%
include figure.html
image="images/2026_ICME_poster_01.png"
caption="团队在IEEE ICME 2026展示路怒推理研究成果"
width="800px"
%}

研究首先对“路怒推理（Road Rage Reasoning）”任务进行了系统定义，从环境线索感知、驾驶事件识别和场景分类三个层次考察视觉语言模型对驾驶视频的理解能力，并构建了包含100段真实驾驶视频及超过2.2万帧细粒度标注的数据集。研究通过对多种主流视觉语言模型进行系统评估发现，现有模型在细粒度视觉感知、关键目标识别以及驾驶事件理解方面仍存在明显不足，并容易受到训练数据统计先验的影响。

在此基础上，研究进一步提出了一种结合VLM视觉编码能力与MLP解码器的高效推理框架，通过利用视觉语言模型提取驾驶场景的视觉特征，实现对不同类型路怒相关驾驶场景的快速识别。相关研究为视觉语言模型在复杂真实驾驶环境中的细粒度理解提供了新的实证结果，也为后续面向路怒诱因识别与主动情感调节的人机交互研究奠定了基础。

本次论文被安排在大会“Poster Session 1: Multimodal LLMs and Vision-Language Reasoning”环节进行展示。现场围绕多模态大模型、视觉语言理解与推理等前沿问题开展了广泛交流。通过海报展示与讨论，团队与来自不同国家和地区的研究人员就视觉语言模型在复杂动态场景中的感知与推理能力、驾驶场景理解以及多模态智能等问题进行了深入交流。
