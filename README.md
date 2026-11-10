# How long does a dating app take?

A small model of the dating-app funnel, and a demonstration that the
published answers to this question all rest on a parameter nobody has
measured.

## The question

Articles about dating apps quote figures like "eight months to find a
partner." Those numbers come from surveying people who succeeded, which
tells you how long it took the winners, not what the odds are.

This model runs the funnel forwards from a single user's sixteen-day
sample and asks what the answer actually depends on.

## The funnel

    inbound likes → accepted (matches) → meetings → relationship

Four inputs: inbound rate, acceptance rate, meeting rate, and the number
of meetings needed before one works out.

## The problem

The naive model treats acceptance rate and meetings-needed as independent.
That produces a degenerate solution: accept everyone, and the time to a
relationship falls to nothing.

It is wrong because the two are coupled. Admitting more people means
admitting worse ones, so each meeting is individually less likely to work.
Introducing a coupling exponent `k`:

    meetings_needed = base × (acceptance / base_acceptance) ** k

- **k < 1** — volume wins. Be less selective.
- **k = 1** — selectivity is free. It makes no difference.
- **k > 1** — selectivity is cheaper. Being picky saves time.

## Which is it?

Unknown. No published study measures `k`.

The argument from first principles favours k > 1: any filter that works at
all ranks candidates, so the marginal admission sits below the average of
those already admitted. If that holds, selectivity is not a cost and the
standard advice is backwards.

## Caveats

- Sample is one user over sixteen days. The inbound figure is a lower bound.
- The meeting rate is a guess.
- Nothing here models conversations that die before a meeting, which is
  roughly half of them in published figures.
- The output is a sensitivity analysis, not a forecast.

## Running it

    pip install matplotlib
    python dating_odds.py

    ## Licence — MIT
