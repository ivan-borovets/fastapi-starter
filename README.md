# About

FastAPI Starter is a self-bootstrapping template that saves you from copying old projects and deleting stuff you don’t
need.
You answer a few questions and get a clean `src/`-layout, working migrations, env-based config, and ready-to-run
Docker.
No boilerplate hell — just a setup that works.
Powered by [Copier](https://copier.readthedocs.io/en/stable/) —
like [Cookiecutter](https://github.com/cookiecutter/cookiecutter), but smarter.

What will the result look like?
Roughly like this: [fastapi-clean-example](https://github.com/ivan-borovets/fastapi-clean-example) — a
framework-agnostic backend using FastAPI, implementing Clean Architecture and CQRS with DDD-inspired patterns, DIP (low
coupling), DI (no globals), hierarchical RBAC with permissions, and session-based authentication (cookies).

# What's included

- ⚙️ Scalable [src-layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) with proper
  packaging — works for both minimal apps and modular monoliths (modules can share a kernel and support common
  entrypoint)
- 🚀 [FastAPI](https://fastapi.tiangolo.com/) — included by default, easy to replace
- 🧩 [SQLAlchemy](https://www.sqlalchemy.org/) + [Alembic](https://alembic.sqlalchemy.org/en/latest/) — preconfigured,
  module-aware migrations (each module can manage its own database)
- 🐘 [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/) — environment-aware setup
  with PostgreSQL
- 📦 [Toml Config Manager](https://github.com/ivan-borovets/toml-config-manager) — structured `.toml` config, `.env`
  generation, multi-env support via `Makefile`
- 🗃️ Optional: [Dishka](https://github.com/reagento/dishka) DI — enables scoped DI with FastAPI; the project is
  structured to support it
- ✅ Optional: [pre-commit](https://pre-commit.com/) hooks and [GitHub Actions](https://github.com/features/actions) —
  basic checks and CI out-of-the-box

# How to generate a project

1. Install Copier

```shell
# sudo apt update
# sudo apt install pipx
# pipx ensurepath
pipx install copier
# or see https://copier.readthedocs.io/en/stable/
```

2. Run the generator

```shell
copier copy https://github.com/ivan-borovets/fastapi-starter <desired project path>
```

The project will be generated based on an interactive prompt — no guessing required.

And that’s it! ✨

> For first steps, see the generated `README.md` — it explains how to run the app, add modules, and manage config.

# What the generator asks you

When you run the generator, you'll be asked a few questions.

Here's what they mean — and what your answers will affect:

## `author_name`

* **Prompt**: What is your full name? (e.g. John Smith)
* **Affects**: `LICENSE`, `pyproject.toml`

## `project_name`

* **Prompt**: What is your project name?
* **Constraints**: Must start with a lowercase letter and contain only lowercase letters, digits or dashes
* **Affects**: `pyproject.toml`, `docker-compose.yaml` (if `use_toml_cfg_mgr` is enabled)

## `module_name`

* **Prompt**: What is the name of the first module?
* **Tip**: Typically derived from the project name, but you can override it
* **Affects**: The name of the first module in src-layout (`src/<module_name>`). Used for Alembic setup

## `use_dishka`

* **Prompt**: Do you need [Dishka](https://github.com/reagento/dishka)?
* **Affects**: Whether Dishka DI with helper plotter script is included
* **Say yes if**: You want scoped DI and plan to use Dishka’s integration with FastAPI

## `use_toml_cfg_mgr`

* **Prompt**: Do you need [Toml Config Manager](https://github.com/ivan-borovets/toml-config-manager)?
* **Affects**: Adds a structured config system (`config/` directory, `.env` generator, `settings.py` preconfigured,
  `Makefile` commands with `Dockerfile` and `docker-compose.yaml`)
* **Say yes if**: You want per-environment TOML configs, generated `.env` files, and `Docker` setup

## `use_pre_commit`

* **Prompt**: Do you need Pre-commit?
* **Visible only if**: `use_toml_cfg_mgr` is enabled
* **Affects**: Adds `.pre-commit-config.yaml` with basic checks
* **Say yes if**: You want checks before every commit

## `use_github_actions`

* **Prompt**: Do you need GitHub Actions?
* **Affects**: Adds a test workflow to `.github/workflows/ci.yml`
* **Say yes if**: You use GitHub and want basic CI out of the box

# Structure
```
.
├── config/...                               # configuration files and scripts, includes Docker
├── Makefile                                 # shortcuts for setup and common tasks
├── scripts/...                              # helper scripts
├── pyproject.toml                           # tooling and environment config (uv)
├── ...
└── src/
    ├── fastapi_starter/                     # first module
    │   ├── application/...                  # application logic (interactors, ports, etc.)
    │   ├── infrastructure/...               # adapters (e.g. SQLAlchemy, alembic setup)
    │   │   └── sqla_persistence/alembic/... # per-module alembic config and versions
    │   └── main/cli.py                      # entrypoint for CLI (`fastapi_starter alembic ...`)
    │
    ├── main/run.py                          # run script (e.g. uvicorn entrypoint)
    │
    ├── setup/
    │   ├── app_factory.py                   # app builder
    │   ├── config/...                       # app settings
    │   └── ioc/...                          # dependency injection setup
    │
    ├── shared/...                           # cross-module helpers or shared interfaces
    └── ...
```