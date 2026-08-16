#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  int N;
  cin >> N;
  vector<int> C(N), E(N - 1);
  for (int i = 0; i < N - 1; i++) {
    int a, b;
    cin >> a >> b;
    E.at(i) = --b, C.at(b) = --a;
  }

  int K = 1;
  vector<int> X(N);

  for (int i = 1; i < N; i++) {
    int c = C.at(i);
    int x = X.at(c) + 1;
    X.at(c) = C.at(i) = (x == C.at(c) ? ++x : x);
    K = max(K, x);
  }

  cout << K << "\n";
  for (int e : E) cout << C.at(e) << "\n";
}