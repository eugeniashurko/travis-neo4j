def get_nodes(driver):
    query = "MATCH (n) RETURN n"
    session = driver.session()
    session.run(query)
    session.close()
