#include <stdio.h>
#include <string.h>

void mysterious_shift(char *input) {
    for (int i = 0; input[i] != '\0'; i++) {
        if ((input[i] >= 'A' && input[i] <= 'Z') || (input[i] >= 'a' && input[i] <= 'z')) {
            char base = (input[i] >= 'a') ? 'a' : 'A';
            input[i] = (((input[i] - base + 13) % 26) + base);
        }
    }
}

int main() {
    char flag_input[50];
    // Assuming the correct decryption of "SFHpgs{7nX3_17_8npX_a0J_lnYY}" is provided as the actual flag
    char encrypted_blocks[][11] = {"SFHpg", "s{7nX", "3_17_", "8npX_", "a0J_l", "nYY}"};
    char decrypted_flag[50] = "";
    
    // Decrypt each block and assemble the decrypted flag
    for (int i = 0; i < sizeof(encrypted_blocks) / sizeof(encrypted_blocks[0]); i++) {
        mysterious_shift(encrypted_blocks[i]);
        strcat(decrypted_flag, encrypted_blocks[i]);
    }

    printf("Enter the flag: ");
    scanf("%49s", flag_input);

    // Check if the entered flag is correct
    if (strcmp(flag_input, decrypted_flag) == 0) {
        printf("Correct flag!\n");
    } else {
        printf("Incorrect flag. Try again.\n");
    }

    return 0;
}
