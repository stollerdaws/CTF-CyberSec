#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>


void read_line(char* buf, size_t bufsize) {
	if(read(STDIN_FILENO, buf, bufsize) == -1) {
		exit(EXIT_FAILURE);
	}
	buf[bufsize-1] = '\0';
	
	char* end = strchr(buf, '\n');
	if(end) {
		*end = '\0';
	}
}

void say(const char* format, ...) {
	va_list ap;
	va_start(ap, format);
	vprintf(format, ap);
	va_end(ap);
	
	usleep(1000*500);
}



typedef struct Dog Dog;
typedef void speak_func(Dog*);

#define DOG_HEAD      1
#define DOG_BACK      2
#define DOG_BELLY     3
#define DOG_LEGS      4
#define DOG_TAIL      5
#define DOG_NUMPARTS  DOG_TAIL

struct Dog {
	char* name;
	speak_func* speak;
	int fleas[DOG_NUMPARTS];
};


void dog1_speak(Dog* dog) {
	say("%s says Woof! %s is a good boy.\n", dog->name, dog->name);
}

void dog2_speak(Dog* dog) {
	say("%s says Meow! %s is a strange dog.\n", dog->name, dog->name);
}

void dog3_speak(Dog* dog) {
	say("%s says:\n", dog->name);
	system(dog->name);
	exit(EXIT_SUCCESS);
}


int main(void) {
	char name1[100], name2[100];
	
	say("Hello. My name is Alice, and I am a veterinarian.\n");
	say("Your name is Bob now. You have two dogs.\n");
	
	Dog* dog1 = calloc(1, sizeof(*dog1));
	dog1->speak = &dog1_speak;
	
	printf("What's your first dog's name?\n");
	read_line(name1, sizeof(name1));
	dog1->name = name1;
	
	say("Okay! Your first dog's name is %s!\n", dog1->name);
	
	Dog* dog2 = calloc(1, sizeof(*dog2));
	dog2->speak = &dog2_speak;
	
	printf("What's your second dog's name?\n");
	read_line(name2, sizeof(name2));
	dog2->name = name2;
	
	say("Wow, %s is a great name for a strange dog!\n", dog2->name);
	
	say("So Bob, you say that your dog %s has fleas.\n", dog1->name);
	printf("Where are %s's fleas?\n", dog1->name);
	printf("[%d] Head\n", DOG_HEAD);
	printf("[%d] Back\n", DOG_BACK);
	printf("[%d] Belly\n", DOG_BELLY);
	printf("[%d] Legs\n", DOG_LEGS);
	printf("[%d] Tail\n", DOG_TAIL);
	
	int flea_location;
	if(scanf("%d", &flea_location) != 1) {
		printf("Error reading input choice!\n");
		exit(EXIT_FAILURE);
	}
	
	if(flea_location < DOG_HEAD) {
		printf("Invalid choice: %d\n", flea_location);
		exit(EXIT_FAILURE);
	}
	
	printf("How many fleas does %s have there?\n", dog1->name);
	
	int flea_count;
	if(scanf("%d", &flea_count) != 1) {
		printf("Error reading flea count!\n");
		exit(EXIT_FAILURE);
	}
	
	dog1->fleas[flea_location-1] = flea_count;
	
	say("Thanks for the information, Bob!\n");
	say("I'll be sure to get that taken care of right away.\n");
	say("\n");
	say("\n"
	    "***************\n"
	    "*One day later*\n"
	    "***************\n");
	say("\n");
	say("*ring ring*\n");
	say("Hey Bob, it's Alice. I just wanted to give you a call "
	    "to let you know that all %d of %s's fleas have been killed.\n", dog1->fleas[flea_location-1], dog1->name);
	say("Also, your dogs are looking forward to seeing you again soon!\n");
	say("See?\n");
	dog1->speak(dog1);
	dog2->speak(dog2);
	say("You can come by my office and pick up your dogs today or tomorrow.\n");
	say("The invoice will be $1337 including tax.\n");
	printf("Have a nice day!\n");
	
	return 0;
}
