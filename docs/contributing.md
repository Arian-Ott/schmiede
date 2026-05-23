# Contributing to Schmiede

Thanks for your interest in contributing to Schmiede! Contributions of all
kinds are welcome. To keep things smooth for everyone, please follow the
workflow below.

## Workflow

1. **Open an issue first.** Before you start coding, open an issue describing
   what you intend to work on. This way everyone knows who's working on what,
   and we avoid duplicated effort or stepping on each other's toes.
2. **Fork the repository.** Create your own fork to work in.
3. **Write meaningful commits.** Keep commits focused and write clear,
   descriptive commit messages. A good commit tells the next person *why* the
   change was made, not just *what* changed.
4. **Write tests.** Once your feature or fix is done, write `pytest` tests for
   it. Cover more than just the happy path — edge cases, error conditions, and
   failure modes matter just as much.
5. **Make sure everything is green.** All tests must pass before you submit.
6. **Update the changelog.** Add a line describing your change under the
   `## [Unreleased]` section of `CHANGELOG.md`, in the appropriate category
   (Added / Changed / Fixed / Removed). Keep it short and user-facing, and
   link the related issue (e.g. `(#42)`). The changelog entry is part of your
   contribution — the reviewer checks it, the maintainer cuts it into a
   versioned release.
7. **Open a merge request.** Once your tests are green, open an MR.
8. **Merge.** After review and approval, your contribution gets merged. 🎉

## Code Quality

Code quality standards in Schmiede are **high**, and we keep them that way.

This applies to **tool-assisted contributions** as well. If you use AI tools or
code generators, the output must meet the same quality bar as anything written
by hand. Review, understand, and clean up generated code before submitting it.
"The tool wrote it" is not a free pass.

> *“A computer can never be held accountable, therefore a computer must never make a management decision.”*
> 
> – attributed to an IBM Training Manual, 1979 [[1]](https://www.ibm.com/think/insights/ai-decision-making-where-do-businesses-draw-the-line)

Functions must be **free of side effects**. Given the same input, a function
should always return the same output and change nothing outside its own scope.
This matters because side-effect-free functions are **predictable**: you can reason
about them in isolation, test them without elaborate setup or mocking, and
compose them freely without worrying about hidden state changing behaviour
elsewhere. Side effects are where subtle, hard-to-trace bugs hide — keeping
them out keeps the codebase reliable.

Of course, there are many best practices around code quality, but those are the most important ones.


## Docstrings

Document your code with docstrings in **Sphinx style**. The one-line summary is
mandatory — and not just for tidiness: Sphinx needs it to generate the API
documentation, and your editor uses it as the tooltip when you hover over the
function. A good summary means readers understand what a function does without
having to open it or read its body.

```python
def enable(self, module: AbstractModule) -> "Schmiede":
    """Enable a module in Schmiede.

    :param module: Module to be enabled.
    :type module: AbstractModule
    :raises ValueError: Module is already enabled.
    :return: Initialised Schmiede object.
    :rtype: Schmiede
    """
```

Keep the summary precise. Every word should earn its place and add to the
reader's understanding. Add a longer description below it only where it helps:
complex behaviour or large functions. Simple, self-explanatory functions need
nothing more than the summary line.

Examples for behaviour requiring more detail:

* Complicated validation logic including complex regex
* Actions with irreversible effects on the system
* Large functions
* `$YOUR_FAVOURITE_EXAMPLE`

## Code Signing

Code signing is **not required**, but it is **recommended**. Signing your
commits helps verify authorship and keeps the project's history trustworthy.

## Questions?

If anything is unclear or you get stuck, **don't hesitate to reach out** — open
an issue or start a discussion or reach out to me via [email](https://github.com/Arian-Ott/schmiede/blob/master/pyproject.toml#L9). We're happy to help.

Happy Hacking! 🔨