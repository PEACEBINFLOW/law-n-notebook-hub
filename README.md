# Law-N Notebook Hub

This repo is the **central notebook lab** for the Law-N ecosystem.

Instead of scattering experiments across multiple repos, this hub gives one place to:

- Run and share notebooks backed by the **8 core Law-N repos**:
  - `law-n-sql-core`
  - `law-n-signal-sim`
  - `law-n-sql-playground`
  - `law-n-sql-api`
  - `law-n-core-spec`
  - `law-n-device-profiles`
  - `law-n-nsql-spec`
  - `law-n-nsql-engine`
- Store datasets used across those experiments
- Prepare clean, exportable notebooks for **Kaggle** and other platforms

Vendor and telco integrations (NVIDIA, Nokia, etc.) will come later as a separate layer.
This repo’s **first job** is simple:

> Be the stable home for notebooks and datasets that demonstrate Law-N in practice.

---

## Repo layout

```text
notebooks/
  core/              → notebooks aligned to each Law-N core repo

datasets/
  raw/               → raw exports / measurements
  processed/         → cleaned, Law-N-shaped tables (e.g. network.routes)
  external/          → public/example data you want to reuse

env/
  requirements.txt   → Python deps for local / Kaggle
  environment.yml    → optional Conda-style env

docs/
  README-extended.md → deeper write-up
  notebook-index.md  → table of notebooks (you fill as you go)
  architecture.md    → how this hub connects to the 8 core repos

kaggle/
  README.md          → how this maps to Kaggle notebooks/datasets
  metadata-templates/→ JSON templates for Kaggle metadata

scripts/
  build_notebook_index.py → helper to auto-build `docs/notebook-index.md`
