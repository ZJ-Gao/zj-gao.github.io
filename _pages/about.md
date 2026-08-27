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
  <img class="profile-img img-responsive" src="/assets/img/avatar_2.jpeg" alt="Profile Image" style="width: 300px; height: auto; max-width: 100%; border-radius: 8px;">
</div>


  <p>
  I recently completed my PhD in geology at the University of Kansas, advised by Dr. Mike Blum. My dissertation traces sand from the Himalayas to the Bengal Fan thousands of kilometers away in the Indian Ocean, reconstructing the dynamic of Earth's largest sediment dispersal system over the past several hundred thousand years.
  </p>

  <p>
  Through my PhD I developed a broad geoscience skill set. I describe and interpret deep-sea sediment cores from IODP Expedition 354 on the Bengal Fan, then date them using multiple geochronology methods: radiocarbon for the most recent deposits, infrared stimulated luminescence (IRSL) for sandy beds beyond the radiocarbon limit, and detrital zircon U-Pb analysis to fingerprint the provenance of these sands in the deep sea. Beyond cores, I use well-log data for basin-scale property mapping and petrophysical calculations, and interpret 3D seismic volumes to characterize subsurface geology.
  </p>

  <p>
  I am equally drawn to the quantitative side of this work. During core description, for example, I recognized two distinct flavors of turbidites but needed to upgrade from qualitative observation to quantitative classification. Unsupervised machine learning let me do that across nearly 1,000 turbidites in the Bengal Fan. The same mindset drives my computer vision work (an open-sourced deep learning pipeline for mineral grain segmentation) and the data tools I built during industry internships at Oxy and Civitas Resources to guide well placement and completion design.
  </p>

  <p>
  I am genuinely passionate about building automated workflows and mining insights from geological data. I am looking for roles where I can bring this combination of geoscience and data science to high-impact problems in exploration, energy, climate, or environmental science.
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