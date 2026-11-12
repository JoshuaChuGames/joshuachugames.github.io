---
layout: bare
title: Journey's End Abilities
permalink: /journeysend/content/abilities
spell_icon: fas fa-book-open fa-8x
---


<div class="section toc no-border" markdown="1">
<div class="section-icon {{ page.spell_icon }}"></div>
<div class="spell-content" markdown="1">
# Abilities 

## [All Spells](/journeysend/abilities/?type=spells)
{% for class in site.je-classes %}
{% if class.spells %}
- [{{ class.class }} Spells](/journeysend/abilities/?type=spells&class={{ class.class | downcase | replace: " ", "-" }})
{% endif %}
{% endfor %}
## [All Techniques](/journeysend/abilities/?type=techniques)
{% for class in site.je-classes %}
{% if class.techniques %}
- [{{ class.class }} Techniques](/journeysend/abilities/?type=techniques&class={{ class.class | downcase | replace: " ", "-" }})
{% endif %}
{% endfor %}
</div>
</div>