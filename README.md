# Task CLI

A tiny command-line to-do list written in Python. Tasks are stored in a local
`tasks.json` file, so there is no database or external service.

```bash
python task.py add buy milk
python task.py list
python task.py done 1
python task.py clear
```

Built as a small side project to practice argument parsing and simple file-based
state.
