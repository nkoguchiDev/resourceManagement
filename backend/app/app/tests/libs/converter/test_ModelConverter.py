import pytest
from pydantic import BaseModel

from app.libs.converter import ModelConverter

testdata01 = [[{"name": 'name0'},
               '{name: "name0",description: "-"}'],
              [{"name": 'name0',
                "description": 'description1'},
               '{name: "name0",description: "description1"}']]

testdata02 = [[{b"name": b"name0"}, {"name": "name0"}]]


class TestModelConverter:
    @pytest.mark.parametrize("data,result", testdata01)
    def test_to_cypher_object(self, data, result):
        class Model(BaseModel):
            name: str
            description: str = "-"

        assert ModelConverter.to_cypher_object(Model(**data)) == result

    @pytest.mark.parametrize("data,result", testdata02)
    def test_byte_key_value_to_dict(self, data, result):

        assert ModelConverter.byte_key_value_to_dict(data) == result
