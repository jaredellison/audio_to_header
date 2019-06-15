#include <stdio.h>
#include "sample.h"

int main(int argv, char **argc) {

  for (int i = 0; i < sample_LENGTH; i++) {
    int x = sample[(int)i];
    printf("%d\n", x);
  }

  return 0;
}