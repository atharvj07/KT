#include <bits/stdc++.h>
using namespace std;
const double PI = 3.1415926535897932238460;
int main() {
  int n;
  cin >> n;
  vector<int> num;
  for (int i = 0; i < n; i++) {
    int k;
    cin >> k;
    num.push_back(k);
  }
  int cost = 0;
  int minCost = 100000;
  int mint;
  for (int i = 1; i < 101; i++) {
    for (int j = 0; j < n; j++) {
      if (abs(i - num[j]) > 0)
        cost += abs(i - num[j]) - 1;
      else
        cost += abs(i - num[j]);
    }
    if (cost < minCost) minCost = cost, mint = i;
    cost = 0;
  }
  cout << mint << " " << minCost << "\n";
}
