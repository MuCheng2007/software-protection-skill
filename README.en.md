<div align="center">

[简体中文](README.md) · **English**

![Software Protection Skill — Learn from failures](assets/hero.svg)

# 🛡️ Software Protection & Licensing Skill

**Ready to sell your app, but licensing still depends on one `if`? Ask your AI to find the weak points.**

Learn from public cracking reports to review software protection, design license key validation, offline activation and device binding, and plan online or hybrid licensing with implementation and acceptance criteria.

[![MIT](https://img.shields.io/badge/License-MIT-65dfc8?style=for-the-badge)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-Compatible-7e9cff?style=for-the-badge)](https://agentskills.io/specification)
[![Maintenance](https://img.shields.io/badge/Maintenance-Evolving_case_collection-ffbd73?style=for-the-badge)](#-ongoing-maintenance)

[Get started](#-get-started) · [Failure patterns](skills/software-protection/references/failure-patterns.md) · [Case index](docs/cases.md) · [Contribute](CONTRIBUTING.md) · [GitHub guide](docs/github-guide.md)

</div>

---

## ✨ What this project does

Your desktop app, plugin, or developer tool is ready to sell. Where should license checks live? How should offline licenses be signed? What happens if an online response is forged, or a local licensing branch is removed?

**This skill helps your assistant answer those questions against your project: locate the weak points, explain failure conditions, choose a practical design, and specify how to test it.**

| Your concern | What the skill helps review and design |
| --- | --- |
| Activation or license key checks can be skipped | Trace how licensing decisions control business capabilities and identify removable or replaceable checks |
| Offline licenses can be copied; device binding complicates legitimate replacement | Design signed licenses, machine binding, expiration, and device replacement, including offline limitations |
| A forged network response unlocks the app | Review response trust and server-side permissions, distinguishing local messages from controlled capabilities |
| Obfuscation or packing is enabled, but protection is unverified | Assess shipped artifacts, loading and update paths, and define anti-tampering acceptance tests |
| AI built the features but left the commercial licensing lifecycle incomplete | Plan issuance, activation, renewal, revocation, seats, outage recovery, and operations |

For independent developers and small teams adding licensing to their own software. It can also help organize remediation after authorized analysis with AI reverse-engineering tools such as REA (Reverse Engineer Anything). This is an independently maintained project, not affiliated with REA, and no protection testing against REA is claimed.

**Expected deliverables: protection priorities, an architecture recommendation, an integration plan, acceptance criteria, and remaining risks.** With source and runtime access, the assistant can help implement the plan. With design materials alone, it starts with a proposal.

**If AI can help modify the entire client, what still controls the paid capability?** The skill challenges cloud-delivered constants and keys that can be extracted and reused, evaluates keeping algorithms or essential computation on the server, and specifies APIs, authorization state, revocation, quotas, and direct API tests. It also explains the limits of fully offline protection. See the [architecture review reference](skills/software-protection/references/hostile-client-design.md) (Chinese).

An activation dialog, RSA signature, or executable packer alone does not explain what your software actually protects.

This project turns public reports into a reusable Agent Skill connecting **failure conditions → defensive measures → acceptance tests → remaining risks**. Ask for a complete design, or let an assistant help implement and harden it when it has access to your project and tools.

| 🔍 Identify priorities | 🧭 Choose an architecture | 🛠️ Implement and verify |
| --- | --- | --- |
| Keys, valuable logic, licensing entry points, assets, APIs, release and update paths | Offline signed licenses, online licensing, hybrid short-lived leases | Integration points, license claims, device and seat policies, operations, migration, acceptance criteria |

**Vendor-neutral, with no required operating system or AI platform.** The skill uses the standard `SKILL.md` format. Actual support depends on the assistant's skill-loading capabilities and its file, build, and runtime permissions. For programs without source code, assess whether modification is feasible first.

**Language coverage:** This page is available in Chinese and English. The skill instructions, references, case summaries, and contribution documents are currently primarily in Chinese. Ask your assistant to explain or deliver its work in English; the entire repository has not been translated.

## 🚀 Get started

1. Download the repository using **Code → Download ZIP**, or run:

```bash
git clone https://github.com/MuCheng2007/software-protection-skill.git
```

2. Copy the entire `skills/software-protection/` directory into your assistant's supported skills directory, preserving `references/`. A project-level Codex example is `.agents/skills/software-protection/`; follow the documentation for other assistants.
3. In a new session, explicitly ask to use `software-protection`. If your assistant does not load skills, ask it to read `SKILL.md` and the relevant references, then provide your project materials.

**Request a design:**

```text
Use software-protection to analyze this project. Respond in English.
Identify the most valuable parts to protect. Compare offline, online,
and hybrid licensing and recommend an architecture.
Include integration, license issuance, revocation, device replacement,
failure recovery, and acceptance tests. Propose a plan before editing code.
```

**Review existing protection:**

```text
Use software-protection to review the existing licensing chain.
Check public-key replacement, tampered verification results, forged
responses, restored caches, update entry points, and whether the business
features still work after licensing calls are removed.
Support each conclusion with project evidence, a fix, a test,
and remaining risks. Respond in English.
```

**Implement licensing:**

```text
Use software-protection to add offline signed licenses to this source
project that I own. Include expiration, a plan for managing up to two
devices, and a legitimate device-replacement process.
Explain the limits of a fully offline design, implement what is feasible,
and verify the behavior. Respond in English.
```

Skill directory reference: [OpenAI documentation](https://developers.openai.com/blog/skills-agents-sdk). Format: [Agent Skills specification](https://agentskills.io/specification).

## 🧩 Twelve failure patterns currently covered

| ID | Failure area | Defensive question |
| --- | --- | --- |
| F01 | Tampered cryptographic execution, public keys, or results | Who controls the actual capability when the verifier is modified? |
| F02 | Fake services or replaced licensing configuration | Is the response bound to the correct issuer, product, device, and permissions? |
| F03 | Client-reconstructible license-generation rules | Can the client issue its own licenses? |
| F04 | Packaging, bytecode, or assets mistaken for secrecy | Which secrets are actually shipped to the user? |
| F05 | Gaps in loading and update integrity | Is the verified file the file that executes? |
| F06 | Multiple checks sharing mutable state | Do all protection layers still depend on one writable boolean? |
| F07 | Missing backend permission or field constraints | Does the server independently enforce tenant, permission, and state checks? |
| F08 | Trials, heartbeats, seats, and time | How are concurrency, outages, revocation, and clock rollback handled? |
| F09 | Startup, import, or migration trusting cached state | Is restored licensing state verified again? |
| F10 | Inadequate cryptographic parameters | Are the actual keys, parameters, and signature scheme suitable? |
| F11 | Removable macro or script licensing modules | Does the business functionality still work after licensing calls are removed? |
| F12 | Semantics recovered through obfuscation or virtualization | Is protection applied to the final build, and is the valuable capability still fully shipped? |

See [failure-patterns.md](skills/software-protection/references/failure-patterns.md) for rules and tests. F08 remains an engineering regression category with limited source claims, not prevalence evidence. F12 research does not establish complete recovery of arbitrary protected products.

## 📚 Cases and evidence

The collection now contains **76 candidate source records and 12 failure patterns**.

The 1,225 supplied candidate rows have been triaged. All remaining 1,177 titles and excerpt passages were screened: 9 records were added after further original-source review and 1,168 excluded. This is not a full-page factual audit of 1,177 posts or runtime reproduction. See the [screening report and per-row decisions](docs/research/remaining-1177-review-2026-10-21.md) (Chinese).

Records include practical claims, educational examples, historical context, and exclusions. **This does not mean 76 independently confirmed cracked products.** Sources include Kanxue, ChinaPYG, 52pojie, Habr, GitHub, and individual research posts. Each record now has a review of its available source passages, date basis, classification, and pattern mapping. Partial access and unresolved dates remain explicit; this is not a complete online recrawl or runtime reproduction.

Records preserve original publication dates, the extent of material read, sources, prerequisites, and limitations. No third-party samples have been independently reproduced. Authors' success claims are not presented as verified results or evidence that current product versions remain vulnerable.

➡️ [Per-record evidence review (Chinese)](docs/research/full-review-2026-10-15.md) · [Case index](docs/cases.md) · [Structured records](skills/software-protection/references/forum-cases.json) · [ChinaPYG follow-up](docs/research/chinapyg-supplement-report.md)

## 🔄 Ongoing maintenance

**Latest release: [v0.3.4](https://github.com/MuCheng2007/software-protection-skill/releases/tag/v0.3.4)** · [Download the skill package](https://github.com/MuCheng2007/software-protection-skill/releases/download/v0.3.4/software-protection-v0.3.4.zip). This update adds execution-layer and runtime-data exposure reviews, plus acceptance scenarios for reuse after one licensed run, new tasks after revocation, and direct backend calls. See the [review guidance](skills/software-protection/references/ai-reverse-engineering.md) and [pinned source attribution and scope](docs/research/r0crawl-review-2026-10-25.md) (Chinese). This workflow study does not increase the case count or claim protection against a particular tool.

**This project will continue collecting public cases of licensing failures, tampering, and software protection to help developers design licensing and protect their software.**

The process is: submit a public source → check dates and evidence → identify the failure conditions → add defenses and acceptance tests → review and merge. Successful defenses, verified fixes, and counterexamples are welcome too.

- Submit cases through [Issues](https://github.com/MuCheng2007/software-protection-skill/issues) using the evidence template.
- Submit improvements through pull requests and run the local checks first.
- Follow [CHANGELOG.md](CHANGELOG.md) and [ROADMAP.md](ROADMAP.md). Maintenance uses human review; there is no promised update schedule or automatic background scraping of entire forums.

## 🧠 Scope and limits

A signature proves who issued a license; it does not ensure that a modified client executes verification. Online licensing protects capabilities actually controlled by the server; returning `true` alone is insufficient. Obfuscation, native compilation, and integrity checks can raise the cost of tampering, but cannot guarantee uncrackable software.

This project provides design and implementation guidance. It is not a ready-made licensing server or a universal EXE packer. Without a target project, the output is a reference design. Without execution, no protection test is claimed to have passed. Use it to improve protection for software you own or are authorized to assess. The repository does not collect usable third-party activation codes, key generators, or cracking attachments.

## 🧰 Repository map

```text
skills/software-protection/  Skill instructions and references loaded as needed
docs/                       Case index, research coverage, and guides
assets/                     Repository artwork
scripts/validate.py         Dependency-free structure and evidence checks
.github/                    Contribution templates and automated checks
```

```bash
python scripts/validate.py
```

Checks cover structure, internal references, case fields, and pattern mappings. They do not prove that a target application is secure.

## ⭐ Star History

Stars over time, provided by [Star History](https://www.star-history.com/?repos=MuCheng2007%2Fsoftware-protection-skill&type=date). This measures stars, not page views or installations. As the project is new, the curve may be empty until there is growth data. Image availability and refresh timing depend on the third-party service and caching.

<a href="https://www.star-history.com/?repos=MuCheng2007%2Fsoftware-protection-skill&type=date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=MuCheng2007/software-protection-skill&amp;type=Date&amp;theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=MuCheng2007/software-protection-skill&amp;type=Date" />
    <img alt="Star History for Software Protection &amp; Licensing Skill" src="https://api.star-history.com/svg?repos=MuCheng2007/software-protection-skill&amp;type=Date" width="800" />
  </picture>
</a>

## 📄 License and sources

Original skill content, scripts, and graphics use the [MIT License](LICENSE). You may use, modify, and share them. Rights in third-party posts, trademarks, and linked pages remain with their respective owners. This repository stores brief original summaries and citations. See [NOTICE](NOTICE).
