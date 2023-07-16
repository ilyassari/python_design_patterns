patterns = {
    1: {
        'group': 'Creational patterns',
        'patterns': {
            1: 'Singleton Pattern',
            2: 'Factory Pattern',
            3: 'Abstract Factory Pattern',
            4: 'Prototype Pattern',
            5: 'Builder Pattern'
        }
    },
    2: {
        'group': 'Structural patterns',
        'patterns': {
            1: 'Adapter Pattern', 
            2: 'Bridge Pattern', 
            3: 'Composite Pattern',
            4: 'Decorator Pattern',
            5: 'Facade Pattern',
            6: 'Proxy Pattern'
        }
    },
    3: {
        'group': 'Behavioral patterns',
        'patterns': {
            1: 'Observer Pattern',
            2: 'Strategy Pattern',
            3: 'Command Pattern',
            4: 'Iterator Pattern',
            5: 'Mediator Pattern',
            6: 'Template Method Pattern',
            7: 'Visitor Pattern',
            8: 'State Pattern',
            9: 'Chain of Responsibility Pattern',
            10: 'Memento Pattern',
            11: 'Interpreter Pattern'
        }
    }
}

# change selection according to patterns
selection = {
    'group': 3,
    'pattern': 1
}

match selection['group']:
    case 1: # Creational patterns
        match selection['pattern']:
            case 1:
                from creational import Singleton

                # Create first instance
                instance1 = Singleton()

                # Create another instance
                instance2 = Singleton()

                # Check instance1 and instance2 are same
                print(instance1 is instance2)  

            case 2:
                from creational import AnimalFactory

                animal_factory = AnimalFactory()

                # Create first instance
                instance1 = animal_factory.create_animal("dog")

                # Create another instance
                instance2 = animal_factory.create_animal("cat")

                # Check their speak
                print('instance1:\t', instance1.speak())
                print('instance2:\t', instance2.speak())

            case 3: # Abstract Factory Pattern
                pass

            case 4: # Prototype Pattern
                pass

            case 5: # Builder Pattern
                from creational import Director, ConcreteBuilder

                # Create Builder and Director
                builder = ConcreteBuilder()
                director = Director(builder)

                # Construct Product
                director.construct('part1', 'part2', 'extra1', 'extra2')
                product = builder.get_result()

                print(product)

            case _:
                print('Wrong Pattern')

    case 2: # Structural patterns
        match selection['pattern']:
            case 1: # Adapter Pattern
                pass

            case _:
                print('Wrong Pattern')

    case 3: # Behavioral patterns
        match selection['pattern']:
            case 1: # Observer Pattern
                from behavioral import Subject, ConcreteObserver
                
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
            case _:
                print('Wrong Pattern')
    case _:
        print('Wrong Pattern Group')
