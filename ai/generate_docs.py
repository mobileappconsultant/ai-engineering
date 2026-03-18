#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
AI = ROOT / "ai"
DOCS = AI / "docs"
DOCS.mkdir(parents=True, exist_ok=True)

timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')

def write(name: str, content: str):
    (DOCS / name).write_text(content.strip() + "\n", encoding="utf-8")

project_type = "backend"
ptype_file = AI / "PROJECT_TYPE.md"
if ptype_file.exists():
    txt = ptype_file.read_text(encoding="utf-8", errors="ignore")
    for line in txt.splitlines():
        if line.lower().startswith("current project type:"):
            project_type = line.split(":", 1)[1].strip().lower()
            break

write("SYSTEM_ARCHITECTURE.md", f'''
# SYSTEM_ARCHITECTURE

Generated automatically on {timestamp}.

## Project Type
{project_type}

## Purpose
Describe the system purpose here.

## Layers
Describe architecture layers here.

## External Integrations
List runtime dependencies here.
''')

write("MODULE_GRAPH.md", f'''
# MODULE_GRAPH

Generated automatically on {timestamp}.

## Top-level structure
Update this file to reflect modules and dependencies.
''')

if project_type in ("backend", "fullstack"):
    write("API_MAP.md", f'''
# API_MAP

Generated automatically on {timestamp}.

## Endpoints
List routes, handlers, auth rules, and purposes.
''')

    write("DATA_MODEL.md", f'''
# DATA_MODEL

Generated automatically on {timestamp}.

## Entities
List models, fields, and relationships.
''')
else:
    write("API_MAP.md", f'''
# API_MAP

Generated automatically on {timestamp}.

Not applicable or minimal for this project type.
''')
    write("DATA_MODEL.md", f'''
# DATA_MODEL

Generated automatically on {timestamp}.

Not applicable or minimal for this project type.
''')

write("RUNTIME_FLOW.md", f'''
# RUNTIME_FLOW

Generated automatically on {timestamp}.

Describe request lifecycle, async jobs, and important runtime flows.
''')
