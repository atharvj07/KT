#include <bits/stdc++.h>
int main() {
  using namespace std;
  int N;
  cin >> N;
  map<string, int> cost;
  for (int i = 0; i < N; ++i) {
    int c;
    cin >> c;
    string s;
    cin >> s;
    sort(s.begin(), s.end());
    if (!cost.count(s)) {
      cost[s] = c;
    } else {
      cost[s] = min(cost[s], c);
    }
  }
  vector<int> price;
  if (cost["A"]) {
    if (cost["B"] && cost["C"]) {
      price.emplace_back(cost["A"] + cost["B"] + cost["C"]);
    }
    if (cost["BC"]) {
      price.emplace_back(cost["A"] + cost["BC"]);
    }
  }
  if (cost["AB"]) {
    if (cost["C"]) {
      price.emplace_back(cost["AB"] + cost["C"]);
    }
    if (cost["AC"]) {
      price.emplace_back(cost["AB"] + cost["AC"]);
    }
    if (cost["BC"]) {
      price.emplace_back(cost["AB"] + cost["BC"]);
    }
  }
  if (cost["AC"]) {
    if (cost["B"]) {
      price.emplace_back(cost["AC"] + cost["B"]);
    }
    if (cost["BC"]) {
      price.emplace_back(cost["AC"] + cost["BC"]);
    }
  }
  if (cost["ABC"]) {
    price.emplace_back(cost["ABC"]);
  }
  if (price.size()) {
    sort(price.begin(), price.end());
    cout << price[0];
  } else {
    cout << -1;
  }
}
