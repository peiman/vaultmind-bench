"""The agent-rg agent, with VaultMind as one more tool.

Same model, prompt, tools and limits as agent-rg, plus Bash allowed only for
`vaultmind ask`. The working directory holds the section files and, in the
hidden `.vm/`, a copy of the set's vault indexed the way `vm` indexes it
(run_vm.prepare_vault). Grep skips hidden directories, so the agent sees the
same files as agent-rg. The prompt adds one sentence naming the command.
"""

from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path

import run_agent_rg
import run_vm

TOOLS = run_agent_rg.TOOLS + ",Bash"
ALLOWED = run_agent_rg.TOOLS + ",Bash(vaultmind ask:*)"

PROMPT = run_agent_rg.PROMPT + (
    "\nYou can also run `vaultmind ask \"<query>\" --vault .vm`, a search over "
    "these docs that returns ranked note ids (a note id is a file name without .md).\n"
)


def run(set_dir: Path, out_dir: Path, max_questions: int | None) -> None:
    with tempfile.TemporaryDirectory(prefix="public-bench-agent-vm-xdg-") as xdg:

        def prepare(work: Path) -> dict:
            _, env = run_vm.prepare_vault(set_dir, work, name=".vm", xdg_root=Path(xdg))
            return env

        run_agent_rg.run_agent(
            "agent-vm", set_dir, out_dir, max_questions, PROMPT, TOOLS, ALLOWED, prepare
        )


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("set_dir")
    parser.add_argument("out_dir")
    parser.add_argument("--max-questions", type=int, default=None)
    args = parser.parse_args(argv)
    run(Path(args.set_dir), Path(args.out_dir), args.max_questions)


if __name__ == "__main__":
    main(sys.argv[1:])
