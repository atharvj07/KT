#include <bits/stdc++.h>
using namespace std;
int Length[1001], n, x, a[1001], Concern, Pos, Ppl;
vector<int> Queues, adj[1001], Ans;
int32_t main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  ;
  cin >> n >> x;
  for (int i = 1; i <= n; ++i) {
    cin >> a[i];
    if (a[i]) adj[a[i]].push_back(i);
  }
  for (int i = 1; i <= n; ++i) {
    if (a[i] == 0) {
      Ppl = i;
      int len = 0;
      while (Ppl) {
        ++len;
        if (Ppl == x) Concern = i, Pos = len;
        if ((int)adj[Ppl].size())
          Ppl = adj[Ppl][0];
        else
          Ppl = 0;
      }
      if (Concern != i) Queues.push_back(len);
    }
  }
  for (int i = Queues.size() - 1; i >= 0; --i) {
    vector<int> Add;
    for (int j = 0; j < Ans.size(); ++j) {
      if (!Length[Ans[j] + Queues[i]])
        Add.push_back(Ans[j] + Queues[i]), Length[Ans[j] + Queues[i]] = 1;
    }
    for (int j = 0; j < Add.size(); ++j) Ans.push_back(Add[j]);
    if (!Length[Queues[i]]) Ans.push_back(Queues[i]), Length[Queues[i]] = 1;
  }
  cout << Pos << "\n";
  sort(Ans.begin(), Ans.end());
  for (int i = 0; i < Ans.size(); ++i) cout << Pos + Ans[i] << "\n";
  return 0;
}
