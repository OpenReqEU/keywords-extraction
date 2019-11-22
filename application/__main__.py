from flask import Flask, request, abort
from flasgger import Swagger, swag_from
from application.preprocessing import preprocessing
from application.entities.requirement import Requirement
from application.util.config import get_ip
import logging

app = Flask(__name__)

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/keywords-extraction/apispec_1.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/keywords-extraction/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/keywords-extraction/swagger-ui.html/"
}

template = {
  "swagger": "2.0",
  "info": {
    "description": "The component is based in the keywords extraction process used in the OpenReq project called [similar-related-requirements-recommender](https://github.com/OpenReqEU/similar-related-requirements-recommender). The main purpose of this service is to preprocess requirements and to obtain the keywords that represent each one.",
    "version": "1.0",
    "title": "Keywords Extraction",
  },
  "host": "api.openreq.eu/keywords-extraction",
  "basePath": "/",
  "schemes": [
    "https"
  ]
}

swagger = Swagger(app, template=template, config=swagger_config)


def encoder(object):
    if isinstance(object, Requirement):
        aux = object.__dict__
        new_dict = dict()
        new_dict['id'] = aux['id']
        new_dict['title_tokens'] = aux['title_tokens']
        new_dict['description_tokens'] = aux['description_tokens']
        return new_dict


@app.route('/keywords-extraction/requirements', methods=['POST'])
@swag_from('./static/preprocess.yml')
def preprocess():
    if not request.json or 'requirements' not in request.json:
        abort(400, 'The input json is empty or it does not contain a requirements array')
    stemmer = request.args.get('stemmer', '')
    if stemmer == "":
        abort(400, 'The stemmer parameter is missing')
    if stemmer != 'true' and stemmer != 'false':
        abort(400, 'The stemmer parameter is not correct')
    requirements = []
    for json_req in request.json['requirements']:
        if 'id' not in json_req:
            abort(400, 'There is a requirement without id')
        id = json_req['id']
        title = ''
        description = ''
        if 'title' in json_req and json_req['title'] is not None:
            title = json_req['title']
        if 'description' in json_req and json_req['description'] is not None:
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
    ip = get_ip()
    logging.basicConfig(filename='logs/keywords-extraction.log', level=logging.INFO)
    app.run(port=9406, host=ip, debug=False, threaded=True)
