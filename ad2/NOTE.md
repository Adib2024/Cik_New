# Pagewise ad v2: premium motion graphics, NOTE

**Deliverable:** `final.mp4`, 1080x1920, 30 fps, 22.0 s. Source `index.html`; audio `audio/mix.wav`.
Made after the user rejected v1 ("very poor, not professional": slide look, cheap music, no people, stiff animation).

## Story (beat grid 123 bpm, every cut on a beat)
1. 0-2 s: bank counter photo card swings up in 3D: "Bank minta salinan IC?"
2. 2-3.9 s: whip to a stressed woman over paperwork: "Risau disalah guna?" (amber shake)
3. 3.9-13.6 s: **one 3D phone carries three real tools.** Palang IC (screen scrolls from the typed purpose to the stamped preview; push-in; "Dalam telefon sahaja" chip) → turns edge-on → Kecilkan PDF ("3.5 MB → 156 KB" chip + "−96%" slam) → edge-on → Gambar → PDF (three document photos fly into the screen, which scrolls to the page grid)
4. 13.6-16.1 s: 12 real tool icons cascade on 16ths: "30+ alat. Semua percuma."
5. 16.1-18 s: relieved woman with phone: "Tanpa daftar. Tanpa muat naik."
6. 18-22 s: logo slam, "Pagewise", "Cuba percuma sekarang →" tapped → green

## Real vs stock vs illustrative
- Real: every phone screen (BM UI captured from the real tools served from the `palang-ic` repo), 3.5 MB → 156 KB (real output on a 6-page sample scan), tool icons, logo, copy.
- Stock (HeyGen catalog via HyperFrames media-use): music track bgm_001 (123 bpm, from 2.18 s), whoosh/impact/stamp/click/chime SFX, and the three photos of people (bank counter, stressed woman, relieved woman).
- Illustrative: specimen IC and sample documents (marked CONTOH), the CSS phone body, the CTA button.

## Gates (look.py / lint.mjs)
G0 PASS 22.00 s with audio · G2 PASS · G3 PASS, CTA 3.97 s = 18 %, ends in motion · G5 PASS · audio -14.5 LUFS, true peak -1.2 dBFS · cut sync 12/16 (75 %).
By eye: G1 headlines 128-150 px, chips 46-96 px; the phone UI text is small at rest (~0.02 H) but the push and chips carry the reading. G4: the phone or the photo card is the one hero; chips are attached to it.
Motion 3.5/255 by the luma metric (below the human median); every beat has 3D camera/object motion and the blobs drift continuously.

## Would improve
Higher-resolution people photos (stock results were 600-1200 px; shown as cards to stay sharp); a BM voiceover; a real Malaysian setting photo.
