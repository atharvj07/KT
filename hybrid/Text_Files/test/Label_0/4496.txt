#include <bits/stdc++.h>
using namespace std;
char cad[102], cad2[102];
int day[2002];
int main() {
  int d, n;
  scanf("%d%d", &d, &n);
  int g = 0;
  for (int i = 0; i < (int)(d); ++i) {
    scanf("%d", &day[i]);
  }
  for (int i = 0; i < (int)(d); ++i) {
    for (int j = i; j <= (int)(d); ++j) {
      g = max(g, (n / day[i]) * day[j] + n % day[i]);
    }
  }
  printf("%d", g);
  return 0;
}
