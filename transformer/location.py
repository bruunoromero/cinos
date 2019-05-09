class CNSLocation:
    def __init__(self, token):
        self.__line_start = token.line
        self.__line_end = token.end_line
        self.__column_start = token.column
        self.__column_end = token.end_column
