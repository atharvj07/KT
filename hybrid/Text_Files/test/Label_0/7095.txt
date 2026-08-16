#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
const double EPS = 1e-5;
template <typename T>
T abs(const T& a) {
  if (a >= 0) return a;
  return -a;
}
int main() {
  ios::sync_with_stdio(false);
  string str;
  cin >> str;
  int sz = str.size();
  int sq = sqrt(sz) + 1;
  if (sz <= 3) {
    cout << "YES\n" << str << "\n";
    return 0;
  }
  bool isp[sz + 1];
  memset(isp, true, sizeof(isp));
  for (int i = 4; i <= sz; i += 2) isp[i] = false;
  isp[2] = true;
  isp[0] = isp[1] = false;
  vector<int> p;
  p.push_back(2);
  for (int i = 3; i <= sq; i += 2) {
    if (isp[i]) {
      for (int j = i + i; j <= sz; j += i) {
        isp[j] = false;
      }
      p.push_back(i);
    }
  }
  for (int i = sq + 1; i <= sz; ++i)
    if (isp[i]) p.push_back(i);
  int pos = 0;
  for (int i = 0; i < p.size(); ++i) {
    if (2 * p[i] > sz) {
      pos = i;
      break;
    }
  }
  int qtd_prim = p.size() - pos;
  int c[26] = {0};
  int maxi = 0, pp = 0;
  for (int i = 0; i < sz; ++i) {
    c[str[i] - 'a']++;
    if (c[str[i] - 'a'] > maxi) {
      maxi = c[str[i] - 'a'];
      pp = str[i] - 'a';
    }
  }
  char vet[sz + 1];
  memset(vet, -1, sizeof(vet));
  if (sz - 1 - qtd_prim <= maxi) {
    cout << "YES\n";
    for (int i = 0; i < sz; ++i) {
      vet[i] = pp + 'a';
    }
    c[pp] -= sz - 1 - qtd_prim;
    for (int i = 0; i < sz; ++i) {
      if (i == 0 || (isp[i + 1] && i + 1 >= p[pos])) {
        for (int j = 0; j < 26; ++j) {
          if (c[j] > 0) {
            vet[i] = j + 'a';
            c[j]--;
            break;
          }
        }
      }
    }
    vet[sz] = 0;
    cout << vet << '\n';
  } else
    cout << "NO\n";
  return 0;
}
