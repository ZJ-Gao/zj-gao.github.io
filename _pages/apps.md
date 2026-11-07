---
layout: page
title: Apps
permalink: /apps/
description: Small tools I design and build in my spare time.
nav: true
nav_order: 3.5
---

{% include apps_style.liquid %}

{% for app in site.data.apps %}
<div class="app-card" id="{{ app.name | slugify }}">
  <div class="app-head">
    <img src="{{ app.icon | relative_url }}" alt="{{ app.name }} icon">
    <div>
      <h2>{{ app.name }}</h2>
      <p class="app-tagline">{{ app.tagline }}</p>
      <div class="app-platforms">{{ app.platforms | join: " · " }}</div>
    </div>
  </div>
  <p>{{ app.description }}</p>
  <div class="app-tags">{% for t in app.tags %}<span>{{ t }}</span>{% endfor %}</div>
  <div class="app-links">
    {% for l in app.links %}<a href="{{ l.url }}" target="_blank" rel="noopener"><i class="{{ l.icon }}"></i>{{ l.label }}</a>{% endfor %}
  </div>
  {% if app.screenshots %}
  <div class="app-shots">
    {% for s in app.screenshots %}<img src="{{ s | relative_url }}" alt="{{ app.name }} screenshot" loading="lazy">{% endfor %}
  </div>
  {% endif %}
</div>
{% endfor %}
