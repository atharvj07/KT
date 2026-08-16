#include <bits/stdc++.h>
using namespace std;
map<long long int, long long int> m;
int H;
double DecayTree(int root, int h, long long int potential) {
  if (h == H) return max(m[root], potential);
  if (potential >= m[root]) return potential;
  int left = 2 * root;
  int right = left + 1;
  return 0.5 * (DecayTree(left, h + 1, max(m[root] - m[left], potential)) +
                DecayTree(right, h + 1, max(m[root] - m[right], potential)));
}
int main() {
  cin >> H;
  int q;
  cin >> q;
  while (q--) {
    string s;
    cin >> s;
    if (s == "add") {
      int node, e;
      cin >> node >> e;
      while (node > 0) {
        m[node] += e;
        node /= 2;
      }
    } else {
      cout << fixed << setprecision(10) << DecayTree(1, 0, 0) << endl;
    }
  }
  return 0;
}
