---
layout: jerules
title: Spells
content_type: Journey’s End 
headers:
 - tier-1-spells
 - tier-2-spells
order: 8
---

# Spells {#spells}
This section details each spell. Each spell has the following.

## Class Requirement
Each spell is available for a unique class.

## Tier Requirement
Each spell has a Tier Requirement based on its Class Requirement. For instance, a Priest spell with a Tier 2 requirement can only be taken if you are a Tier 2 Priest.

## Learn Cost
Each spell costs Skill Points in order to learn.

## Use Cost
Each spell costs resources to use. Spells use Mana.

## Tier
The Tier of the spell denotes how much you can augment it when you use it.

## Description
The description for the effect of the spell. Sections written in Bold denote Augment Effects.

{% assign spells = site.je-spells | where: "content_type", "Spell" %}
{% for i in (1..10) %}
{% assign tier_spells = spells | where: "tier", i %}

{% if tier_spells.size > 0 %}
# Tier {{ i }} Spells {#tier-{{ i }}-spells}

{% for spell in tier_spells %}
## {{ spell.title }} {#{{ spell.slug }}}

{% if spell.concentration %}
**Use Cost:** {{ spell.use_cost }} (Concentration)
{% else %}
**Use Cost:** {{ spell.use_cost }}
{% endif %}**Learn Cost:** {{ spell.learn_cost }}

{{ spell.content }}
<div class="break"></div>
<div class="spell-lists">
    {% if page.spell_lists %}
      <span class="bold">Spell Lists:</span>
      {% assign spell_link_items = '' | split: ', ' %}
      {% assign known_class = false %}
      {% for list in page.spell_lists %}
        {% for class in site.je-classes %}
          {% if class.class == list.list %}
            {% assign link = '<a href="' | append: class.url | append: '">' | append: class.class | append: '</a>' %}
            {% assign spell_link_items = spell_link_items | push: link %}
            {% assign known_class = true %}
          {% endif %}
        {% endfor %}
      {% endfor %}
      {% if known_class %}
        {{ spell_link_items | join: ', ' }}
      {% else %}
        {% for list in page.spell_lists %}
          {% assign spell_link_items = spell_link_items | push: list.list %}
        {% endfor %}
        {{ spell_link_items | join: ', ' }}
      {% endif %}
    {% endif %}
</div>
{% endfor %}

{% endif %}
{% endfor %}
