class compress_pyramid_task():
    def __init__(self):
        pass

    def read_string(self, file_path):
        with open(file_path, 'r') as file:
            self.string = file.read().strip()

    def write_string(self, file_path):
        with open(file_path, 'w') as file:
            file.write(self.string)

    def check_string(self, str):
        if self.get_len_and_pow(str):
            print("Строка валидна")
            print("Длина строки =", self.str_len)
            print("Степень 4-ки =", self.str_pow)
            return True
        else:
            print("Длина строки не является степенью 4-ки")
            return False
        
    def get_len_and_pow(self, string):
        self.str_len = len(string)
        self.str_pow = 0
        tmp_str_len = self.str_len

        if self.str_len != 1 and self.str_len % 4 != 0:
            return False
        else:
            while tmp_str_len != 1:
                self.str_pow += 1
                tmp_str_len /= 4
            return True

    def compress_pyramid(self, string):
        self.pyramid_arr = []
        self.triangle_arr = []
        row_counter = 0
        spot_flag = True

        current_row = 1
        while string:
            row_string = []
            for _ in range(current_row):
                row_string.append(string[-1])
                string = string[:-1]

            self.pyramid_arr.append(row_string)

            current_row += 2

        for arr in self.pyramid_arr:
            while len(arr) > 0:
                if spot_flag:
                    self.triangle_arr.append(arr[-1:])
                    arr = arr[:-1]
                else:
                    self.triangle_arr.append(arr[-3:])
                    arr = arr[:-3]

                spot_flag = not spot_flag

        merge_count = 1
        self.merget_triangle = []
        while self.triangle_arr:
            tmp_arr = []
            for j in range(merge_count):
                self.triangle_arr[0].extend(self.triangle_arr[merge_count - j])
                tmp_arr.append(self.triangle_arr[0])
                del self.triangle_arr[merge_count - j]
                del self.triangle_arr[0]

            for arr in tmp_arr[::-1]:
                self.merget_triangle.append(arr)
            

            merge_count += 2

        self.new_string = ''
        self.merget_triangle = self.merget_triangle[::-1]
        for elem in self.merget_triangle:
            if elem.count(elem[0]) == 4:
                self.new_string += elem[0]
            else:
                for el in elem:
                    self.new_string += el

        return self.new_string
        
    def print_separate_pyramid(self):
        pass

    def print_pyramid(self, string):
        self.get_len_and_pow(string)

        current_row = 1
        print("{: ^64}".format("^"))

        while string:
            row_string = []
            for _ in range(current_row):
                row_string.append(string[-1])
                string = string[:-1]

            print_string = ''
            for i in range(len(row_string)):
                if i % 2 == 0:
                    print_string += '/' + row_string[i]
                else:
                    print_string += '\\' + row_string[i]
            print_string += '\\'
            print("{: ^64}".format(print_string))

            delemetr_string = ''
            for i in range(len(print_string) + 2):
                if i % 4 == 0:
                    delemetr_string += '*'
                else:
                    delemetr_string += '-'
            print("{: ^64}".format(delemetr_string))

            current_row += 2



    def get_examples(self):
        self.ex_1 = 'a'
        self.ex_2 = 'abcd'
        self.ex_3 = 'aaabcccabbbcdddd'
        self.ex_4 = 'aaaaaaabcccccccaaaaabbbcccccaaabbbbbcccabbbbbbbcdddddddddddddddd'
        self.ex_5 = 'aaaaaaabcccccccaaaaabbbcccccaaabbbbbcccabbbbbbbcddddddddddddddddaaaaaaabcccccccaaaaabbbcccccaaabbbbbcccabbbbbbbcddddddddddddddddaaaaaaabcccccccaaaaabbbcccccaaabbbbbcccabbbbbbbcddddddddddddddddaaaaaaabcccccccaaaaabbbcccccaaabbbbbcccabbbbbbbcdddddddddddddddd'
        self.ex_6 = 'abcdefghijklmnop'

    def get_info(self):
        pass
    
    def compress_process(self):
        # self.get_info()
        while self.check_string(self.string) and len(self.string) > 4:
            self.print_pyramid(self.string)
            self.string = self.compress_pyramid(self.string)


if __name__ == "__main__":
    task = compress_pyramid_task()
    task.get_examples()

    task.read_string('input.txt')
    task.compress_process()
    task.write_string('output.txt')