#!/usr/bin/env python3
"""A tiny command-line to-do list.

Tasks are stored in tasks.json next to this script. No dependencies.
"""

import argparse
import json
from pathlib import Path

STORE = Path(__file__).with_name("tasks.json")


def load():
    if not STORE.exists():
        return []
    return json.loads(STORE.read_text(encoding="utf-8"))


def save(tasks):
    STORE.write_text(json.dumps(tasks, indent=2), encoding="utf-8")


def cmd_add(args):
    tasks = load()
    tasks.append({"text": " ".join(args.text), "done": False})
    save(tasks)
    print(f"added: {' '.join(args.text)}")


def cmd_list(args):
    tasks = load()
    if not tasks:
        print("no tasks")
        return
    for i, task in enumerate(tasks, 1):
        mark = "x" if task["done"] else " "
        print(f"{i}. [{mark}] {task['text']}")


def cmd_done(args):
    tasks = load()
    index = args.index - 1
    if index < 0 or index >= len(tasks):
        print("invalid task number")
        return
    tasks[index]["done"] = True
    save(tasks)
    print(f"done: {tasks[index]['text']}")


def cmd_clear(args):
    save([])
    print("cleared all tasks")


def main():
    parser = argparse.ArgumentParser(description="Tiny to-do list")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="add a task")
    add.add_argument("text", nargs="+")
    add.set_defaults(func=cmd_add)

    lst = sub.add_parser("list", help="list tasks")
    lst.set_defaults(func=cmd_list)

    done = sub.add_parser("done", help="mark a task done")
    done.add_argument("index", type=int)
    done.set_defaults(func=cmd_done)

    clear = sub.add_parser("clear", help="clear all tasks")
    clear.set_defaults(func=cmd_clear)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
