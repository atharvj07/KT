#include <bits/stdc++.h>
#pragma comment(linker, "/STACK:16777216")
using namespace std;
int main() {
  int N;
  cin >> N;
  vector<pair<int, int> > A;
  string a1(N, '0');
  string a2(N, '0');
  for (long long i = 0; i < (int)N; i++) {
    int a, b;
    cin >> a >> b;
    A.push_back(make_pair(a, (i + 1)));
    A.push_back(make_pair(b, -(i + 1)));
  }
  for (long long i = 0; i < (int)N / 2; i++) {
    if (A[2 * i].second < 0)
      a2[(-A[2 * i].second) - 1] = '1';
    else
      a1[(A[2 * i].second) - 1] = '1';
    if (A[2 * i + 1].second < 0)
      a2[(-A[2 * i + 1].second) - 1] = '1';
    else
      a1[(A[2 * i + 1].second) - 1] = '1';
  }
  sort((A).begin(), (A).end());
  for (long long i = 0; i < (int)N; i++) {
    if (A[i].second < 0)
      a2[(-A[i].second) - 1] = '1';
    else
      a1[(A[i].second) - 1] = '1';
  }
  cout << a1 << endl << a2;
  return 0;
}
