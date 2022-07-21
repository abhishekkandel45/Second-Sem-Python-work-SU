// To Print the following pattern:
//              A
//             AAA
//            AAAAA
//           AAAAAAA

#include<stdio.h>
void main() {
  int m = 1;
  int p_height = 4;
  int p_space = p_height - 1;
  int i, j, k;
  for (i = 0; i < p_height; i++) {
    for (j = p_space; j > i; j--) {
      printf(" ");
    }
    for (k = 0; k < m; k++) {
      printf("A", i);
    }
    m += 2;
    printf("\n");
  }
}