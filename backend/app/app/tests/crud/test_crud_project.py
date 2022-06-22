

from app import crud

from hypothesis import given, assume, settings
from hypothesis.strategies import integers, lists, text


class TestCRUDUser:

    @given(name=text(), description=text())
    @settings(max_examples=10)
    def test_create(self, db, name, description):
        result = crud.project.create(db=db,
                                     name=name,
                                     description=description)
        assert result.name == name
        assert result.description == description

    @given(name=text(), description=text())
    @settings(max_examples=10)
    def test_get_by_id(self, db, name, description):
        create_result = crud.project.create(db=db,
                                            name=name,
                                            description=description)

        _project = crud.project.get_by_id(db=db,
                                          id=create_result.id)

        assert _project.name == name
        assert _project.description == description

    @given(name=text(), description=text())
    @settings(max_examples=10)
    def test_delete(self, db, name, description):
        create_result = crud.project.create(db=db,
                                            name=name,
                                            description=description)
        crud.project.delete_by_id(db, id=create_result.id)

        _project = crud.project.get_by_id(db=db,
                                          id=create_result.id)

        assert _project is None
