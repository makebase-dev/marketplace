# Right-to-left and multilingual checks

Run for any page offered in a right-to-left language (Arabic, Hebrew, Persian, Urdu), and the text checks for any multilingual page.

## Layout

- [ ] `dir` and `lang` on `<html>` match the interface language; every passage in another language has its own `lang` (3.1.2).
- [ ] Navigation, reading order and serial-position emphasis start from the right.
- [ ] Directional icons (back, chevrons, forward) mirror; checks, crosses, clocks, clockwise progress rings, media controls and logos do not.
- [ ] Progress bars, sliders and strips of days fill from the start side (right).
- [ ] Content in its own direction keeps its own controls: page arrows for an English document inside an Arabic interface follow the document.
- [ ] Centred or floating elements stay on screen (an RTL `translateX` rule combined with `dir="ltr"` pushes them off).
- [ ] Nothing uses physical left/right where a logical property was meant (look for misplaced padding, icons on the wrong side).

## Mixed-direction text (1.3.2 Meaningful Sequence)

- [ ] Number ranges and fractions read correctly: "2026-27" not "27-2026", "3-4" not "4-3", "14/20" in order. Fix: `<bdi dir="ltr">` around each run, or words ("3 من 6").
- [ ] Isolation was not done with a regex over HTML: no markup inside attributes (run `page-check.md`; `brokenAttr` catches it).
- [ ] Isolation did not touch SVG text.
- [ ] Latin titles inside right-to-left cards align with the rest of the card.

## Type and copy

- [ ] Arabic text not below about 15 px (Arabic needs a larger size than Latin for the same legibility); line height about 1.7.
- [ ] No letter-spacing or uppercase transforms on Arabic.
- [ ] Every accessible name is in the interface language (no English `aria-label` in an Arabic UI).
- [ ] Accessible names begin with the visible label (2.5.3).
- [ ] One word per concept across screens and languages.
- [ ] Dates and numbers formatted for the locale; digits as the market expects.
