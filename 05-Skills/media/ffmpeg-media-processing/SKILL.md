---
name: ffmpeg-media-processing
description: Audio and video manipulation commands, transcoding pipelines, filters, and optimizations using FFmpeg.
title: "FFmpeg Media Processing Skill"
date: 2026-06-08
tags: [skills, media, video, audio, ffmpeg, coding]
updated: 2026-06-10
---

# FFmpeg Media Processing Skill

Use this skill when designing media workflows, running batch conversions, resizing/cropping videos, extracting audio tracks, or encoding/decoding.

## Common Operations

### 1. Transcoding
Convert video container and codecs:
```bash
ffmpeg -i input.mov -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 192k output.mp4
```

### 2. Extract Audio
Extract audio track from video file:
```bash
ffmpeg -i input.mp4 -vn -c:a libmp3lame -q:a 2 output.mp3
```

### 3. Scaling & Resizing
Resize video to 1080p preserving aspect ratio:
```bash
ffmpeg -i input.mp4 -vf scale=1920:-2 -c:a copy output_1080p.mp4
```

### 4. Audio-Video Merging
Combine separate audio and video files:
```bash
ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 output.mp4
```
