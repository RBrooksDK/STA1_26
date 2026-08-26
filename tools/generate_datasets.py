"""Generate reproducible engineering datasets for STA1_26.

True parameters are written to data/generation_log.json so tutorials can
refer to the data-generating process without treating it as unknown.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)

rng = np.random.default_rng(2026)


def sensor_thickness() -> dict:
    """Wafer / plate thickness in micrometres on a production line."""
    n = 180
    mu, sigma = 250.0, 4.2
    thickness = rng.normal(mu, sigma, size=n)
    shift = np.zeros(n)
    shift[-25:] = 3.5  # late drift, useful in Session 12
    thickness = thickness + shift
    line = np.where(np.arange(n) < 90, "A", "B")
    df = pd.DataFrame(
        {
            "sample_id": np.arange(1, n + 1),
            "line": line,
            "thickness_um": np.round(thickness, 3),
            "shift_um": shift,
        }
    )
    path = DATA / "sensor_thickness.csv"
    df.to_csv(path, index=False)
    return {"file": path.name, "n": n, "mu": mu, "sigma": sigma, "late_shift_um": 3.5}


def response_times() -> dict:
    """API response times (ms) under two server configurations."""
    n = 60
    a = rng.normal(118.0, 14.0, size=n)
    b = rng.normal(109.0, 16.0, size=n)
    paired_b = a - rng.normal(8.0, 6.0, size=n)
    df = pd.DataFrame(
        {
            "request_id": np.arange(1, n + 1),
            "server_a_ms": np.round(np.clip(a, 60, None), 2),
            "server_b_ms": np.round(np.clip(b, 60, None), 2),
            "server_b_paired_ms": np.round(np.clip(paired_b, 60, None), 2),
        }
    )
    path = DATA / "response_times.csv"
    df.to_csv(path, index=False)
    return {
        "file": path.name,
        "n": n,
        "mu_a": 118.0,
        "mu_b_independent": 109.0,
        "paired_mean_improvement_ms": 8.0,
    }


def component_lifetimes() -> dict:
    """Hours to failure for a component, exponential with rate 1/400."""
    n = 80
    rate = 1 / 400
    hours = rng.exponential(scale=1 / rate, size=n)
    df = pd.DataFrame(
        {
            "unit_id": np.arange(1, n + 1),
            "lifetime_h": np.round(hours, 2),
        }
    )
    path = DATA / "component_lifetimes.csv"
    df.to_csv(path, index=False)
    return {"file": path.name, "n": n, "rate_per_hour": rate, "mean_h": 1 / rate}


def energy_load() -> dict:
    """Energy use (kWh/day) versus CPU load (percent)."""
    n = 40
    load = np.linspace(15, 92, n) + rng.normal(0, 1.2, size=n)
    beta0, beta1, sigma = 12.0, 0.38, 3.5
    energy = beta0 + beta1 * load + rng.normal(0, sigma, size=n)
    df = pd.DataFrame(
        {
            "day": np.arange(1, n + 1),
            "cpu_load_pct": np.round(np.clip(load, 0, 100), 2),
            "energy_kwh": np.round(np.clip(energy, 0, None), 3),
        }
    )
    path = DATA / "energy_load.csv"
    df.to_csv(path, index=False)
    return {"file": path.name, "n": n, "beta0": beta0, "beta1": beta1, "sigma": sigma}


def defect_types() -> dict:
    """Defect categories by production line."""
    types = ["solder", "alignment", "contamination", "other"]
    # Line 1 slightly more contamination; line 3 more alignment
    probs = {
        "L1": [0.45, 0.20, 0.25, 0.10],
        "L2": [0.50, 0.25, 0.15, 0.10],
        "L3": [0.40, 0.35, 0.15, 0.10],
    }
    rows = []
    for line, p in probs.items():
        n = 120
        cats = rng.choice(types, size=n, p=p)
        for c in cats:
            rows.append({"line": line, "defect_type": c})
    df = pd.DataFrame(rows)
    path = DATA / "defect_types.csv"
    df.to_csv(path, index=False)
    return {"file": path.name, "n_per_line": 120, "probabilities": probs}


def packet_trials() -> dict:
    """Bernoulli packet-loss indicators for n transmissions."""
    n, p = 200, 0.04
    lost = rng.binomial(1, p, size=n)
    df = pd.DataFrame({"trial": np.arange(1, n + 1), "packet_lost": lost})
    path = DATA / "packet_loss.csv"
    df.to_csv(path, index=False)
    return {"file": path.name, "n": n, "p_loss": p}


def main() -> None:
    log = {
        "seed": 2026,
        "datasets": [
            sensor_thickness(),
            response_times(),
            component_lifetimes(),
            energy_load(),
            defect_types(),
            packet_trials(),
        ],
    }
    (DATA / "generation_log.json").write_text(json.dumps(log, indent=2), encoding="utf-8")
    print(json.dumps(log, indent=2))


if __name__ == "__main__":
    main()
