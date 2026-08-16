#include <bits/stdc++.h>
using namespace std;
void affiche(int t[], int n) {
  for (int i = 0; i < n; i++) cout << t[i] << " ";
  cout << '\n';
}
void afficheV(vector<int> t) {
  for (int i = 0; i < t.size(); i++) cout << t[i] << " ";
  cout << '\n';
}
int main() {
  ios_base::sync_with_stdio(0), cin.tie(0);
  map<int, int> mp;
  map<int, int>::iterator it;
  int ans = 0, mx = 0, second = 0;
  for (int i = 0; i < 5; i++) {
    int x;
    cin >> x;
    second += x;
    mp[x]++;
  }
  for (it = mp.begin(); it != mp.end(); it++) {
    if (it->second == 1) continue;
    int c = min(3, it->second);
    int sum = c * it->first;
    mx = max(mx, sum);
  }
  cout << second - mx;
}
