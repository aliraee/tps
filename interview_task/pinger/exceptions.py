class InvalidIPExeption(Exception):
    def __init__(self, message):
        self.message = f'InvalidIPExeption {message}'
        super().__init__(self.message)
