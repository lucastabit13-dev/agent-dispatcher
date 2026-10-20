"""Dependency-free structural checks; these do not evaluate model behavior."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def validate():
    catalog = json.loads((ROOT / '.agents/plugins/marketplace.json').read_text(encoding='utf-8'))
    assert catalog['name'] == 'agent-dispatcher-local'
    assert len(catalog['plugins']) == 1
    entry = catalog['plugins'][0]
    relative = entry['source']['path']
    assert relative.startswith('./') and '..' not in Path(relative).parts
    plugin = (ROOT / relative).resolve()
    assert plugin.is_relative_to(ROOT)
    manifest = json.loads((plugin / 'plugin.json').read_text(encoding='utf-8'))
    assert manifest['name'] == entry['name'] == 'agent-dispatcher'
    assert re.fullmatch(r'\d+\.\d+\.\d+', manifest['version'])
    assert manifest['$schema'] == 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json'
    assert manifest['description'].strip()
    assert entry['policy'] == {'installation': 'AVAILABLE', 'authentication': 'ON_INSTALL'}
    assert entry['category'] == 'Productivity'
    skills = list((plugin / 'skills').glob('*/SKILL.md'))
    assert len(skills) == 1
    for skill in skills:
        body = skill.read_text(encoding='utf-8')
        header = body.split('---', 2)
        assert len(header) == 3 and not header[0].strip()
        assert f'name: {skill.parent.name}\n' in header[1]
        assert re.search(r'^description: \S.+', header[1], re.M)
        for target in re.findall(r'\]\(([^)]+)\)', header[2]):
            resource = (skill.parent / target).resolve()
            assert resource.is_relative_to(plugin) and resource.is_file(), target
    packaged = plugin / 'skills/dispatch-agents/references/task-brief.md'
    assert packaged.read_bytes() == (ROOT / 'task-brief.md').read_bytes(), 'Worker briefs differ'
    print('PASS: catalog resolution, manifest, skill metadata, references, worker brief consistency')
    print('Structural checks only; no workers started or behavioral results claimed.')


if __name__ == '__main__':
    validate()
