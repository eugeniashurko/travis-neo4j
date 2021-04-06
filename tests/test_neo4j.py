from package.dummy import get_nodes

def test_neo4j(neo4j_driver):
    get_nodes(neo4j_driver)
