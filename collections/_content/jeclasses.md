---
layout: bare
title: Journey's End Classes
permalink: /journeysend/content/classes
hero_icon: fa-solid fa-person-rays fa-8x
mage_icon: fa-solid fa-wand-sparkles fa-8x
monk_icon: fa-solid fa-hand-fist fa-8x
priest_icon: fas fa-person-praying fa-8x
thief_icon: fa-solid fa-eye-low-vision fa-8x
warrior_icon: fa-solid fa-gavel fa-8x
---
{% for class in site.je-classes %}
<div class="section toc" markdown="1">
<div class="section-icon {{ class.icon }}"></div>
<div class="class-content" markdown="1">
{% if class.finished %}

## [{{ class.title }}]( {{ class.url }}) <i class="fa-solid fa-star"></i>

{% else %}

## [{{ class.title }}]( {{ class.url }})

{% endif %}
***{{ class.description }}***

</div>
</div>
{% endfor %}
