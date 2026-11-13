---
layout: jerules
title: Races
content_type: Journey’s End 
headers:
    - dwarf
    - elf
    - human
order: 10
---

{% assign races = site.je-races | where: "content_type", "Race" %}

{% for race in races %}
# {{ race.title }} {#{{ race.slug }}}

{{ race.content }}

<div class="break"></div>
{% endfor %}
