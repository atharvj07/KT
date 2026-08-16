#include <bits/stdc++.h>
using namespace std;
int main() {
  int N;
  long long P, K;
  scanf("%d %lld %lld\n", &N, &P, &K);
  map<long long, int> freq;
  for (int i = 0; i < N; ++i) {
    long long a;
    scanf("%lld", &a);
    long long key = (K * a % P - a * a % P * a % P * a % P) % P;
    key = (key + P) % P;
    if (freq.find(key) == freq.end()) {
      freq[key] = 1;
    } else {
      freq[key]++;
    }
  }
  long long answer = 0;
  for (pair<long long, int> kv : freq) {
    int f = kv.second;
    answer += f * (long long)(f - 1) / 2;
  }
  printf("%lld\n", answer);
  return 0;
}
