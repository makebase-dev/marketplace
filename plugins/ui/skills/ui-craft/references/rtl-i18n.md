# Right-to-left and multilingual UI

## Layout

- Only logical properties: `margin-inline-start`, `padding-inline`, `inset-inline-end`, `border-start-start-radius`, `text-align: start`.
- `dir` and `lang` on `<html>` from the interface language; `lang` on every passage in another language (an English title inside an Arabic card).
- Transforms, shadows, gradients, background positions and SVG coordinates ignore logical properties: use a `--dir` multiplier or `:dir(rtl)` overrides. `scrollLeft` is negative in RTL.
- Mirror: back, chevrons, progress bars, slides, swipes, the order of a strip of days. Don't mirror: clockwise rings, clocks, checks, media controls, logos, maths.
- Content in its own direction keeps its own controls: an English PDF in the Arabic UI turns pages left to right, and its page pill is `dir="ltr"`.

## Mixed-direction text (the bugs that recurred)

| Bug | Fix |
|---|---|
| "2026-27" shows as "27-2026", "3-4" as "4-3", "14/20" reversed inside Arabic | Wrap every number range and fraction in `<bdi dir="ltr">` |
| Doing that with a regex over finished HTML rewrote `aria-label` attributes and leaked `">` into the page | Isolate on **text nodes** (TreeWalker) or in the i18n helper when inserting values; never touch attributes |
| `closest('[lang=en]')` matched `<html lang="en">` and skipped everything | Bound the search (`closest('.screen [lang=en]')`) |
| `<bdi>` injected into SVG `<text>` broke the rings | Skip SVG |
| "3 / 6" reads backwards in an RTL line | Write fractions with words in Arabic: "3 من 6" |
| English title in an Arabic card aligned left, ragged against the rest | `<bdi lang="en">` inside an element that keeps the page's `text-align: start` |

## Type

- Arabic never below 15 px: in tokens, raise the small steps inside `[lang="ar"]` and reset inside `[lang="en"]`/`[lang="fr"]`; hierarchy in Arabic comes from weight and colour.
- Arabic line height about 1.75, no letter-spacing, no uppercase transforms on labels.
- Western digits are normal in Lebanon; check the market.
- One family that covers both scripts (e.g. Readex Pro = Lexend + Arabic) keeps mixed lines even.

## Copy and names

- Write all languages together, not translated after; check units and plurals per language.
- Every `aria-label` comes from the same dictionary as the visible text; never hard-coded English in an Arabic UI.
- Accessible names begin with the visible label (WCAG 2.5.3): visible "12 study days" → name "12 study days, streak details".
- Use one word per concept across the product (e.g. always "program", never mixing "scope" and "program").
