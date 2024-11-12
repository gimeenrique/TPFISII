# singleton.py

class SingletonMeta(type):
    """
    Clase de metaclase para implementar el patrón Singleton.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

def test_singleton(instance1, instance2, class_name):
    if instance1 is instance2:
        print(f"{class_name} es un Singleton: ambas instancias son iguales.")
    else:
        print(f"{class_name} NO es un Singleton: las instancias son diferentes.")
