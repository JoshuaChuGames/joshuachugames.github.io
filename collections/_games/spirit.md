---
layout: project
title: Spirit
description: Spirit is a turn-based JRPG that follows a knight and a young sorcerer on a journey to cure a strange illness plaguing the lands. Explore a fantastical world of monsters and strange people, slash alongside the knight's sword, and create your own spells to wield!
short_description: A turn-based JRPG where you fight monsters, explore a fantastical world, and create your own spells!
warning: This project is currently in development and may change significantly!
projectlink: 
image: /assets/Projects/Spirit/bannervertical.png
media: []
tags: [2D, Narrative, Godot]
start_date: October 2025
end_date: Present
order: 3
---
<div class="project-feature">
<div markdown="1" class="project-feature-content">

## Cutscene System

- Integrated Godot’s AnimationPlayer with Dialogic so animation and dialogue can pause and resume each other through signals.
- Built editor markers that set actors’ positions and facing directions. Cutscenes wait for actors to reach their marks before playback begins.
- Used story flags to control when cutscenes can play and locked player input during playback.
</div>
<video class="project-feature-image" src="/assets/Projects/Spirit/cutscene.mp4" controls autoplay muted playsinline loop></video>
</div>

<div class="project-feature">
<div markdown="1" class="project-feature-content">

## Combat System

- Built initiative-based turn order and target selection for single combatants, groups, and actions that affect both sides. Invalid targets are filtered out.
- Designed Clint’s multi-strike attacks around directional strike zones. Each input is scored as a miss, OK, or perfect and adjusts that strike’s power.
- Built Kally’s spellcasting around a randomized pool of words. Players combine available words to determine a spell’s effects and power.
</div>
<video class="project-feature-image" src="/assets/Projects/Spirit/combat.mp4" controls autoplay muted playsinline loop></video>
</div>

<div class="project-feature">
<div markdown="1" class="project-feature-content">

## Level & Overworld Zone System

- Built reusable loading zones and entrance markers that place the party at the correct entry point when moving between areas.
- Coordinated player repositioning, camera bounds, music, and ambience during zone transitions, with optional fades and input locking.
- Queued post-battle events so combat outcomes can update story flags, remove NPCs, or trigger follow-up cutscenes.
</div>
<video class="project-feature-image" src="/assets/Projects/Spirit/overworld.mp4" controls autoplay muted playsinline loop></video>
</div>