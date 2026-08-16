#include <bits/stdc++.h>
using namespace std;
long long int N, a[1010101], q;
long long int sparse_table[1010101][30];
long long int lg_table[1010101];
set<long long int> final_result;
map<long long int, long long int> red;
long long int gcd(long long int a, long long int b) {
  if (a > b) return gcd(b, a);
  if (a == 0) return b;
  return gcd(b % a, a);
}
void build_log() {
  lg_table[1] = 0;
  for (long long int i = 2; i < 1010101; i++) lg_table[i] = 1 + lg_table[i / 2];
}
void build_sparse() {
  for (long long int i = 0; i < N; i++) sparse_table[i][0] = a[i];
  for (long long int lg = 1; lg < 30; lg++)
    for (long long int i = 0; i + (1 << lg) <= N; i++)
      sparse_table[i][lg] = gcd(sparse_table[i][lg - 1],
                                sparse_table[i + (1 << (lg - 1))][lg - 1]);
}
long long int get_gcd(long long int l, long long int r) {
  long long int lg = lg_table[r - l + 1];
  return gcd(sparse_table[l][lg], sparse_table[r - (1 << lg) + 1][lg]);
}
void get_distinct_gcd(long long int L) {
  long long int st = L;
  while (st < N) {
    long long int idx = st;
    for (long long int z = 10000; z >= 1; z /= 2) {
      while (idx + z < N && get_gcd(L, idx + z) == get_gcd(L, st)) idx += z;
    }
    red[get_gcd(L, st)] += (idx - st + 1);
    st = idx + 1;
  }
}
int main() {
  long long int x;
  cin >> N;
  for (long long int i = 0; i < N; i++) cin >> a[i];
  build_log();
  build_sparse();
  for (long long int i = 0; i < N; i++) {
    get_distinct_gcd(i);
  }
  cin >> q;
  while (q--) {
    cin >> x;
    cout << red[x] << endl;
  }
}
