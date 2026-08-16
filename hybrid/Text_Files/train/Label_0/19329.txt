#include <bits/stdc++.h>
using namespace std;

int main() {
  string S;
  cin >> S;
  cout << S.size() / 2 - count(S.begin(), S.end(), 'p') << "\n";
}