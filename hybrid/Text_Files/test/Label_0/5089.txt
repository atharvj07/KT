#include <bits/stdc++.h>
#pragma GCC optimize(3)
using namespace std;
bool Finish_read;
template <class T>
inline void read(T &x) {
  Finish_read = 0;
  x = 0;
  int f = 1;
  char ch = getchar();
  while (!isdigit(ch)) {
    if (ch == '-') f = -1;
    if (ch == EOF) return;
    ch = getchar();
  }
  while (isdigit(ch)) x = x * 10 + ch - '0', ch = getchar();
  x *= f;
  Finish_read = 1;
}
template <class T>
inline void print(T x) {
  if (x / 10 != 0) print(x / 10);
  putchar(x % 10 + '0');
}
template <class T>
inline void writeln(T x) {
  if (x < 0) putchar('-');
  x = abs(x);
  print(x);
  putchar('\n');
}
template <class T>
inline void write(T x) {
  if (x < 0) putchar('-');
  x = abs(x);
  print(x);
}
int cnt[26];
char s[100005];
int main() {
  scanf("%s", s + 1);
  int n = strlen(s + 1);
  for (int i = 1; i <= n; i++) cnt[s[i] - 'a']++;
  vector<int> now;
  for (int i = 0; i < 26; i++)
    if (cnt[i]) now.push_back(cnt[i]);
  if (now.size() < 2 || now.size() > 4) {
    puts("No");
    return 0;
  }
  if (now.size() == 4) {
    puts("Yes");
    return 0;
  }
  sort(now.begin(), now.end());
  if (now.size() == 3) {
    if (now[now.size() - 1] > 1)
      puts("Yes");
    else
      puts("No");
    return 0;
  }
  if (now.size() == 2) {
    if (now[0] >= 2 && now[1] >= 2)
      puts("Yes");
    else
      puts("No");
    return 0;
  }
  puts("No");
  return 0;
}
