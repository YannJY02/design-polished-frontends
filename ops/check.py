"""Validate the distributable skill, links and archive without invoking it."""
from pathlib import Path
import re
import tarfile
import tempfile
import yaml

root = Path(__file__).resolve().parents[1]
files = ['SKILL.md', 'agents/openai.yaml', 'references/resource-routes.md', 'README.md', 'README.zh-CN.md']
frontmatter = yaml.safe_load((root / 'SKILL.md').read_text().split('---', 2)[1])
assert frontmatter['name'] == 'design-polished-frontends'
assert isinstance(frontmatter['description'], str) and frontmatter['description'].strip()
interface = yaml.safe_load((root / 'agents/openai.yaml').read_text())['interface']
assert all(isinstance(interface[key], str) and interface[key].strip()
           for key in ['display_name', 'short_description', 'default_prompt'])
assert '$design-polished-frontends' in interface['default_prompt']
for name in files:
    path = root / name
    assert path.is_file() and path.stat().st_size > 0, name
    if path.suffix != '.md':
        continue
    for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
        target = link.split('#', 1)[0]
        if not target or '://' in target or target.startswith('mailto:'):
            continue
        assert (path.parent / target).is_file(), f'{name}: missing {target}'
with tempfile.TemporaryDirectory() as directory:
    archive = Path(directory) / 'design-polished-frontends.tar.gz'
    with tarfile.open(archive, 'w:gz') as bundle:
        for name in files:
            bundle.add(root / name, arcname='design-polished-frontends/' + name)
    with tarfile.open(archive) as bundle:
        assert set(bundle.getnames()) == {'design-polished-frontends/' + name for name in files}
        assert all(bundle.extractfile(member).read() for member in bundle.getmembers())
print('Skill metadata, bundled links and distribution archive passed.')
