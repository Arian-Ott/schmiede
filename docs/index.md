# 🔨 Schmiede

> Forge the API, **not** the boilerplate.

Schmiede is a **batteries-included** FastAPI framework crafted around the
builder pattern. Compose production-ready APIs from ready-made modules like
middleware, observability (OTel), ORM (Tortoise), user management, and your own
custom modules. Everything is cleanly logged out of the box, so you can focus
on your business logic.

!!! warning "Early alpha"
    Schmiede is in early alpha (**v0.0.1a2**). The API is unstable and may
    change without notice between releases. Not yet recommended for production.
    Feedback and contributions are very welcome!

## Why Schmiede?

Past a certain point, every FastAPI project starts to feel the same. You write
the same user login, the same auth, the same middleware stack — over and over,
purely pro forma. And it's exactly this repetitive plumbing that bites you: get
the middleware order wrong and you've quietly broken your security. Before
you've written a single line of actual business logic, you've already burned
hours on logging, wiring, and boilerplate that has nothing to do with what
you're building.

Schmiede takes care of the plumbing. Compose your app from pre-wired, correctly
ordered modules and get back to the part that matters — your business logic.

## Get Started

<div class="grid cards" markdown>

-   :material-rocket-launch: **[Quick Start](quickstart.md)**

    Install Schmiede and forge your first API in minutes.

-   :material-puzzle: **[Modules](modules/middleware.md)**

    Explore the ready-made modules and learn how to plug in your own.

-   :material-api: **[API Reference](api.md)**

    Browse the full API, generated straight from the source.

-   :material-hand-heart: **[Contributing](contributing.md)**

    Found a bug or want to help? Here's how to get involved.

</div>

## Installation

```bash
pip install schmiede
```

## License

Schmiede is released under the **Apache 2.0** license, which includes an
express grant of patent rights. See [LICENSE](https://github.com/<your-user>/schmiede/blob/main/LICENSE)
for details.