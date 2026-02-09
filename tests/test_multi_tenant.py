from app.services.vector_store import VectorStore

def test_tenant_isolation():
    store = VectorStore()

    store.add("tenant_a", [[0.1, 0.2]], ["Doc A"])
    store.add("tenant_b", [[0.1, 0.2]], ["Doc B"])

    result_a = store.search("tenant_a", [0.1, 0.2])
    result_b = store.search("tenant_b", [0.1, 0.2])

    assert result_a == ["Doc A"]
    assert result_b == ["Doc B"]
