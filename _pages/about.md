---
layout: page
permalink: /
# title: about
nav: false

social: true
<!--description: <a href="https://ai.google/" target="_blank">Google AI</a> -->
address: <a href="https://www.google.com/maps/place/Lawrence,+KS/@38.9734813,-95.2921264,13z/data=!3m1!4b1!4m6!3m5!1s0x87bf40c7ce479883:0x151713d50478ab2e!8m2!3d38.9716689!4d-95.2352501!16zL20vMHQ2aGs?entry=ttu" class="page-description" target="_blank">Lawrence, KS, USA </a>
---

<div class="col p-0 pt-4 pb-4">
  <h1 class="pb-3 title text-left font-weight-bold">Zijie Gao</h1>
  <h6 class="m-0 mb-2" style="font-size: 0.83em;">{{ page.description }}</h6>
  {% if page.address %}
      <h6 class="m-0 mb-2" style="font-size: 0.83em;">{{ page.address }}</h6>
  {% endif %}
</div>

<!-- Introduction -->

<style>
  .about-photo { float: right; margin: 0 0 10px 22px; text-align: center; }
  .about-photo img { width: 300px; height: auto; max-width: 100%; border-radius: 8px; }
  @media (max-width: 767px) {
    .about-photo { float: none; margin: 0 auto 1.25rem; }
    .about-photo img { width: 220px; }
  }
</style>
<div class="about-photo">
  <img class="profile-img img-responsive" src="/assets/img/avatar_2.jpeg" alt="Profile Image">
</div>


  <p>
  I recently completed my PhD in geology at the University of Kansas, advised by Dr. Mike Blum. I am a quantitative sedimentologist, and my work combines detailed core description with new applications of geochronology. My dissertation focuses on the Bengal Fan, Earth's largest submarine fan, built from Himalayan sediment carried by the Ganges and Brahmaputra rivers. In deep-sea cores drilled nearly 1,400 km from the shelf edge, I described more than 1,000 sediment gravity flow deposits bed by bed. Because bed-scale data like these come mostly from confined basins, the dataset offers a baseline for how flows in an unconfined fan partition sand and mud. Among these deposits, rare meters-thick sand beds account for nearly half of the total thickness. Coarse sand has little reason to travel this far, so these beds likely record unusually powerful events. Yet their timing was known only indirectly from the surrounding mud. Using luminescence, a method still rarely applied to deep-sea sediments, I dated the sands themselves and extended direct ages beyond the reach of radiocarbon. These ages now anchor a source-to-sink synthesis that tests how Himalayan climate signals travel to the deep sea, and how much of that history the fan preserves.
  </p>

  <p>
  Alongside my PhD, I completed geology internships at Oxy and Civitas Resources, where I built Python and Spotfire tools that integrate well, seismic, and microseismic data to guide well placement and completion design. I like building things with code, from data workflows in research and industry to small iPhone and Mac apps in my spare time. Now I am looking for roles that bring geoscience and data science together in exploration, energy, climate, or environmental science.
  </p>

<!-- Apps -->
{% include apps_style.liquid %}
<div style="clear: both;"></div>
<h1 class="title mb-2 p-0" style="color: var(--global-text-color);">apps I build</h1>
<div class="app-strip">
  {% for app in site.data.apps %}
  <a class="app-chip" href="{{ '/apps/' | relative_url }}#{{ app.name | slugify }}">
    <img src="{{ app.icon | relative_url }}" alt="{{ app.name }} icon">
    <div>
      <div class="app-chip-name">{{ app.name }}</div>
      <div class="app-chip-tag">{{ app.tagline }}</div>
    </div>
    <i class="fa-solid fa-arrow-right app-chip-arrow"></i>
  </a>
  {% endfor %}
</div>

<!-- News -->
<div class="news mt-3 p-0">
  <h1 class="title mb-4 p-0" style="color: var(--global-text-color);">news</h1>
  {% assign news = site.news | reverse %}
  {% assign sticky_news = news | where: 'sticky', true %}
  {% assign normal_news = news | where_exp: 'item', 'item.sticky != true' %}
  {% assign remaining = site.news_limit | minus: sticky_news.size %}
  {% if remaining > 0 %}
    {% assign filler = normal_news | slice: 0, remaining %}
    {% assign display_news = sticky_news | concat: filler %}
  {% else %}
    {% assign display_news = sticky_news %}
  {% endif %}
  {% assign display_news = display_news | sort: 'date' | reverse %}
  {% for item in display_news %}
    <div class="row p-0">
      <div class="col-sm-2 p-0">
        <span class="badge font-weight-bold text-uppercase align-middle date ml-3" 
              style="background-color: var(--global-theme-color); color: var(--global-badge-text-color);">
          {{ item.date | date: "%b  %Y" }}
        </span>
      </div>
      <div class="col-sm-10 mt-2 mt-sm-0 ml-3 ml-md-0 p-0 font-weight-light text" 
           style="color: var(--global-text-color);">
        <p>{{ item.content | remove: '<p>' | remove: '</p>' | emojify }}</p>
      </div>
    </div>
  {% endfor %}
</div>