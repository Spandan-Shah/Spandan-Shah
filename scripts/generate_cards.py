#!/usr/bin/env python3
"""Generate GitHub-native-looking SVG cards for the Spandan-Shah profile.

Uses GitHub's public REST API when GITHUB_TOKEN is available, but safely
falls back to known project descriptions with no invented stars/forks.
No third-party dependencies and no secrets committed to git.
"""
import json
import os
import pathlib
import textwrap
import urllib.error
import urllib.request
from xml.sax.saxutils import escape

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEST = ROOT / 'assets' / 'project-cards'
DEST.mkdir(parents=True, exist_ok=True)
USER = 'Spandan-Shah'

PROJECTS = [
    dict(slug='goblinwisp', title='GoblinWisp', public_repo=None,
         description='Identity-bound, directionally isolated secure sessions for infrastructure-free peer communication.',
         language='Embedded C/C++', status='Embedded security prototype', color='#A371F7'),
    dict(slug='aeronexus-command-center', title='Aeronexus Command Center',
         public_repo='Aeronexus-Command-Center-Unified-Mission-Control-for-Next-Generation-UAV-Systems',
         description='UAV mission control with mapping, live telemetry, aircraft health, geofencing and alerts.',
         language='TypeScript', status='Active development', color='#3178C6'),
    dict(slug='vigilantedge', title='VigilantEdge', public_repo=None,
         description='Layered AI-assisted firewall research with explainable anomaly detection and policy controls.',
         language='Python', status='Staged R&D', color='#3572A5'),
    dict(slug='exotrace', title='ExoTrace', public_repo=None,
         description='Exoplanet candidate screening using TESS light curves, BLS search and machine learning.',
         language='Python', status='Research prototype', color='#3572A5'),
    dict(slug='examforge', title='ExamForge AI', public_repo='Question-Paper-Generator',
         description='Structured generative-AI question paper builder for academic practice and assessment.',
         language='JavaScript', status='Functional application', color='#F1E05A'),
    dict(slug='tinyml-esp32', title='TinyML - ESP32-CAM Vision',
         public_repo='TinyML---Object-Detection-Using-ESP32-Cam',
         description='Low-latency ESP32-CAM frame streaming with receiver-side computer vision processing.',
         language='Python', status='Embedded vision prototype', color='#3572A5'),
    dict(slug='vigil', title='Vigil', public_repo=None,
         description='Computer-vision situational awareness for public safety with human-reviewed alerts.',
         language='Python', status='Research system', color='#3572A5'),
    dict(slug='narcotrace', title='NarcoTrace AI', public_repo=None,
         description='Multimodal OSINT research combining text, vision and geospatial analysis for analysts.',
         language='Python', status='Research prototype', color='#3572A5'),
    dict(slug='spectraguard', title='SpectraGuard', public_repo=None,
         description='Controlled ESP32 and NRF24L01 testing for wireless protocol security and RF resilience.',
         language='Embedded C/C++', status='RF testbed', color='#A371F7'),
    dict(slug='flowops', title='FlowOps', public_repo=None,
         description='n8n automation for registration, validation, records and event-driven workflows.',
         language='n8n', status='Functional workflow', color='#EA4B71'),
    dict(slug='berlin', title='Berlin', public_repo=None,
         description='Traffic video analytics with vehicle detection, tracking, OCR and speed estimation.',
         language='Python', status='Vision prototype', color='#3572A5'),
    dict(slug='my-portfolio', title='My Portfolio', public_repo='My-Portfolio',
         description='Personal engineering portfolio showcasing projects, research and founder work.',
         language='TypeScript', status='Portfolio', color='#3178C6'),
]


def get_meta(repo):
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        return None
    request = urllib.request.Request(
        f'https://api.github.com/repos/{USER}/{repo}',
        headers={
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28',
            'Authorization': f'Bearer {token}',
            'User-Agent': 'spandan-profile-card-builder',
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            data = json.load(response)
        if data.get('private') is True:
            return None
        return data
    except (OSError, ValueError, urllib.error.HTTPError) as exc:
        print(f'Warning: metadata unavailable for {repo}: {exc}')
        return None


def wrap_lines(text, width=62, max_lines=3):
    lines = textwrap.wrap(text, width=width, break_long_words=False, break_on_hyphens=False)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1].rstrip(' .') + '...'
    return lines


def build_svg(project):
    width, height = 580, 178
    meta = get_meta(project['public_repo']) if project['public_repo'] else None
    is_public = bool(project['public_repo'])
    if meta is not None:
        if meta.get('language'):
            project_language = meta['language']
        else:
            project_language = project['language']
    else:
        project_language = project['language']
    desc = project['description']
    title = project['title']
    if len(title) > 43:
        title = title[:42].rstrip() + '…'
    header_x = 53
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(project["title"])} project card">',
        f'<rect width="{width}" height="{height}" fill="#0D1117"/>',
        '<g fill="none" stroke="#58A6FF" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round">',
        '<path d="M24 27 H39 V48 H24 Z M28 27 V23 H35 V27 M27 44 V52 L31.5 49 L36 52 V44"/>',
        '</g>',
        f'<text x="{header_x}" y="46" fill="#58A6FF" font-family="Arial, Helvetica, sans-serif" font-size="21" font-weight="700">{escape(title)}</text>',
    ]
    for i, line in enumerate(wrap_lines(desc)):
        out.append(f'<text x="24" y="{83 + 21*i}" fill="#E6EDF3" font-family="Arial, Helvetica, sans-serif" font-size="16">{escape(line)}</text>')
    out.extend([
        f'<circle cx="31" cy="153" r="6" fill="{escape(project["color"])}"/>',
        f'<text x="45" y="158" fill="#C9D1D9" font-family="Arial, Helvetica, sans-serif" font-size="14">{escape(project_language)}</text>',
    ])
    if meta is not None and is_public:
        stars = meta.get('stargazers_count', 0)
        forks = meta.get('forks_count', 0)
        out.extend([
            '<g fill="none" stroke="#58A6FF" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round">',
            '<path d="M375 144 L378.5 150.5 L386 151.6 L380.6 157 L382 164 L375 160.5 L368 164 L369.4 157 L364 151.6 L371.5 150.5 Z"/>',
            '<circle cx="457" cy="146" r="3"/><circle cx="457" cy="161" r="3"/><circle cx="473" cy="153" r="3"/>',
            '<path d="M457 149 V158 M460 146 H465 Q468 146 468 150 V153 H470"/>',
            '</g>',
            f'<text x="394" y="158" fill="#C9D1D9" font-family="Arial, Helvetica, sans-serif" font-size="14">{stars}</text>',
            f'<text x="486" y="158" fill="#C9D1D9" font-family="Arial, Helvetica, sans-serif" font-size="14">{forks}</text>',
        ])
    else:
        label = ('Public repository' if is_public else project['status'])
        out.append(f'<text x="550" y="158" text-anchor="end" fill="#8B949E" font-family="Arial, Helvetica, sans-serif" font-size="13">{escape(label)}</text>')
    out.append('</svg>')
    return '\n'.join(out) + '\n'


def main():
    for project in PROJECTS:
        dest = DEST / f'{project["slug"]}.svg'
        dest.write_text(build_svg(project), encoding='utf-8')
        print(f'Wrote {dest.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
