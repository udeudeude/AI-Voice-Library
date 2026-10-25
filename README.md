# AI Voice Library

A shared, English-first workspace for evaluating, preserving, and generating synthetic voices for podcasts and other creative projects.

## Goals
- Compare English-language voices using identical audition passages.
- Preserve exact model, voice, software, and license versions so production does not depend on a distributor remaining online.
- Offer one reproducible interface for podcast projects, without forcing them to change their established narrators.
- Remain engine-agnostic: Kokoro is the first candidate, not the architecture.
- Support voice blending, pronunciation dictionaries, and later custom voice development.

## Status
**Foundation only.** No voice model has been archived, no audio synthesis has been tested, and no production podcast has been changed.

See [architecture](docs/architecture.md), [voice registry](voices/registry.json), and [evaluation rubric](docs/evaluation.md).

## Principles
1. English voices first, including regional accents.
2. No silent voice replacements: every production voice is pinned to a version and tested.
3. GitHub Actions caches are disposable accelerators, never archives.
4. Model and voice licenses are reviewed separately; archive only assets we are entitled to retain and redistribute.
5. Keep original model downloads out of Git history unless storage and licensing have been deliberately reviewed.

## Next milestone
Verify the existing podcast synthesis workflows, select a reproducible Kokoro runtime, record SHA-256 checksums and source licenses, then produce a common listening comparison. Preserve the runtime before wiring any production podcast to it.
