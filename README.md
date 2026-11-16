# Longhand

**Teach your AI assistant to write in your own voice.** Longhand is an agent skill that builds a personal writing-style profile from texts you really wrote, in any language, so that what the assistant writes for you sounds like you and not like AI.

[Leggi in italiano](README.it.md)

A humanizer takes the AI out of a text. Longhand puts you into it.

## Example

One request, "ask the team for comments on the report by Friday", three results. The example is illustrative.

**Default AI:**

> Hi team, I hope this message finds you well! I wanted to reach out regarding the Q3 report. It would be greatly appreciated if you could share your feedback by Friday. Please don't hesitate to reach out with any questions. Best regards

**After removing the AI patterns:**

> Hi team, please send your comments on the Q3 report by Friday. Thanks.

Clean, but anyone could have written it.

**With a Longhand profile** (here, of someone whose emails are short, start in lowercase after the greeting, give the reason for a deadline and sign off with "thanks,"):

> Hi all,
>
> report's attached, v0.2. Comments by Friday so I can close it before the board meets.
>
> thanks,
> Sam

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

A language model writes the most likely next thing, so by default it makes the choice that suits the widest range of readers. You choose for one reader and one subject. Longhand records those choices.

1. **It collects samples.** Files you attach, text you paste, mail and documents if you connect them and agree.
2. **It weighs them.** Not every text counts the same: recent, very tidy ones may already have been through an AI. The best sample is an AI draft together with the version you rewrote by hand, because it shows what you cut, what you add and what you change.
3. **It writes the profile.** Only traits that appear at least twice in your texts.
4. **It tests it with you.** You get two short texts written with the new skill and a question: what is off?
5. **It keeps it current.** Every time you correct a text, the skill can learn from the correction.

Two rules set this apart from a list of banned phrases. First: what is yours stays yours. If your hand-written texts contain a pattern usually blamed on AI, it is your voice and it is left alone. Second: voice is not good writing. The skill is not there to improve you. It is there to sound like you (typos excluded).

## Longhand and humanizers

Tools such as [Humanizer](https://github.com/blader/humanizer) are very good at finding and removing AI writing patterns in a text you already have, and Humanizer can also match a writing sample you paste along with the text. Longhand does a different job:

- it builds your profile once, from many texts, and keeps it as a skill you reuse;
- it records what you do (greetings, formulas, rhythm, registers), not only what to avoid;
- it works in your language, with a pack of patterns and punctuation rules written for it;
- it updates when you correct a text.

They work well together: a humanizer cleans any text, Longhand makes texts start out in your voice.

Longhand writes for human readers. Getting past AI detectors is not a goal.

## Install

In Claude Code, as a plugin:

```text
/plugin install longhand --marketplace fdesimone/longhand
```

With any agent that supports skills, paste:

```text
Install the longhand skill from https://github.com/fdesimone/longhand
```

Or with `npx`:

```sh
npx skills add fdesimone/longhand --skill longhand --global --yes
```

Or by hand: copy the `skills/longhand` folder into your assistant's skills folder. In apps that let you upload skills, zip the folder and upload it from the settings.

Longhand is a standard agent skill in plain Markdown. It has been tried with Claude so far.

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

The pattern lists build on [no-ai-slop](https://github.com/petergyang/no-ai-slop) by Peter Yang and [Humanizer](https://github.com/blader/humanizer) by Siqi Chen, both MIT, and through them on Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). See [NOTICE.md](NOTICE.md).

## License

MIT. See [LICENSE](LICENSE). Changes are listed in [CHANGELOG.md](CHANGELOG.md).

If Longhand helps you, a star helps other people find it.
