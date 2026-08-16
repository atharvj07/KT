#include <bits/stdc++.h>
using namespace std;

const int MAXN = 50005;
const int MAXM = 50005;
const string str[12] = {"C","C#","D","D#","E","F","F#","G","G#","A","A#","B"};

map<string, int> id;
int n, m;
int T[MAXN], S[MAXM];

bool rec(int k, int p) {
  if((m - p) * 2 < (n - 1) - k) return false;
  if(p == m) return (n + 1) - k <= 2;
  if(k-1 > 0 && (T[k-1]+11)%12 == S[p] && rec(k-1, p+1)) return true;
  if(k+1 < n+1 && (T[k+1]+0)%12 == S[p] && rec(k+1, p+1)) return true;
  if(k+2 < n+1 && (T[k+2]+1)%12 == S[p] && rec(k+2, p+1)) return true;
  return false;
}

int main() {
  for(int i = 0; i < 12; ++i) id[str[i]] = i;

  int Tc; cin >> Tc;
  while(Tc--) {
    cin >> n >> m;
    for(int i = 0; i < n; ++i) {
      string s; cin >> s;
      T[i+1] = id[s];
    }
    for(int i = 0; i < m; ++i) {
      string s; cin >> s;
      S[i] = id[s];
    }
    cout << (rec(0, 0) ? "Yes" : "No") << endl;
  }
  return 0;
}