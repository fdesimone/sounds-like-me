# Contributing

Thank you for helping. Longhand grows through small contributions from people who know a language well. You do not need to write code.

## Add a language

Each language has a pack in `skills/longhand/languages/<code>/`:

- `ai-patterns.md`: how AI gives itself away in that language (required);
- `punctuation.md`: the essential punctuation rules (required);
- `example.md`: a filled-in personal skill for an invented person (optional).

Steps:

1. Copy `skills/longhand/languages/_template/` to a folder named with the ISO code of your language (`es`, `fr`, `pt-BR`).
2. Fill in the two files in the language itself. Full guidance is in `skills/longhand/references/adding-a-language.md`. The short version: do not translate another pack, start from real AI texts in your language, one invented example per entry, and say what to write instead.
3. Run `python3 scripts/check_packs.py`.
4. Add your language to the table in `README.md`.
5. Open a pull request.

## Add or fix a pattern

Found a pattern that is missing, or a better example? Edit the pack and open a pull request. One entry is enough. If you would rather not edit files, open an issue with:

- the example sentence (invented or anonymized);
- why it sounds artificial;
- what a person would write instead.

## Report a profile that missed

If you used the skill and the profile did not sound like you, tell us what went wrong: which samples you gave, what it misread, what you had to correct. You do not need to attach your texts.

## Rules

- No personal data, names of real people or passages from confidential documents in examples.
- No profiles of real people in this repository. The method lives here. Profiles stay with the people who make them.
- Short, invented examples.
- One change per pull request, with two lines on why.
- Be kind in reviews. Many contributors are not developers.

## Maintainers of a language

If you add a pack and are willing to review later changes to it, say so in your pull request. Changes to a pack are best judged by someone who writes in that language every day.
