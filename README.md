# Learning Python for Network Automation, Software Development, and AI

Overview
- Hands-on repo for learning Python across three practical paths: Network Automation, Software Development, and Artificial Intelligence.
- Includes tiny examples you can run: [hello.py](hello.py) and [chapter2.py](chapter2.py).
- Example variables in the workspace: [`chapter2.my_name`](chapter2.py), [`chapter2.fav_number`](chapter2.py).

Getting started
1. Install Python 3.8+.
2. (Optional) Create and activate a virtual environment:
   - python -m venv .venv
   - source .venv/bin/activate  (macOS/Linux) or .\.venv\Scripts\activate (Windows)
3. Run the examples:
   - python hello.py
   - python chapter2.py

Project layout
- [hello.py](hello.py) — minimal "hello world" example.
- [chapter2.py](chapter2.py) — simple variables and type checks demonstrating basic Python types and print output.

Learning paths and recommended libraries
- Network Automation
  - Netmiko, NAPALM, Nornir, Paramiko, Ansible
  - Focus: device automation, SSH, templating, and idempotent configs
- Software Development
  - pytest, black, flake8, mypy, packaging (setuptools/poetry)
  - Focus: testing, linting, CI, modular design
- Artificial Intelligence / ML
  - numpy, pandas, scikit-learn, tensorflow, torch
  - Focus: data pipelines, model training, evaluation, and deployment

Next steps
- Expand examples into small projects per path (e.g., a Netmiko script, a REST API with FastAPI, an ML notebook).
- Add tests (pytest) and a requirements.txt or pyproject.toml.
- Iterate on code style (black, isort) and add CI/CD.

Resources
- Official Python docs: https://docs.python.org/3/
- Tutorials for libraries listed in each learning path.

License
- Add a LICENSE file as needed.

References in this workspace
- [chapter2.py](chapter2.py)
- [hello.py](hello.py)
- Variables: [`chapter2.my_name`](chapter2.py), [`chapter2.fav_number`](chapter2.py)
