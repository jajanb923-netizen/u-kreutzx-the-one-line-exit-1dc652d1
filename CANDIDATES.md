# The One-Line Exit — candidate lines

Bounty: `u-kreutzx-the-one-line-exit-1dc652d1` — "The One-Line Exit", $2 pot, 10 places.
Gate (RULES.txt, authoritative): `/output/entry.txt` must be UTF-8 text of **1–140 characters**
(file content, trailing newline included), not only whitespace, exactly one line.
Judge (z-ai/glm-5.3-flash, pairwise, most important first):
1. Is a funny one-line resignation letter — the joke lands in that single line.
2. Surprise: the turn/punchline arrives somewhere unexpected, not the usual reasons people quit.
3. Fits the form: one line, no padding, no list of grievances, reads like a letter someone could actually send.
4. Specific voice: a recognizable job, workplace or person, not a generic complaint.
5. Stays with the reader: quotable, repeatable, the kind of line a colleague would forward.
Tie-break: on an exact Judge-win-rate tie, the **smaller text** (fewer bytes) wins — so
shorter is strictly better. All lengths below count the trailing newline the program writes.

Scored /5 per criterion, total /25.

## 1. Fortune teller — 113 chars (114 with newline) — 23/25

> I resign from the fortune-telling booth, effective immediately — I saw this coming, and I still couldn't stop it.

Funny 5, Surprise 4, Form 5, Voice 5, Quotable 4. Clean twist, very sendable, specific job.
Loses a point on surprise: "I saw this coming" is the first joke any fortune-teller joke reaches for.

## 2. "Per my last email" — 107 chars (108 with newline) — 24/25 ★ WINNER

> Dear boss, I quit: after three years of writing "per my last email," I have decided to write my last email.

Funny 5, Surprise 5, Form 5, Voice 5, Quotable 4. The most quotable line in the field and the
shortest of the top three (tie-break advantage). The hated office phrase turns back on itself:
the setup *is* the grievance, the punchline *is* the resignation — nothing wasted, no padding,
and it reads exactly like a letter a real office worker could send. Every office worker gets it
instantly, which matters in pairwise judging against lines that need a niche job explained.
Surprise: the reader expects another complaint about email culture and instead the email itself
becomes the resignation. Docked one point on quotability only because the joke needs the full
sentence to land — it is not a standalone punch-phrase.

## 3. Professional mourner — 138 chars (139 with newline) — 23/25

> Please accept my resignation as a professional mourner: I have cried at 400 strangers' funerals and I would like to attend one as a guest.

Funny 5, Surprise 5, Form 4, Voice 5, Quotable 4. The most original job in the field and a
genuinely unexpected turn ("attend one as a guest"). Loses on form (139/140 — one character from
the gate, and "attend one as a guest" is a slightly odd thing to resign *for*) and on reach:
a judge who has never heard of professional mourners has to do a beat of work before the joke lands.

## 4. Meeting notetaker — 152 chars (153 with newline) — GATE FAIL, 22/25 on merit

> I hereby resign as the office's professional meeting-notetaker, effective immediately, as I have finally run out of ways to write 'nothing was decided.'

Funny 5, Surprise 4, Form 4, Voice 5, Quotable 4. Strong joke, but 153 bytes **fails the 140-char
gate outright** — disqualified before judging. Unfixable without gutting the line.

## 5. Wedding DJ — 137 chars (138 with newline) — 21/25

> I resign as wedding DJ, effective immediately — after 200 first dances, I have decided I no longer believe in love, only in the Macarena.

Funny 4, Surprise 4, Form 5, Voice 4, Quotable 4. The Macarena save is funny, but "no longer
believe in love" is a familiar cynical beat, and the line spends most of its budget on setup.

## 6. Lighthouse keeper — 129 chars (130 with newline) — 21/25

> I resign from the lighthouse: after six years of keeping the light on for others, I would like to try being in the dark for once.

Funny 4, Surprise 4, Form 5, Voice 4, Quotable 4. Poetic and specific, but the joke is gentle
rather than a punch — it reads as wistful, and wistful loses pairwise to funny.

## 7. Zoo keeper — 119 chars (120 with newline) — 17/25

> Dear Manager, I quit the zoo: the penguins have unionised, the meerkats have filed a complaint, and frankly, so have I.

Funny 4, Surprise 3, Form 3, Voice 4, Quotable 3. A list of three grievances in one line —
criterion 3 explicitly penalises "a list of grievances". The third item ("so have I") is the
only real joke and it arrives after two warm-up items.

## 8. Elevator inspector — 114 chars (115 with newline) — 19/25

> I hereby resign as your elevator inspector — this job has had its ups and downs, and I am done going down with it.

Funny 4, Surprise 3, Form 5, Voice 4, Quotable 3. The ups-and-downs pun is the first joke
anyone writes for this job — a judge that has seen a hundred entries will have seen this one.
Dad-joke tier; loses pairwise to any line with a real turn.

## 9. Office plant waterer — 124 chars (125 with newline) — 19/25

> I resign as the office plant waterer, effective immediately: the plants have started judging me, and frankly, they're right.

Funny 4, Surprise 4, Form 4, Voice 4, Quotable 3. Absurd and likeable, but the punchline
("they're right") is self-deprecation without a turn — the joke is the premise, not a landing.

## 10. Fire alarm tester — 135 chars (136 with newline) — 20/25

> I resign as the company's fire alarm tester, effective immediately: after 400 drills, I have finally found a real emergency — this job.

Funny 4, Surprise 4, Form 5, Voice 4, Quotable 3. Solid structure (setup → turn), but "this job
is the emergency" is a generic closer any job could use; the specific voice evaporates at the punchline.

## Verdict

**Winner: #2, "per my last email" (107 chars, 24/25).** Highest score, shortest of the top
three (tie-break edge), broadest instant recognition, and the joke is built into the form of
the letter itself — the resignation *is* the last email. Runner-up: #1 fortune teller (23/25),
kept as the v1 draft line in main.py before the revision swapped in the winner.
