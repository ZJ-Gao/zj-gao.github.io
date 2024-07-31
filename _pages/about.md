---
layout: page
permalink: /
# title: about
nav: false

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

<div style="float: right; margin-left: 20px; margin-bottom: 10px; max-width: 100%; text-align: center;">
  <img class="profile-img img-responsive" src="{{ 'avatar.jpg' | prepend: '/assets/img/' | prepend: site.baseurl | prepend: site.url }}" alt="Profile Image" style="width: 300px; height: auto; max-width: 100%;">
</div>


<p>
  I am a PhD student at the <a href="https://geo.ku.edu/" target="_blank">Geology Department</a> of the <a href="https://www.ku.edu/" target="_blank">University of Kansas (KU) </a> in Lawrence, KS, advised by <a href="https://geo.ku.edu/people/michael-blum" target="_blank">Dr. Mike Blum</a>, and co-advised by <a href="https://www.researchgate.net/profile/Jennifer-Pickering" target="_blank">Dr. Jennifer Pickering</a> from the <a href="https://caeser.memphis.edu/" target="_blank">CAESER University of Memphis</a>. My dissertation seeks to develop Python-based visualization methods to highlight turbidites and their interbedding relationships in core samples. By analyzing IODP 354 cores through the lens of turbidite, my work strives to unravel both external controls and autogenic processes shaping the evolution of the Bengal Fan during the Pleistocene with a data-driven method.
</p>

<p>
  Previously, I was a master student at the Geology Department of KU, where I attempted to synthesize dolomite and very-high-magnesium calcite under pressurized conditions with <a href="https://geo.ku.edu/people/jennifer-roberts" target="_blank">Dr. Jennifer Roberts</a>.
</p>

<div class="col text-justify p-0">
    <p>
      Before I joined KU, I graduated with a B.E. in Resource Exploration Engineering from the <a href="https://www.cup.edu.cn/pub/xyyww/collegeofgeosciences/introduction/index.htm" target="_blank">College of Geoscience, China University of Petroleum-Beijing</a> . During my time there, I discovered my passion for sedimentology as a career path. Participating in numerous mathematical modeling competitions helped me become a great team player and sparked my preference for solving geological questions with data-driven quantitative methods instead of relying on published models. Additionally, my involvement in various volunteering and community outreach activities ignited my interest in designing and teaching geology courses for students with different levels of prior knowledge.
    </p>
</div>

<!-- News -->
<div class="news mt-3 p-0">
  <h1 class="title mb-4 p-0">news</h1>
  {% assign news = site.news | reverse %}
  {% for item in news limit: site.news_limit %}
    <div class="row p-0">
      <div class="col-sm-2 p-0">
        <span class="badge light-green darken-1 font-weight-bold text-uppercase align-middle date ml-3">
          {{ item.date | date: "%b %-d, %Y" }}
        </span>
      </div>
      <div class="col-sm-10 mt-2 mt-sm-0 ml-3 ml-md-0 p-0 font-weight-light text">
        <p>{{ item.content | remove: '<p>' | remove: '</p>' | emojify }}</p>
      </div>
    </div>
  {% endfor %}
</div>
