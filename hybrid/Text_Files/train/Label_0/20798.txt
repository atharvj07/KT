#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <stack>
#include <queue>
#include <algorithm>
#include <iostream>
#include <string>

#define REP(i,n) for(long long i=0;i<n;++i)
#define REPR(i,n) for(long long i=n;i>=0;--i)
#define REPI(itr,v) for(auto itr=v.begin();itr!=v.end();++itr)
#define REPIR(itr,v) for(auto itr=v.rbegin();itr!=v.rend();++itr)
#define FOR(i,a,b) for(long long i=a;i<b;++i)
#define SORT(v,n) sort(v, v+n)
#define SORTV(v) sort(v.begin(), v.end())
#define ALL(v) v.begin(),v.end()
#define llong long long
#define INF 999999999
#define MOD 1000000007
#define pb push_back
#define pf push_front
#define MP make_pair
#define SV(v) {for(long long sitr=0;sitr<v.size();++sitr){cin>>v[sitr];}}

int dx[] = {0, 0, -1, 1};
int dy[] = {1, -1, 0, 0};

using namespace std;

typedef pair<int,int> pii;

int main(){

  int n, m;
  cin >> n >> m;

  vector<string> word(n), word_rev(n), slate(m);
  REP(i,n){
    cin >> word[i];
    word_rev[i] = word[i];
    reverse(ALL(word_rev[i]));
  }
  REP(i,m){
    cin >> slate[i];
  }

  sort(ALL(word));
  sort(ALL(word_rev));

  REP(i,m){
    int idx = slate[i].find("?");

    //ない時
    if(idx == -1){
      if(slate[i][0] == '*'){
        string tmp = slate[i].substr(1, slate[i].length()-1);
        reverse(ALL(tmp));
        cout << distance(lower_bound(ALL(word_rev), tmp), lower_bound(ALL(word_rev), tmp+"~")) << endl;
      }else if(slate[i].back() == '*'){
        string tmp = slate[i].substr(0, slate[i].length()-1);
        //cerr << tmp << endl;
        cout << distance(lower_bound(ALL(word), tmp), lower_bound(ALL(word), tmp+"~")) << endl;
      }else{
        cout << distance(lower_bound(ALL(word), slate[i]), upper_bound(ALL(word), slate[i])) << endl;
      }
    }else{
      //ある時
      int ans = 0;
      REP(j,26){
        
        slate[i][idx] = 'a' + j;
        if(slate[i][0] == '*'){
          string tmp = slate[i].substr(1, slate[i].length()-1);
          reverse(ALL(tmp));
          ans += distance(lower_bound(ALL(word_rev), tmp), lower_bound(ALL(word_rev), tmp+"~"));
        }else if(slate[i].back() == '*'){
          string tmp = slate[i].substr(0, slate[i].length()-1);
          //cerr << tmp << endl;
          ans += distance(lower_bound(ALL(word), tmp), lower_bound(ALL(word), tmp+"~"));
        }else{
          ans += distance(lower_bound(ALL(word), slate[i]), upper_bound(ALL(word), slate[i]));
        }
      }
      cout << ans << endl;
    }
  }

  return 0;
}


