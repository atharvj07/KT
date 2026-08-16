#include <bits/stdc++.h>
using namespace std;
void imprimirVector(vector<int> &v) {
  if (!v.empty()) {
    int p = v.size();
    cout << "[";
    for (int i = 0; i < (int)(p - 1); i++) cout << v[i] << ",";
    cout << v[p - 1] << "]" << endl;
  } else
    cout << "[]" << endl;
}
int main() {
  int N;
  cin >> N;
  vector<long long> pizzas(N);
  for (int i = 0; i < (int)(N); i++) cin >> pizzas[i];
  long long am = 0;
  bool can = true;
  for (int i = 0; i < (int)(N); i++) {
    if (pizzas[i] > 0)
      am += pizzas[i];
    else {
      can &= (am % 2 == 0);
    }
  }
  can &= (am % 2 == 0);
  if (can)
    cout << "YES\n";
  else
    cout << "NO\n";
  return 0;
}
