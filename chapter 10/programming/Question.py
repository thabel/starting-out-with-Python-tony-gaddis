class Question:
    def __init__(
        self, trivia_question: str, answers: tuple[str], correct_answer_index: int
    ) -> None:
        """
        answers: must be 4 potential answer

        """
        
        if len(answers) == 4:     
            self.__trivia_question = trivia_question
            self.__answers = answers
            self.__correct_answer_index = correct_answer_index
        else:
            raise Exception(f"Can not initiate object because there are only {len(answers)} answers instead of 4.")
    # accessors
    def get_trivia_question(self):
        return self.__trivia_question

    def get_answers(self):
        return self.__answers

    def get_correct_answer_index(self):
        return self.__correct_answer_index

    # mutator
    def set_trivia_question(self, trivia_question):
        self.__trivia_question = trivia_question

    def set_answers(self, answers):
        self.__answers = answers

    def set_correct_answer_index(self, correct_answer_index):
        self.__correct_answer_index = correct_answer_index

    def display_answers(self):
        for i , answer in enumerate(self.__answers):
            print(" {:<4}  {:<15}".format(i,answer))
    
    def is_answered_correctly(self,index):
        return self.__correct_answer_index == index
    
    def get_correct_answer(self):
        return self.__answers[self.__correct_answer_index]