#include <stdio.h>
#include <conio.h>

int main() {
  unsigned int a;
  unsigned int zero = 0;
  int count = 0;
  scanf("%u",&a);
  while(a!=0) {
    if (a&1 == 1) {
      zero |= 1;
    }
    count += 1;
    if(count != 31){
      zero <<= 1;
    }
    a >>= 1;
  }
  zero <<= (31-count);
  printf("%u",zero);
  return 0;
}
