# Pagewise: 15 s promo, NOTE

**Deliverable:** `final.mp4` (1080x1920, 30 fps, 15.0 s, AAC). Editable source: `index.html` (open via `node .claude/skills/motionmaxxing/scripts/render.mjs`). Plan: `STORYBOARD.md`.

## The one idea
The IC copy gets stamped for one purpose as you type, then the green lock badge from Pagewise's own logo lands on the card, and the card becomes the logo.
The lock-on-a-page *is* the Pagewise mark, so a competitor couldn't use this film.

## Beats and what each buys
| frames | beat | buys |
|---|---|---|
| 0-74 | hook: "Nak hantar salinan IC kepada bank?" over a clean specimen IC tilting toward camera | the viewer recognises their own moment of sending an IC copy |
| 75-229 | proof: "Untuk siapa / tujuan" types PINJAMAN PERUMAHAN; the stamp on the card grows with each character; the camera rotates 30° along the stamp and pushes in until "PINJAMAN PERUMAHAN" reads level | the copy is now only good for one purpose |
| 230-334 | turn: "Gambar anda diproses dalam telefon anda sahaja." The green lock badge crashes onto the card. "Tiada apa-apa dimuat naik." | nothing left the phone |
| 335-397 | proof: the real BM tool list races past: "30+ alat. Percuma, tanpa daftar." | it's a whole toolbox, free |
| 398-449 | CTA: logo lands from 3.5x, "Pagewise", "Tanpa muat naik.", drifting smaller | the name |

## Real vs illustrative
- **Real:** every stamp frame (rendered by the real Palang IC tool, served locally from the `palang-ic` repo, pulled from its canvas at 1400x883); the tool list (BM homepage, mobile capture); all copy (the site's own BM strings, e.g. "Gambar anda diproses dalam telefon anda sahaja. Tiada apa-apa dimuat naik."); the logo; 31 tools counted in the repo, so "30+" holds.
- **Illustrative:** the IC is an invented specimen ("KAD PENGENALAN CONTOH", "BUKAN DOKUMEN SEBENAR"), deliberately not a real MyKad. The input field and the lock badge are rebuilt in HTML from the site's CSS and logo, because the mobile capture of the field was covered by the sticky header.
- **Sound:** no ElevenLabs key, so `audio/compose.py` synthesises the music (96 bpm soft pad + pluck, sections on the cuts, a silence 8.55-9.07 s before the badge) and four hits: stamp thump 4.5 s, badge chime 9.07 s, air on the whip 11.17 s, logo bell 13.27 s. -14.9 LUFS integrated, -3.3 dBFS peak. A licensed track can replace it: same cut grid, 96 bpm.

## Gates (draft at 0.5x; final numbers below)
- G0 PASS: 15.00 s, matches --expect.
- G2 PASS: no run of more than 3 flat frames.
- G3 PASS: end hold 0.57 s (ends mid-drift); final shot 1.73 s = 12 % of the film.
- G5 PASS: `lint.mjs`, all checks.
- G1 (by eye): typed field 78 px (0.041 H); the stamp text is about 0.03 H at the push peak, below the 0.04 H target, but it's the tool's own line, level and centred; the BM headline lines are 84-150 px.
- G4 (by eye): one hero per frame (card, or card + badge as one object, list, logo).
- Motion: mean luma change 3.4/255, below the human median 6.8. Deliberately calm for a "clean & premium" privacy brand.

## Frame descriptions (draft sheet)
0.47 s: clean specimen card tilting up, "Nak hantar salinan" rising in. 1.40 s: question complete, "kepada" lit indigo, card settling. 2.33 s: the same, card nearly flat (the longest calm stretch). 3.27 s: input reads "PINJA", the stamp has appeared across the card. 4.20 s: "PINJAMAN PERUM". 5.13 s: full purpose typed; the stamp names it. 6.07 s: camera rotating and pushing along the stamp. 7.00 s: stamp level and centred: "…PINJAMAN PERUMAHAN…". 7.97 s: mint-lit card, "Gambar" arriving. 8.90 s: the first line almost complete. 9.83 s: badge on the card corner, "Tiada apa-apa" rising. 10.77 s: "Tiada apa-apa dimuat naik." complete. 11.70 s: the tool list racing, "30+ alat." shrinking in. 12.63 s: "Percuma, tanpa daftar." 13.57 s: logo + "Pagewise". 14.50 s: "Tanpa muat naik." added, drifting smaller.

## What I'd still improve
- The stamp line's own type is small at the push peak. A higher-resolution source image (e.g. 3000 px wide) would allow a deeper, sharper push.
- 1.4-2.5 s is the calmest stretch. A slower card creep or an earlier cut would tighten it.
- Replace the synthesised score with a licensed track, or add an ElevenLabs BM voiceover.
