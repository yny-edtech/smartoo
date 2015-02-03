from django.test import TestCase
from knowledge.models import Vertical, Topic, KnowledgeBuilder, KnowledgeGraph
from exercises.models import Exercise, ExercisesCreator


class ExercisesCreatorTestCase(TestCase):
    def setUp(self):
        # create a vertical, topic, knowledge builder and knowledge graph
        self.vertical = Vertical.objects.create(
            content='test line')
        self.topic = Topic.objects.create(
            uri='http://en.wikipedia.org/wiki/Pan_Tau',
            vertical=self.vertical)
        self.knowledge_builder = KnowledgeBuilder.objects.create(
            behavior_name='fake',
            parameters={"alpha": 0.5})
        self.knowledge_graph = KnowledgeGraph.objects.create(
            topic=self.topic,
            knowledge_builder=self.knowledge_builder)

    def test_create_exercises(self):
        creator = ExercisesCreator.objects.create(
            behavior_name='fake', parameters={})
        # check exercises yielding
        exercises_count = 0
        for exercise in creator.create_exercises(self.knowledge_graph):
            self.assertIsInstance(exercise, Exercise)
            self.assertIsInstance(exercise.data, dict)
            self.assertTrue('question' in exercise.data)
            self.assertIsInstance(exercise.data['question'], str)
            exercises_count += 1
        # check that nonzerou number of exercises was yielded
        self.assertGreater(exercises_count, 0)
        # check that all the exercises were stored
        self.assertEqual(len(Exercise.objects.all()), exercises_count)
