# FLUX 3 Dev API: Python Wrapper for Black Forest Labs' Fast, Low-Cost FLUX 3 Variant

[![Powered by MuAPI](https://img.shields.io/badge/Powered%20by-MuAPI-6366f1?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMSAxNHYtNGgtMnYtMmg0djZoLTJ6bTAtOFY2aDJ2MmgtMnoiLz48L3N2Zz4=)](https://muapi.ai?utm_source=github&utm_medium=badge&utm_campaign=flux-3-dev-api)

[![PyPI version](https://img.shields.io/pypi/v/flux-3-dev-api.svg)](https://pypi.org/project/flux-3-dev-api/)
[![GitHub stars](https://img.shields.io/github/stars/Anil-matcha/Flux-3-Dev-API.svg)](https://github.com/Anil-matcha/Flux-3-Dev-API/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

A Python wrapper for **FLUX 3 Dev** — the faster, lower-cost variant of Black Forest Labs' **FLUX 3** frontier model — delivered via [muapi.ai](https://muapi.ai/flux-3?utm_source=github&utm_medium=readme&utm_campaign=flux-3-dev-api). FLUX 3 Dev trades a small amount of peak fidelity for significantly reduced latency and cost, making it ideal for rapid iteration, prototyping, and high-volume generation, with an open-weight release planned for later in 2026. This SDK also covers the full FLUX 3 family through the same client.

> ⚠️ **Status**: FLUX 3 **Text-to-Video** and **Image-to-Video** are **live now** on MuAPI. FLUX 3 **Dev**, flagship **Text-to-Image**, and **Image-to-Image** (the three endpoints this repo is named after) are still **coming soon** — they're wired into this SDK ahead of launch, but the underlying MuAPI routes aren't enabled yet and calls to `generate()`/`text_to_image()`/`image_to_image()` will fail until Black Forest Labs opens general availability. See [muapi.ai/flux-3](https://muapi.ai/flux-3?utm_source=github&utm_medium=readme&utm_campaign=flux-3-dev-api) for current status of every FLUX 3 endpoint.
>
> MuAPI's FLUX 3 video API has also expanded beyond Text-to-Video/Image-to-Video since this SDK was written — Start-End-to-Video, Video Extend, Video Upscaler, and fast draft modes are live too. This repo doesn't wrap those; see [flux-3-video-api](https://github.com/SamurAIGPT/flux-3-video-api) (all seven live video endpoints), [flux-3-video-edit](https://github.com/Anil-matcha/flux-3-video-edit) (Video Extend), and [flux-3-video-upscaler](https://github.com/Anil-matcha/flux-3-video-upscaler) if you need those.

<p align="center">
  <a href="https://www.youtube.com/watch?v=pq0B_A0K770">
    <img src="docs/assets/flux-3-api-video-thumbnail.png" alt="FLUX 3 API: Image & Video Generation from One Multimodal Model" width="640">
  </a>
</p>

<p align="center">
  <a href="https://www.youtube.com/watch?v=pq0B_A0K770"><b>📺 FLUX 3 API: Image & Video Generation from One Multimodal Model →</b></a>
</p>

## Related Projects

- [MiniMax-H3-API](https://github.com/Anil-matcha/MiniMax-H3-API) — Python SDK for MiniMax H3 text-to-video, image-to-video, and first/last-frame video generation.
- [Wan-3.0-API](https://github.com/Anil-matcha/Wan-3.0-API) — Python SDK and MCP server for Wan 3.0-compatible AI video generation.
- [awesome-flux-3-api-prompts](https://github.com/Anil-matcha/awesome-flux-3-api-prompts) — FLUX 3 API guide, prompt engineering, and a curated prompt library
- [flux-3-video-api](https://github.com/SamurAIGPT/flux-3-video-api) — Python wrapper covering all seven live FLUX 3 video endpoints (Text-to-Video, Image-to-Video, Start-End-to-Video, Video Extend, Video Upscaler, plus draft modes)
- [flux-3-video-edit](https://github.com/Anil-matcha/flux-3-video-edit) — Python SDK for FLUX 3 Video Extend (continues an existing clip with new prompt-guided motion)
- [flux-3-video-upscaler](https://github.com/Anil-matcha/flux-3-video-upscaler) — Python SDK for upscaling FLUX 3 (or any) video output beyond its native resolution
- [flux-3-omni](https://github.com/Anil-matcha/flux-3-omni) — Python SDK for FLUX 3's multi-reference Omni Reference mode (coming soon)
- [Seedance-2-API](https://github.com/Anil-matcha/Seedance-2-API) — Python SDK for ByteDance's Seedance 2.x video models
- [awesome-ai-image-models](https://github.com/Anil-matcha/awesome-ai-image-models) — comparison of AI image generation models across providers
- [Grok-Imagine-Image-2-API](https://github.com/Anil-matcha/Grok-Imagine-Image-2-API) — Python SDK and MCP server for Grok Imagine Image 2.0 image generation and editing through MuAPI
- [Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) — open-source, self-hosted AI image & video generation studio (200+ models)
- [ai-creator-academy](https://github.com/Anil-matcha/ai-creator-academy) — free curriculum teaching creators how to monetize FLUX and other generative AI models

## 🚀 Why Use FLUX 3 Dev?

FLUX 3 is Black Forest Labs' newest frontier model — a unified multimodal system jointly trained across image, video, and audio, extendable to action prediction for robotics. **FLUX 3 Dev** is its fast, affordable entry point:

- **Lower Latency & Cost**: Trades a small amount of peak fidelity from the flagship model for significantly faster, cheaper generation.
- **Same Prompting Conventions**: Uses the same prompt structure as flagship FLUX 3 — validate ideas cheaply, then re-run on the full model if needed.
- **Planned Open-Weight Release**: Black Forest Labs has confirmed a faster, open-weight version of FLUX 3 is coming later in 2026.
- **Full FLUX 3 Family Access**: This SDK also wraps FLUX 3 Text-to-Image, Image-to-Image, Text-to-Video, and Image-to-Video — one client for the whole model family (see status note above — Dev/T2I/I2I are coming soon, T2V/I2V are live).
- **Native Audio in Video**: FLUX 3 Video variants can generate scene-appropriate synchronized audio directly alongside the clip, no extra charge.
- **Developer-First**: Simple Python SDK on top of MuAPI's unified infrastructure — no separate account or waitlist needed once you have a MuAPI key.

## 🌟 Key Features

- 🕒 **FLUX 3 Dev Text-to-Image** (coming soon): Fast, low-cost image generation via `generate()`.
- 🕒 **FLUX 3 Text-to-Image** (coming soon): Flagship higher-fidelity image generation via `text_to_image()`.
- 🕒 **FLUX 3 Image-to-Image** (coming soon): Instruction-driven editing with up to 4 reference images via `image_to_image()`.
- ✅ **FLUX 3 Text-to-Video** (live): Cinematic video with optional native synchronized audio via `text_to_video()`.
- ✅ **FLUX 3 Image-to-Video** (live): Animate a still image into video with optional native audio via `image_to_video()`.
- ✅ **File Upload**: Upload local images/videos directly using `upload_file()`.
- ✅ **MCP Server**: Use FLUX 3 Dev as a Model Context Protocol server for Claude Desktop, Cursor, and other MCP clients.

---

## 🛠 Installation

### Via Pip (Recommended)
```bash
pip install flux-3-dev-api
```

### From Source
```bash
git clone https://github.com/Anil-matcha/Flux-3-Dev-API.git
cd Flux-3-Dev-API
pip install -r requirements.txt
```

### Configuration
Create a `.env` file in the root directory and add your [MuAPI](https://muapi.ai/flux-3?utm_source=github&utm_medium=readme&utm_campaign=flux-3-dev-api) API key:
```env
MUAPI_API_KEY=your_muapi_api_key_here
```

---

## 🤖 FLUX 3 Dev MCP Server

Use FLUX 3 Dev as an **MCP (Model Context Protocol)** server so AI clients (like Claude Desktop or Cursor) can directly invoke FLUX 3 generation tools.

### Running the MCP Server
1. Ensure `MUAPI_API_KEY` is set in your environment.
2. Run the server:
   ```bash
   python3 mcp_server.py
   ```
3. To test with the MCP Inspector:
   ```bash
   npx -y @modelcontextprotocol/inspector python3 mcp_server.py
   ```

---

## 💻 Quick Start (Python)

```python
from flux3_dev_api import Flux3DevAPI

# Initialize the client
api = Flux3DevAPI()

# Generate an image with FLUX 3 Dev
print("Generating image with FLUX 3 Dev...")
submission = api.generate(
    prompt="A minimalist product shot of a ceramic mug on a wooden table, soft natural light",
    aspect_ratio="1:1",
    resolution="1k"
)

# Wait for completion
result = api.wait_for_completion(submission["request_id"])
print(f"Success! Output: {result['outputs'][0]}")
```

---

## 📡 API Endpoints & Reference

### 1. FLUX 3 Dev (Text-to-Image, fast/low-cost) — 🕒 Coming Soon
**Endpoint**: `POST https://api.muapi.ai/api/v1/flux-3-dev`

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/flux-3-dev" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "A minimalist product shot of a ceramic mug on a wooden table, soft natural light",
      "aspect_ratio": "1:1",
      "resolution": "1k"
  }'
```

**Python SDK:**
```python
submission = api.generate(
    prompt="A minimalist product shot of a ceramic mug on a wooden table, soft natural light",
    aspect_ratio="1:1",
    resolution="1k",
)
result = api.wait_for_completion(submission["request_id"])
print(result["outputs"][0])
```

### 2. FLUX 3 Text-to-Image (flagship) — 🕒 Coming Soon
**Endpoint**: `POST https://api.muapi.ai/api/v1/flux-3-text-to-image`

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/flux-3-text-to-image" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "A hyperrealistic portrait of an astronaut standing on red Martian dunes at golden hour",
      "aspect_ratio": "16:9",
      "resolution": "2k"
  }'
```

**Python SDK:**
```python
submission = api.text_to_image(
    prompt="A hyperrealistic portrait of an astronaut standing on red Martian dunes at golden hour",
    aspect_ratio="16:9",
    resolution="2k",
)
```

### 3. FLUX 3 Image-to-Image (Edit) — 🕒 Coming Soon
**Endpoint**: `POST https://api.muapi.ai/api/v1/flux-3-image-to-image`

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/flux-3-image-to-image" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "Replace the background with a neon-lit city street at night, keep the subject unchanged",
      "images_list": ["https://example.com/input.jpg"],
      "aspect_ratio": "1:1"
  }'
```

**Python SDK:**
```python
submission = api.image_to_image(
    prompt="Replace the background with a neon-lit city street at night, keep the subject unchanged",
    images_list=["https://example.com/input.jpg"],
    aspect_ratio="1:1",
)
```

### 4. FLUX 3 Text-to-Video — ✅ Live
**Endpoint**: `POST https://api.muapi.ai/api/v1/flux-3-text-to-video` · **$0.25/sec @720p, $0.42/sec @1080p**

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/flux-3-text-to-video" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "A drone shot glides over a bioluminescent forest at night, fireflies drifting between glowing trees",
      "aspect_ratio": "16:9",
      "resolution": "1080p",
      "duration": 6,
      "generate_audio": true
  }'
```

**Python SDK:**
```python
submission = api.text_to_video(
    prompt="A drone shot glides over a bioluminescent forest at night, fireflies drifting between glowing trees",
    aspect_ratio="16:9",
    resolution="1080p",
    duration=6,
    generate_audio=True,
)
```

### 5. FLUX 3 Image-to-Video — ✅ Live
**Endpoint**: `POST https://api.muapi.ai/api/v1/flux-3-image-to-video` · **$0.25/sec @720p, $0.42/sec @1080p**

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/flux-3-image-to-video" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "The camera slowly pushes in as steam rises from the coffee cup",
      "image_url": "https://example.com/product.jpg",
      "duration": 5,
      "generate_audio": true
  }'
```

**Python SDK:**
```python
submission = api.image_to_video(
    prompt="The camera slowly pushes in as steam rises from the coffee cup",
    image_url="https://example.com/product.jpg",
    duration=5,
    generate_audio=True,
)
```

---

## 🎬 Other Live FLUX 3 Video Endpoints

This SDK only wraps Text-to-Video and Image-to-Video. MuAPI's FLUX 3 video API also includes these live endpoints, covered by sibling projects:

| Endpoint | What it does | SDK |
| :--- | :--- | :--- |
| `flux-3-text-to-video-draft` | Fast, lower-cost draft mode of Text-to-Video ($0.09/sec flat) | [flux-3-video-api](https://github.com/SamurAIGPT/flux-3-video-api) |
| `flux-3-start-end-to-video` | Video transition between a start and end keyframe | [flux-3-video-api](https://github.com/SamurAIGPT/flux-3-video-api) |
| `flux-3-video-extend` | Continue an existing clip with new prompt-guided motion | [flux-3-video-edit](https://github.com/Anil-matcha/flux-3-video-edit), [flux-3-video-api](https://github.com/SamurAIGPT/flux-3-video-api) |
| `flux-3-video-extend-draft` | Fast, lower-cost draft mode of Video Extend ($0.09/sec flat) | [flux-3-video-api](https://github.com/SamurAIGPT/flux-3-video-api) |
| `flux-3-video-upscaler` | Upscale any video beyond its native resolution | [flux-3-video-upscaler](https://github.com/Anil-matcha/flux-3-video-upscaler) |

---

## 📖 Method Reference

| Method | Parameters | Status | Description |
| :--- | :--- | :--- | :--- |
| `generate` | `prompt`, `aspect_ratio`, `resolution` | 🕒 Coming soon | FLUX 3 Dev — fast, low-cost text-to-image. |
| `text_to_image` | `prompt`, `aspect_ratio`, `resolution` | 🕒 Coming soon | Flagship FLUX 3 text-to-image (higher fidelity than Dev). |
| `image_to_image` | `prompt`, `images_list`, `aspect_ratio`, `resolution` | 🕒 Coming soon | FLUX 3 instruction-driven image editing (up to 4 reference images). |
| `text_to_video` | `prompt`, `aspect_ratio`, `resolution`, `duration`, `generate_audio` | ✅ Live | FLUX 3 text-to-video with optional native synchronized audio. $0.25/sec @720p, $0.42/sec @1080p. |
| `image_to_video` | `prompt`, `image_url`, `aspect_ratio`, `resolution`, `duration`, `generate_audio` | ✅ Live | FLUX 3 image-to-video with optional native synchronized audio. $0.25/sec @720p, $0.42/sec @1080p. |
| `upload_file` | `file_path` | Upload a local file (image or video) to MuAPI for use in generation tasks. |
| `get_result` | `request_id` | Check task status for a FLUX 3 generation. |
| `wait_for_completion` | `request_id`, `poll_interval`, `timeout` | Blocking helper that polls until the task completes. |

---

## 🔗 Official Resources
- **FLUX 3 Announcement (Black Forest Labs)**: [bfl.ai/models/flux-3](https://bfl.ai/models/flux-3)
- **Playground — FLUX 3 (all variants)**: [muapi.ai/flux-3](https://muapi.ai/flux-3?utm_source=github&utm_medium=readme&utm_campaign=flux-3-dev-api)
- **Playground — FLUX Kontext (available today)**: [muapi.ai/flux-kontext](https://muapi.ai/flux-kontext?utm_source=github&utm_medium=readme&utm_campaign=flux-3-dev-api)
- **API Provider**: [MuAPI.ai](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=flux-3-dev-api)

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Keywords**: FLUX 3 API, FLUX 3 Dev, FLUX 3 Dev API, Black Forest Labs FLUX 3, FLUX 3 Python SDK, FLUX 3 text to image, FLUX 3 image to image, FLUX 3 text to video, FLUX 3 image to video, FLUX multimodal model, AI image generation API, AI video generation API, MuAPI, Python image generation SDK, open-weight FLUX.
