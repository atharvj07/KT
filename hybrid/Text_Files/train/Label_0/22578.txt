#include <bits/stdc++.h>
using namespace std;
int main() {
  int a, b, c, d, e, f;
  cin >> d;
  while (d--) {
    cin >> a >> b;
    string s;
    cin >> s;
    int ar[b];
    for (int i = 0; i < b; i++) {
      cin >> ar[i];
    }
    vector<int> ff(a + 1, 0), alt(26, 0);
    for (int i = 0; i < a; i++) {
      alt[s[i] - 'a'] += 1;
    }
    for (int i = 0; i < b; i++) {
      ff[0] += 1;
      ff[ar[i]] -= 1;
    }
    for (int i = 0; i < a; i++) {
      ff[i + 1] += ff[i];
      alt[s[i] - 'a'] += ff[i];
    }
    for (int i = 0; i < 26; i++) {
      cout << alt[i] << " ";
    }
    cout << endl;
  }
}
