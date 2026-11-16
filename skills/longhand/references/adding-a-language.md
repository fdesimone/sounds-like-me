# Adding or improving a language

The analysis method is the same for every language. Two things change: the patterns that give AI away and the punctuation rules. Each language keeps them in its own pack:

- `languages/<code>/ai-patterns.md` (required)
- `languages/<code>/punctuation.md` (required)
- `languages/<code>/example.md` (optional: a filled-in personal skill for an invented person)

`<code>` is the two-letter ISO 639-1 code, lowercase (`it`, `en`, `es`, `fr`, `de`, `pt`). For a regional variety add the region: `pt-BR`, `en-GB`.

Packs are written in their own language. Skeletons to copy are in `languages/_template/`.

## Writing a new pack

- **Do not translate.** AI patterns differ from language to language. Translating an existing pack produces entries that do not exist in the new language and misses the ones that do. Start from real texts generated in the language.
- **Collect first, sort later.** Have several models write about ten texts of different kinds (an email, a post, a report page) and mark what keeps coming back.
- **One example per entry.** Invented, short, with no reference to real people or companies.
- **Say what to do instead.** A list of prohibitions alone produces stiff texts.
- **Flag imports from English.** Many models think in English and translate: constructions, punctuation and capitalization carried over are among the clearest tells.
- **Keep the same sections** as the template, so people moving between languages find their way.
- **Write natively.** The author should be a native speaker or use the language for work.

## Improving an existing pack

Small additions are the most useful contributions: a pattern that is missing, a better example, a punctuation rule people keep getting wrong. One entry is enough for a pull request.

## Contributing from a session

After building someone's profile you may have found patterns the pack lacks. To turn them into a contribution:

1. keep only the general pattern, not the sentence it came from;
2. write a new, invented example for it;
3. add what a person would write instead;
4. give the person the snippet and point them to CONTRIBUTING.md in the repository.

Never include the person's texts, name or profile, and do not submit on their behalf unless they ask.

## Check before submitting

From the repository root:

```sh
python3 scripts/check_packs.py
```

It verifies that every pack has the required files and that no template placeholders are left.
