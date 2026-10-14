# CLAUDE.md

This repo holds the RevealJS lecture decks, lecture notes and recitation exercises for **Giải thuật nền tảng của Khoa học dữ liệu** (UET.DSE2053). The current semester is `2627-1/`.

`AGENTS.md` is the full, authoritative specification, written in Vietnamese. `slide_authoring_standard.md` is the mandatory standard for how slides build knowledge for second-year students. This file tells Claude Code how to apply both: repo layout, commands, the rules most often broken, and how the multi-agent workflow maps onto Claude Code tools. Precedence: the user's instructions first, then `AGENTS.md` (including its own priority list), then this file. Read the relevant section of `AGENTS.md` and `slide_authoring_standard.md` before any deck or notes work.

The presentation rules were aligned on 2026-10-14 with the sibling courses `../math-4-AI` and `../rl-plan` (their `AGENTS.md`, `CLAUDE.md`, strand title slides, density caps, textbook-style notes), with the author's MAT1101 slides in `../MAT1101/` and with the author's textbook *Học máy thống kê* in `../SML-textbook-main.zip`. Those are style models only, never content sources; the content sources stay in `sources/`.

## Repo map

| Path | Contents |
|---|---|
| `sources/source.md` | Course-level source map: recommended lecture order, original-session mapping, learning outcomes, prerequisites, materials, open questions. **Read first for every lecture.** |
| `sources/reference-slides/README.md` | Reference-slide mapping for the 15 recommended lectures, with completeness status |
| `sources/reference-slides/`, `textbooks/`, `exercises/`, `papers/` | Detailed sources (MMDS, Stanford CS246, db-book…); binaries are gitignored |
| `2627-1/lecture-NN-<ten-bai>.html` | One RevealJS deck per lecture; `NN` follows the recommended order in `sources/source.md` |
| `2627-1/lecture-template.html` | Base for every deck: opening strand, strand title slide, algorithm slide, conclusion strand, recitation strand |
| `2627-1/lecture-style.css` | The **only** course stylesheet for decks; holds `.strand-title`. Lecture 02 is the reference for shared components |
| `2627-1/revealjs/`, `plugin/`, `vendor/` | Local runtime; nothing core loads from the network |
| `2627-1/img/lec-NN/` | SVG assets for each lecture |
| `2627-1/planning/lec-NN/` | `outline.md`, `storyboard.md`, `review-log.md` (tracked; never linked from the index) |
| `2627-1/materials/lec-NN/lecture-note.md` | Public self-study note, rendered by `material-viewer.html`; template in `materials/_templates/` |
| `2627-1/material-viewer.{html,css,js}`, `material-index.css` | Static Markdown viewer (14 block types, `DIRECTIVE_LABELS` in the JS); no build step |
| `2627-1/examples/`, `materials/lec-NN/code/` | Practice bundles that exist only where the source has matching content |
| `2627-1/index.html` | Semester index; links only finished decks and checked notes |
| `skills/build-slide-deck-outline/` | Project skill, exposed to Claude via `.claude/skills/` (symlink). Its default "năm 3" audience is overridden by `AGENTS.md`: the audience is second-year students |
| `.codex/`, `codex-orchestrator`, `openrouter-mcp/` | Historical Codex/OpenRouter tooling. Do not use it; its authorisations no longer apply |

Ignore `.DS_Store`, `._*` and `~$*` files everywhere.

## Commands

```bash
python3 -m reloadserver 8765                      # from repo root; port is positional, never --port
# deck:  http://localhost:8765/2627-1/lecture-NN-<ten-bai>.html
# note:  http://localhost:8765/2627-1/material-viewer.html?doc=materials/lec-NN/lecture-note.md&deck=lecture-NN-<ten-bai>.html
git diff --check
```

Port 8765 may be held by a sibling project's server; check the process cwd before trusting a 404. Headless Chromium through Python Playwright is installed and is the visual-check tool (see Visual verification). A density-count script (syllables, lines, syllables per line per slide) lives in the session scratchpad when needed; its results go in `review-log.md`.

## Hard rules

- Never read, load or send `.env` or `.env.*`. Never put secrets in prompts, logs or commits.
- Do not use OpenRouter, `openrouter-mcp/`, Codex or direct model API/CLI calls to stand in for sub-agents.
- **Intake:** a lecture request starts by reading `sources/source.md`, then the matching row in `sources/reference-slides/README.md` and every local file it maps. If a required source is missing, stop after the inventory and ask. Never pick a lecture for the user.
- **MMDS-anchored lectures:** compare the official `mmds.org` slides with the mapped Stanford CS246 slides cluster by cluster; prefer MMDS when equal and log any Stanford choice. Redraw everything; never copy their CSS, fonts or rasters. Credit `http://www.mmds.org` on the cover or the sources slide when a substantial part is used.
- **CSS:** decks link `2627-1/lecture-style.css` only.
  - No `<style>` blocks; no inline styles that override the shared type scale; no `.dense` or inline `font-size` to squeeze a slide under the density cap.
  - Lecture-specific styles live in the shared file, scoped by the deck's root class (e.g. `.lecture-pagerank`); decks using shared components carry `.course-deck`.
  - Before adding a style, look for an existing class and its Lecture 02 usage. Editing shared CSS means checking every affected deck, at least Lecture 02 and 03, at wide and narrow sizes, and logging the scope in `review-log.md`.
- **RevealJS config:** `lang="vi"`, 1280×720; outer `<section>` = one strand, inner `<section>` = one slide; footer at the end of `.slides` with course name, semester and lecture number.
  - Settings: `controlsLayout: "edges"`, `slideNumber: true`, `hash: true`, `hashOneBasedIndex: true`.
  - Plugins: `RevealMath.KaTeX`, `RevealNotes`, `RevealHighlight`, all local. No `fragment`.
  - Every slide has a unique `data-slide-id`, which never appears on the slide face or in notes.
- **Paths** are relative and must work when the server runs at the repo root.
- **Maths and figures:** in Markdown use only `$...$` and `$$...$$`. Formulas, tables, pseudocode and code are KaTeX, HTML or code blocks, never images.
  - Every diagram is redrawn as SVG in `img/lec-NN/` with `role="img"` and specific alt text; colour is never the only signal.
  - Rasters need a user-approved exception logged in `review-log.md`; if not approved, stop that part and ask. No AI-generated images standing in for data or evidence.
- **Recitation exercises** come directly from the assigned textbook or source, with problem number, section and page recorded in the storyboard and speaker notes. Translate, split or trim, but never invent data or change the mathematical task.
- **Index:** `index.html` never links `planning/`, outlines, storyboards, review logs or sources, and never links unfinished work. A note link appears only after the note passed its checks; until then show the `Chưa có` status.

## Writing course content (Vietnamese)

Everything a student sees is formal, academic, native Vietnamese: slide text, titles, figure labels, speaker notes, lecture notes, solutions.

- **English:** only for proper names, software, standard symbols, algorithm names and terms without a stable translation. The English term goes in parentheses at its first use in each document.
- **Abbreviations:** spell out in Vietnamese first, abbreviation in parentheses.
- **Terminology:** write `X (còn gọi là Y)` the first time, `X` afterwards. "Lời giải", never "Đáp án". Define or recall ("Nhắc lại:") every symbol, assumption and result before its first use on a slide or in a section. The lecture's Vietnamese–English term table lives in `outline.md`.
- **Banned tone:** no exclamations, praise, slogans, marketing or rhetorical questions.
  - No simulated speech or instructor/author directions, e.g. "chúng ta hãy nhìn", "nhấn mạnh với sinh viên", "đến đây chuyển sang trang sau", "người viết cần bổ sung hình".
  - Learning tasks ("Tính", "Xác định", "Chứng minh") and algorithm steps are fine.
  - In lecture notes a genuine research question answered immediately in the same section is allowed; an unanswered one is rhetorical.
  - Authoring and coordination notes live only in `outline.md`, `storyboard.md` and `review-log.md`.
- **Titles:** name the concept, algorithm or result. No questions ("Tại sao…?", "Vì sao…?") and no progress phrasing ("Từ … đến …"). Function prefixes before a noun phrase are allowed: "Ví dụ: <đối tượng>", "Bài tập: <chủ đề>", "Chứng minh: <kết quả>", "Tính đúng: <thuật toán>", "Thuật toán: <tên>", "Chi phí: <đối tượng>"; a prefix never stands alone. A title repeats across slides when an example continues, with the step name after a comma.
- **Slide sentences:** terse mathematical prose ("Đặt …", "Suy ra …", "Với mỗi dải $j$, tạo khóa …"). No "ta thấy", "rõ ràng", "chúng ta" or "=" used for "là". At most one closing line per slide, a conditional result or a number, never a slogan or arrow chain.
- **Allowed labels** (bold): with a period `Định nghĩa. Định lý. Mệnh đề. Bổ đề. Hệ quả. Nhận xét. Thuật toán. Chứng minh. Trực quan. Ví dụ.`; with a colon `Nhu cầu: Ý nghĩa: Diễn giải: Lưu ý: Nhắc lại: Cách khác: Dạng khác: Ký hiệu: Quy ước: Giả thiết: Kết luận: Đầu vào: Đầu ra: Bất biến: Điều kiện dừng: Trường hợp biên: Mô hình: Câu hỏi: Gợi ý: Lời giải: Đọc trước: Nguồn:`. Section-type labels **Đọc thêm** and **Thực hành** use the shared CSS class.
- **Keep off the slide face and out of speaker notes:** slide IDs, workflow labels, timings, and internal codes from planning files ("N02", "V02", "HT3", "MT1"). A note result number such as "(Định lý 06.3)" may follow a verbal statement at most once per slide. Per-slide source lines are gone: sources go in the speaker notes and on the "Nguồn và tài liệu đọc" slide; the cover may carry the MMDS credit and recitation slides the book exercise number.
- **Questions on slides** use the label **"Câu hỏi:"**.
- **Speaker notes** are short academic explanation: assumptions, what a formula or figure means, why the algorithm is correct, easy confusions, the link to the next result, and hints, solutions or grading guidance for exercises. Usually 40–150 syllables, up to ~250 for proofs or solutions (longer is only a `nhẹ` finding). Never open with "Trang này …" or with the document as subject. They must not repeat the slide.
- **Voice of lecture notes (from *Học máy thống kê*):** "chúng ta" for plans, needs, method choices and limits; "ta" inside calculations; "người ta" only for common practice; the document is never the subject ("Mục này định nghĩa…" is banned); objective sentences inside definition/theorem/algorithm blocks; no "hãy" outside exercise statements. Slides and speaker notes never use "chúng ta".
- **no-ai-slop is mandatory.** It is installed as the user-level Claude skill `no-ai-slop` (`~/.claude/skills/no-ai-slop/`). Load it with the `Skill` tool, or read `SKILL.md` and `eval.md` there, before editing or reviewing text. Sub-agents must load it too.
  - Editors use Edit mode, then self-check against `eval.md`.
  - Read-only reviewers use Detect mode: quote the problem line and propose a fix.
  - Academic register and algorithmic precision take priority over the skill's voice and humour advice. Never use AI-detector scores as evidence.
- **Continuity check (`quill`):** use the user-level Claude skill `quill` (`~/.claude/skills/quill/`) to check outline, concept order, terminology, notation and continuity between sections. Load it with the `Skill` tool. This is not a book project: never create `quill.json`, never run its Init workflow, and ignore its `/quill:*` commands and manuscript templates. Use only its consistency and continuity checks.

## Deck structure and content

- **Audience and time:** second-year students with programming, discrete maths, linear algebra and basic probability. 120 minutes of lecture plus a separate vertical part of 60 minutes of recitation in the same HTML. Timings go in the storyboard and notes, never on slides.
- **Strands:** 5–7 outer sections, including an opening and a conclusion; the recitation part is its own outer section after the conclusion. Each strand has a type from `AGENTS.md` (giới thiệu, khái niệm/mô hình, thuật toán, chi phí, hệ thống, thực hành, tổng kết), a function, an input from the strand before, and an output the next one uses. Going outside 5–7 needs a source or user reason recorded in `storyboard.md` and `review-log.md`.
- **Opening strand, in order** (`AGENTS.md` §"Mẫu RevealJS bắt buộc"): cover with a one-sentence thesis; "Tiên quyết và quy ước" ("Nhắc lại:" line for reused results, "Ký hiệu:" line for domains, sizes and index conventions); objectives; "Nội dung" numbered to match the strand title slides and `#/N`, optional "Đọc trước:" line; "Vấn đề trung tâm" (the big-data problem in one line plus each strand's conditional answer in one line), or a merged "Nhắc lại / Ví dụ / Nhu cầu" slide.
- **Strand title slides (`AGENTS.md` §"Trang tiêu đề mạch"):** every strand except the opening starts with a `section.strand-title` slide, `id="mach-N"`, `data-slide-id` `<prefix>-00` (or `<prefix>-T` if taken).
  - Face: number in digits in `span.strand-number` ("2.", "3.", …), a noun-phrase name that differs from the first content slide's title, one declarative lead `p.strand-lead` (≤ 25 syllables, "Muốn <đích>, phải <việc>" or "Nhu cầu:"), optional `p.strand-keys` (≤ 5 noun phrases joined by " · "). Markup: `div.strand-title-body` > `h2` + `p.strand-lead` + `p.strand-keys`; styles live in `lecture-style.css`.
  - No definitions, formulas, pseudocode, figures, "Đầu vào/Đầu ra" or codes on the face. Notes of 40–100 syllables: inherited result, the strand's task, the output handed on. One storyboard entry each, position "điểm vào mạch N".
  - Existing decks get strand title slides only in a logged revision pass requested by the user.
- **Conclusion strand:** its own strand title; a summary table `Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán`; for multi-algorithm lectures also `Thuật toán | Đầu vào | Bảo đảm | Chi phí`; a slide answering the central problem conditionally; "Câu hỏi tự kiểm tra" opening with "Câu hỏi: trả lời và nêu kết quả đã dùng." and 2–4 short questions with solutions in the notes; "Nguồn và tài liệu đọc" with the sources, the MMDS credit and the viewer link; a one-line link to the next lecture when `sources/source.md` supports it. No new concepts.
- **Learning cycle for every core concept or algorithm:** big-data use case → problem → intuition → worked example → formalisation → algorithm and correctness → application and cost → check.
  - Steps may share a slide but may not be silently dropped; a reduced cycle for a minor concept needs a reason in the storyboard.
  - Lecture notes use their own order: need (with a numeric lead-in example) → definition → worked example → intuition/geometry → theorem → algorithm → proof → application and check, at textbook depth (see Lecture notes).
- **Opening a concept:** the problem slide starts with "Muốn …" or "Nhu cầu:", then 1–3 concrete lead-in examples with numbers (a small hand-computable dataset or a sourced scale). The formal slide may keep the same title. "Ý nghĩa:" after a result never replaces the intuition step.
- **Algorithm clusters** (`AGENTS.md` §"Mở một khái niệm hoặc một thuật toán"): limit of the previous method in one line with a number → idea in words, compared to a known algorithm ("tương tự … nhưng khác ở …") → the structural observation that beats the naive method → hand-run one step → "Đầu vào:"/"Đầu ra:" right before the pseudocode → a reading of the pseudocode naming the deciding operation and what is left open → correctness (invariant, induction, exchange or contradiction, never intuition alone) → one cost sentence with named parameters, then the count table. Never open an algorithm with its name or pseudocode. State the cost model and which complexity (worst, average, expected, amortised). Re-run every worked example yourself.
- **Result slides:** statement with assumptions, optional "Ý nghĩa:" line, optional one-line "Chứng minh.". Longer proofs go on "Chứng minh: <kết quả>" slides; correctness on "Tính đúng: <thuật toán>" slides (initialisation–maintenance–termination).
- **Example and exercise slides:** "Ví dụ: <đối tượng>": data with numbers → "Tính …" → one step per line or table row → result with "Diễn giải:" or a check. "Bài tập: <chủ đề>": "Câu hỏi:" typed, data tables in the same layout as the lead-in example; a worked exercise puts "Lời giải:" on the next slide with the same title; self-study answers stay in notes. Each content strand has at least one worked exercise or a "Câu hỏi" slide with solutions in the notes.
- **Running examples:** 1–2 hand-computable datasets reused across concepts, named by object ("bốn tập đặc trưng", "kho một triệu tài liệu"), never by code. Each reuse answers a new question or compares two tools on the same numbers. The opening big-data situation is recalled with numbers in the conclusion.
- **Cost sections:** "Mô hình:" line first; count step × times × cost per time before asymptotics; separate work, completion time, memory and transfer; mark which numbers are counted, assumed or measured.
- **One central point per slide.** Split long proofs, pseudocode, traces or recurrences; never shrink text to fit. Body text ≥ 0.75em.
- **Density (from MAT1101, `AGENTS.md` §"Văn phong và mật độ mặt trang chiếu"):** count syllables as whitespace tokens, excluding title, KaTeX, pseudocode blocks, table numbers, figure labels and notes.
  - Aim for ≤ 40 per content slide, hard cap 60 (80 for objectives, contents, summary, comparison and cost tables, recitation problem statements).
  - ≤ 6 content lines (table rows count, max 8 for trace/cost tables), ≤ 20 syllables per line, ≤ 3 display formulas; pseudocode over 8 lines gets its own slide, over 20 lines is split; ≤ 1 text box of ≤ 2 sentences.
  - Over the cap means split or move prose to notes; never shrink fonts. An exception needs a reason in `storyboard.md` with syllable counts before and after. Reviewers rate an over-cap slide without one `trung bình`, over 1.5× the cap `nghiêm trọng`.
- **Slide links** state which result is inherited, which assumption changes, and which limit creates the next need. Signposts like "tiếp theo chúng ta…" don't count.
- **Storyboard entries:** a section map (type, function, input, output, contribution, strand title slide code) plus one entry per slide with its strand, purpose, student action, central object, inherited data/notation, input knowledge, learning product and the evidence for checking it, plus a decision (`giữ | sửa | gộp | tách | thêm | bỏ`) with a reason, and for fixed slides the syllable count before and after. When slides and notes are done together, keep both `data-slide-id` and `note-topic-id` and the map between them.

## Multi-agent workflow in Claude Code

`AGENTS.md` requires an orchestrator plus sub-agents; don't do the whole workflow in one role.

This model assignment is a standing user instruction (2026-10-07, given for `../math-4-AI`, adopted here on 2026-10-14) and matches `AGENTS.md` §"Điều phối mô hình trong dự án".

- **Master and quality controller:** this session runs Claude Fable 5.1 (`claude-fable-5-1`).
  - It splits the work, writes the briefs, merges results, and accepts or rejects every sub-agent output.
  - It does not take a sub-agent role itself. Drafting, reviewing and editing go to sub-agents.
  - If the session runs another model, say so before delegating and ask the user to switch.
- **Sub-agents:** every workflow role, including agents spawned by sub-agents, runs Claude Opus 5.5 (`claude-opus-5-5`) at effort `high`.
- **Quality control of every output:** no sub-agent output reaches the next stage, a repo file or the user until the master has reviewed it.
  - Plans and reports: check every finding against the cited file or line; re-derive the maths and constants.
  - Written files: read the diff; run the checks in this file (visual check, viewer check, density count, `git diff --check`).
  - Record `chấp nhận | yêu cầu sửa | bác bỏ` with a reason in `review-log.md`. Send requested fixes back to the same agent with `SendMessage`.
- **Creating agents:** use the `Agent` tool with `subagent_type: "general-purpose"`, `model: "opus"` and `effort: "high"`, or a `.claude/agents/` definition pinned to `claude-opus-5-5` at `high` once one exists.
  - Do not use `subagent_type: "fork"` for workflow roles: a fork inherits the master's model and ignores the override.
  - Never assign a workflow role to an agent type pinned to another model.
  - Continue an existing agent with `SendMessage` rather than spawning a new one.
- **Stopping rule:** if no Opus 5.5 sub-agent can be created, say so and stop the dependent work. The master does not do that work itself and does not fall back silently to another model.
- **Concurrency:** read-only agents may run in parallel. **Only one agent writes files at a time.** The note writer and the deck writer never run together.
- **Every brief states:** role, inputs, output, file scope, done condition, whether `no-ai-slop` Edit or Detect mode applies, and "do not commit". Sub-agents writing long files work in stages of ≤ ~150 lines.
- **Logging:** record each agent's role, type, model and effort in `review-log.md`, using the tool call as evidence rather than the agent's own claim, plus the master's decision for each output.

| Stage | Role(s) | Writes files? |
|---|---|---|
| Plan | Planning agent: scope, time budget, concept/algorithm map, learning cycles, strand map with title slides, risks | No |
| Source analysis | Source-to-slide mapping, figure inventory, MMDS vs CS246 comparison, gaps | No |
| Topic map (notes) | Labels topics `cốt lõi`/`cầu nối`/`bổ sung`/`đọc thêm` with sources; orchestrator merges with the plan | No |
| Draft | Authoring agent: outline, storyboard, deck, SVGs, notes; `no-ai-slop` Edit + `eval.md`; `quill` continuity check | Yes |
| Storyboard gate | Every slide's reason to exist, the learning cycles, strand title slides, density list, 120 + 60 minutes | No |
| Review | Five independent roles on one frozen draft: student (also measures density), algorithms/data-science expert, maths and algorithm accuracy, academic/pedagogical critique (also `no-ai-slop` Detect), storyline and linking | No |
| Revise | Editor merges the reports, fixes, records rejected suggestions | Yes |
| Recheck | Accuracy on changed proofs, algorithms and costs. Storyline on the changed slides, ±2 neighbours and section boundaries; the whole deck if the opening, conclusion or thesis changed | No |
| Final check | Verifier: `slide_authoring_standard.md` checklist, technical, density count, strand titles, visual, planning sync, note consistency, git; the master reviews the evidence | — |

- **Report format:** reviews return findings as `mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa` (notes use `vị trí` instead of `trang chiếu`). The storyline role must also give `vai trò trong mạch`, `kết nối vào`, `kết nối ra`.
  - Severities are `chặn bàn giao`, `nghiêm trọng`, `trung bình` and `nhẹ`.
  - Every blocking and serious finding must be resolved.
- **Logging findings:** record each one in `review-log.md` with its status and decision. Never delete resolved findings.
- **Scaling to small edits:** a one-slide edit still goes editor → accuracy and storyline rechecks on the affected slides → browser check → log. The full five-role review isn't needed.

## Visual verification

Required after every deck or note change. Only claim a visual check you actually ran.

1. Start `python3 -m reloadserver 8765` in the background from the repo root.
2. With Playwright Chromium, open the deck and jump to a slide by ID. Use `Reveal.getIndices(document.querySelector('section[data-slide-id="X"]'))`, then `Reveal.slide(h, v, 99)`, where `99` reveals all fragments.
3. Capture **1600×900** (16:9) and **390×844** (narrow); for notes also check print media. Check every strand title slide at both sizes and that its number matches `#/N`.
4. Check: no console or page errors, no `.katex-error`, content fits the frame at 16:9, no horizontal overflow, body font sizes above the minimum, keyboard navigation works, no overlaps, no raster references without a logged exception, no network requests for core assets.
   - Ignore `.katex-mathml`, which is visually hidden.
5. View the screenshots yourself before reporting.
6. Keep screenshots in the session scratchpad, not in the repo.

## Lecture notes

- **Viewer contract:** `material-viewer.html?doc=materials/lec-NN/lecture-note.md&deck=lecture-NN-<ten-bai>.html`; the viewer only accepts paths under `materials/lec-NN/` and both parameters must name the same lecture. Pipeline: protect maths → Marked → DOMPurify → restore maths → KaTeX.
- **Blocks:** `::: definition|theorem|proposition|lemma|corollary|remark|algorithm|example|application|derivation|proof|exercise|hint|solution Optional title`, closed by `:::`, not nested. The title carries the number (`::: theorem Định lý 06.2 (Tên)`). `proof`, `hint`, `solution` are collapsed by default, keyboard-operable and open in print. `<!-- note-topic-id: lec-NN-topic-k -->` before a section heading is validated and hidden by the viewer.
- **Lecture note = self-contained textbook chapter** (`AGENTS.md` §"Tiêu chuẩn giáo trình cho ghi chú bài giảng", binding). The deck is the summary of the note; on conflict fix the note first. Reading test: a prepared second-year student reads it top to bottom without the deck and understands every sentence where it stands.
  - Problem before tool; every formula wrapped in prose; every symbol named at first appearance; every derivation and cost step justified; verbal reading after each definition, theorem and algorithm with the role of each assumption and counterexamples; a numeric example before the general statement and a worked example after it; section endings in prose (result obtained, what is missing, how the next section fixes it); no "xem trang chiếu"; full sentences; common confusions named; figures read in text; 12 000–32 000 whitespace-separated syllables per chapter (under 9 000 needs a logged reason; over 32 000 means splitting exercises or moving content to further reading).
  - Numbered environments: one counter for Định nghĩa/Định lý/Mệnh đề/Bổ đề/Hệ quả/Nhận xét/Thuật toán (`Định lý 06.2`), separate counters for Ví dụ, Tình huống and Bài tập; four-part theorems (Giả thiết, Kết luận, Điều kiện áp dụng, Phạm vi); `algorithm` blocks with input, output, assumptions, numbered steps, stopping, edge cases and cost; proofs in labelled steps, `aligned` one relation per line, ending with $\square$.
  - Linking paragraphs: concept–concept, result–result, algorithm–variant, reasoning chain in the section ending, **"Trong thực hành"** after each main result, applications back to theory, previous and next lecture.
  - Chapter structure: title; ≤ 1 short intro paragraph and the deck link; objectives; prerequisites (bold group name + numbers + restated statement); notation table; topic map with `note-topic-id`s; numbered sections `## 1.` … matching strands; application situations (≥ 2, one with a violated assumption); chapter summary (5–8 sentence narrative, results by section, formulas and algorithms to remember, forgotten assumptions); exercises in three level subsections with hint and solution, including the recitation book exercises; references with the MMDS credit. Use `materials/_templates/lecture-note.md`.
  - Consult the standard textbooks (MMDS 3e; Silberschatz et al. 7e; Nelson & Gailly; CLRS 4e for invariants and cost analysis; *Học máy thống kê* for voice) for how they motivate, order and interpret each concept and log the sections in `review-log.md`. Never translate or copy passages.
  - Review checklist before publishing: `AGENTS.md` §"Kiểm định ghi chú bài giảng".
- **Notes-only requests:** don't rewrite the deck. Update the note, the SVGs it needs, the three planning files by topic (`note-topic-id`), and the index entry. If shared notation, assumptions, examples or conclusions change, review the deck and log the impact.

## Git

- **Branch:** `main` tracks `origin/main`. Never create or switch branches, rebase, amend, force-push or rewrite remote history unless the user asks.
- **When:** `AGENTS.md` makes a deck or note complete only once committed and pushed to `origin/main` after passing every check. Commit or push other changes (e.g. `AGENTS.md`/`CLAUDE.md`) only when the user asks.
- **Before committing:**
  - Run `git status --short` and `git diff --check`.
  - Stage explicit paths only; never `git add .` or `-A`.
  - Then run `git diff --cached --check`.
- **Commit scope:** a deck commit holds the deck HTML, `img/lec-NN/`, the three `planning/lec-NN/` files, the `index.html` entry, and shared files that truly had to change. A note commit holds `lecture-note.md`, its SVGs, related planning changes, the index entry and any viewer change it needs. Never stage someone else's pending changes or another lecture's unfinished work.
- **Commit messages:**
  - `feat(lecture-NN): add <ten-bai> slide deck` / `fix(lecture-NN): revise <ten-bai> slide deck`;
  - `feat(materials-NN): add <ten-bai> lecture note` / `fix(materials-NN): revise <ten-bai> lecture note`;
  - `docs(agents): …` for `AGENTS.md`/`CLAUDE.md`/`slide_authoring_standard.md`, templates and viewer infrastructure.
- **After pushing:** confirm with `git fetch` and `git branch -r --contains HEAD`. If the push fails, keep the local commit, report the hash and the error, and do not claim the work is delivered.

## Done means

- Every blocking and serious finding is resolved and logged; five independent reports exist.
- The `slide_authoring_standard.md` checklist passed and the results are in `review-log.md`.
- `outline.md`, `storyboard.md` and `review-log.md` match the current deck or note, including `data-slide-id`s and strand title slides.
- No slide exceeds the density caps without a storyboard exception; the density count is in `review-log.md`.
- The browser check passed at both sizes (and print, for notes).
- `index.html` is updated for completed work only.
- Commits are pushed and verified.

The handoff lists: product files and local URLs, main sources, approved supplementary topics, redrawn figures and raster exceptions, checks run, intended deviations from the sources, exceptions, commit hash, push verification, and remaining limits.
