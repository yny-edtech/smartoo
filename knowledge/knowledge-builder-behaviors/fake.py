from knowledge import KnowledgeBuilderBehavior as BaseKnowledgeBuilderBehavior


"""
Fake Knowledge Builder
----------------------

Pretends to create knowledge graph for given topic.
For demo/testing purposes only.
"""


class KnowledgeBuilderBehavior(BaseKnowledgeBuilderBehavior):

    def build_knowledge_graph(self, topic):
        """
        Creates knowledge graph for given topic.

        Args:
            topic (knowledge.models.Term): topic for which to build
                the knowledge graph
        Retuns:
            knowledge graph (knowledge.models.KnowledgeGraph)
        """
        pass