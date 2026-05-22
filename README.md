# 🔨 Schmiede

[![PyPI version](https://badge.fury.io/py/schmiede.svg)](...)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](...)

> Forge the API, **not** the boilerplate.

Schmiede is a **batteries-included** FastAPI framework crafted around the builder
pattern. Compose production-ready APIs from ready-made modules like middleware,
observability (OTel), ORM (Tortoise), user management, and your own custom
modules. Everything is cleanly logged out of the box, so you can focus on
your business logic.

> [!WARNING]
> **Schmiede is in early alpha (v0.0.1a2).** The API is **unstable** and may change
> without notice between releases. Not yet recommended for production. Feedback
> and contributions are very welcome!

## Why Schmiede?

Past a certain point, every FastAPI project starts to feel the same. You write
the same user login, the same auth, the same middleware stack — over and over,
purely pro forma. And it's exactly this repetitive plumbing that bites you:
get the middleware order wrong and you've quietly broken your security. Before
you've written a single line of actual business logic, you've already burned
hours on logging, wiring, and boilerplate that has nothing to do with what
you're actually building.

Schmiede takes care of the plumbing. Compose your app from pre-wired, correctly
ordered modules and get back to the part that matters — your business logic.

## Installation

```bash
pip install schmiede
```

> [!WARNING]
> Schmiede is in early alpha (v0.0.1a2). Expect breaking changes between
> releases, and don't use it in production just yet.

## Quick Start

<!-- TODO: minimal runnable builder example -->

## Modules

| Module        | Description                              | Status   |
|---------------|------------------------------------------|----------|
| Middleware    | Pre-wired, correctly ordered middleware (CORS, GZip,...) | 🚧 WIP   |
| Observability | OpenTelemetry integration                | 🚧 WIP   |
| ORM           | Tortoise ORM setup (for User Management and other modules)                      | 🚧 WIP   |
| User Mgmt     | Authentication & user management         | 🚧 WIP   |
| Custom        | Build and plug in your own modules       | 🚧 WIP   |

## Roadmap

- [ ] Stabilize the core builder API
- [ ] Middleware module
- [ ] Observability module (OpenTelemetry)
- [ ] ORM module (Tortoise)
- [ ] User management module
- [ ] Documentation site
- [ ] First beta release (v0.1.0)

## Contributing

Patches welcome! Fork the repo and open a merge request. For anything larger,
feel free to open an issue first so we can discuss the direction.

## License

Apache 2.0 &copy; 2026 Arian Ott — see [LICENSE](LICENSE) for details.
Includes an express grant of patent rights. 