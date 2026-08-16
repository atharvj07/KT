#include <bits/stdc++.h>
using namespace std;
const int TAM = 2e5 + 2;
int q, a, b;
string s;
int acum[TAM][30];
void carry_on(int pos) {
  for (int j = 0; j < 26; j++) acum[pos][j] = acum[pos - 1][j];
}
bool check(int a, int b) {
  int cont = 0;
  for (int j = 0; j < 26; j++) {
    if (acum[b][j] - acum[a - 1][j]) cont++;
  }
  return cont >= 3;
}
int main() {
  cin >> s;
  for (int i = 0; i < s.size(); i++) {
    carry_on(i + 1);
    acum[i + 1][s[i] - 'a']++;
  }
  cin >> q;
  while (q--) {
    cin >> a >> b;
    if (a == b or s[a - 1] != s[b - 1] or check(a, b))
      cout << "Yes\n";
    else
      cout << "No\n";
  }
  return 0;
}
