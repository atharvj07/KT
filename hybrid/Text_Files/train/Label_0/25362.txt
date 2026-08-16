#include <bits/stdc++.h>

#define reps(v, f, l) for (int v = (f), v##_ = (l); v < v##_; ++v)
#define rep(v, n) reps(v, 0, n)
#define lep(v, n) reps(v, 1, n + 1)

using namespace std;

typedef long long int lint;

static inline int in(){ int x; scanf("%d", &x); return x; }
static inline lint inl(){ lint x; scanf("%lld", &x); return x; }
template<typename T> void show(T& a, char del='\n', char last='\n'){ rep(i, a.size() - 1) cout << a[i] << del; cout << a[a.size() - 1] << last; }

int main()
{
  int n;
  while (n = in()){
    vector<int> v;
    vector<int> counter(n + 1, 0);
    lep(i, n - 1) v.push_back(i * i % n);
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(), v.end()), v.end());
    rep(i, v.size()){
      rep(j, v.size()){
        if (i == j) continue;
        int x = v[i] - v[j];
        if (x < 0) x += n;
        if (x > (n - 1) / 2) x = n - x;
        counter[x]++;
      }
    }
    lep(i, (n - 1) / 2){
      printf("%d\n", counter[i]);
    }
  }
  return 0;
}