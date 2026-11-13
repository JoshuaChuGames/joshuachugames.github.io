---
layout: jerules
title: Equipment
content_type: Journey’s End 
headers:
    - dwarf
    - elf
    - human
order: 10
---

{% assign equipment = site.je-items | where: "content_type", "Equipment" %}
{% assign weapons = equipment | where: "item_type", "Weapon" %}
{% assign items = equipment | where: "item_type", "Item" %}
{% assign starting_items = items | where_exp: "item", "item.item_subtype contains 'Starting Magical Item'" %}
{% assign armor = equipment | where: "item_type", "Armor" %}

# Weapons {#weapons}

{% for i in (1..10) %}
{% assign weapon_tier = weapons | where: "tier", i %}
{% if weapon_tier.size > 0 %}
# Tier {{ i }} Weapons

| Name | Trait | Range | Damage | Burden | Feature |
| --- | --- | --- | --- | --- | --- |
{% for weapon in weapon_tier -%}
| {{ weapon.title }} | {{ weapon.trait }} | {{ weapon.range }} | {{ weapon.damage }} | {{ weapon.burden }} | {{ weapon.content | strip | newline_to_br | strip_newlines }} |
{% endfor -%}
{% endif %}
{% endfor %}

# Armor {#armor}

{% for i in (1..10) %}
{% assign armor_tier = armor | where: "tier", i %}
{% if armor_tier.size > 0 %}
# Tier {{ i }} Armor

| Name | Damage Threshold Bonus | Feature |
| --- | --- | --- |
{% for armor in armor_tier -%}
| {{ armor.title }} | {{ armor.damage_thresholds }} | {{ armor.content | strip | newline_to_br | strip_newlines }} |
{% endfor -%}
{% endif %}
{% endfor %}

# Starting Magical Items {#starting-magical-items}

| Name | Description |
| --- | --- |
{% for starting_item in starting_items -%}
| {{ starting_item.title }} | {{ starting_item.content | strip | newline_to_br | strip_newlines }} |
{% endfor %}

