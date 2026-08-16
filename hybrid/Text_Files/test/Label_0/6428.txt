#include <algorithm>
#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
#include <unordered_set>
inline int getInt(){ int s; scanf("%d", &s); return s; }

using namespace std;

int main(){
  const int n = getInt();
  const int m = getInt();

  std::unordered_set<int> s;
  vector<int> v(n);

  REP(i,n) v[i] = getInt();
  reverse(v.begin(), v.end());

  for(int i = 0; i < n; i++){
    if((int) s.size() < m && s.count(v[i]) == 0){
      printf("%d\n", v[i]);
      s.insert(v[i]);
    }
  }

  return 0;
}