import unittest

from application import __main__
__main__.testing = True

input = {
	"requirements": [{
		'id': 'UPC-1',
		'title': 'The swagger version is deprecated.',
		'description': 'There is a new version available.'
	}]
}

output = {
	'requirements': [{
		'description_tokens': ['there', 'is', 'a', 'new', 'version', 'available'],
		'id': 'UPC-1',
		'title_tokens': ['the', 'swagger', 'version', 'is', 'deprecated']
	}]
}

output_stemmer = {
	'requirements': [{
		'description_tokens': ['there', 'is', 'a', 'new', 'version', 'avail'],
		'id': 'UPC-1',
		'title_tokens': ['the', 'swagger', 'version', 'is', 'deprec']
	}]
}




class TestApi(unittest.TestCase):

    def setUp(self):
      self.app_context = __main__.app.app_context()
      self.app_context.push()

    def test_without_stemmer(self):
        with __main__.app.test_client() as client:
            # send data as POST form to endpoint
            result = client.post(
              '/keywords-extraction/requirements?stemmer=false',
              json=input
            )
            # check result from server with expected data
            self.assertEqual(
                result.json,
                output
            )

    def test_with_stemmer(self):
        with __main__.app.test_client() as client:
            # send data as POST form to endpoint
            result = client.post(
              '/keywords-extraction/requirements?stemmer=true',
              json=input
            )
            # check result from server with expected data
            self.assertEqual(
                result.json,
                output_stemmer
            )