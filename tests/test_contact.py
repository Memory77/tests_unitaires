import pytest 
from source.contact import Contact

#definir une usine a contact à la place d'instancier plusieurs contact
@pytest.fixture
def contact_factory():
    def create_contact(name,age):
        return Contact(name=name, age=age)
    return create_contact

def test_contact_greeting(contact_factory):
    contact = contact_factory("John Doe", 30)
    assert contact.greet() == "Hello, my name is John Doe, and I have 30 years old."

def test_contact_underage(contact_factory):
    contact = contact_factory("Jane Doe", 17)
    assert contact.age < 18

def test_contact_adult(contact_factory):
    contact = contact_factory("Bob Smith", 25)
    assert contact.age >= 18