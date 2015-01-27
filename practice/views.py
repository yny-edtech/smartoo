#from django.http import JsonResponse
#from django.template import RequestContext, loader
from django.shortcuts import render
from practice.models import Session, Term
#import json


# ----------------------------------------------------------------------------
#  Views
# ----------------------------------------------------------------------------

def practice_session(request, topic):
    """
    Main view for practice session. Creates new session for given topic,
    selects components and returns base HTML page for the practice session.
    """
    # TODO: vytovreni tematu ... tema = term, musi existovat v DB vsech termu
    topic = Term(name=topic)

    # create session and select components
    session = Session(topic=topic)
    session.select_components()
    session.save()

    # remember the session id
    request.session['session_id'] = session.id
    # print 'key', request.session.session_key

    # render and returns base HTML for practice session
    #template = loader.get_template('smartoosession/index.html')
    #context = RequestContext(request, topic)
    #return HttpResponse(template.render(context))
    return render(request, 'practice/index.html', {
        'topic': topic})


# ----------------------------------------------------------------------------
#  Interface (for AJAX calls)
# ----------------------------------------------------------------------------

def built_knowledge(request):
    """
    Builds knowledge (if not already built) and returns "done" message.
    """
    pass


def create_exercises(request):
    """
    Creates exercises (if not already created) and returns "done" message.
    """
    pass


def new_exercise(request):
    """
    Saves the feedback from previous exercise and returns a new exercise
    (or feedback form, if the session is over).
    """
    #print 'key', request.session.session_key
    try:
        # retrieve current session
        session_id = request.session['session_id']
        session = Session.objects.get(id=session_id)

        # get a new exercise, render it and return
        exercise = session.get_new_exercise()
        # TODO: pokud uz je konec session, vratit feedback form
        #return JsonResponse(exercise)
        return render_exercise(request, exercise)

    except:
        # TODO: asi nejakou chybovou informaci?
        raise


def session_feedback(request):
    """
    Saves global feedback for the whole session.
    """
    pass


# ----------------------------------------------------------------------------
#  Helper functions
# ----------------------------------------------------------------------------

def render_exercise(request, exercise):
    """Renders exercise according to exercise type (multichoice etc.)
    """
    return render(request, 'practice/multichoice-question.html', exercise)