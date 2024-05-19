class ServiceDescriptor:
    def __init__(self, type, implementation, factory):
        self.type = type
        self.implementation = implementation
        self.factory = factory

class Container:
    collection: list[ServiceDescriptor] = []

    def register(self, type, implementation, factory) -> None:
        self.collection.append(ServiceDescriptor(type, implementation, factory))

    def get_service(self, type) -> type:
        descriptor = list(filter(lambda x : x.type == type, self.collection))

        if len(descriptor) == 0:
            raise Exception(f"No service of type {type} found")
        
        if descriptor[0].implementation is not None:
            return descriptor[0].implementation
        
        return descriptor[0].factory()
    
    
container_instance = Container()

def get_container():
    return container_instance