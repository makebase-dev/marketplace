# makebase marketplace

Claude Code plugins by [makebase](https://makebase.dev), free under the MIT licence.

| Plugin | Skills | What it does |
|---|---|---|
| [video](plugins/video/) | `video-start`, `video-montage`, `video-sound` | Edits short narrated videos with Remotion, and sources, mixes and masters their sound |

## Install

```bash
claude plugin marketplace add makebase-dev/marketplace
claude plugin install video@makebase
```

Inside a session, run `/plugin marketplace add makebase-dev/marketplace`, then `/plugin install video@makebase`. Skills are called as `/<plugin>:<skill>`, such as `/video:video-start`.

Each plugin's README lists the tools it needs and how to set up a computer for it.

## Update

```bash
claude plugin marketplace update makebase
claude plugin update video@makebase
```

## Contributing

This repository is generated from a private source and replaced on each release, so pull requests cannot be merged. Open an issue to report a bug or suggest a change.

## Licence

MIT. See [LICENSE](LICENSE).
