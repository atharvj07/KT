#include <bits/stdc++.h>
int main(void) {
  int Count, Number;
  char E[5];
  scanf("%d", &Number);
  gets(E);
  char String[Number + 1];
  gets(String);
  for (Count = 0; Count < Number; Count++) {
    if (String[Count] != 'a' && String[Count] != 'e' && String[Count] != 'i' &&
        String[Count] != 'o' && String[Count] != 'u' && String[Count] != 'y')
      printf("%c", String[Count]);
    else {
      if (String[Count] != String[Count - 1]) printf("%c", String[Count]);
      if ((String[Count] == 'e' || String[Count] == 'o') &&
          String[Count - 1] == String[Count] &&
          String[Count - 2] != String[Count] &&
          String[Count + 1] != String[Count])
        printf("%c", String[Count]);
    }
  }
  printf("\n");
  return 0;
}
