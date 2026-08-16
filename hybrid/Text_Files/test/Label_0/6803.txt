#include <bits/stdc++.h>
using namespace std;
int main() {
  int v1, v2, v3, vm, vc;
  cin >> v1 >> v2 >> v3 >> vm;
  vc = v3;
  if (2 * vm < v3) {
    cout << "-1";
    return 0;
  }
  if (vc < vm) vc = vm;
  if (v3 * 2 < vc) {
    cout << "-1";
    return 0;
  }
  if (vm * 2 >= v1 * 2 || vm * 2 >= v2 * 2) {
    cout << "-1";
    return 0;
  }
  cout << v1 * 2 << '\n' << v2 * 2 << '\n' << vc;
  return 0;
}
