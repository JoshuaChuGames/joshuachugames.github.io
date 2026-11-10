---
layout: project
title: Into the Depths
description: Into the Depths is a 2D roguelike deckbuilder inspired by Slay the Spire. Descend through procedurally generated dungeons, battle a diverse cast of fantasy enemies, and collect cards, feats, and relics to create powerful builds. With unique enemy encounters, strategic turn-based combat, and a variety of possible synergies, each run challenges players to adapt their strategies and experiment with new combinations.
short_description: A roguelike deckbuilder game where you fight monsters to grow more powerful, collecting new cards, items, and feats!
projectlinks: [
    {
        icon: "fa-brands fa-itch-io",
        url: "https://spiritboundstudios.itch.io/into-the-depths",
    },
]
image: /assets/Projects/IntoTheDepths/intothedepths.png
hero: /assets/Projects/IntoTheDepths/devlog.mp4
media: [
    {
        type: "video",
        src: "/assets/Projects/IntoTheDepths/devlog.mp4",
        alt: "Into the Depths - Hero Video"
    }
]
tags: [Roguelike, Godot, 2D]
start_date: December 2023
end_date: December 2024
order: 1
featured: true
---

<div class="project-feature">

<div markdown="1" class="project-feature-content">

## Persistent Deck System

- Designed and implemented a persistent card system to reduce frustration caused by unfavorable card draws.
- Created a set of weaker, always-accessible cards that provide reliable offensive and defensive options without replacing traditional drawn cards.
- Balanced persistent cards against drawn cards to preserve the importance of deckbuilding while giving players greater control over their turns.

</div>
<img class="project-feature-image" src="/assets/Projects/IntoTheDepths/persistentdeck.png" alt="Persistent Deck System" />
</div>

<div class="project-feature">
<div markdown="1" class="project-feature-content">

## Procedural Dungeon Generation
- Developed a randomized dungeon generation system featuring enemy encounters, events, rest areas, and elite battles.
- Implemented encounter selection logic to prevent the same enemy or event from appearing twice consecutively.
- Designed weighted encounter probabilities that increase the likelihood of certain encounters, including rest areas and elite fights, when they have not appeared recently.
</div>
<img class="project-feature-image" src="/assets/Projects/IntoTheDepths/procedural.png" alt="Procedural Dungeon Generation" />
</div>

<div class="project-feature">
<div markdown="1" class="project-feature-content">

## Enemy Design
- Designed a diverse roster of 13 enemies, including 6 bosses, with unique abilities, attack patterns, and status effects.
- Implemented reactive enemy AI with weighted decision-making, allowing enemies to change their behavior based on combat conditions.
- Collaborated with artist Yuuki Matsuda to create visually distinct fantasy enemies, incorporating their appearances and identities into their combat mechanics.
</div>
<img class="project-feature-image" src="/assets/Projects/IntoTheDepths/enemydesign.png" alt="Enemy Design" />
</div>