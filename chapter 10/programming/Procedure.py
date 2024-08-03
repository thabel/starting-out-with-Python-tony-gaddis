class Procedure:
    def __init__(
        self, procedure_name, procedure_date, practitionner_name, charges
    ) -> None:
        self.__procedure_name = procedure_name
        self.__procedure_date = procedure_date
        self.__practitionner_name = practitionner_name
        self.__charges = charges

    def get_procedure_name(self):
        return self.__procedure_name

    def get_procedure_date(self):
        return self.__procedure_date

    def get_practitionner_name(self):
        return self.__practitionner_name

    def get_charges(self):
        return self.__charges

    def set_procedure_name(self, procedure_name):
        self.__procedure_name = procedure_name

    def set_procedure_date(self, procedure_date):
        self.__procedure_date = procedure_date

    def set_practitionner_name(self, practitionner_name):
        self.__practitionner_name = practitionner_name

    def set_charges(self, charges):
        self.__charges = charges

    def __str__(self) -> str:
        return f"""
procedure_name ={self.__procedure_name}, procedure_date ={self.__procedure_date}, practitionner_name ={self.__practitionner_name}, charges ={self.__charges}
                """
