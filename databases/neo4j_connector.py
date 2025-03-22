from neo4j import GraphDatabase
# import logging
# from neo4j.exceptions import ServiceUnavailable

URI = "neo4j+s://c90b17ac.databases.neo4j.io"
USER = "neo4j"
PASSWORD = "8EHr3bL9a2EJBHm8RWj6234QpKdlpDvUzgtOBPQU_6E"


# class Neo4jApp:
#
#     def __init__(self, uri, user, password):
#         self.driver = GraphDatabase.driver(uri, auth=(user, password))
#
#     def close(self):
#         self.driver.close()
#
#     def create_friendship(self, person1_name, person2_name):
#         with self.driver.session(database="neo4j") as session:
#             # Write transactions allow the driver to handle retries and transient errors
#             result = session.execute_write(self._create_and_return_friendship, person1_name, person2_name)
#             for row in result:
#                 print("Created friendship between: {p1}, {p2}".format(p1=row['p1'], p2=row['p2']))
#
#     @staticmethod
#     def _create_and_return_friendship(tx, person1_name, person2_name):
#         # To learn more about the Cypher syntax, see https://neo4j.com/docs/cypher-manual/current/
#         # The Reference Card is also a good resource for keywords https://neo4j.com/docs/cypher-refcard/current/
#         query = (
#             "CREATE (p1:Person { name: $person1_name }) "
#             "CREATE (p2:Person { name: $person2_name }) "
#             "CREATE (p1)-[:KNOWS]->(p2) "
#             "RETURN p1, p2"
#         )
#         result = tx.run(query, person1_name=person1_name, person2_name=person2_name)
#         try:
#             return [{"p1": row["p1"]["name"], "p2": row["p2"]["name"]}
#                     for row in result]
#         # Capture any errors along with the query and data for traceability
#         except ServiceUnavailable as exception:
#             logging.error("{query} raised an error: \n {exception}".format(
#                 query=query, exception=exception))
#             raise
#
#     def find_person(self, person_name):
#         with self.driver.session(database="neo4j") as session:
#             result = session.execute_read(self._find_and_return_person, person_name)
#             for row in result:
#                 print("Found person: {row}".format(row=row))
#
#     @staticmethod
#     def _find_and_return_person(tx, person_name):
#         query = (
#             "MATCH (p:Person) "
#             "WHERE p.name = $person_name "
#             "RETURN p.name AS name"
#         )
#         result = tx.run(query, person_name=person_name)
#         return [row["name"] for row in result]


class Neo4jApp:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def find_all_cities(self):
        with self.driver.session(database="neo4j") as session:
            result = session.execute_read(self.find_and_return_all_cities)
            for row in result:
                print("Found city: {row}".format(row=row))

    @staticmethod
    def find_and_return_all_cities(tx):
        query = (
            "MATCH (c:CITY) "
            "RETURN c.name AS name"
        )

        result = tx.run(query)
        return [row["name"] for row in result]


if __name__ == "__main__":
    app = Neo4jApp(URI, USER, PASSWORD)
    app.find_all_cities()
    app.close()
