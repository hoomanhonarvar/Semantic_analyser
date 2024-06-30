// Function with incorrect return type
char greet() {
    print("Hello, world!\n");
    return "Hello" ; // Error: Cannot return a string literal
}

// Function with incorrect parameter type
bool printNumber(char num) {
    num = 'd' ;
    print("Number: %d\n" , num);  // Error: Incorrect format specifier for char
}

int main() {
    // Variable declarations
    int x, y;
    char z;
    bool flag;  // Error: 'bool' is not a standard type in C

    // Array declaration
    int arr[10];  // Correct array declaration

    // Multiple variables of the same type separated by comma
    int a, b, c;  // Correct multiple variables of the same type

    // Incorrect variable declaration
    int d, e, f;  // Error: Extra comma

    // Conditional statements
    x = 10;
    y = 5;

    if (x > y) {
        print("x is greater than y\n");
    } else
        print("x is less than or equal to y\n");  // Error: Missing braces for else part

    // Unmatched if-else structure
    if (x > y) {
        print("x is greater than y\n");
    } else
        if (x < y)
            print("x is less than y\n");  // Error: Missing braces for else-if part

    // Incorrect syntax for if statement
    if (x > y) {
        print("x is greater than y\n");  // Error: Missing parentheses and braces
    }

    // For loop
    for (int i = 0 ; i < 10 ; i = i + 1)
        print("%d ", i);  // Error: Missing braces for loop body

    // Infinite loop
    int j = 0 ;
    // Incorrect usage of continue
    for (int k = 0 ; k < 10 ; k= k + 1)
        continue;  // Error: continue outside of loop

    // Printing integer
    int num = 10;
    print("Number: %d\n", num);

    // Printing character
    char ch = 'A';
    print("Character: %c\n", ch);

    // Incorrect format specifier for string
    char str [ 0 ] = "Hello, world!";
    print("String: %d\n", str);  // Error: Incorrect format specifier for string

    // Function calls with errors
    greet();
    printNumber(3);  // Error: Character '5' instead of integer

    return 0 ;
}