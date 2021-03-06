# encoding=utf-8

from __future__ import unicode_literals

#from django.core.urlresolvers import reverse
from django.test import TestCase

from common.utils.mock import MockObject
from common.settings import SKIP_ONLINE_TESTS, SKIP_LOGGING_TESTS
from knowledge.namespaces import TERM
from knowledge.models import KnowledgeGraph
from exercises.models import Exercise, GradedExercise
from smartoo.models import Session
from smartoo.views import start_session, build_knowledge, create_exercises, next_exercise

from json import loads, dumps
from unittest import skipIf


class StartSessionViewTestCase(TestCase):
    fixtures = ['fake-components-article.xml']

    def setUp(self):
        pass

# NOTE: As it's problematic too test views using session data (and encode
# request body the same way as AngularJS?!), we will test directly views
# methods using fake requests (with fake session dictionary)

    @skipIf(SKIP_LOGGING_TESTS, 'logging successfully started session')
    def test_start_session_successfully(self):
        #response = self.client.post('/interface/start-session',
        #    {"topic": "Abraham_Lincoln"})
        fake_request = MockObject(
            session={},
            body=dumps({'topic': 'Abraham_Lincoln'}))
        response = start_session(fake_request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(loads(response.content)["success"], True)
        sessions = Session.objects.all()
        self.assertEqual(len(sessions), 1)
        session = sessions[0]
        self.assertEqual(session.topic, TERM['Abraham_Lincoln'])

    @skipIf(SKIP_ONLINE_TESTS, 'connection to Wikipedia API')
    def test_start_session_unsuccessfully(self):
        #response = self.client.post('/interface/start-session',
        #    {'topic': 'Some_nonsense_definitely_not_in_Wiki'})
        fake_request = MockObject(
            session={},
            body=dumps({'topic': 'sdfslfjalkfjsfl'}))
        response = start_session(fake_request)
        self.assertEqual(loads(response.content)["success"], False)
        self.assertEqual(response.status_code, 400)
        sessions = Session.objects.all()
        self.assertEqual(len(sessions), 0)


class BuildKnowledgeViewTestCase(TestCase):
    fixtures = ['fake-components-article.xml']

    def test_build_knowledge(self):
        #response = self.client.post('/interface/build-knowledge')
        topic = TERM['Abraham_Lincoln']
        session = Session.objects.create_with_components(topic)
        fake_request = MockObject(session={'session_id': session.id})

        response = build_knowledge(fake_request)
        self.assertEqual(loads(response.content)["success"], True)
        self.assertEqual(response.status_code, 200)

        # check that the knowledge was built
        knowledge_graphs = KnowledgeGraph.objects.all()
        self.assertEqual(len(knowledge_graphs), 1)
        knowledge_graph = knowledge_graphs[0]
        self.assertEqual(knowledge_graph.topic, topic)


class CreateExercisesViewTestCase(TestCase):
    fixtures = ['fake-components-article.xml']

    def test_create_exercises(self):
        topic = TERM['Abraham_Lincoln']
        session = Session.objects.create_with_components(topic)
        session.build_knowledge()
        fake_request = MockObject(session={'session_id': session.id})
        response = create_exercises(fake_request)
        self.assertEqual(loads(response.content)["success"], True)
        self.assertEqual(response.status_code, 200)

        # check that exercises were stored
        exercises = Exercise.objects.all()
        grades = GradedExercise.objects.all()
        self.assertGreater(len(exercises), 0, "No exercises were stored.")
        self.assertGreater(len(grades), 0, "No grades were stored.")
        self.assertEqual(len(exercises), len(grades),
            "The number of stored grades and exercises is different.")


class NextExerciseViewTestCase(TestCase):
    fixtures = ['fake-components-article.xml']

    def test_next_exercise(self):
        topic = TERM['Abraham_Lincoln']
        session = Session.objects.create_with_components(topic)
        session.build_knowledge()
        session.create_graded_exercises()
        fake_request = MockObject(session={'session_id': session.id}, body=None)
        response = next_exercise(fake_request)
        self.assertEqual(response.status_code, 200)
        response_content = loads(response.content)
        self.assertEqual(response_content["success"], True)
        self.assertIn('exercise', response_content)
        self.assertIn('question', response_content['exercise'])
