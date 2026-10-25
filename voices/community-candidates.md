# Community English-voice candidates

These are **research candidates, not installed or tested voices**. Compatibility and license terms must be checked against each exact revision before integration.

| Candidate | Source | Why test |
|---|---|---|
| Kokoro 1.1 Chinese checkpoint English voices `af_maple`, `af_sol`, `bf_vale` | https://huggingface.co/hexgrad/Kokoro-82M-v1.1-zh | Additional American female and British female voices; test with their intended checkpoint. |
| Kokoro ONNX community conversion | https://huggingface.co/onnx-community/Kokoro-82M-v1.0-ONNX | Portable, potentially lower-footprint synthesis runtime; primarily the same base voice family, not automatically new voices. |
| KokoroTTS community interface | https://github.com/Hangry-Labs/kokoroTTS | Interface and integration ideas; review code, provenance, and maintenance before adoption. |

## English-first evaluation
Prioritize British and American long-form narration, distinctive but intelligible character voices, and expressive control. Do not add other languages to the working selector solely because an upstream project supports them.

## Distinguish three things
1. **New voice:** a genuinely different voice embedding or model.
2. **New engine:** another way to synthesize with the same model and voices.
3. **New effects:** audio processing after synthesis.

The Voice Lab already implements (3). Its existing catalog provides base voices from Kokoro 1.0. Community additions should be evaluated in (1) and (2) separately.
