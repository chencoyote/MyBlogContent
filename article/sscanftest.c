#include <stdio.h>

int main(void){
   
   char text[] = "cpu0   23374 2283 10255 19579488 69434 2 568 822 0 0";
   char cpu[5];
   int num_1 = 0;
   int num_2 = 0;
   int num_3 = 0;
   int num_4 = 0;
   int num_5 = 0;
   int num_6 = 0;
   int num_7 = 0;
   int num_8 = 0;
   int num_9 = 0;
   int num_10= 0;
   

   sscanf( text, "%s %[0-9] ", cpu, &num_1, &num_2);

   printf("%d %d %d %d %d %d %d %d %d %d", num_1, num_2, num_3, \
          num_4, num_5, num_6, num_7,num_8, num_9, num_10);
   return 0;
}
