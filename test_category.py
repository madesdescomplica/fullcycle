import pytest
from uuid import UUID, uuid4

from category import Category

class TestCategory:
    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_have_less_than_255_characters(self):
        with pytest.raises(ValueError, match="name can not be longer than 255 characters"):
            Category(name="a" * 256)

    def test_category_must_be_created_with_id_as_uuid_by_default(self):
        category = Category(name="Category")
        assert category.id is not None
        assert isinstance(category.id, UUID)

    def test_created_category_with_default_values(self):
        category = Category(name="Category")
        assert category.name == "Category"
        assert category.description == ""
        assert category.is_active == True

    def test_category_is_created_as_active_by_default(self):
        category = Category(name="Category")
        assert category.is_active is True

    def test_category_is_created_with_provided_values(self):
        category_id = uuid4()
        category = Category(
            id=category_id,
            name="Category",
            description="Category Description",
            is_active=False,
        )
        assert category.id == category_id
        assert category.name == "Category"
        assert category.description == "Category Description"
        assert category.is_active is False

    def test_can_not_create_category_with_empty_name(self):
        with pytest.raises(ValueError, match="name can not be empty or null"):
            Category(name="")

    def test_can_not_create_category_with_null(self):
        with pytest.raises(ValueError, match="name can not be empty or null"):
            Category(name=None)

class TestUpdateCategory:
    def test_update_category_with_name_and_description(self):
        category = Category(name="Filme", description="Filme Description")
        category.update_name_and_description(name="Séries", description="Séries Description")

        assert category.name == "Séries"
        assert category.description == "Séries Description"

    def test_update_category_with_invalid_name_raises_exception(self):
        category = Category(name="Filme", description="Filme Description")

        with pytest.raises(ValueError, match="name can not be longer than 255 characters"):
            category.update_name_and_description(name="a" * 256, description="Séries Description")

    def test_can_not_update_category_with_empty_name(self):
        with pytest.raises(ValueError, match="name can not be empty or null"):
            Category(name="")

    def test_can_not_update_category_with_null(self):
        with pytest.raises(ValueError, match="name can not be empty or null"):
            Category(name=None)

class TestActivateCategory:
    def test_activate_inactive_category(self):
        category = Category(name="Filme", description="Filme Description", is_active=False)
        category.activate()

        assert category.is_active is True

    def test_activate_activate_category(self):
        category = Category(name="Filme", description="Filme Description")
        category.activate()

        assert category.is_active is True

    def test_deactivate_inactive_category(self):
        category = Category(name="Filme", description="Filme Description", is_active=False)
        category.deactivate()

        assert category.is_active is False

    def test_deactivate_activate_category(self):
        category = Category(name="Filme", description="Filme Description")
        category.deactivate()

        assert category.is_active is False