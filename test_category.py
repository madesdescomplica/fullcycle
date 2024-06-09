from faker import Faker
import pytest
from uuid import UUID, uuid4

from category import Category


class TestCategory:
    faker = Faker()

    category_id: UUID = uuid4()
    name: str = faker.word()
    description: str = faker.sentence(nb_words=10)

    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_have_less_than_255_characters(self):
        with pytest.raises(ValueError, match="name can not be longer than 255 characters"):
            Category(name=self.faker.sentence(100))

    def test_category_must_be_created_with_id_as_uuid_by_default(self):
        category = Category(name=self.name)

        assert category.id is not None
        assert isinstance(category.id, UUID)

    def test_created_category_with_default_values(self):
        category = Category(name=self.name)

        assert category.name == self.name
        assert category.description == ""
        assert category.is_active == True

    def test_category_is_created_as_active_by_default(self):
        category = Category(name=self.name)

        assert category.is_active is True

    def test_category_is_created_with_provided_values(self):
        category = Category(
            id=self.category_id,
            name=self.name,
            description=self.description,
            is_active=False
        )

        assert category.id == self.category_id
        assert category.name == self.name
        assert category.description == self.description
        assert category.is_active is False

    def test_can_not_create_category_with_empty_name(self):
        with pytest.raises(ValueError, match="name can not be empty or null"):
            Category(name="")

    def test_can_not_create_category_with_null(self):
        with pytest.raises(ValueError, match="name can not be empty or null"):
            Category(name=None)

class TestUpdateCategory:
    faker = Faker()

    name: str = faker.word()
    description: str = faker.sentence(nb_words=10)

    def test_update_category_with_name_and_description(self):
        updated_name = self.faker.word()
        updated_description = self.faker.sentence(nb_words=7)

        category = Category(name=self.name, description=self.description)
        category.update_name_and_description(
            name=updated_name,
            description=updated_description
        )

        assert category.name == updated_name
        assert category.description == updated_description

    def test_update_category_with_invalid_name_raises_exception(self):
        updated_name = self.faker.sentence(100)
        updated_description = self.faker.sentence(nb_words=7)

        category = Category(name=self.name, description=self.description)

        with pytest.raises(ValueError, match="name can not be longer than 255 characters"):
            category.update_name_and_description(
                name=updated_name,
                description=updated_description
            )

    def test_can_not_update_category_with_empty_name(self):
        with pytest.raises(ValueError, match="name can not be empty or null"):
            Category(name="")

    def test_can_not_update_category_with_null(self):
        with pytest.raises(ValueError, match="name can not be empty or null"):
            Category(name=None)

class TestActivateCategory:
    faker = Faker()

    name: str = faker.word()
    description: str = faker.sentence(nb_words=10)
    
    def test_activate_inactive_category(self):
        category = Category(
            name=self.name,
            description=self.description,
            is_active=False
        )
        category.activate()

        assert category.is_active is True

    def test_activate_activate_category(self):
        category = Category(name=self.name, description=self.description)
        category.activate()

        assert category.is_active is True

    def test_deactivate_inactive_category(self):
        category = Category(
            name=self.name,
            description=self.description,
            is_active=False
        )
        category.deactivate()

        assert category.is_active is False

    def test_deactivate_activate_category(self):
        category = Category(name=self.name, description=self.description)
        category.deactivate()

        assert category.is_active is False