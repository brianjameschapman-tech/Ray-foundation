# Placeholder analytics core for v0.1 foundation.
# Swap in full Monte Carlo and headwind engine later.
import numpy as np
import pandas as pd

def quick_roi_estimate(purchase, rehab, arv, carry=0.0, sell_pct=0.05):
    tpc = purchase + rehab + carry + sell_pct*arv
    if tpc <= 0: return {"roi_pct": 0.0}
    roi = (arv - tpc)/tpc
    return {"roi_pct": round(100*roi, 2)}

def mock_table():
    return pd.DataFrame([
        {"address":"Sample — 1234 W Belmont Ave", "region":"Urban Core", "price": 350000},
        {"address":"Sample — 27 E Maple St", "region":"Inner Collar", "price": 290000},
    ])
