<h1 align="center">Datasets</h1>

All course files live in the repository folder `data/`. From a session notebook:

```python
from pathlib import Path
DATA = Path("../data")
```

Synthetic files are generated reproducibly by `tools/generate_datasets.py` with seed `2026`. Analyse them as measurements whose generating parameters are unknown.

## Files

| File | Origin | Rows | Columns | Used in |
| --- | --- | --- | --- | --- |
| `sensor_thickness.csv` | Synthetic | 180 | `sample_id`, `line` (A/B), `thickness_um`, `shift_um` | Sessions 01, 05, 06, 07, 12 |
| `packet_loss.csv` | Synthetic | 200 | `trial`, `packet_lost` | Session 03 |
| `response_times.csv` | Synthetic | 60 | `request_id`, `server_a_ms`, `server_b_ms`, `server_b_paired_ms` | Sessions 04, 08 |
| `component_lifetimes.csv` | Synthetic | 80 | `unit_id`, `lifetime_h` | Session 04 |
| `energy_load.csv` | Synthetic | 40 | `day`, `cpu_load_pct`, `energy_kwh` | Session 10 |
| `defect_types.csv` | Synthetic | 360 | `line`, `defect_type` | Session 11 |
| `batteries.xlsx` | STA_26 | 30 | `Producer 1`, `Producer 2` (lifetimes) | Session 08 extra |
| `cpu_order_lines.xlsx` | STA_26 | 31 | `Sample`, `CPU_utilisation`, `Order_lines_per_day` | Session 10 extra |
| `resin_impurities.xlsx` | STA_26 | 15 | `resin`, `impurity` | Session 09 |
| `scope_filter_intensity.xlsx` | STA_26 | 60 | `filter`, `intensity` | Session 09 |

`shift_um` in `sensor_thickness.csv` documents a late production drift used in Session 12. Do not use it as a predictor in earlier sessions; treat `thickness_um` as the measurement.

## Regenerating the synthetic files

```text
python tools/generate_datasets.py
```

Do not replace the four `.xlsx` files; they are curated measurements from the previous Danish course.
