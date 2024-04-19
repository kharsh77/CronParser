from components.time_component import TimeComponent

class YearComponent(TimeComponent):
    NUMERAL_RANGE=[2023,2030]
    def __init__(self, current_expression):
        TimeComponent.__init__(self, numeral_range=YearComponent.NUMERAL_RANGE)
        super().parse(current_expression)
        
    def get_values(self):
        return ["Year", super().get_values()]
