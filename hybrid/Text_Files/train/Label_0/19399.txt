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
int N, C;
int grid[10][10];
bool valid(int x, int y){
  return (y >= 0 && x >= 0 && y < N && x <= y);
}
int dx[6] = {1, 1, 0, -1, -1, 0};
int dy[6] = {0, 1, 1, 0, -1, -1};
int calc(){
  int res = 0;
  bool used[10][10] = {};
  REP(y, N)REP(x, y + 1){
    if(grid[y][x] != 0 && !used[y][x]){
      int cnt = 1;
      queue<int> qx, qy;
      qx.push(x); qy.push(y);
      used[y][x] = true;
      bool removed = true;
      while(!qx.empty()){
        int xx = qx.front(), yy = qy.front();
        qx.pop(), qy.pop();
        REP(r, 6){
          int nx = xx + dx[r];
          int ny = yy + dy[r];
          if(valid(nx, ny) && grid[ny][nx] == 0) removed = false;
          if(valid(nx, ny) && grid[ny][nx] == grid[yy][xx] && !used[ny][nx]){
            cnt ++;
            used[ny][nx] = true;
            qx.push(nx), qy.push(ny);
          }
        }
      }
      if(removed){
        if(C == grid[y][x]) cnt *= -1;
        res += cnt;
      }
    }
  }
  return res;
}

int main(){
  int cnt = 0;
  while(cin>>N>>C && N){
    //printf("Case %d:\n", ++cnt);
    int board[10][10] = {};
    REP(i, N)REP(j, i + 1){
      cin>>board[i][j];
    }
    int ans = -INF;
    REP(y, N)REP(x, y + 1)if(board[y][x] == 0){
      memcpy(grid, board, sizeof(grid));
      grid[y][x] = C;
      ans = max(ans, calc());
    }
    cout<<ans<<endl;
  }
  return 0;
}