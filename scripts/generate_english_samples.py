#!/usr/bin/env python3
"""Generate matched English Kokoro auditions. Requires kokoro, soundfile and espeak-ng."""
import argparse
import hashlib
import json
from pathlib import Path

SCRIPT = "The road is long, and fortune seldom walks beside us. Still, you may roll."

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", default="voice-lab/voice-catalog.json")
    parser.add_argument("--out", default="dist/voice-samples")
    parser.add_argument("--voices", nargs="*", help="Optional voice IDs; defaults to all English voices")
    args = parser.parse_args()
    from kokoro import KPipeline
    import numpy as np
    import soundfile as sf

    catalog = json.loads(Path(args.catalog).read_text())
    voices = [(group, voice) for group in catalog["groups"] for voice in group["voices"] if group["code"] in ("a", "b")]
    if args.voices:
        wanted = set(args.voices)
        missing = wanted - {v["id"] for _, v in voices}
        if missing:
            parser.error("Unknown voices: " + ", ".join(sorted(missing)))
        voices = [(g, v) for g, v in voices if v["id"] in wanted]
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    pipelines = {}
    records = []
    for group, voice in voices:
        lang = group["code"]
        if lang not in pipelines:
            pipelines[lang] = KPipeline(lang_code=lang)
        pieces = []
        for _, _, audio in pipelines[lang](group["sample"], voice=voice["id"], speed=1.0):
            pieces.append(np.asarray(audio, dtype=np.float32))
        if not pieces:
            raise RuntimeError("No audio generated for " + voice["id"])
        filename = voice["id"] + ".wav"
        path = out / filename
        sf.write(path, np.concatenate(pieces), 24000, subtype="PCM_16")
        records.append({"id": voice["id"], "file": filename,
                        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                        "engine": catalog["engine"], "sample": group["sample"]})
        print("Generated", filename, flush=True)
    (out / "manifest.json").write_text(json.dumps({
        "schemaVersion": 2, "format": "WAV PCM 16-bit mono 24 kHz",
        "available": [r["id"] for r in records], "records": records,
        "completed": True}, indent=2) + "\n")

if __name__ == "__main__":
    main()
