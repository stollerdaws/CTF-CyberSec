#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>

#define BUFFER_SIZE 256
#define FLAG_SIZE 64

int fd;
char flag_buffer[FLAG_SIZE]; // Global buffer to hold the flag

void open_flag() {
    fd = open("flag.txt", O_RDONLY);
    if (fd < 0) {
        perror("Failed to open flag.txt");
        exit(1);
    }
}

void read_flag() {
    ssize_t bytes_read = read(fd, flag_buffer, FLAG_SIZE - 1);
    if (bytes_read < 0) {
        perror("Failed to read flag");
        exit(1);
    }
    flag_buffer[bytes_read] = '\0'; // Null-terminate the string
}

void print_flag() {
    printf("%s\n", flag_buffer);
}

void vulnerable_function() {
    char buffer[BUFFER_SIZE];
    printf("Enter some text: ");
    gets(buffer); // This is where the buffer overflow can occur
}

int main() {
    vulnerable_function();
    return 0;
}
