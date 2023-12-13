**Python**

Дана строка длины N, где N - целое число, степень 4. Элементами строки являются латинские маленькие буквы от "a" до "z".

Строка может быть записана в виде пирамиды.

Например, строка "a" может быть записана в виде:

    ^
   /a\
  *---*

строка "abcd" в виде:

      ^
     /d\
    *---*
   /c\b/a\
  *---*---*

строка "abcdefghijklmnop" в виде:

          ^
         /p\
        *---*
       /o\n/m\
      *---*---*
     /l\k/j\i/h\
    *---*---*---*
   /g\f/e\d/c\b/a\
  *---*---*---*---*

и так далее.

Пирамида размером более 4 элементов может быть представлена в виде нескольких пирамид по 4 элемента.

Например, пирамида:

          ^
         /p\
        *---*
       /o\n/m\
      *---*---*
     /l\k/j\i/h\
    *---*---*---*
   /g\f/e\d/c\b/a\
  *---*---*---*---*

может быть представлена в виде 4х пирамид:
               ^
              /p\
             *---*
            /o\n/m\
           *---*---*

      *    *---*---*    *
     /l\    \k/j\i/    /h\
    *---*    *---*    *---*
   /g\f/e\    \d/    /c\b/a\
  *---*---*    *    *---*---*

Пирамида из 64 элементов разбивается на

                               ^
                              / \
                             *---*
                            / \ / \
                           *---*---*

                      *    *---*---*    *
                     / \    \ / \ /    / \
                    *---*    *---*    *---*
                   / \ / \    \ /    / \ / \
                  *---*---*    *    *---*---*

             *    *---*---*    *    *---*---*    *
            / \    \ / \ /    / \    \ / \ /    / \
           *---*    *---*    *---*    *---*    *---*
          / \ / \    \ /    / \ / \    \ /    / \ / \
         *---*---*    *    *---*---*    *    *---*---*

    *    *---*---*    *    *---*---*    *   *---*---*    *
   / \    \ / \ /    / \    \ / \ /    / \    \ / \ /    / \
  *---*    *---*    *---*    *---*    *---*    *---*    *---*
 / \ / \    \ /    / \ / \    \ /    / \ / \    \ /    / \ / \
*---*---*    *    *---*---*    *    *---*---*    *    *---*---*

И так далее.

Если все элементы внутри пирамиды из 4-х элементов одинаковые, то пирамида может быть сжата до одного элемента:

      ^
     /a\                ^
    *---*      ->      /a\
   /a\a/a\            *---*
  *---*---*

Пирамида размером более 4-х элементов может быть сжата, если сжимаются все 4-х элементные пирамиды, из которых она состоит.


          ^
         /a\
        *---*                 ^
       /a\a/a\               /a\
      *---*---*      ->     *---*
     /b\c/c\c/d\           /b\c/d\
    *---*---*---*         *---*---*
   /b\b/b\c/d\d/d\
  *---*---*---*---*

К полученной пирамиде можно снова попробовать применить операцию сжатия.

Необходимо написать программу на языке программирования Python, сжимающую пирамиду до самого маленького размера и вывести ее строковое представление.
Исходная строка находится в файле input.txt
Результирующую строку необходимо записать в файл output.txt

Критерии оценки:
1. Программа должна работать правильно.
2. Код должен легко читаться и обслуживаться.
3. Код не должен включать в себе лишнюю функциональность, а делать только то, что требуется в задаче.
4. Код должен быть оформлен по PEP8.
5. В реализации должно быть использовано ООП.


Пример 1:

input.txt
a
output.txt
a

Пример 2:

input.txt
abcd
output.txt
abcd

Пример 3:

input.txt
aaabcccabbbcdddd
output.txt
abcd

Пример 4:

input.txt
aaaaaaabcccccccaaaaabbbcccccaaabbbbbcccabbbbbbbcdddddddddddddddd
output.txt
abcd