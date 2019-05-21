class NumbersToMonth(object):

    def numbers_to_months(self, argument):
        """Dispatch method"""
        method_name = 'month_' + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid month")
        # Call the method as we return it
        return method()

    # Define methods which return name of month
    def month_1(self):
        return "janurary"

    def month_2(self):
        return "february"

    def month_3(self):
        return "march"

    def month_4(self):
        return "april"

    def month_5(self):
        return "may"

    def month_6(self):
        return "june"

    def month_7(self):
        return "july"

    def month_8(self):
        return "august"

    def month_9(self):
        return "september"

    def month_10(self):
        return "october"

    def month_11(self):
        return "november"

    def month_12(self):
        return "december"
