"""Build a deterministic, self-contained plugin ZIP after structural checks."""
import json
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

from validate import ROOT, validate


def package():
    validate()
    plugin = ROOT / 'plugins/agent-dispatcher'
    version = json.loads((plugin / 'plugin.json').read_text(encoding='utf-8'))['version']
    output = ROOT / 'dist' / f'agent-dispatcher-{version}.zip'
    output.parent.mkdir(exist_ok=True)
    # Explicit contents prevent editor files, caches, or future local secrets from entering a release.
    members = [plugin / 'plugin.json',
               plugin / 'skills/dispatch-agents/SKILL.md',
               plugin / 'skills/dispatch-agents/references/task-brief.md']
    with ZipFile(output, 'w', compression=ZIP_DEFLATED) as archive:
        for path in members:
            info = ZipInfo(path.relative_to(plugin).as_posix(), (2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    with ZipFile(output) as archive:
        assert archive.testzip() is None
        assert set(archive.namelist()) == {p.relative_to(plugin).as_posix() for p in members}
        for path in members:
            assert archive.read(path.relative_to(plugin).as_posix()) == path.read_bytes()
    print(f'PASS: release archive contents and integrity: {output}')
    return output


if __name__ == '__main__':
    package()
