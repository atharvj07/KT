#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 5;
bool cmax(int &a, int b) { return (a < b) ? a = b, 1 : 0; }
bool cmin(int &a, int b) { return (a > b) ? a = b, 1 : 0; }
template <typename T>
T read() {
  T ans = 0, f = 1;
  char ch = getchar();
  while (!isdigit(ch) && ch != '-') ch = getchar();
  if (ch == '-') f = -1, ch = getchar();
  while (isdigit(ch))
    ans = (ans << 3) + (ans << 1) + (ch - '0'), ch = getchar();
  return ans * f;
}
void file() {}
int n, dep[N];
int same;
void input() {
  n = read<int>();
  for (register int i = (int)1; i <= (int)n + 1; ++i) {
    dep[i] = read<int>();
    if (dep[i] > 1 && dep[i - 1] > 1) same = i;
  }
}
void work() {
  int old = 0, now = 0;
  if (!same) {
    puts("perfect");
    return;
  }
  puts("ambiguous");
  for (register int i = (int)1; i <= (int)n + 1; ++i) {
    for (register int j = (int)1; j <= (int)dep[i]; ++j) {
      now++;
      printf("%d ", old);
    }
    old = now;
  }
  printf("\n");
  old = now = 0;
  for (register int i = (int)1; i <= (int)n + 1; ++i) {
    for (register int j = (int)1; j <= (int)dep[i]; ++j) {
      now++;
      if (i == same) {
        printf("%d ", old - 1);
        same = 0;
      } else
        printf("%d ", old);
    }
    old = now;
  }
}
int main() {
  file();
  input();
  work();
  return 0;
}
