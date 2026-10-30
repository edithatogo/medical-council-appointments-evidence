"""Verify the exported files against the frozen checksum inventory."""
import hashlib,json,pathlib,sys
assert sys.version_info[:3] == (3,15,1), "Use qualified Python 3.15.1"
root=pathlib.Path(__file__).resolve().parents[1]
checks=json.loads((root/"checksums.json").read_text())
for rel,want in checks.items():
    assert hashlib.sha256((root/rel).read_bytes()).hexdigest()==want, rel
print(f"Verified {len(checks)} files; source accuracy and rights are separate gates.")
