---
title: Team
nav:
  order: 1
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team

We are the Intelligent Interaction (I+) Lab, dedicated to advancing smart sensing and context-aware technologies through Signal Processing, AI, Machine Learning, and Hardware Design. Focused on pervasive and affective computing, we foster innovation, inclusivity, and collaboration in tackling real-world challenges.

{% include section.html %}
# faculty
{% include list.html data="members" component="portrait" filter="role == 'pi'" %}
{% include list.html data="members" component="portrait" filter="role == 'ap'" %}

# PhD Student
{% include list.html data="members" component="portrait" filter="role == 'phd'" %}

# Postgraduate Student
# Third-Year
{% include list.html data="members" component="portrait" filter="role == 'Third-Year postgrad'" %}
# Second-Year
{% include list.html data="members" component="portrait" filter="role == 'Second-Year postgrad'" %}
# First-Year
{% include list.html data="members" component="portrait" filter="role == 'First-Year postgrad'" %}

# Undergrad Student
{% include list.html data="members" component="portrait" filter="role == 'undergrad'" %}

