import datetime as _dt
import random

THEMES = [
    ("Timing", "When listings linger, the best deals require patience and proof."),
    ("Liquidity", "Rising inventory can create temporary value gaps—verify rather than fear."),
    ("Community", "Your reputation compounds faster than interest; price it into decisions."),
    ("Humility", "Models fail quietly; reality fails loudly. Favor robustness over elegance.")
]

def atypical(depth=2, ethical=True, context=None):
    now = _dt.datetime.now().strftime("%b %d, %Y • %I:%M %p")
    theme = random.choice(THEMES)
    base  = theme[1]
    if context:
        base = f"{base} Context: {context}."
    if depth == 1:
        text = base
    elif depth == 2:
        text = base + " Stress-test assumptions ±10%."
    else:
        text = base + " Triangulate with comps, permits, taxes, and days-on-market."
    meta = f"{theme[0]} — {'Blend ethics' if ethical else 'Pragmatic lens only'}"
    return { "text": text, "meta": meta, "generated_at": now }
