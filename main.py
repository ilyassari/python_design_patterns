patterns = {
    1: 'Singleton Pattern',
    2: 'Factory Pattern',
    3: 'Observer Pattern',
    4: 'Builder Pattern',
    5: 'Prototype Pattern',
    6: 'Decorator Pattern',
    7: 'Strategy Pattern',
    8: 'Template Method Pattern',
    9: 'Adapter Pattern', 
    10: 'Iterator Pattern',
    11: 'Facade Pattern',
    12: 'Orchestrator Pattern',
    13: 'State Pattern',
    14: 'Proxy Pattern',
    15: 'Composite Pattern',
    16: 'Mediator Pattern'
}

# change selection according to patterns
selection = 4

match selection:
    case 1:
        from singleton import Singleton

        # Create first instance
        instance1 = Singleton()

        # Create another instance
        instance2 = Singleton()

        # Check instance1 and instance2 are same
        print(instance1 is instance2)  

    case 2:
        from factory import AnimalFactory

        animal_factory = AnimalFactory()

        # Create first instance
        instance1 = animal_factory.create_animal("dog")

        # Create another instance
        instance2 = animal_factory.create_animal("cat")

        # Check their speak
        print('instance1:\t', instance1.speak())
        print('instance2:\t', instance2.speak())

    case 3:
        from observer import Subject, ConcreteObserver
        
        # Create Main Object
        subject = Subject()

        # Create Observers
        observer1 = ConcreteObserver()
        observer2 = ConcreteObserver()
        observer3 = ConcreteObserver()

        # Attach Observers
        subject.attach(observer1)
        subject.attach(observer2)
        subject.notify("Hello observers!")
        print("")
        
        # Attach Observer
        subject.attach(observer3)
        subject.notify("Hello observers!")

    case 4:
        from builder import Director, ConcreteBuilder

        # Create Builder and Director
        builder = ConcreteBuilder()
        director = Director(builder)

        # Construct Product
        director.construct('part1', 'part2', 'extra1', 'extra2')
        product = builder.get_result()

        print(product)

    case _:
        try:
            print(f'{patterns[selection]} is not ready, yet')
        except KeyError:
            print('Key Error:', selection)
