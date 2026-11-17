# Capturing screens

For a product or UI explainer. Use Playwright with its own browser profile, so captures are repeatable.

## Signing in

- The owner signs in by hand in the Playwright window, once. Never type a password or store one in a script.
- A saved profile holds login cookies, which work like a password. Keep the profile folder outside the project, or list it in `.gitignore`, and never upload it.
- Use a demo or test account when one exists.
- Capture read-only. Do not click anything that sends, posts, buys or deletes.

## Before each capture

- Hide what the film does not need with injected CSS: avatars, handles, personal names, sticky headers, cookie bars, chat bubbles.
- Set a fixed window size and a device scale of 2 for sharp text.
- Use realistic demo data. Get permission for anything real that stays on screen.

## After each capture

Read every capture at full size. Contact sheets miss names and small text, and one missed name is a privacy problem in a published film. Check the corners, tooltips, tab titles and notification counts.

Keep raw captures out of a public repo if they might contain personal data.
