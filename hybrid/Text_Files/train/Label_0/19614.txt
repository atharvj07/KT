#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

#define FOR(i,k,n) for(int i=(k); i<(int)n; ++i)
#define REP(i,n) FOR(i,0,n)
#define FORIT(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)

template<class T> void debug(T begin, T end){ for(T i = begin; i != end; ++i) cout<<*i<<" "; cout<<endl; }

typedef long long ll;
const int INF = 100000000;
const double EPS = 1e-8;
const int MOD = 1000000007;

int main(){
  string hand[15] = {"Rock", "Fire", "Scissors", "Snake", "Human", "Tree", "Wolf", "Sponge", "Paper", "Air", "Water", "Dragon", "Devil", "Lightning", "Gun"};
  map<string, int> hand_id;
  REP(i, 15) hand_id[hand[i]] = i;
  int N;
  while(cin>>N && N){
    vector<string> result(N);
    REP(i, N) cin>>result[i];
    vector<int> win(N);
    vector<int> lose(N);
    REP(i, N) FOR(j, i + 1, N){
      int id1 = hand_id[result[i]];
      int id2 = hand_id[result[j]];
      if(id1 == id2){
      }else if((id1 - id2 + 15) % 15 <= 7){
        win[j] ++;
        lose[i]++;
      }else{
        assert((id2 - id1 + 15) % 15 <= 7);
        win[i] ++;
        lose[j]++;
      }
    }
    string winner = "Draw";
    REP(i, N) if(win[i] > 0 && lose[i] == 0) winner = result[i];
    cout<<winner<<endl;
  }
    
  return 0;
}