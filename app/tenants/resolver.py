def resolve_tenant(api_key: str) -> str:
    if not api_key:
        raise ValueError("Missing API key")
    return api_key.split("_")[0]
