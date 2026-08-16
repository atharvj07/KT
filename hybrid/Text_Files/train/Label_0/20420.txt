#include <bits/stdc++.h>
using namespace std;
int main(){
  int N, K;
  cin >> N >> K;
  vector<int> a(N);
  for (int i = 0; i < N; i++){
    cin >> a[i];
  }
  vector<long long> S1(N + 1, 0);
  for (int i = 0; i < N; i++){
    S1[i + 1] = S1[i] + max(a[i], 0);
  }
  vector<long long> S2(N + 1, 0);
  for (int i = 0; i < N; i++){
    S2[i + 1] = S2[i] + a[i];
  }
  long long ans = 0;
  for (int i = 0; i <= N - K; i++){
    ans = max(ans, (S1[i] - S1[0]) + max(S2[i + K] - S2[i], (long long) 0) + (S1[N] - S1[i + K]));
  }
  cout << ans << endl;
}