#include <bits/stdc++.h>

using namespace std;

typedef long long int64;

int main()
{
  int64 N, M, K, A, B, C, T, S[3001];

  cin >> N >> M >> K;
  cin >> A >> B >> C;
  cin >> T;
  for(int i = 0; i < M; i++) cin >> S[i];
  S[M] = N + 1;
  K -= M;

  int64 ret = -1;

  priority_queue< int64, vector< int64 >, greater< int64 > > que;

  for(int i = 0; i < M; i++) {
    int64 rest = T - (S[i] - 1) * B;
    if(rest < 0) break;
    int64 pv = S[i], reach = min(S[i + 1], pv + rest / A + 1);
    ret += reach - S[i];
    for(int j = 0; j < K && reach < S[i + 1]; j++) {
      rest -= (reach - pv) * C;
      if(rest < 0) break;
      pv = reach;
      reach = min(S[i + 1], pv + rest / A + 1);
      if(que.size() > K && que.top() >= reach - pv) continue;
      que.push(reach - pv);
      ret += reach - pv;
      if(que.size() > K) ret -= que.top(), que.pop();
    }
  }

  cout << ret << endl;
}