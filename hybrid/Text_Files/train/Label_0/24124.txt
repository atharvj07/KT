#include <bits/stdc++.h>
using namespace std;
int n;
string s;
bool f = false;
bool l = false;
long long res = 0;
int main() {
  scanf("%d", &n);
  cin >> s;
  res = (long long)n * (n - 1) / 2;
  for (int i = 0; i < n; i++) {
    char c = s[i];
    int j = i + 1;
    int br = 0;
    while (j < n && s[j] != c) {
      br++;
      j++;
    }
    res -= br;
    br = 0;
    j = i - 1;
    while (j >= 0 && s[j] != c) {
      br++;
      j--;
    }
    if (br != 0) {
      br--;
    }
    res -= br;
  }
  cout << res;
  return 0;
}
