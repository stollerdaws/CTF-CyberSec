#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    // The encoded flag as a list of integers, each XOR'd with 'X' and converted to decimal
    int encoded_flag[] = {30, 11, 13, 59, 44, 62, 35, 10, 107, 46, 107, 10, 109, 107, 7, 10, 107, 46, 107, 42, 109, 107, 7, 104, 54, 107, 7, 16, 104, 8, 7, 111, 16, 105, 109, 7, 111, 105, 53, 107, 37};
    int flag_len = sizeof(encoded_flag) / sizeof(encoded_flag[0]);
    char decoded_flag[flag_len + 1]; // +1 for the null terminator

    // Decode the flag by XOR'ing with 'X'
    for (int i = 0; i < flag_len; i++) {
        decoded_flag[i] = encoded_flag[i] ^ 'X';
    }
    decoded_flag[flag_len] = '\0'; // Null-terminate the decoded string
    // Prompt the user to enter the flag
    char user_input[256]; // Buffer for user input
    printf("Enter the flag: ");
    fgets(user_input, sizeof(user_input), stdin);
    user_input[strcspn(user_input, "\n")] = 0; // Remove newline character if present

    // Compare the user input against the decoded flag
    if (strcmp(user_input, decoded_flag) == 0) {
        printf("Correct flag!\n");
    } else {
        printf("Incorrect flag. Try again.\n");
    }

    return 0;
}
