# Keywords extraction

_This service was created as a result of the OpenReq project funded by the European Union Horizon 2020 Research and Innovation programme under grant agreement No 732463._

## Introduction

The component is based in the preprocess used in the project called similar-related-requirements-recommender. The main purpose of this service is to preprocess requirements and return their clean tokens.

## Technical description

Next sections provide a general overview of the technical details of the service.

### Main functionalities

There is only one method that returns the clean tokens of the input requirements. Check API details in the swagger documentation.

The API uses UTF-8 charset. Also, it uses the OpenReq format for input JSONs.


### Used technologies

### How to install

Steps to configure the service:

    - Install python3, python3-venv and pip3: sudo apt-get install python3 python3-venv pip3
    - Install virtualenv: python3 -m pip install --user virtualenv
    - Generate a virtual environment: python3 -m venv env
    - Activate the virtual environment: source env/bin/activate
    - Install component dependencies with the requirements file: pip3 install -r requirements.txt

Steps to run the service:
    
    - Activate the virtual environment: source env/bin/activate
    - Run the service: python3 -m application
    - Go to http://127.0.0.1:9406/swagger/ to see the swagger generated. You can use the component through the swagger or through http connections to the endpoints indicated in the swagger documentation.

### How to use it

The service expects a JSON with OpenReqJson format.

### Notes for developers

### Sources

## How to contribute

See OpenReq project contribution [guidelines](https://github.com/OpenReqEU/OpenReq/blob/master/CONTRIBUTING.md)

## License

Free use of this software is granted under the terms of the [EPL version 2 (EPL2.0)](https://www.eclipse.org/legal/epl-2.0/)
