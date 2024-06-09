from dataclasses import dataclass,field
from uuid import uuid4, UUID

@dataclass
class Category:
    name: str
    description: str = ""
    is_active: bool = True
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self):
        self.validate()

    def validate(self):
        if not self.name:
            raise ValueError("name can not be empty or null")

        if len(self.name) > 255:
            raise ValueError("name can not be longer than 255 characters")

    def update_name_and_description(self, name, description):
        self.name = name
        self.description = description

        self.validate()

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False
