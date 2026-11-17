# Captions

Use `templates/Captions.tsx`. Viewers read along even with sound on, and many watch muted, so the muted version has to tell the story.

## Chunks

- 2 to 5 words per chunk, one line. Keep reading speed under about 20 characters a second.
- Write chunks by hand, in the script's spelling, each timed by its spoken words `[first, last]`. Do not use raw speech-to-text as caption text.
- Never break between a noun and its adjective, a preposition and its noun, or a number and what it counts.
- No lone word on a line unless it is a deliberate beat.

## Arabic

- Animate by word, never by letter, so letters stay joined. Set `dir="rtl"`.
- In Arabic never break between مضاف and مضاف إليه.
- Use diacritics only where the meaning would change.
- Give Arabic room: line height near 1.45 for captions, and 1.4 for large display titles. Marks collide at 1.05.
- A middle dot next to Arabic digits can read as a zero (٠). Separate with «،» or a line break.

## Look

- Show one chunk at a time. Words not yet spoken stay hidden, with their space kept, so the box does not resize. The newest word takes the accent colour.
- Use a solid box (about 86% opacity) over busy pictures.
- Two weights of one family is enough.

## Place

No platform publishes official safe zones. On 1080×1920 keep text inside about x 140–940 and y 220–1440: that clears the button rail and the description on Reels, TikTok and Shorts. For right-to-left text, right-align to about 940, not the frame edge.

Default the caption near 66% of the height. Move it per shot when it covers the subject: `bottom` sets the height, and `only` shows a second `Captions` in one range.

## When to hide

Use `hidden` where a title card says the same line. Reading the same words twice feels like a mistake.

## Remotion trap

Keep the early `return null` after every hook. Returning before `useLayout` breaks React's hook order when the condition changes.
