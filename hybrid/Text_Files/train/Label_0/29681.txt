#include <iostream>
#include <vector>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
int N, Q;

//FenwickTree
vector<int> FenTree;

void init(void) {
  FenTree.resize(N+1);
  rep(i, N+1) FenTree[i] = 0;
}

void add(int i, int x) {
  for(; i <= N; i += (i & -i))
    FenTree[i] += x;
}

int sum(int i) {
  int ret = 0;
  for(; i > 0; i -= (i & -i))
    ret += FenTree[i];
  return ret;
}

int query(int l, int r) {
  return sum(r) - sum(l-1);
}

int main(void) {
  ios::sync_with_stdio(false);
  cin >> N >> Q;
  vector<int> C(N);
  rep(i, N) cin >> C[i];
  vector<vector<pair<int, int>>> LR(N+1);
  rep(i, Q) {
    int L, R;
    cin >> L >> R;
    LR[R].emplace_back(L, i);
  }

  init();
  vector<int> answer(Q);
  vector<int> pos(N+1, 0);
  for(int i = 1; i <= N; ++i) {
    if(pos[C[i-1]] > 0) {
      add(pos[C[i-1]], -1);
    }
    add(i, +1);
    pos[C[i-1]] = i;
    rep(j, (int)LR[i].size()) {
      answer[LR[i][j].second] = query(LR[i][j].first, i);
    }
  }
  rep(i, Q) cout << answer[i] << endl;
  return 0;
}
