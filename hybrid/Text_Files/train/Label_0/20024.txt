#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  while (cin >> n) {
    string word;
    cin >> word;
    int n_a = 0, n_c = 0, n_t = 0, n_g = 0;
    if (n % 4) {
      cout << "===" << endl;
      continue;
    }
    for (int i = 0; i < n; i++) {
      if (word[i] == 'A') {
        n_a++;
      }
      if (word[i] == 'C') {
        n_c++;
      }
      if (word[i] == 'T') {
        n_t++;
      }
      if (word[i] == 'G') {
        n_g++;
      }
    }
    if (n_a > n / 4 || n_t > n / 4 || n_c > n / 4 || n_g > n / 4) {
      cout << "===" << endl;
      continue;
    } else {
      for (int i = 0; i < n; i++) {
        if (word[i] == '?') {
          int ok = 0;
          if (n_a < n / 4 && !ok) {
            word[i] = 'A';
            n_a++;
            ok = 1;
          }
          if (n_t < n / 4 && !ok) {
            word[i] = 'T';
            n_t++;
            ok = 1;
          }
          if (n_g < n / 4 && !ok) {
            word[i] = 'G';
            n_g++;
            ok = 1;
          }
          if (n_c < n / 4 && !ok) {
            word[i] = 'C';
            n_c++;
            ok = 1;
          }
        }
      }
      cout << word << endl;
    }
  }
}
