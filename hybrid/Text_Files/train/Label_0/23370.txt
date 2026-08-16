#include <bits/stdc++.h>
using namespace std;
const long long int mod = 1e9 + 7;
const long double error = 2e-6;
const long double PI = acosl(-1);
inline long long int MOD(long long int x, long long int m = mod) {
  long long int y = x % m;
  return (y >= 0) ? y : y + m;
}
const int inf = 1e9;
const long long int infl = 1061109567;
const int nmax = 1000 + 10;
bool cmp(pair<int, int> p1, pair<int, int> p2) {
  if (p1.first != p2.first) return p1.first < p2.first;
  return p1.second > p2.second;
}
int main() {
  int n;
  cin >> n;
  int i;
  vector<pair<int, int> > vc(n);
  vector<int> ara;
  for (i = 0; i < n; i++) {
    int xx;
    cin >> xx;
    ara.push_back(xx);
    vc[i] = {xx, i};
  }
  sort(vc.begin(), vc.end(), cmp);
  vector<int> ott[n + 2];
  set<int> tes;
  int pussy = 1;
  for (i = n - 1; i >= 0; i--) {
    tes.insert(vc[i].second);
    ott[pussy].insert(ott[pussy].end(), tes.begin(), tes.end());
    pussy++;
  }
  int m;
  cin >> m;
  for (i = 1; i <= m; i++) {
    int k, pos;
    cin >> k >> pos;
    vector<int> sv;
    int j;
    int ans = ott[k][pos - 1];
    cout << ara[ans] << "" << endl;
  }
  return 0;
}
