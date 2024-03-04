#include <stdio.h>
#include <string.h>

int main() {
    // Incremented each character of "FSUctf{why_u_50_4ngry_b01_0r_g1rl}" by 1
    char obfuscatedFlag[] = "GTVdug|xiz`v`61`5ohsz`c12`1s`h2sm~";
    char input[100];
    printf("Enter the flag: ");
    scanf("%99s", input);

    // Obfuscate user input for comparison
    for (int i = 0; input[i] != '\0'; i++) {
        input[i] = input[i] + 1; // Increment each character by 1
    }

    if (strcmp(input, obfuscatedFlag) == 0) {
        printf("Correct!\n");
    } else {
        printf("No good.\n");
    }

    return 0;
}

