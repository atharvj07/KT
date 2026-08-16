#include <bits/stdc++.h>
using namespace std;
const int MAX = 1e5 + 10;
const long long MOD = 1e9 + 7;
int N, M, K, Q;
pair<long long, long long> A[MAX];
double prob[MAX];
int main() {
  int i, j;
  long long P;
  scanf("%d%lld", &N, &P);
  for (i = 0; i < N; ++i) {
    scanf("%lld %lld", &A[i].first, &A[i].second);
  }
  for (i = 0; i < N; ++i) {
    long long y = A[i].second / P;
    long long x = (A[i].first + P - 1) / P;
    prob[i] = (double)(y - x + 1) / (double)(A[i].second - A[i].first + 1);
    prob[i] = 1.0 - prob[i];
  }
  double exp = 0.0;
  for (i = 0; i < N; ++i) {
    double tmp = prob[i] * prob[(i + 1) % N];
    exp += 2000.0 * (1.0 - tmp);
  }
  printf("%.6lf", exp);
}
