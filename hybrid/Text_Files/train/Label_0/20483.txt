#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  long long A = 1;
  for (int i = 1; i <= N; i++) {
    A = (A * i) % 1000000007;
  }
  cout << A;
}