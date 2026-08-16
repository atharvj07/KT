#include <bits/stdc++.h>
using namespace std;
int n, cnt, ok = -1;
int sign[1003], p[1003], letter[26];
string second;
void prime_gen() {
  p[2] = 1;
  for (int i = 3; i <= 1000; i += 2) {
    p[i] = 1;
  }
  for (int i = 3; i <= 1000; i += 2) {
    if (p[i]) {
      for (int j = i * i; j <= 1000; j += (2 * i)) {
        p[j] = 0;
      }
    }
  }
}
int main() {
  ios_base::sync_with_stdio(false);
  prime_gen();
  cin >> second;
  n = second.size();
  for (int i = 0; i < n; i++) {
    letter[second[i] - 'a']++;
  }
  for (int i = 2; i <= n / 2; i++) {
    if (p[i]) {
      for (int j = i; j <= n; j += i) {
        if (!sign[j]) {
          sign[j] = 1;
          cnt++;
        }
      }
    }
  }
  for (int i = 0; i < 26; i++) {
    if (letter[i] >= cnt) {
      ok = i;
      letter[i] -= cnt;
      break;
    }
  }
  if (ok == -1) {
    cout << "NO" << endl;
    return 0;
  }
  int ptr = 0;
  for (int i = 0; i < n; i++) {
    if (sign[i + 1]) {
      second[i] = 'a' + ok;
    } else {
      while (!letter[ptr]) ptr++;
      second[i] = 'a' + ptr;
      letter[ptr]--;
    }
  }
  cout << "YES" << endl;
  cout << second << endl;
  return 0;
}
