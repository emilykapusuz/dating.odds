# dating-odds

A funnel analysis of one person's dating-app data, with confidence intervals, because
the headline rates are usually quoted from sample sizes that cannot support them.

Sample period: Oct–Nov 2026. Platforms: OkCupid, Hinge. Germany.

---

## 1. The observed funnel

| Stage | Count | Rate | 95% CI |
|---|---|---|---|
| Profiles seen (OkCupid) | 1200 | — | — |
| Likes sent | 9 | **0.75%** of seen | 0.40% – 1.42% |
| Likes → conversation | 2 | 22% of likes | — |
| Seen → conversation | 2 | **1 in 600** | — |
| Hinge matches | 4 | — | — |
| Hinge match → conversation | 2 | 50% | — |
| **Conversations (total)** | **4** | — | — |
| Conversations → in-person meeting | 1 | **25%** | **3% – 72%** |

Conversation outcomes: 2 long, 1 medium, 1 short. One ask-out, unanswered.

## 2. What this data can and cannot establish

Only one number here is estimated with any precision.

**Estimable.** The like rate. n = 1200, so 0.75% (CI 0.40–1.42%) is real. One profile
in roughly 133 clears the bar. This is the single hardest constraint in the funnel and
it is the one most people never measure.

**Not estimable.** Everything downstream. The conversation-to-meeting rate rests on
n = 4 with 1 success; the 95% interval runs from 3% to 72%. A Jeffreys interval gives
3–72% as well. Any projection built on "25%" is a projection built on one event.

This is the central finding and it is methodological, not romantic: a personal dating
funnel generates thousands of observations at the top and single digits at the bottom,
so the stage that matters most is the stage you know least about.

## 3. Probability of zero meetings

P(no in-person meeting) after *n* conversations, at various true per-conversation rates:

| conversations | p=0.10 | p=0.15 | p=0.20 | p=0.25 | p=0.30 |
|---|---|---|---|---|---|
| 4 | 65.6% | 52.2% | 41.0% | 31.6% | 24.0% |
| 6 | 53.1% | 37.7% | 26.2% | 17.8% | 11.8% |
| 10 | 34.9% | 19.7% | 10.7% | 5.6% | 2.8% |
| 15 | 20.6% | 8.7% | 3.5% | 1.3% | 0.5% |
| 20 | 12.2% | 3.9% | 1.2% | 0.3% | 0.1% |
| 30 | 4.2% | 0.8% | 0.1% | 0.0% | 0.0% |

Read the p=0.25 column across: four conversations producing zero meetings is a 32%
outcome. It is not evidence of anything. Fifteen producing zero would be — that is a
1.3% outcome and would falsify the rate.

## 4. Throughput

At 200 profiles reviewed per week, using the observed seen→conversation rate of 1 in 600:

| | |
|---|---|
| Conversations per week | 0.33 |
| Conversations per year | 17.3 |
| Meetings per year (at p=0.25) | 4.3 |
| Weeks per meeting | ~12 |
| 50% chance of ≥1 meeting | 8 weeks |
| 90% chance of ≥1 meeting | 28 weeks |

Volume needed, at observed rates:

| Target | Conversations | Profiles to review |
|---|---|---|
| 1 meeting | 4 | 2,400 |
| 3 meetings | 12 | 7,200 |
| 5 meetings | 20 | 12,000 |

## 5. External benchmarks

Published figures, for comparison. Note what each dataset actually is — the numbers in
circulation are routinely mis-attributed.

**Zhang & Yasseri (2016), arXiv:1607.03320.** ~400,000 users, 30 US metropolitan areas,
anonymised mobile dating app. **US data, not European.**

- 49% of conversations receive no reply at all
- Mean length of a mutual conversation: 14.6 messages; median 8; mode 3
- Phone numbers are typically exchanged around message 27
- Only **19%** of replied-to conversations ever reach that length

**Oxford Internet Institute / eharmony.** Frequently quoted as "seven simultaneous
conversations." The actual figure is **seven new people per week**, UK sample. Different
claim entirely.

**Childlessness, German men (GESIS, reported via FAS).** Men aged 35–39 in Germany:
**54% childless**, up from 22% in 1980. Relevant to any filter that excludes existing
children — the pool of childless men in that bracket is larger than the stereotype
suggests, and the filter is less costly than it appears.

## 6. Filter design

A funnel with a 0.75% top-of-stage rate and a near-unmeasurable bottom stage argues for
moving filters *forward*, not adding more of them at the end.

**Door filters** — stated in the profile, so disqualifying facts arrive before the
conversation does:

1. No children, and none planned
2. Monogamous
3. Within meeting distance

**Exit filters** — assessed in conversation, where they cost nothing to apply:
everything else. Height, profession, and similar criteria belong here or nowhere; moving
them to the door compounds against an already 0.75% rate.

Two of the five contacts in this sample ended on facts that were printed in the profile
the whole time. That is a door-filter failure, not a compatibility failure.

## 7. Method

Wilson score intervals for proportions; Jeffreys (Beta) intervals as a cross-check on
the small-n stage. Zero-outcome probabilities are binomial, (1−p)^n. Time-to-first-meeting
uses a Poisson arrival approximation at the computed weekly rate. Source: `odds.py`.

## 8. Known corrections

Earlier working figures that did not survive recomputation, recorded here rather than
quietly dropped:

- "~35 conversations and ~7 meetings per year" at 200 profiles/week — **wrong**, roughly
  double. Correct values are 17.3 and 4.3.
- "Three years to find someone" — not derived from this model. The model gives ~12 weeks
  to a first meeting. Time to a lasting relationship is a different quantity and is not
  computed here.
- P(0 meetings | n=4) quoted as 43% — that corresponds to p≈0.19, not the observed 0.25.
  At p=0.25 it is 31.6%.
