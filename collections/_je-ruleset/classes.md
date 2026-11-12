---
layout: jerules
title: Classes
content_type: Journey’s End 
headers:    
    - the-hero
    - the-mage
    - the-monk
    - the-priest
    - the-thief
    - the-warrior

order: 6
---

# Classes {#classes}
This section details each class. Your chosen class grants the following:

## Class Traits
Class traits are improvable traits like Hit Points, Stamina, and Mana.

### Starting Hit Points
Each class has its own starting Hit Points. Regardless of this value, it is a Tier 1 trait when you choose the class.

### Starting Stamina
Each class has its own starting Stamina. Like Hit Points, it is a Tier 1 trait when you choose the class.

### Starting Mana
If your class casts spells, it has a starting Mana. Like Hit Points, it is a Tier 1 trait when you choose the class.

### Evasion
The value for your Evasion. Unlike Traits, Evasion does not have a Tier and thus is not improved by using Skill Points.

### Damage Thresholds
The values for your Minor, Moderate, and Major damage thresholds. For all classes, the starting value for your Minor damage threshold is 0.

### Tier 1 Class Feature
Each class has a unique class feature at Tier 1

### Spell or Technique List
Each class has a specific list of spells or techniques to choose from.

### Starting Equipment
Each class has a unique set of starting items.

## Subclasses
Each class has two subclasses. Your chosen subclass grants the following:

### Tier 1 Subclass Feature
Each subclass has a unique subclass feature at Tier 1

### Primary Trait
Each subclass has a trait it uses any time a spell or technique calls for a check, otherwise known as a Primary check.

{% for class in site.je-classes %}
# {{ class.title }} {#{{ class.title | slugify }}}
{{ class.content }}
{% endfor %}