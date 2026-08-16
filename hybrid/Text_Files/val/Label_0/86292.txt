#include <stdio.h>
#include <string>
#include <map>
int main(void) {
  char type[3];
  int _tmp;
  std::map<std::string, int> m;

  m["A"] = 0;
  m["B"] = 0;
  m["0"] = 0;
  m["AB"] = 0;

  while(scanf("%d,%s", &_tmp, type) != EOF) {
    m[type] += 1;
  }

  printf("%d\n%d\n%d\n%d\n", m["A"], m["B"], m["AB"], m["O"]);
  return 0;
}