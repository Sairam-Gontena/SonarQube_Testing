"""Import all the model classes from the parent folder
    Generate parent tables first."""
import config.database_connection
from models import app_enum, category, category_map, choice_group, choice, patient_questionnaire, question, \
    question_category_map, question_dependency, question_map, questionnaire_template

app_enum.Base.metadata.create_all(bind=config.database_connection.engine)
category.Base.metadata.create_all(bind=config.database_connection.engine)
category_map.Base.metadata.create_all(bind=config.database_connection.engine)
choice_group.Base.metadata.create_all(bind=config.database_connection.engine)
choice.Base.metadata.create_all(bind=config.database_connection.engine)
patient_questionnaire.Base.metadata.create_all(bind=config.database_connection.engine)
question.Base.metadata.create_all(bind=config.database_connection.engine)
question_category_map.Base.metadata.create_all(bind=config.database_connection.engine)
question_dependency.Base.metadata.create_all(bind=config.database_connection.engine)
question_map.Base.metadata.create_all(bind=config.database_connection.engine)
questionnaire_template.Base.metadata.create_all(bind=config.database_connection.engine)

print("~~~~~~~~~~~~~~~~~~~~Completed Creating tables~~~~~~~~~~~~~~~~~~~~")

config.database_connection.connection.close()
