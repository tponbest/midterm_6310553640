class MidtermChatBot:
    def showSubjectName(self):
        print("AI for robot system")

    def showStudentYear(self, student_id):
        try:
            student_id = int(student_id)
            year = 67 - (student_id // 100000000)
            print(f"{year}")
        except ValueError:
            print("error")

    def calculator(self, operator, operand1, operand2):
        try:
            operand1 = int(operand1)
            operand2 = int(operand2)
            if operator == '+':
                result = operand1 + operand2
            elif operator == '-':
                result = operand1 - operand2
            elif operator == '*':
                result = operand1 * operand2
            print(f"{result}")
        except ValueError:
            print("error")
    
    def main(self):
        while True:
            command = input("")
            if command == 'subject':
                self.showSubjectName()
            elif command == 'year':
                student_id = input("")
                self.showStudentYear(student_id)
            elif command == 'calc':
                operator = input("")
                operand1 = input("")
                operand2 = input("")
                self.calculator(operator, operand1, operand2)

if __name__ == '__main__':
    chatbot = MidtermChatBot()
    chatbot.main()
