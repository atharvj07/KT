#include <bits/stdc++.h>
using namespace std;
int const N = 1 << 18;
int const M = 1 << 18;
int main(int argc, char* argv[]) {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int color[30];
  for (int i = 0; i < 24; ++i) cin >> color[i];
  const char* ans[12] = {
      "111155223333224466554466", "111144223333664422555566",
      "114422225533434315156666", "115522224433414135356666",
      "111122553333442255666644", "111122443333446655226655",
      "212132326363444455556161", "616112122323444455556363",
      "121223233636444455551616", "161621213232444455553636",
      "551122223344141453536666", "441122223355343451516666"};
  for (int k = 0; k < 12; ++k) {
    const char* s = ans[k];
    bool ok = true;
    for (int i = 0; i < 24; ++i) {
      for (int j = 0; j < 24; ++j) {
        bool a = color[i] == color[j];
        bool b = s[i] == s[j];
        if (a ^ b) {
          ok = false;
        }
      }
    }
    if (ok) {
      puts("YES");
      return 0;
    }
  }
  puts("NO");
  return 0;
}
