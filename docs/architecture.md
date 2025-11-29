# Architecture — How This Hub Connects to Law-N

The Law-N ecosystem (so far):

- **Specs / core:**
  - `law-n-core-spec`
  - `law-n-nsql-spec`
- **Engines / implementations:**
  - `law-n-sql-core`
  - `law-n-nsql-engine`
  - `law-n-sql-api`
  - `law-n-sql-playground`
- **Simulation / profiles:**
  - `law-n-signal-sim`
  - `law-n-device-profiles`

This repo sits **above** them as a notebook + dataset layer.

Recommended local layout:

```text
workspace/
  law-n-core-spec/
  law-n-nsql-spec/
  law-n-sql-core/
  law-n-nsql-engine/
  law-n-sql-api/
  law-n-sql-playground/
  law-n-signal-sim/
  law-n-device-profiles/
  law-n-notebook-hub/          ← this repo
