#include <bits/stdc++.h>
using namespace std;
const int N = 1e6 + 100;
const double PI = 3.14159;
vector<int> v;
long long n, m, k, t, sum, r, l, d, a, b, c;
long long ans;
map<int, int> mp;
string s;
bool f;
set<long long> st;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(NULL);
  cin >> n;
  int prv = 0;
  for (int i = 0; i < n; i++) {
    int x, y;
    cin >> x >> y;
    if (!i)
      prv = max(x, y);
    else {
      if (prv >= x && prv >= y)
        prv = max(x, y);
      else if (prv >= x)
        prv = x;
      else if (prv >= y)
        prv = y;
      else {
        cout << "NO" << endl;
        return 0;
      }
    }
  }
  cout << "YES";
  return 0;
}
