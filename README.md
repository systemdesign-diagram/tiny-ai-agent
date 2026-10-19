# Tiny AI Agent

A small AI agent built step by step, with a newsletter documenting the engineering process.

The goal is to build a minimal, understandable agent that can:
- respond to a user's message using an LLM,
- call a small set of explicitly allowed tools,
- maintain simple conversation memory,
- handle common errors safely.

## Project status

This repository is an initial scaffold. Features should only be marked complete after they are implemented and tested.

## Quick start

Requires Python 3.10+.

1. Create and activate a virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and add your API key.
4. Run:

   ```bash
   python main.py
   ```

The initial version is a scaffold and does not yet call an LLM. The implementation tasks are tracked in `DEVELOPMENT.md`.

## Project structure

```text
tiny-ai-agent/
├── agent/
│   ├── __init__.py
│   ├── errors.py
│   ├── memory.py
│   ├── tools.py
│   └── llm.py
├── docs/
│   └── architecture.md
├── tests/
│   └── test_memory.py
├── .env.example
├── .gitignore
├── DEVELOPMENT.md
├── main.py
└── requirements.txt
```

## Engineering principles

- Keep the first version small and easy to understand.
- Record architecture decisions in `docs/architecture.md`.
- Do not claim a task is complete without implementation or test evidence.
- Never commit API keys or other secrets.
