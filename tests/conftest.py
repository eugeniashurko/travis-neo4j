import pytest
from neo4j import GraphDatabase


# Neo4j credentials (should be moved to some config files or env vars)
NEO4J_URI = "bolt://0.0.0.0:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "neo4j"


@pytest.fixture(scope="module")
def neo4j_driver():
    driver = GraphDatabase.driver(
        NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    yield driver
    cleanup_query = (
        "MATCH (n) "
        "WHERE any(l IN labels(n) WHERE l STARTS WITH 'Test') "
        "DETACH DELETE n"
    )
    session = driver.session()
    session.run(cleanup_query)
    session.close()
