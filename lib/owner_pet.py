# class Pet:
#     PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
#     all=[]
#     def __init__(self,name,pet_type,owner=None):
#         self.name=name
#         self.pet_type=pet_type
#         self.owner=owner
#         Pet.all.append(self)
#     @property
#     def pet_type(self):
#         return self.pet_type
#     @pet_type.setter
#     def pet_type(self,pet_type):
#         if pet_type not in self.PET_TYPES:
#             raise ValueError("Invalid pet type")
#         self._pet_type=pet_type

#     @property
#     def owner(self):
#         return self._owner
#     @owner.setter
#     def owner(self,owner):
#         if not (isinstance(owner,Owner) or not owner):
#             raise Exception("Object is not of type Owner")
#         self._owner=owner




# class Owner:
#     def __init__(self,name):
#         self.name=name
#     def pets(self):
#         return [pet for pet in Pet.all if pet.owner==self]
#     def add_pet(self, pet):
#         if not isinstance(pet,Pet):
#             raise Exception("Input object is not of type Pet")
#         pet.owner=self
#     def get_sorted_pets(self):
#         return sorted(self.pets(),key=lambda pet: pet.name)
        
# Class for Pet with name, pet_type, and owner attributes
# Class for Pet with name, pet_type, and owner attributes
class Pet:
    # List of valid pet types
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    # List of all Pet instances
    all=[]
    def __init__(self,name,pet_type,owner=None):
        # Initialize name and pet_type attributes
        print("Initializing Pet instance")
        self.name=name
        self.pet_type=pet_type
        # Initialize owner attribute
        self.owner=owner
        # Add instance to all list
        Pet.all.append(self)
        print(f"Added Pet instance to all list: {self.name}")
    # Getter for pet_type attribute
    @property
    def pet_type(self):
        print("Getting pet_type attribute")
        return self._pet_type
    # Setter for pet_type attribute
    @pet_type.setter
    def pet_type(self,pet_type):
        # Check if pet_type is valid
        print("Setting pet_type attribute")
        if pet_type not in self.PET_TYPES:
            raise ValueError("Invalid pet type")
        # Set pet_type attribute
        self._pet_type=pet_type
        print(f"Set pet_type to {pet_type}")

    # Getter for owner attribute
    @property
    def owner(self):
        print("Getting owner attribute")
        return self._owner
    # Setter for owner attribute
    @owner.setter
    def owner(self,owner):
        # Check if owner is of type Owner or None
        print("Setting owner attribute")
        if not (isinstance(owner,Owner) or not owner):
            raise Exception("Object is not of type Owner")
        # Set owner attribute]
        self._owner=owner
        print(f"Set owner to {owner.name if owner else 'None'}")

# Class for Owner with name attribute
class Owner:
    def __init__(self,name):
        # Initialize name attribute
        print("Initializing Owner instance")
        self.name=name
    # Method to return all pets owned by this owner
    def pets(self):
        print("Getting pets for this owner")
        return [pet for pet in Pet.all if pet.owner==self]
    # Method to add a pet to this owner
    def add_pet(self, pet):
        print("Adding pet to this owner")
        # Check if input is of type Pet
        if not isinstance(pet,Pet):
            raise Exception("Input object is not of type Pet")
        # Set pet's owner to this owner
        pet.owner=self
        print(f"Added pet {pet.name} to this owner")
    # Method to return all pets owned by this owner, sorted by name
    def get_sorted_pets(self):
        print("Getting sorted pets for this owner")
        return sorted(self.pets(),key=lambda pet: pet.name)

# Example usage:
owner1 = Owner("John")
pet1 = Pet("Fido", "dog")
pet2 = Pet("Whiskers", "cat")
owner1.add_pet(pet1)
owner1.add_pet(pet2)
print(owner1.get_sorted_pets())


        