# Pickle investigation

How can an instance of a class with a reference to an external function be dumped using pickle?

The straightforward approach is to dump only the instance. However, reproducing the external function in the scope of loading the instance is required; otherwise, an `AttributeError` exception will be raised. For instance, the error message "Can't get attribute 'function_b' on <module 'main' ..." will be displayed.

For example, the `Vectorizer` class has references to `function_a` and `function_b`. When an instance of this class is dumped in `use_objects.py`, the aforementioned exception is raised because `function_a` and `function_b` are not defined.

The proposed solution is to use a wrapper class that implements the required functions as static methods, for example `WrappedVectorizer`. This class needs to be imported into the scope before loading the dump as well. The benefit of using this solution is that the logic is encapsulated into a single class. And in this case  `use_objects.py` can load a dumped instance and execute its method successfully. 