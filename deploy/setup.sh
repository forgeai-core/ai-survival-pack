
---

### 🔹 `deploy/setup.sh`
```bash
#!/bin/bash

echo "🔧 Setting up ForgeAI Survival Pack..."

# Check dependencies
command -v python3 >/dev/null 2>&1 || { echo >&2 "Python3 is required but not installed. Aborting."; exit 1; }
command -v docker >/dev/null 2>&1 || echo "⚠️ Docker not found. Required for micro-tools like LabGPT."

# Create folders for runtime (if needed)
mkdir -p runtime/logs runtime/output

echo "✅ Environment initialized."
