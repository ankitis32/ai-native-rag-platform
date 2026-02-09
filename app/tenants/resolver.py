def resolve_tenant(api_key: str) -> str:
    # In production: lookup from DB / IAM
    return api_key.split("_")[0]
