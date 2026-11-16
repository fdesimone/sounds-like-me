# Longhand

Teach your AI assistant to write in your own hand, starting from texts you really wrote. Works in any language.

[Leggi in italiano](README.it.md)

## The problem

AI-written texts all sound alike, and readers notice by the first line. Tools that "remove the AI" from a text help, but they work by subtraction: they strip the patterns typical of language models and leave a clean text that belongs to nobody.

To get a text that is yours you need the other half: a profile of how you write. Where you put the point, how much you cut, which words you use, how you greet people, which figures of speech come naturally, what you would never write.

## What it does

`longhand` is a skill that builds another, personal skill. It reads your texts, derives the profile of your voice and saves it as a skill of its own (`style-yourname`). From then on your assistant uses it whenever you ask for something written in your name.

The personal skill contains:

- the traits of your voice, each with an example from your own texts;
- the words, formulas and figures of speech you use;
- the punctuation rules of your language, plus your preferences;
- your registers (short emails, documents, complaints, messages) with greetings and sign-offs;
- the AI patterns that are not yours;
- a final check the assistant runs before handing you the text.

## How it works

1. **It collects samples.** Files you attach, text you paste, mail and documents if you connect them and agree.
2. **It weighs them.** Not every text counts the same: recent, very tidy ones may already have been through an AI. The best sample is an AI draft together with the version you rewrote by hand, because it shows what you cut, what you add and what you change.
3. **It writes the profile.** Only traits that appear at least twice in your texts.
4. **It tests it with you.** You get two short texts written with the new skill and a question: what is off?
5. **It keeps it current.** Every time you correct a text, the skill can learn from the correction.

Two rules set this apart from a list of banned phrases. First: what is yours stays yours. If your hand-written texts contain a pattern usually blamed on AI, it is your voice and it is left alone. Second: voice is not good writing. The skill is not there to improve you. It is there to sound like you (typos excluded).

## Install

With an agent that supports skills, paste:

```text
Install the longhand skill from https://github.com/fdesimone/longhand
```

Or with `npx`:

```sh
npx skills add fdesimone/longhand --skill longhand --global --yes
```

Or by hand: copy the `skills/longhand` folder into your assistant's skills folder. In apps that let you upload skills, zip the folder and upload it from the settings.

## Use

```text
/longhand
```

Or in words: "learn my style", "I want you to write like me". Have about ten emails ready, a couple of long texts and, if you can, an AI draft with your own rewrite.

## Languages

The method is the same for every language. What changes is how AI gives itself away and how punctuation works, so those live in language packs.

| Language | Code | AI patterns | Punctuation | Example profile |
| :- | :- | :-: | :-: | :-: |
| Italian | `it` | yes | yes | yes |
| English | `en` | yes | yes | not yet |

No pack for your language? The skill still works: it derives the patterns from an AI draft and your rewrite. And you can add the pack for everyone else.

## Help it grow

This project gets better with every language and every pattern people add. The most useful contributions:

- **a new language pack**: two files, written natively, from the skeletons in `skills/longhand/languages/_template/`;
- **one more pattern** for a language that already has a pack: one entry is enough for a pull request;
- **a report** of a profile that did not sound like you, and what you had to fix.

See [CONTRIBUTING.md](CONTRIBUTING.md). The skill itself offers to draft a contribution when it finds patterns the pack lacks, always with invented examples and never with your texts.

## What is inside

- `skills/longhand/SKILL.md`: the steps the assistant follows;
- `skills/longhand/references/method.md`: which samples to trust and what to look for;
- `skills/longhand/references/adding-a-language.md`: how to add or improve a language;
- `skills/longhand/assets/personal-skill-template.md`: the template of the personal skill;
- `skills/longhand/languages/<code>/`: one pack per language;
- `scripts/check_packs.py`: checks that every pack is complete.

## Privacy

- The skill reads mail and documents only if you ask and only as much as needed.
- No personal data, third-party names or passages from confidential documents go into the personal skill.
- Your profile stays with you: this repository holds the method, not the profiles of the people who use it.
- The skill builds the profile of the person using it. It is not for imitating other people.

## Limits

The method came out of building one person's profile and was generalized from there. It works better with more samples and with at least one draft and rewrite pair. Reports and corrections are welcome.

## Credits

The list of patterns to avoid and the idea of a final check build on [no-ai-slop](https://github.com/petergyang/no-ai-slop) by Peter Yang (MIT license). See [NOTICE.md](NOTICE.md).

## License

MIT. See [LICENSE](LICENSE).
