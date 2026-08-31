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


def supplier_impurity() -> dict:
    """Impurity concentration (mg/kg) from three independent supplier samples."""
    n = 24
    params = {"A": (12.0, 1.4), "B": (15.2, 1.5), "C": (12.4, 1.3)}
    rows = []
    sample_id = 1
    for supplier, (mu, sigma) in params.items():
        vals = np.clip(rng.normal(mu, sigma, size=n), 0.0, None)
        for value in vals:
            rows.append(
                {
                    "sample_id": sample_id,
                    "supplier": supplier,
                    "impurity_mg_kg": round(float(value), 3),
                }
            )
            sample_id += 1
    df = pd.DataFrame(rows)
    path = DATA / "supplier_impurity.csv"
    df.to_csv(path, index=False)
    return {
        "file": path.name,
        "n_per_supplier": n,
        "mu": {k: v[0] for k, v in params.items()},
        "sigma": {k: v[1] for k, v in params.items()},
    }


def system_benchmark() -> dict:
    """Independent benchmark runs for the Session 12 integrated case.

    True generating parameters are stored here for reproducibility. Tutorials
    must not treat them as known analysis inputs.
    """
    n_per = 40
    configs = np.repeat(["C1", "C2", "C3"], n_per)
    rng.shuffle(configs)
    n = configs.size
    load = np.clip(rng.uniform(22.0, 88.0, size=n) + rng.normal(0, 1.2, size=n), 18.0, 92.0)
    latency0 = {"C1": 96.0, "C2": 82.0, "C3": 89.0}
    energy0 = {"C1": 10.0, "C2": 12.4, "C3": 9.6}
    latency = np.array(
        [
            latency0[c] + 0.52 * load[i] + rng.normal(0.0, 8.5)
            for i, c in enumerate(configs)
        ]
    )
    latency = np.clip(latency, 45.0, None)
    energy = np.array(
        [
            energy0[c] + 0.33 * load[i] + rng.normal(0.0, 2.1)
            for i, c in enumerate(configs)
        ]
    )
    energy = np.clip(energy, 1.0, None)
    p_incident = 1.0 / (1.0 + np.exp(-(latency - 148.0) / 11.0))
    incident = rng.binomial(1, p_incident)
    df = pd.DataFrame(
        {
            "run_id": np.arange(1, n + 1),
            "configuration": configs,
            "load_pct": np.round(load, 2),
            "latency_ms": np.round(latency, 2),
            "energy_kwh": np.round(energy, 3),
            "incident": incident.astype(int),
        }
    )
    path = DATA / "system_benchmark.csv"
    df.to_csv(path, index=False)
    return {
        "file": path.name,
        "n": int(n),
        "n_per_configuration": n_per,
        "note": "Generating parameters are for reproducibility only.",
    }


def assignment01_digital_services() -> dict:
    """Service latency and security-alert categories for Assignment 1."""
    n = 144
    services = rng.choice(
        ["identity", "orders", "telemetry"], size=n, p=[0.32, 0.38, 0.30]
    )
    baseline = {"identity": 72.0, "orders": 96.0, "telemetry": 84.0}
    latency = np.array(
        [baseline[s] + rng.gamma(shape=2.2, scale=11.0) for s in services]
    )
    latency[[18, 87, 131]] += [82.0, 105.0, 76.0]
    alert_type = rng.choice(
        ["none", "authentication", "rate_limit", "injection_signature"],
        size=n,
        p=[0.72, 0.15, 0.08, 0.05],
    )
    df = pd.DataFrame(
        {
            "observation_id": np.arange(1, n + 1),
            "service": services,
            "latency_ms": np.round(latency, 2),
            "alert_type": alert_type,
        }
    )
    path = DATA / "assignment01_digital_services.csv"
    df.to_csv(path, index=False)
    return {
        "file": path.name,
        "n": n,
    }


def assignment01_smart_building() -> dict:
    """Two-zone building measurements for climate and building engineering."""
    hours = np.tile(np.arange(1, 49), 2)
    zones = np.repeat(["north", "south"], 48)
    outdoor_base = 7.0 + 5.5 * np.sin(2 * np.pi * (np.arange(1, 49) - 9) / 24)
    outdoor = np.tile(outdoor_base, 2) + rng.normal(0.0, 0.45, size=96)
    zone_temp = np.where(zones == "north", 20.7, 21.5)
    indoor = zone_temp + 0.10 * outdoor + rng.normal(0.0, 0.45, size=96)
    zone_energy = np.where(zones == "north", 3.0, 0.0)
    energy = 43.0 - 0.85 * outdoor + zone_energy + rng.normal(0.0, 2.2, size=96)
    df = pd.DataFrame(
        {
            "measurement_id": np.arange(1, 97),
            "hour": hours,
            "zone": zones,
            "outdoor_temp_c": np.round(outdoor, 2),
            "indoor_temp_c": np.round(indoor, 2),
            "energy_kwh": np.round(energy, 2),
        }
    )
    path = DATA / "assignment01_smart_building.csv"
    df.to_csv(path, index=False)
    return {
        "file": path.name,
        "n": int(df.shape[0]),
    }


def assignment01_production() -> dict:
    """Component dimensions and machine vibration for Assignment 1."""
    n_per_machine = 40
    machines = np.repeat(["M1", "M2", "M3"], n_per_machine)
    diameter_mu = {"M1": 20.00, "M2": 20.04, "M3": 19.98}
    vibration_mu = {"M1": 2.15, "M2": 2.70, "M3": 2.35}
    diameter = np.array(
        [rng.normal(diameter_mu[m], 0.045) for m in machines]
    )
    vibration = np.array(
        [max(0.15, rng.normal(vibration_mu[m], 0.32)) for m in machines]
    )
    vibration[111] = 5.60  # unusual but valid measurement
    df = pd.DataFrame(
        {
            "part_id": np.arange(1, machines.size + 1),
            "machine": machines,
            "diameter_mm": np.round(diameter, 3),
            "vibration_mm_s": np.round(vibration, 2),
        }
    )
    path = DATA / "assignment01_production.csv"
    df.to_csv(path, index=False)
    return {
        "file": path.name,
        "n_per_machine": n_per_machine,
        "valid_unusual_measurement": "vibration_mm_s = 5.60 for part_id 112",
    }


def assignment01_supplier_deliveries() -> dict:
    """Right-skewed supplier lead times for Assignment 1."""
    n_per_supplier = 40
    suppliers = np.repeat(["S1", "S2", "S3"], n_per_supplier)
    base = {"S1": 2.8, "S2": 3.3, "S3": 3.0}
    scale = {"S1": 1.10, "S2": 1.35, "S3": 1.55}
    lead_time = np.array(
        [base[s] + rng.gamma(shape=2.0, scale=scale[s]) for s in suppliers]
    )
    lead_time[116] = 18.50  # a valid, documented customs delay
    df = pd.DataFrame(
        {
            "shipment_id": np.arange(1, suppliers.size + 1),
            "supplier": suppliers,
            "lead_time_days": np.round(lead_time, 2),
        }
    )
    path = DATA / "assignment01_supplier_deliveries.csv"
    df.to_csv(path, index=False)
    return {
        "file": path.name,
        "n_per_supplier": n_per_supplier,
        "documented_event": "shipment_id 117 had a genuine customs delay",
    }


def assignment02_concrete_strength() -> dict:
    """Concrete compressive-strength measurements for Assignment 2."""
    n = 160
    mean_strength = 42.0
    sd_strength = 4.2
    strength = rng.normal(mean_strength, sd_strength, size=n)
    df = pd.DataFrame(
        {
            "specimen_id": np.arange(1, n + 1),
            "strength_mpa": np.round(strength, 2),
        }
    )
    path = DATA / "assignment02_concrete_strength.csv"
    df.to_csv(path, index=False)
    return {
        "file": path.name,
        "n": n,
        "generating_mean_mpa": mean_strength,
        "generating_sd_mpa": sd_strength,
        "note": "Generating parameters are recorded only for reproducibility.",
    }


def assignment02_service_repairs() -> dict:
    """Right-skewed service-restoration times for Assignment 2."""
    n = 180
    mean_minutes = 72.0
    repair_time = rng.exponential(scale=mean_minutes, size=n)
    df = pd.DataFrame(
        {
            "incident_id": np.arange(1, n + 1),
            "repair_time_min": np.round(repair_time, 2),
        }
    )
    path = DATA / "assignment02_service_repairs.csv"
    df.to_csv(path, index=False)
    return {
        "file": path.name,
        "n": n,
        "generating_mean_minutes": mean_minutes,
        "note": "Generating parameters are recorded only for reproducibility.",
    }


def assignment03_sensor_calibration() -> dict:
    """Temperature-sensor calibration errors for Assignments 3 and 4."""
    assignment_rng = np.random.default_rng(2402)
    n = 64
    mean_error_c = 0.18
    sd_error_c = 0.60
    error = assignment_rng.normal(mean_error_c, sd_error_c, size=n)
    df = pd.DataFrame(
        {
            "sensor_id": np.arange(1, n + 1),
            "calibration_error_c": np.round(error, 3),
        }
    )
    path = DATA / "assignment03_sensor_calibration.csv"
    df.to_csv(path, index=False)
    return {
        "file": path.name,
        "n": n,
        "generating_mean_error_c": mean_error_c,
        "generating_sd_error_c": sd_error_c,
        "note": "Generating parameters are recorded only for reproducibility.",
    }


def assignment03_access_control() -> dict:
    """False rejections of legitimate login attempts for Assignments 3 and 4."""
    assignment_rng = np.random.default_rng(2516)
    n = 240
    false_reject_probability = 0.085
    false_reject = assignment_rng.binomial(1, false_reject_probability, size=n)
    df = pd.DataFrame(
        {
            "attempt_id": np.arange(1, n + 1),
            "false_reject": false_reject,
        }
    )
    path = DATA / "assignment03_access_control.csv"
    df.to_csv(path, index=False)
    return {
        "file": path.name,
        "n": n,
        "generating_false_reject_probability": false_reject_probability,
        "observed_false_rejections": int(false_reject.sum()),
        "note": "Generating parameters are recorded only for reproducibility.",
    }


def assignment04_coating_durability() -> dict:
    """Independent durability samples from two coating processes."""
    assignment_rng = np.random.default_rng(2804)
    parameters = {"standard": (44, 118.0, 14.0), "modified": (48, 128.0, 22.0)}
    rows = []
    specimen_id = 1
    for process, (n, mean_h, sd_h) in parameters.items():
        values = assignment_rng.normal(mean_h, sd_h, size=n)
        for value in values:
            rows.append(
                {
                    "specimen_id": specimen_id,
                    "process": process,
                    "durability_h": round(float(value), 2),
                }
            )
            specimen_id += 1
    df = pd.DataFrame(rows)
    path = DATA / "assignment04_coating_durability.csv"
    df.to_csv(path, index=False)
    return {
        "file": path.name,
        "n_by_process": {key: value[0] for key, value in parameters.items()},
        "note": "Generating parameters are recorded only for reproducibility.",
    }


def assignment04_energy_retrofit() -> dict:
    """Paired energy use before and after a building-control retrofit."""
    assignment_rng = np.random.default_rng(2805)
    n = 36
    before = assignment_rng.normal(82.0, 9.0, size=n)
    reduction = assignment_rng.normal(4.5, 5.5, size=n)
    after = before - reduction
    df = pd.DataFrame(
        {
            "building_id": np.arange(1, n + 1),
            "before_kwh_day": np.round(before, 2),
            "after_kwh_day": np.round(after, 2),
        }
    )
    path = DATA / "assignment04_energy_retrofit.csv"
    df.to_csv(path, index=False)
    return {
        "file": path.name,
        "n_pairs": n,
        "generating_mean_reduction_kwh_day": 4.5,
        "note": "Generating parameters are recorded only for reproducibility.",
    }


def assignment05_composite_strength() -> dict:
    """Composite strength under four curing methods for Assignment 5."""
    assignment_rng = np.random.default_rng(2905)
    parameters = {
        "ambient": (24, 52.0, 4.7),
        "thermal": (24, 57.0, 4.7),
        "uv": (24, 56.0, 4.7),
        "hybrid": (24, 63.0, 4.7),
    }
    rows = []
    specimen_id = 1
    for method, (n, mean_mpa, sd_mpa) in parameters.items():
        values = assignment_rng.normal(mean_mpa, sd_mpa, size=n)
        for value in values:
            rows.append(
                {
                    "specimen_id": specimen_id,
                    "curing_method": method,
                    "strength_mpa": round(float(value), 2),
                }
            )
            specimen_id += 1
    df = pd.DataFrame(rows)
    path = DATA / "assignment05_composite_strength.csv"
    df.to_csv(path, index=False)
    return {
        "file": path.name,
        "n_per_method": 24,
        "note": "Generating parameters are recorded only for reproducibility.",
    }


def assignment05_pump_energy() -> dict:
    """Pump energy use over an observed flow-rate range for Assignment 5."""
    assignment_rng = np.random.default_rng(2906)
    n = 55
    flow = np.sort(assignment_rng.uniform(22.0, 98.0, size=n))
    energy = 8.0 + 0.42 * flow + assignment_rng.normal(0.0, 3.2, size=n)
    df = pd.DataFrame(
        {
            "run_id": np.arange(1, n + 1),
            "flow_l_min": np.round(flow, 2),
            "energy_kwh": np.round(energy, 3),
        }
    )
    path = DATA / "assignment05_pump_energy.csv"
    df.to_csv(path, index=False)
    return {
        "file": path.name,
        "n": n,
        "observed_flow_range_l_min": [float(flow.min()), float(flow.max())],
        "note": "Generating parameters are recorded only for reproducibility.",
    }


def assignment06_safety_events() -> dict:
    """Safety-event categories across three sites for Assignment 6."""
    assignment_rng = np.random.default_rng(3011)
    event_types = ["sensor", "network", "mechanical", "power"]
    probabilities = {
        "north": [0.52, 0.20, 0.18, 0.10],
        "central": [0.38, 0.34, 0.18, 0.10],
        "coastal": [0.28, 0.22, 0.35, 0.15],
    }
    rows = []
    event_id = 1
    for site, probs in probabilities.items():
        events = assignment_rng.choice(event_types, size=90, p=probs)
        for event_type in events:
            rows.append(
                {"event_id": event_id, "site": site, "event_type": event_type}
            )
            event_id += 1
    df = pd.DataFrame(rows)
    path = DATA / "assignment06_safety_events.csv"
    df.to_csv(path, index=False)
    return {
        "file": path.name,
        "n_per_site": 90,
        "note": "Generating parameters are recorded only for reproducibility.",
    }


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
            supplier_impurity(),
            system_benchmark(),
            assignment01_digital_services(),
            assignment01_smart_building(),
            assignment01_production(),
            assignment01_supplier_deliveries(),
            assignment02_concrete_strength(),
            assignment02_service_repairs(),
            assignment03_sensor_calibration(),
            assignment03_access_control(),
            assignment04_coating_durability(),
            assignment04_energy_retrofit(),
            assignment05_composite_strength(),
            assignment05_pump_energy(),
            assignment06_safety_events(),
        ],
    }
    (DATA / "generation_log.json").write_text(json.dumps(log, indent=2), encoding="utf-8")
    print(json.dumps(log, indent=2))


if __name__ == "__main__":
    main()
