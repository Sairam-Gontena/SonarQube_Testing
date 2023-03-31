"""Please define all controllers that have routes here which will be imported in main.py"""
from fastapi import APIRouter

from controllers import app_enum_controller, category_controller, category_map_controller, choice_controller, \
    choice_group_controller, patient_questionnaire_controller, question_category_map_controller, \
    question_controller, question_dependency_controller, question_map_controller, \
    questionnaire_template_controller

all_routes = APIRouter()

all_routes.include_router(
    app_enum_controller.router,
    prefix="/appEnum",
    tags=["appEnum"],
    responses={418: {"description": "I'm a appEnum"}},
)
all_routes.include_router(
    category_controller.router,
    prefix="/category",
    tags=["category"],
    responses={418: {"description": "I'm a category"}},
)
all_routes.include_router(
    category_map_controller.router,
    prefix="/categoryMap",
    tags=["categoryMap"],
    responses={418: {"description": "I'm a categoryMap"}},
)
all_routes.include_router(
    choice_controller.router,
    prefix="/choice",
    tags=["choice"],
    responses={418: {"description": "I'm a choice"}},
)
all_routes.include_router(
    choice_group_controller.router,
    prefix="/choiceGroup",
    tags=["choiceGroup"],
    responses={418: {"description": "I'm a choiceGroup"}},
)
all_routes.include_router(
    patient_questionnaire_controller.router,
    prefix="/patientQuestionnaire",
    tags=["patientQuestionnaire"],
    responses={418: {"description": "I'm a patientQuestionnaire"}},
)
all_routes.include_router(
    question_category_map_controller.router,
    prefix="/questionCategoryMap",
    tags=["questionCategoryMap"],
    responses={418: {"description": "I'm a questionCategoryMap"}},
)
all_routes.include_router(
    question_controller.router,
    prefix="/question",
    tags=["question"],
    responses={418: {"description": "I'm a question"}},
)
all_routes.include_router(
    question_dependency_controller.router,
    prefix="/questionDependency",
    tags=["questionDependency"],
    responses={418: {"description": "I'm a questionDependency"}},
)
all_routes.include_router(
    question_map_controller.router,
    prefix="/questionMap",
    tags=["questionMap"],
    responses={418: {"description": "I'm a questionMap"}},
)
all_routes.include_router(
    questionnaire_template_controller.router,
    prefix="/questionTemplate",
    tags=["questionTemplate"],
    responses={418: {"description": "I'm a questionTemplate"}},
)
