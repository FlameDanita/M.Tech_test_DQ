class compress_pyramid_task():
    def __init__(self):
        self.string = ''
        self.new_string = ''
        self.str_pow = 0

    def read_string(self, file_path):
        with open(file_path, 'r') as file:
            self.string = file.read().strip()

    def write_string(self, file_path):
        with open(file_path, 'w') as file:
            file.write(self.string)

    def check_string(self, string):
        str_len = len(string)
        if str_len != 1 and str_len % 4 != 0:
            # Длина строки не является степенью 4-ки
            return False
        else:
            while str_len > 1:
                self.str_pow += 1
                str_len /= 4
            return True

    def compress_pyramid(self, string):
        # Получение данных в пирамиде построчно
        len_current_row = 1
        self.pyramid_arr = []
        while string:
            data_current_row = []
            for _ in range(len_current_row):
                data_current_row.append(string[-1])
                string = string[:-1]

            self.pyramid_arr.append(data_current_row)
            len_current_row += 2

        # Разбиение строк пирамиды на пары 1-3
        spot_flag = True
        self.triangle_arr = []
        for arr in self.pyramid_arr:
            while len(arr) > 0:
                if spot_flag:
                    self.triangle_arr.append(arr[-1:])
                    arr = arr[:-1]
                else:
                    self.triangle_arr.append(arr[-3:])
                    arr = arr[:-3]
                spot_flag = not spot_flag

        # Слияние строк по 4 элемента в ряд
        merge_count = 1
        self.merget_triangle = []
        while self.triangle_arr:
            tmp_arr = []
            for j in range(merge_count):
                self.triangle_arr[0].extend(self.triangle_arr[merge_count - j])
                tmp_arr.append(self.triangle_arr[0])
                del self.triangle_arr[merge_count - j], self.triangle_arr[0]
            for arr in tmp_arr[::-1]:
                self.merget_triangle.append(arr)
            merge_count += 2
        self.merget_triangle = self.merget_triangle[::-1]

        # Объединение треугольников из одинаковых элементов
        new_string = ''
        for elem in self.merget_triangle:
            if elem.count(elem[0]) == 4:
                new_string += elem[0]
            else:
                for el in elem:
                    new_string += el

        return new_string

    def compress_process(self):
        while self.check_string(self.string) and len(self.string) > 4:
            # self.print_pyramid(self.string)
            self.new_string = self.compress_pyramid(self.string)
            
            if len(self.string) == len(self.new_string):
                break
            else:
                self.string = self.new_string

        # if self.check_string(self.string):
        #     self.print_pyramid(self.string)

    def print_pyramid(self, string):
        len_current_row = 1
        print("{: ^64}".format("^"))

        while string:
            data_current_row = []
            for _ in range(len_current_row):
                data_current_row.append(string[-1])
                string = string[:-1]

            printed_string = ''
            for i in range(len(data_current_row)):
                if i % 2 == 0:
                    printed_string += '/' + data_current_row[i]
                else:
                    printed_string += '\\' + data_current_row[i]
            printed_string += '\\'
            print("{: ^64}".format(printed_string))

            delemetr_string = ''
            for i in range(len(printed_string) + 2):
                if i % 4 == 0:
                    delemetr_string += '*'
                else:
                    delemetr_string += '-'
            print("{: ^64}".format(delemetr_string))
            len_current_row += 2
        print()

    def get_examples(self):
        self.ex_1 = 'a'
        self.ex_2 = 'abcd'
        self.ex_3 = 'aaabcccabbbcdddd'
        self.ex_4 = 'aaaaaaabcccccccaaaaabbbcccccaaabbbbbcccabbbbbbbcdddddddddddddddd'
        self.ex_5 = 'abcdefghijklmnop'

if __name__ == "__main__":
    task = compress_pyramid_task()
    task.get_examples()

    task.read_string('input.txt')
    task.compress_process()
    task.write_string('output.txt')