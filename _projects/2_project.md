---
layout: page
title: SEM Image Segmentation with Deep Learning Techniques
description: general pipeline for grain-based segmentation
img: assets/img/ML_SEM/binary.png
importance: 2
category: Current Projects
giscus_comments: false
---
First, I have to thank [Dr. Tammy Rittenour](https://www.usu.edu/geo/people/faculty/rittenour-tammy) and [Dr. Michael Strange](https://www.usu.edu/geo/people/researchers/strange-michael) for having insightful conversations with me and offering the SEM data to save my deep learning project back to life!

This is the binary mask of the segmented result, which literally means now we know the coordinates of all the grains being segmented out. 
<div style="text-align: center;">
    <img src="/assets/img/ML_SEM/binary.png" style="width: 30%; margin: 0 auto; display: block;" />
</div>
<div class="caption">
    Binary Mask of the Segmentation Result
</div>
More interesting stuff can be done based once we know where each grain is, which means we are able to segment each individual out, like analyzing grain types (indicated by EDS results), grain morphology, percentages, and more. Due to the fact that I don't own this data, the original EDS map color-coded by the elementary content better not to be shared at this moment, so as to more details. A little teaser is down here, will update after obtaining permissions!
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/ML_SEM/idx66_ele_combo.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Each grain has a unique ID. By inputting this ID, you can retrieve a combined output of the same grain mapped with different elements.
</div>
The pipeline was initially built to segment loose sand thin sections cut from IODP 354 cores microphotograhed under PPL and corresponding XPL views. The original goal was to: 1) segment grains, and 2) build an open-source benchmark dataset for siliciclastic grains (feldspar, quartz, and rock fragments). However, due to the complexities of the various rock fragment types and the overlapping relationships between grains, that project is currently suspended.

Nonetheless, the pipeline works quite well for SEM images, which are way less complex after undergoing mineral separation processes. Actually it didn't take me too much time to migrate my data type from thin section images to SEM images because of the well-established pipepline, which will be useful for any grain-based segmentation tasks. While the project isn’t complete, some key challenges have been overcome, including: 1) fine-tuning published segmentation models to fit custom tasks; 2) addressing minor microscopic focus shifts between corresponding images, such as different elementary maps under the same view; and 3) developing a GUI-based labeling and cleaning process. I’m open to collaboration (zgao@ku.edu) and would love to help with tasks that share a similar skill set. Even if you have ideas for applying this pipeline to your data but aren’t sure where to start, feel free to reach out—I’d be happy to chat!