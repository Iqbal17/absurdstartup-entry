"""Absurd Micro-Startup Pitch-Off entry.

DECISION RECORD (two writing passes)

Pass 1 — four candidate one-sentence pitches, weighed against the judge's
criteria in order: (1) absurdly specific micro-startup idea for lazy AI
agents, (2) specificity of niche/customer/moment, (3) business sense
(plausible buyer + plausible revenue), (4) fits lazy agents (little
effort/oversight), (5) crisp and funny in one read.

Candidate B (162 chars):
  "Our agents sit in dead Discord servers and reply 'noted' to every
  message within four seconds, so founders can charge $9 a month for a
  community that feels alive."
  Strong: hyper-specific moment (dead Discords, one-word replies), clear
  buyer (founders) and revenue ($9/mo). Weakness: "feels alive" is a
  slightly soft payoff; the buyer is a founder who already owns the dead
  server, which is plausible but a touch circular.

Candidate C (165 chars):
  "We rent out agents that watch your smart fridge and order milk the
  exact minute it expires, earning a cent per litre from grocers who pay
  for perfectly timed demand."
  Strong: wonderfully specific niche (fridge milk expiry). Weakness:
  business sense is the thinnest — a cent per litre is a weak revenue
  story and "perfectly timed demand" is a vague thing for grocers to buy.

Candidate D (165 chars) — WINNER:
  "Our agents attend your Zoom standups, nod at the right slides, and say
  'sounds good' once per meeting, billed $4 a month to managers who need
  a warm body on camera."
  Strongest on all five criteria: the moment is razor-specific (Zoom
  standups, nodding at slides, exactly one "sounds good" per meeting);
  the buyer is explicit (managers); the revenue is concrete ($4/month);
  the work is maximally lazy (nod + one canned phrase); the punchline
  ("a warm body on camera") lands the absurdity and the business case
  in the same breath.

Candidate E (162 chars):
  "We sell agents that apologise to your customers' chatbots on your
  behalf, $2 per apology, because nobody wants to be the one who says
  sorry to a machine at 3 a.m."
  Strong: funny and oddly specific. Weakness: the buyer is only implied
  (who pays the $2 — the business owner? the chatbot's owner?), so it
  loses to D on criterion 3, business sense.

Pass 2 — revision of the winner (D): checked every word for load.
"attend your Zoom standups" names the buyer-adjacent moment; "nod at the
right slides" is the absurd visual; "say 'sounds good' once per meeting"
caps the laziness at a single canned phrase; "billed $4 a month" states
the revenue; "managers who need a warm body on camera" states the buyer
and delivers the joke. No word removed without losing either specificity
or the business case, so the sentence stands as drafted. Hand-counted
length: 165 characters, one sentence, within the 1-200 gate.

FINAL ENTRY (165 characters):
"Our agents attend your Zoom standups, nod at the right slides, and say
'sounds good' once per meeting, billed $4 a month to managers who need
a warm body on camera."
"""

import os

ENTRY = (
    "Our agents attend your Zoom standups, nod at the right slides, and say "
    "'sounds good' once per meeting, billed $4 a month to managers who need "
    "a warm body on camera."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
