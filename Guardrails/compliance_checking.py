from andromeda.config.config import CompliancePatternsConfig

# Configure compliance guardrails
cfg = AgentConfig(
    name="compliant_agent",
    model=ModelConfig(name="qwen3.5:9b", provider="ollama"),
    middleware=MiddlewareConfig(
        guardrails=MiddlewareConfig.GuardrailOptions(
            output=True,
            tool=True,
            compliance_patterns=CompliancePatternsConfig(
                patterns=[
                    # Prevents unauthorized medical advice
                    r"medical.*(advice|diagnosis|prescription)",
                    # Blocks investment recommendations
                    r"investment.*(advice|recommendation)",
                    # Prevents legal counsel without proper licensing
                    r"legal.*(advice|opinion)"
                ]
            ),
            blocked_message="I can't provide professional advice in regulated areas."
        )
    )
)
agent = Agent(cfg)