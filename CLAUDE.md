# CLAUDE.md

This repo holds the RevealJS lecture decks, lecture notes and recitation exercises for **Giải thuật nền tảng của Khoa học dữ liệu** (UET.DSE2053). The current semester is `2627-1/`.

The workspace file `../CLAUDE.md` carries the rules shared by every course: environment, static-site rules, shared CSS, writing style, `no-ai-slop`/`quill`, the sub-agent policy, visual verification and git basics. This file holds only what is specific to this course. `AGENTS.md` is the full, authoritative specification, written in Vietnamese. `slide_authoring_standard.md` is the mandatory standard for how slides build knowledge for second-year students. Precedence: the user's instructions first, then `AGENTS.md` (including its own priority list), then this file, then `../CLAUDE.md`. Read the relevant section of `AGENTS.md` and `slide_authoring_standard.md` before any deck or notes work.

The presentation rules were aligned on 2026-10-14 with the sibling courses `../math-4-AI` and `../rl-plan` (their `AGENTS.md`, `CLAUDE.md`, strand title slides, density caps, textbook-style notes), with the author's MAT1101 slides in `../MAT1101/` and with the author's textbook *Học máy thống kê* in `../SML-textbook-main.zip`. Those are style models only, never content sources; the content sources stay in `sources/`.

## Repo map

| Path | Contents |
|---|---|
| `sources/source.md` | Course-level source map: recommended lecture order, original-session mapping, learning outcomes, prerequisites, materials, open questions. **Read first for every lecture.** |
| `sources/reference-slides/README.md` | Reference-slide mapping for the 15 recommended lectures, with completeness status |
| `sources/reference-slides/`, `textbooks/`, `exercises/`, `papers/` | Detailed sources (MMDS, Stanford CS246, db-book…); binaries are gitignored |
| `2627-1/lecture-NN-<ten-bai>.html` | One RevealJS deck per lecture; `NN` follows the recommended order in `sources/source.md` |
| `2627-1/lecture-template.html` | Base for every deck: opening strand, strand title slide, algorithm slide, conclusion strand, recitation strand |
| `2627-1/lecture-style.css` | Shared stylesheet, identical in every course; synced from `../shared/css/`, never edited here |
| `2627-1/lecture-course.css` | This course's deck styles (holds `.strand-title`), loaded after `lecture-style.css`. Lecture 02 is the reference for shared components |
| `2627-1/revealjs/`, `plugin/`, `vendor/` | Local runtime; nothing core loads from the network |
| `2627-1/img/lec-NN/` | SVG assets for each lecture; their generator scripts live in `../tools/courses/ds-foundation-algorithms/2627-1/img/lec-NN/` |
| `2627-1/planning/lec-NN/` | `outline.md`, `storyboard.md`, `review-log.md` (tracked; never linked from the index) |
| `2627-1/materials/lec-NN/lecture-note.md`, `exercises.md` | Public self-study note and its consolidation exercises, rendered by `material-viewer.html`; templates in `materials/_templates/` |
| `2627-1/material-viewer.{html,css,js}`, `material-index.css` | Static Markdown viewer (14 block types, `DIRECTIVE_LABELS` in the JS); course overrides in the `*-course.css` beside them |
| `2627-1/examples/`, `materials/lec-NN/code/` | Student practice bundles (course content, stays in the repo); exist only where the source has matching content |
| `2627-1/index.html` | Semester index; links only finished decks and checked notes |
| `skills/build-slide-deck-outline/` | Project skill, exposed to Claude via `.claude/skills/` (symlink). Its default "năm 3" audience is overridden by `AGENTS.md`: the audience is second-year students |
| `.codex/` | Historical Codex tooling. Do not use it; its authorisations no longer apply |

## Commands

```bash
../.venv/bin/python -m reloadserver 8765          # from repo root
# deck:  http://localhost:8765/2627-1/lecture-NN-<ten-bai>.html
# note:  http://localhost:8765/2627-1/material-viewer.html?doc=materials/lec-NN/lecture-note.md&deck=lecture-NN-<ten-bai>.html
git diff --check
```

A density-count script (syllables, lines, syllables per line per slide) lives in the session scratchpad when needed; its results go in `review-log.md`. Figure generators: `../.venv/bin/python ../tools/courses/ds-foundation-algorithms/2627-1/img/lec-NN/…` (they write into `2627-1/img/lec-NN/`).

## Course-specific rules

- **Intake:** a lecture request starts by reading `sources/source.md`, then the matching row in `sources/reference-slides/README.md` and every local file it maps. If a required source is missing, stop after the inventory and ask. Never pick a lecture for the user.
- **MMDS-anchored lectures:** compare the official `mmds.org` slides with the mapped Stanford CS246 slides cluster by cluster; prefer MMDS when equal and log any Stanford choice. Redraw everything; never copy their CSS, fonts or rasters. Credit `http://www.mmds.org` on the cover or the sources slide when a substantial part is used.
- **CSS:** decks link `lecture-style.css` then `lecture-course.css` only.
  - No `<style>` blocks; no inline styles that override the shared type scale; no `.dense` or inline `font-size` to squeeze a slide under the density cap.
  - Lecture-specific styles live in `lecture-course.css`, scoped by the deck's root class (e.g. `.lecture-pagerank`); decks using shared components carry `.course-deck`.
  - Before adding a style, look for an existing class and its Lecture 02 usage. Editing `lecture-course.css` means checking every affected deck, at least Lecture 02 and 03, at wide and narrow sizes, and logging the scope in `review-log.md`.
- **RevealJS config:** `lang="vi"`, 1280×720; outer `<section>` = one strand, inner `<section>` = one slide; footer at the end of `.slides` with course name, semester and lecture number.
  - Settings: `controlsLayout: "edges"`, `slideNumber: true`, `hash: true`, `hashOneBasedIndex: true`.
  - Plugins: `RevealMath.KaTeX`, `RevealNotes`, `RevealHighlight`, all local. No `fragment`.
  - Every slide has a unique `data-slide-id`, which never appears on the slide face or in notes.
- **Rasters:** if a raster exception isn't approved, stop that part and ask.
- **Recitation exercises** come directly from the assigned textbook or source, with problem number, section and page recorded in the storyboard and speaker notes. Translate, split or trim, but never invent data or change the mathematical task.
- **Index:** a note link appears only after the note passed its checks; until then show the `Chưa có` status.

## Writing (in addition to `../CLAUDE.md`)

- **Terminology:** define or recall ("Nhắc lại:") every symbol, assumption and result before its first use on a slide or in a section. The lecture's Vietnamese–English term table lives in `outline.md`.
- **Banned tone also covers author directions** ("người viết cần bổ sung hình"). Authoring and coordination notes live only in `outline.md`, `storyboard.md` and `review-log.md`. In lecture notes a genuine research question answered immediately in the same section is allowed; an unanswered one is rhetorical.
- **Title prefixes** also allowed: "Tính đúng: <thuật toán>", "Thuật toán: <tên>", "Chi phí: <đối tượng>". A title repeats across slides when an example continues, with the step name after a comma.
- **Slide sentences:** terse mathematical prose ("Đặt …", "Suy ra …", "Với mỗi dải $j$, tạo khóa …"). No "ta thấy", "rõ ràng", "chúng ta" or "=" used for "là". At most one closing line per slide, a conditional result or a number, never a slogan or arrow chain.
- **Allowed labels** (bold): with a period `Định nghĩa. Định lý. Mệnh đề. Bổ đề. Hệ quả. Nhận xét. Thuật toán. Chứng minh. Trực quan. Ví dụ.`; with a colon `Nhu cầu: Ý nghĩa: Diễn giải: Lưu ý: Nhắc lại: Cách khác: Dạng khác: Ký hiệu: Quy ước: Giả thiết: Kết luận: Đầu vào: Đầu ra: Bất biến: Điều kiện dừng: Trường hợp biên: Mô hình: Câu hỏi: Gợi ý: Lời giải: Đọc trước: Nguồn:`. Section-type labels **Đọc thêm** and **Thực hành** use the course CSS class.
- **Off the slide face:** internal codes from planning files ("N02", "V02", "HT3", "MT1"). A note result number such as "(Định lý 06.3)" may follow a verbal statement at most once per slide. Per-slide source lines are gone: sources go in the speaker notes and on the "Nguồn và tài liệu đọc" slide; the cover may carry the MMDS credit and recitation slides the book exercise number.
- **Speaker notes** also cover why the algorithm is correct and grading guidance for exercises. Usually 40–150 syllables, up to ~250 for proofs or solutions (longer is only a `nhẹ` finding).
- **Voice of lecture notes (from *Học máy thống kê*):** "chúng ta" for plans, needs, method choices and limits; "ta" inside calculations; "người ta" only for common practice; the document is never the subject ("Mục này định nghĩa…" is banned); objective sentences inside definition/theorem/algorithm blocks; no "hãy" outside exercise statements. Slides and speaker notes never use "chúng ta".
- **`quill`:** ignore its `/quill:*` commands and manuscript templates; use only its consistency and continuity checks.

## Deck structure and content

- **Audience and time:** second-year students with programming, discrete maths, linear algebra and basic probability. 120 minutes of lecture plus a separate vertical part of 60 minutes of recitation in the same HTML. Timings go in the storyboard and notes, never on slides.
- **Strands:** 5–7 outer sections, including an opening and a conclusion; the recitation part is its own outer section after the conclusion. Each strand has a type from `AGENTS.md` (giới thiệu, khái niệm/mô hình, thuật toán, chi phí, hệ thống, thực hành, tổng kết), a function, an input from the strand before, and an output the next one uses. Going outside 5–7 needs a source or user reason recorded in `storyboard.md` and `review-log.md`.
- **Opening strand, in order** (`AGENTS.md` §"Mẫu RevealJS bắt buộc"): cover with a one-sentence thesis; "Tiên quyết và quy ước" ("Nhắc lại:" line for reused results, "Ký hiệu:" line for domains, sizes and index conventions); objectives; "Nội dung" numbered to match the strand title slides and `#/N`, optional "Đọc trước:" line; "Vấn đề trung tâm" (the big-data problem in one line plus each strand's conditional answer in one line), or a merged "Nhắc lại / Ví dụ / Nhu cầu" slide.
- **Strand title slides (`AGENTS.md` §"Trang tiêu đề mạch"):** every strand except the opening starts with a `section.strand-title` slide, `id="mach-N"`, `data-slide-id` `<prefix>-00` (or `<prefix>-T` if taken).
  - Face: number in digits in `span.strand-number` ("2.", "3.", …), a noun-phrase name that differs from the first content slide's title, one declarative lead `p.strand-lead` (≤ 25 syllables, "Muốn <đích>, phải <việc>" or "Nhu cầu:"), optional `p.strand-keys` (≤ 5 noun phrases joined by " · "). Markup: `div.strand-title-body` > `h2` + `p.strand-lead` + `p.strand-keys`; styles live in `lecture-course.css`.
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

## Sub-agents (course settings)

The policy in `../CLAUDE.md` applies (standing user instruction 2026-10-07, given for `../math-4-AI`, adopted here on 2026-10-14; master confirmed 2026-10-16; matches `AGENTS.md` §"Điều phối mô hình trong dự án"):

- **Effort:** every sub-agent runs at `high`.
- The note writer and the deck writer never run together.
- **Checks the master runs on written files:** visual check, viewer check, density count, `git diff --check`.
- The storyline role must also give `vai trò trong mạch`, `kết nối vào`, `kết nối ra`.

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

## Visual verification (course notes)

Also required after every note change. Check every strand title slide at both sizes and that its number matches `#/N`; flag raster references without a logged exception.

## Lecture notes

- **Viewer contract:** `material-viewer.html?doc=materials/lec-NN/lecture-note.md&deck=lecture-NN-<ten-bai>.html`; the viewer only accepts paths under `materials/lec-NN/` and both parameters must name the same lecture. Pipeline: protect maths → Marked → DOMPurify → restore maths → KaTeX.
- **Blocks:** `::: definition|theorem|proposition|lemma|corollary|remark|algorithm|example|application|derivation|proof|exercise|hint|solution Optional title`, closed by `:::`, not nested. The title carries the number (`::: theorem Định lý 06.2 (Tên)`). `proof`, `hint`, `solution` are collapsed by default, keyboard-operable and open in print. `<!-- note-topic-id: lec-NN-topic-k -->` before a section heading is validated and hidden by the viewer.
- **Lecture note = self-contained textbook chapter** (`AGENTS.md` §"Tiêu chuẩn giáo trình cho ghi chú bài giảng", binding). The deck is the summary of the note; on conflict fix the note first. Reading test: a prepared second-year student reads it top to bottom without the deck and understands every sentence where it stands.
  - Problem before tool; every formula wrapped in prose; every symbol named at first appearance; every derivation and cost step justified; verbal reading after each definition, theorem and algorithm with the role of each assumption and counterexamples; a numeric example before the general statement and a worked example after it; section endings in prose (result obtained, what is missing, how the next section fixes it); no "xem trang chiếu"; full sentences; common confusions named; figures read in text; no sentences on where numbers come from ("do học phần dựng", "không phải số đo", erratum notes on the book): the references at the end suffice, and provenance goes to `review-log.md`; 12 000–32 000 whitespace-separated syllables per chapter (under 9 000 needs a logged reason; length excludes `exercises.md`; over 32 000 means moving content to further reading).
  - Numbered environments: one counter for Định nghĩa/Định lý/Mệnh đề/Bổ đề/Hệ quả/Nhận xét/Thuật toán (`Định lý 06.2`), separate counters for Ví dụ, Tình huống and Bài tập; four-part theorems (Giả thiết, Kết luận, Điều kiện áp dụng, Phạm vi); `algorithm` blocks with input, output, assumptions, numbered steps, stopping, edge cases and cost; proofs in labelled steps, `aligned` one relation per line, ending with $\square$.
  - Linking paragraphs: concept–concept, result–result, algorithm–variant, reasoning chain in the section ending, **"Trong thực hành"** after each main result, applications back to theory, previous and next lecture.
  - Chapter structure: title; ≤ 1 short intro paragraph and the deck link; objectives; prerequisites (bold group name + numbers + restated statement); notation table; no topic map (the four-group map lives in `outline.md`; keep the `note-topic-id` comments); numbered sections `## 1.` … matching strands; application situations (≥ 2, one with a violated assumption); chapter summary (5–8 sentence narrative, results by section, formulas and algorithms to remember, forgotten assumptions); end-of-section exercises in the note, and every lecture's consolidation exercises in `materials/lec-NN/exercises.md` (three levels, one hint and one solution each, the recitation book exercises, shared Bài tập counter; lecture 10 is the model, `AGENTS.md` §"Cấu trúc bắt buộc" item 10); references with the MMDS credit. Use `materials/_templates/lecture-note.md`.
  - Consult the standard textbooks (MMDS 3e; Silberschatz et al. 7e; Nelson & Gailly; CLRS 4e for invariants and cost analysis; *Học máy thống kê* for voice) for how they motivate, order and interpret each concept and log the sections in `review-log.md`. Never translate or copy passages.
  - Review checklist before publishing: `AGENTS.md` §"Kiểm định ghi chú bài giảng".
- **Notes-only requests:** don't rewrite the deck. Update the note, the SVGs it needs, the three planning files by topic (`note-topic-id`), and the index entry. If shared notation, assumptions, examples or conclusions change, review the deck and log the impact.

## Git (course settings)

- **When:** `AGENTS.md` makes a deck or note complete only once committed and pushed to `origin/main` after passing every check. Commit or push other changes (e.g. `AGENTS.md`/`CLAUDE.md`) only when the user asks.
- **Commit scope:** a deck commit holds the deck HTML, `img/lec-NN/`, the three `planning/lec-NN/` files, the `index.html` entry, and shared files that truly had to change. A note commit holds `lecture-note.md`, its SVGs, related planning changes, the index entry and any viewer change it needs.
- **Commit messages:** `feat(lecture-NN): add <ten-bai> slide deck` / `fix(lecture-NN): revise <ten-bai> slide deck`; `feat(materials-NN): add <ten-bai> lecture note` / `fix(materials-NN): revise <ten-bai> lecture note`; `docs(agents): …` for `AGENTS.md`/`CLAUDE.md`/`slide_authoring_standard.md`, templates and viewer infrastructure.

## Done means

- Every blocking and serious finding is resolved and logged; five independent reports exist.
- The `slide_authoring_standard.md` checklist passed and the results are in `review-log.md`.
- `outline.md`, `storyboard.md` and `review-log.md` match the current deck or note, including `data-slide-id`s and strand title slides.
- No slide exceeds the density caps without a storyboard exception; the density count is in `review-log.md`.
- The browser check passed at both sizes (and print, for notes).
- `index.html` is updated for completed work only.
- Commits are pushed and verified.

The handoff lists: product files and local URLs, main sources, approved supplementary topics, redrawn figures and raster exceptions, checks run, intended deviations from the sources, exceptions, commit hash, push verification, and remaining limits.
