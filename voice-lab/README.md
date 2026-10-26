# Voice Lab migration

This is a source copy of the existing browser-based Kokoro Voice Lab from `udeudeude/udeudeude.github.io/voice-lab`.

## Current state
- Existing application interface, signal-processing worker, style, service worker, and saved Lewis recipes have been copied.
- The existing 54-voice catalog is preserved; the present goal is English only.
- Audio sample manifest and MP3 recordings are still hosted at `https://udeudeude.github.io/voice-lab/voice-samples/`. The imported JavaScript explicitly references that location.
- This private repository is **not yet hosting a deployed Voice Lab**. The working public URL remains `https://udeudeude.github.io/voice-lab/`.
- The browser app edits/plays existing recordings; it is **not** an in-browser Kokoro speech generator.

## Next migration tasks
1. Compare imported files with the working deployed app and test in Safari on iPhone.
2. Keep the public site as a deployment target, but move the canonical development source here.
3. Add English community-model candidates as separate model/version families, not as unverified additions to the original 54-voice catalog.
4. Render and audition samples with matched text, loudness, and playback conditions.
5. Preserve models and voices in durable storage with checksums, license information, and an offline recovery test.

## Safety
Do not change existing podcast voice assignments or presets without explicit review.

## October 25 update
The public site and this repository currently contain separate copies of the app. Automatic deployment from this repository has not been implemented. The original 54 voices are catalogued; the 26 non-English voices require new English-language recordings before they become playable in the accented-English selector. Three v1.1 community voices are also catalogued but require generated recordings. Generation workflows are committed in the public site repository; their success and audio quality remain unverified. The app processes recordings rather than synthesizing arbitrary text in-browser.
