import os
from andromeda.config import AndromedaConfig
from andromeda.core.team import Team

def build_team(config_path: str) -> Team:
      # Tokenization requires one of these env vars.
      # Prefer ANDROMEDA_ENCRYPTION_KEY in production.
      if not (
            os.getenv("ANDROMEDA_ENCRYPTION_KEY")
            or os.getenv("ANDROMEDA_ENCRYPTION_SECRET")
      ):
            raise RuntimeError(
                  "Tokenization is enabled but no encryption env var is set. "
                  "Set ANDROMEDA_ENCRYPTION_KEY or ANDROMEDA_ENCRYPTION_SECRET."
            )

      try:
            cfg = AndromedaConfig.load_from_file(config_path)
      except FileNotFoundError as exc:
            raise SystemExit(f"Config file missing: {exc}")
      except ValueError as exc:
            # Includes validation errors, unknown tool names,
            # and missing ${ENV_VAR} interpolation values.
            raise SystemExit(f"Invalid configuration: {exc}")

      return Team(cfg)

team = build_team("config.production.yaml")
result = team.begin("Customer email: john.doe@company.com cannot log in")
print(result.get("report_output") or result["messages"][-1].content)