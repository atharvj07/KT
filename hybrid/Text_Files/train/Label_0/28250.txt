#include <bits/stdc++.h>
void scan(int* i) {
  int t = 0;
  char c;
  bool negative = false;
  c = getchar_unlocked();
  while (c < '0' || c > '9') {
    if (c == '-') negative = true;
    c = getchar_unlocked();
  }
  while (c >= '0' && c <= '9') {
    t = (t << 3) + (t << 1) + c - '0';
    c = getchar_unlocked();
  }
  if (negative) t = ~(t - 1);
  *i = t;
}
void scan(long long int* i) {
  long long int t = 0;
  char c;
  bool negative = false;
  c = getchar_unlocked();
  while (c < '0' || c > '9') {
    if (c == '-') negative = true;
    c = getchar_unlocked();
  }
  while (c >= '0' && c <= '9') {
    t = (t << 3) + (t << 1) + c - '0';
    c = getchar_unlocked();
  }
  if (negative) t = ~(t - 1);
  *i = t;
}
using namespace std;
int main() {
  int n, a, b;
  cin >> a >> b >> n;
  vector<int> A(a);
  vector<int> B(b);
  for (int i = 0; i < a; ++i) cin >> A[i];
  sort(A.begin(), A.end());
  for (int i = 0; i < b; ++i) cin >> B[i];
  sort(B.begin(), B.end());
  int i = 0, j = 0;
  while (i < a && j < b) {
    if (B[j] < A[i]) {
      ++j;
    } else {
      ++i;
      ++j;
    }
  }
  int count = a - i;
  int bcount = b - j;
  if (count <= bcount)
    cout << "NO" << endl;
  else
    cout << "YES" << endl;
  return 0;
}
