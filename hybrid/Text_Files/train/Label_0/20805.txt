#include <bits/stdc++.h>
using namespace std;
int A, B;
struct Client {
  int a, b, idx;
};
bool cmp(Client x, Client y) {
  return (x.a * A + x.b * B) < (y.a * A + y.b * B);
}
int main() {
  int n, d;
  cin >> n >> d >> A >> B;
  vector<Client> v(n);
  for (int i = 0; i < n; i++) {
    cin >> v[i].a >> v[i].b;
    v[i].idx = i + 1;
  }
  sort(v.begin(), v.end(), cmp);
  long long sum = 0;
  vector<int> ans;
  for (int i = 0; i < n; i++) {
    sum += (long long)(v[i].a * A) + v[i].b * B;
    if (sum > d) {
      cout << ans.size() << endl;
      for (int i = 0; i < ans.size(); i++) cout << ans[i] << " ";
      return 0;
    } else
      ans.push_back(v[i].idx);
  }
  cout << ans.size() << endl;
  for (int i = 0; i < ans.size(); i++) cout << ans[i] << " ";
  return 0;
}
