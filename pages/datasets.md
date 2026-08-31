<h1 align="center">Datasets</h1>

All course files live in the folder `data/` on GitHub. You do not need Git: [download the data folder](https://download-directory.github.io/?url=https://github.com/RBrooksDK/STA1_26/tree/main/data), unzip it, and keep a folder named `data` next to your notebook. Session 00 has the full steps. If a file is missing later in the semester, download the folder again and replace the old copy.

From a session notebook:

```python
from pathlib import Path
DATA = Path("../data")
```

Synthetic files are generated reproducibly by `tools/generate_datasets.py` with seed `2026`. Analyse them as measurements whose generating parameters are unknown.

## Files

| File | Origin | Rows | Columns | Used in |
| --- | --- | --- | --- | --- |
| `sensor_thickness.csv` | Synthetic | 180 | `sample_id`, `line` (A/B), `thickness_um`, `shift_um` | Sessions 01, 06, 07 |
| `packet_loss.csv` | Synthetic | 200 | `trial`, `packet_lost` | Session 03 |
| `response_times.csv` | Synthetic | 60 | `request_id`, `server_a_ms`, `server_b_ms`, `server_b_paired_ms` | Sessions 04, 08 |
| `component_lifetimes.csv` | Synthetic | 80 | `unit_id`, `lifetime_h` | Session 04 |
| `energy_load.csv` | Synthetic | 40 | `day`, `cpu_load_pct`, `energy_kwh` | Session 10 |
| `defect_types.csv` | Synthetic | 360 | `line`, `defect_type` | Session 11 |
| `supplier_impurity.csv` | Synthetic | 72 | `sample_id`, `supplier` (A/B/C), `impurity_mg_kg` | Session 09 |
| `system_benchmark.csv` | Synthetic | 120 | `run_id`, `configuration`, `load_pct`, `latency_ms`, `energy_kwh`, `incident` | Session 12 |
| `assignment01_digital_services.csv` | Synthetic | 144 | `observation_id`, `service`, `latency_ms`, `alert_type` | Assignment 1 |
| `assignment01_smart_building.csv` | Synthetic | 96 | `measurement_id`, `hour`, `zone`, `outdoor_temp_c`, `indoor_temp_c`, `energy_kwh` | Assignment 1 |
| `assignment01_production.csv` | Synthetic | 120 | `part_id`, `machine`, `diameter_mm`, `vibration_mm_s` | Additional practice |
| `assignment01_supplier_deliveries.csv` | Synthetic | 120 | `shipment_id`, `supplier`, `lead_time_days` | Additional practice |
| `assignment02_concrete_strength.csv` | Synthetic | 160 | `specimen_id`, `strength_mpa` | Assignment 2 |
| `assignment02_service_repairs.csv` | Synthetic | 180 | `incident_id`, `repair_time_min` | Assignment 2 |
| `assignment03_sensor_calibration.csv` | Synthetic | 64 | `sensor_id`, `calibration_error_c` | Assignments 3–4 |
| `assignment03_access_control.csv` | Synthetic | 240 | `attempt_id`, `false_reject` | Assignments 3–4 |
| `assignment04_coating_durability.csv` | Synthetic | 92 | `specimen_id`, `process`, `durability_h` | Assignment 4 |
| `assignment04_energy_retrofit.csv` | Synthetic | 36 | `building_id`, `before_kwh_day`, `after_kwh_day` | Assignment 4 |
| `assignment05_composite_strength.csv` | Synthetic | 96 | `specimen_id`, `curing_method`, `strength_mpa` | Assignment 5 |
| `assignment05_pump_energy.csv` | Synthetic | 55 | `run_id`, `flow_l_min`, `energy_kwh` | Assignment 5 |
| `assignment06_safety_events.csv` | Synthetic | 270 | `event_id`, `site`, `event_type` | Assignment 6 |
| `batteries.xlsx` | STA_26 | 30 | `Producer 1`, `Producer 2` (lifetimes) | Additional practice |
| `cpu_order_lines.xlsx` | STA_26 | 31 | `Sample`, `CPU_utilisation`, `Order_lines_per_day` | Additional practice |
| `resin_impurities.xlsx` | STA_26 | 15 | `resin`, `impurity` | Additional practice |
| `scope_filter_intensity.xlsx` | STA_26 | 60 | `filter`, `intensity` | Additional practice |

`shift_um` in `sensor_thickness.csv` documents a late production drift used when generating the file. Do not use it as a predictor in Sessions 01--07; treat `thickness_um` as the measurement.

The two active Assignment 1 files support descriptive analysis in [Assignment 1](../assignments/assignment_01_data_and_probability_foundations.md). The production and supplier files remain available as additional descriptive-practice data.

The Assignment 2 files support normal- and exponential-model assessment in [Assignment 2](../assignments/assignment_02_discrete_and_continuous_models.md).

The Assignment 3 files are first used for estimation in [Assignment 3](../assignments/assignment_03_sampling_and_estimation.md) and then revisited for one-sample tests in [Assignment 4](../assignments/assignment_04_one_and_two_sample_tests.md). The remaining files provide new two-sample, ANOVA, regression, and categorical cases for Assignments 4–6. Treat all generating parameters as unknown analysis targets.

## Regenerating the synthetic files

```text
python tools/generate_datasets.py
```

Do not replace the four `.xlsx` files; they are curated measurements from the previous Danish course.
