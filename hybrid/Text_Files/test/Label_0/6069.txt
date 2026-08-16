#include <bits/stdc++.h>
using namespace std;
vector<long long> v;
int main() {
  long long n, x;
  long double a, b;
  cin >> n >> a >> b;
  long double S = 0.0f;
  for (int i = 0; i < n; i++) {
    cin >> x;
    v.push_back(x);
    S += x;
  }
  long double p = a * v[0];
  sort(v.begin() + 1, v.end());
  int l = 0;
  for (int i = v.size() - 1; i >= 0; i--) {
    long double r = p / S;
    if (r >= b) {
      cout << l << endl;
      return 0;
    }
    l++;
    S -= v[i];
  }
  cout << (n - 1) << endl;
}
