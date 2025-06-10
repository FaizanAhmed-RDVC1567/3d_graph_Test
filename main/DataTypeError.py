class DataTypeError(TypeError):
    """
    A custom exception class for data type mismatches that carries a bit more context. It extends the superclass
    'TypeError' and provides specific information about the error that was raised.
    """
    def __init__(self, message, data_object, expected_type, received_type, error_code=None):
        """
        The constructor for this class that requires a minimum of three arguments to be thrown, however a fourth
        parameter can also be specified. The first parameter should be of type *str* that describes the error where it
        was raised, the second and third parameters should be the *type* of data that was expected and received, respectively.
        For example, if the expected value was an int with value *25* but the received value was given as *"25"*; using
        the in-built *type* function would return *int* and *str* for these values. The last parameter is an optional
        parameter that should be of type *int* when supplied during initialization, that allows quicker identification
        of a developer's error.
        :param message: The message to be displayed when the error is raised by specific code.
        :param data_object: The exact instance of the object in memory that caused an exception to occur.
        :param expected_type: The type of the data that a method or function expects when said method or function is called.
        :param received_type: The type of the data that was actually received by the method or function, that caused the error to be raised.
        :param error_code: A custom integer value that can be set when the error is raised, to identify the type of error.
        """
        # Initialise the base TypeError with the error message.
        super().__init__(message)

        # Explicitly check the type of data received by the constructor before constructing the exception.
        if error_code is not None:
            if not isinstance(error_code, int):
                raise TypeError(f"Error: 'error_code' must be an integer, but got {type(error_code)}")

        if not isinstance(received_type, type(data_object)):
            raise TypeError("Error: The 'type' of the received object, and the object that caused the error do not "
                            "match")

        # Store additional properties
        self.expected_type = expected_type
        self.received_type = received_type
        self.error_code = error_code

    def __str__(self):
        # Override __str__ to provide a rich error message when the exception is printed
        base_message = super().__str__()
        return (f"{base_message} | Expected: {self.expected_type}, Received: {self.received_type}" +
                f"\nError Code: {self.error_code if self.error_code is not None else ""} ")
