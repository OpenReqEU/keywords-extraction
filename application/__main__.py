from flask import Flask, request, abort
from flask_swagger_ui import get_swaggerui_blueprint
from application.preprocessing import preprocessing
from application.entities.requirement import Requirement

app = Flask(__name__)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "keywords-extraction"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


def encoder(object):
    if isinstance(object, Requirement):
        aux = object.__dict__
        new_dict = dict()
        new_dict['id'] = aux['id']
        new_dict['title_tokens'] = aux['title_tokens']
        new_dict['description_tokens'] = aux['description_tokens']
        return new_dict


@app.route('/keywords-extraction/requirements', methods=['POST'])
def create_task():
    if not request.json or 'requirements' not in request.json:
        abort(400, 'The input json is empty or it does not contain a requirements array')
    stemmer = request.args.get('stemmer', '')
    if stemmer != 'true' and stemmer != 'false':
        abort(400, 'The stemmer parameter is missing')
    requirements = []
    for json_req in request.json['requirements']:
        if 'id' not in json_req:
            abort(400, 'There is a requirement without id')
        id = json_req['id']
        title = ''
        description = ''
        if 'title' in json_req:
            title = json_req['title']
        if 'description' in json_req:
            description = json_req['description']
        requirements.append(Requirement(id, title, description, ''))
    if len(requirements) == 0:
        abort(400, 'The input requirements array is empty')
    if stemmer == 'true':
        preprocessed_requirements = preprocessing.preprocess_requirements(requirements, True)
    else:
        preprocessed_requirements = preprocessing.preprocess_requirements(requirements, False)
    result = {'requirements': []}
    for requirement in preprocessed_requirements:
        result['requirements'].append(encoder(requirement))
    return result, 200


@app.errorhandler(400)
def bad_request(error):
    return {'error': 'Bad request', 'message': error.description}, 400


if __name__ == '__main__':
    app.run(port=9406, host='0.0.0.0', debug=False, threaded=True)
