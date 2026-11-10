---
layout: project
title: Quest!
description: Quest is a 3D isometric tactics game inspired by tabletop RPGs. Players explore a hex-based overworld, discover randomized encounters, and fight turn-based battles where breaking cover can open new routes across the map.
short_description: A 3D isometric tactics game where you explore a hex-based overworld, fight turn-based battles, and use cover to control the battlefield.
projectlink: https://spiritboundstudios.itch.io/quest
image: /assets/Projects/Quest/bannercardvertical.png
hero: /assets/Projects/Quest/hero.mp4
media: []
tags: [Roguelike, Unity, 3D]
start_date: April 2026
end_date: June 2026
order: 2
featured: true
---

<div class="project-feature">
<div markdown="1" class="project-feature-content">

## Hex Grid & Movement

- Built a hex grid in Unity and C# that maps tiles to world positions and uses axial and cube coordinates for neighbor and distance calculations.
- Developed a custom tool to paint terrain, set tile elevation and cover, and place or erase obstacles.
- Implemented A* pathfinding with a hex-distance heuristic and a fallback that routes units to a walkable tile beside a blocked destination.
- Tracked tile occupancy and walkability as entities entered, moved across, or left the grid.

</div>

<video autoplay muted loop controls playsinline class="project-feature-image">
    <source src="/assets/Projects/Quest/hexmapbuilder.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>
</div>

<div class="project-feature">
<div markdown="1" class="project-feature-content">

## Destructible Cover

- Designed destructible cover so players could open new movement routes by breaking obstacles during combat.  
- Implemented enemy pathfinding logic that evaluates whether breaking through cover would get an enemy to the player faster than going around it.
</div>
<video autoplay muted loop controls playsinline class="project-feature-image">
    <source src="/assets/Projects/Quest/destruction.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>
</div>

<div class="project-feature">
<div markdown="1" class="project-feature-content">

## Randomized Overworld Encounters

- Implemented randomized encounters as players traverse the hex-based overworld.
- Separated overworld exploration from combat, using dedicated battle maps for turn-based encounters.
</div>
<video autoplay muted loop controls playsinline class="project-feature-image">
    <source src="/assets/Projects/Quest/overworld.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>
</div>