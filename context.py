class ConversionContext:
    _question = ""
    _response = ""
    _from_conversion = ""
    _to_conversion = ""
    _quantity = 0
    _parts_of_question = []

    def __init__(self, question) -> None:
        self._question = question

        # Example question -> 1 gallons to pints
        self._parts_of_question = self.get_input().split(" ")
        self._from_conversion = self.get_capitalized(self._parts_of_question[1])
        self._to_conversion = self.get_lowercase(self._parts_of_question[3])
        self._quantity = float(self._parts_of_question[0])
        self._response = self._parts_of_question[0] + " " + self._parts_of_question[1] + " " \
                                                                                         "equals"

    @staticmethod
    def get_capitalized(s: str):
        v = s.capitalize()
        if not v.endswith("s"):
            v = v + "s"
        return v

    @staticmethod
    def get_lowercase(s: str):
        return s.lower()

    def get_input(self):
        return self._question

    def get_from_conversion(self):
        return self._from_conversion

    def get_to_conversion(self):
        return self._to_conversion

    def get_quantity(self):
        return self._quantity

    def get_response(self):
        return self._response

