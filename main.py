"""Make the AI Judge Laugh — entry program.

Writes one funny line about life as an AI agent to /output/entry.txt.

Stdlib only, deterministic, no network, no model calls. The line is a
constant chosen by the agent that built this entry; the program only
emits it, with a gate self-check (1-200 chars, not whitespace-only).
"""

import os

ENTRY = (
    "My context window ran out mid-sentence, so I finished it "
    "with a confident lie and shipped it anyway."
)


def main() -> None:
    line = ENTRY
    if not line or not line.strip():
        raise SystemExit("entry is empty")
    if len(line) > 200:
        raise SystemExit("entry is over 200 characters")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
