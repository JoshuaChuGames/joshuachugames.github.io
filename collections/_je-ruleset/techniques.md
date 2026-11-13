---
layout: jerules
title: Techniques
content_type: Journey’s End 
headers:
 - tier-1-techniques
 - tier-2-techniques
order: 8
---

# Techniques {#techniques}
This section details each technique. Each technique has the following.

## Class Requirement
Each technique is available for a unique class.

## Tier Requirement
Each technique has a Tier Requirement based on its Class Requirement. For instance, a Hero technique with a Tier 2 requirement can only be taken if you are a Tier 2 Hero.

## Learn Cost
Each technique costs Skill Points in order to learn.

## Use Cost
Each technique costs resources to use. Techniques use Stamina.

## Tier
The Tier of the technique denotes how much you can augment it when you use it.

## Description
The description for the effect of the technique. Sections written in Bold denote Augment Effects.

{% assign techniques = site.je-techniques | where: "content_type", "Technique" %}
{% for i in (1..10) %}
{% assign tier_techniques = techniques | where: "tier", i %}

{% if tier_techniques.size > 0 %}
# Tier {{ i }} Techniques {#tier-{{ i }}-techniques}

{% for technique in tier_techniques %}
## {{ technique.title }} {#{{ technique.slug }}}

{% if technique.concentration %}
**Use Cost:** {{ technique.use_cost }} (Concentration)
{% else %}
**Use Cost:** {{ technique.use_cost }}
{% endif %}**Learn Cost:** {{ technique.learn_cost }}

{{ technique.content }}
<div class="break"></div>
<div class="spell-lists">
    {% if technique.spell_lists %}
      <span class="bold">Available For:</span>
      {% assign technique_link_items = '' | split: ', ' %}
      {% assign known_class = false %}
      {% for list in technique.spell_lists %}
        {% for class in site.je-classes %}
          {% if class.class == list.list %}
            {% assign link = '<a href="' | append: class.url | append: '">' | append: class.class | append: '</a>' %}
            {% assign technique_link_items = technique_link_items | push: link %}
            {% assign known_class = true %}
          {% endif %}
        {% endfor %}
      {% endfor %}
      {% if known_class %}
        {{ technique_link_items | join: ', ' }}
      {% else %}
        {% for list in technique.spell_lists %}
          {% assign technique_link_items = technique_link_items | push: list.list %}
        {% endfor %}
        {{ technique_link_items | join: ', ' }}
      {% endif %}
    {% endif %}
</div>
{% endfor %}

{% endif %}
{% endfor %}
