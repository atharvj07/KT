#include <bits/stdc++.h>
using namespace std;
int a[111];
int ok(char ch) {
  if (ch == 'A') return 100;
  if (ch == 'B') return 10;
  if (ch == 'C') return 1;
  return 0;
}
int main(int argc, char const *argv[]) {
  ios::sync_with_stdio(false);
  cin.tie(0);
  char s[111];
  cin >> s;
  for (int i = 0; s[i] != '\0'; i++) {
    if (s[i] != '.') {
      for (int j = -1; j <= 1; j++) {
        if (i + j >= 0) {
          a[i + j] += ok(s[i]);
        }
      }
    }
  }
  for (int i = 0; s[i] != '\0'; i++) {
    if (a[i] == 111) {
      cout << "yes\n";
      return 0;
    }
  }
  cout << "no\n";
  return 0;
}
