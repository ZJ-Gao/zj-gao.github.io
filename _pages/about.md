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

<div style="float: right; margin-left: 22px; margin-bottom: 10px; max-width: 100%; text-align: center;">
  <img class="profile-img img-responsive" src="/assets/img/avatar.jpg" alt="Profile Image" style="width: 300px; height: auto; max-width: 100%; border-radius: 8px;">
</div>


  <p>
  I am a PhD candidate at the University of Kansas (graduating May 2026) working at the intersection of data science and geoscience. I specialize in building machine learning pipelines for complex, messy natural datasets, from deep-sea sediment cores to SEM imagery.

  </p>

  <p>
  My technical toolkit includes Python (scikit-learn, PyTorch, Pandas), statistical modeling, and computer vision. I've applied unsupervised learning algorithms (GMM, K-means, DBSCAN) to classify sediment deposits from sparse core measurements, and built an end-to-end deep learning pipeline using Meta's Segment Anything Model for automated mineral grain segmentation, which I open-sourced on GitHub. During industry internships at Occidental and Civitas Resources, I developed Python ETL (Extract, Transform, Load) pipelines to integrate heterogeneous geoscience datasets and created Spotfire analytics tools that informed well placement, well spacing and completion design decisions.
</p>

<p>
  What sets me apart is my ability to combine quantitative rigor with domain expertise. I understand the geology behind the data, which helps me build models that are not just statistically sound but scientifically meaningful. I'm drawn to roles where I can apply transferable data science skills to high-impact problems in exploration, climate, or environmental science.
</p>

<p>
  I welcome collaboration and discussion. Feel free to reach out.
</p>
<!-- News -->
<div class="news mt-3 p-0">
  <h1 class="title mb-4 p-0" style="color: var(--global-text-color);">news</h1>
  {% assign news = site.news | reverse %}
  {% for item in news limit: site.news_limit %}
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