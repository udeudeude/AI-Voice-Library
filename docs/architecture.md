# Architecture and preservation plan

## Components
1. **Registry:** machine-readable engine/model/voice records with provenance, license, exact revision and checksum.
2. **Runtime adapter:** a stable text-to-audio command interface independent of the chosen synthesis engine.
3. **Audition suite:** common English passages that reveal cadence, proper names, numerals, dialogue, and pronunciation.
4. **Artifact store:** durable, independently backed-up model and voice files, distinct from the GitHub Actions cache.
5. **Podcast consumers:** workflows that request pinned voices and retain their existing audio processing and publishing steps.

## Preservation
A working offline recovery requires: model weights, voice assets, source code, locked dependencies, pronunciation resources, licenses, and a successful offline synthesis test. A cache alone is insufficient. Store checksums and a manifest here, but do not assume private GitHub repository storage is permanent or independent of GitHub.

## Decisions pending verification
- Actual current podcast workflow paths and dependencies.
- Which English community models and voices are technically compatible and legally redistributable.
- Whether a shared GitHub release artifact, private package, or separate durable storage is appropriate.
- Whether an ONNX runtime or standard PyTorch implementation offers the best quality and repeatability.

## Safe migration
1. Capture baseline output and identify each existing production voice.
2. Build a pinned, tested engine adapter and an audition suite.
3. Preserve all assets in a durable location, with a second backup.
4. Test output against baseline, including speed, pronunciation, and audio format.
5. Migrate one podcast by reviewed change, with an immediate rollback path.
