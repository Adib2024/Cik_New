# Video, motion & 3D skill stack

Claude Code loads every folder in `.claude/skills/` as a skill when a session opens this repo.
These were copied from upstream on 2026-11-07. Each folder keeps the upstream LICENSE.
`.git`, `.github` and (for motionmaxxing) `docs/` were left out.

| Group | Skill folder(s) | Source repo | Commit |
|---|---|---|---|
| Video | `hyperframes`, `hyperframes-cli`, `hyperframes-registry`, `reverse-any-video`, `media-use`, `remotion-to-hyperframes`, `slideshow`, `style-sampling`, `figma` | heygen-com/hyperframes | 7b1d9cc |
| Video | `remotion-*` (13 skills) | remotion-dev/skills (no LICENSE file upstream) | a2824c6 |
| Video | full app, git submodule at `vendor/OpenMontage` | calesthio/OpenMontage | d21f5d4 |
| Motion | `gsap-*` (8 skills) | greensock/gsap-skills | aed9cfd |
| Motion | `video-shotcraft` | Vincentwei1021/video-shotcraft | 1266a3e |
| Motion | `motionmaxxing` | Tejashmakwana/motionmaxxing | 8c8ec0f |
| Blender | MCP server + Blender add-on, git submodule at `vendor/mcp-for-blender` | ahujasid/mcp-for-blender | 2e4b0bc |
| Blender | 94 skills (`blender-director`, `blender-modeler`, `*-style`, `genre-*`, ... plus shared `references/`) | arjun988/blender-skills | 904f095 |
| Blender | `dream-loop` | achimala/dream-loop | 9bddb90 |
| 3D Web | `threejs-*` (9 skills) | majidmanzarpour/threejs-game-skills | 8286774 |
| 3D Web | `anatomy` | wheresryan22/anatomy | 1482e84 |
| 3D Web | `3dviz-pro-max` | viettranx/3dviz-pro-max | d077e0e |

## Setup notes

- **Submodules**: after cloning, run `git submodule update --init` to fetch `vendor/OpenMontage` and `vendor/mcp-for-blender`.
- **hyperframes**: needs Node.js and FFmpeg. Update with `npx hyperframes skills update`.
- **Blender skills** (blender-skills, dream-loop, mcp-for-blender) need Blender running on your **own computer**.
  Install the add-on (`vendor/mcp-for-blender/addon.py`) in Blender, then add the MCP server to Claude Code:
  `claude mcp add blender -- uvx mcp-for-blender`. They will not work in a cloud session.
- **Updating**: re-copy from the source repos above. The commit column shows which version is here now.
