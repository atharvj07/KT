#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

typedef long long lli;

typedef pair<lli, lli> P;

const lli MAX = 100000;

lli w, h, gx, gy, n;
vector<P> input;
vector<lli> vec[4][MAX+1]; //(x, y)
string r;

bool check(lli x, lli y, lli d){
  bool f = false;
  for(lli i=0;i<=r.size();i++){
    lli nx, ny;
    if(d == 0){
      nx = x;
      ny = *(lower_bound(vec[0][x].begin(), vec[0][x].end(), -y));
      ny = -ny;
      if(nx == gx && ny == gy) return true;
      ny = ny + 1;
      if(nx == gx && ny <= gy && gy <= y) return true;

    }
    if(d == 1){
      nx = *(lower_bound(vec[1][y].begin(), vec[1][y].end(), x));
      ny = y;
      if(nx == gx && ny == gy) return true;
      nx = nx - 1;
      if(x <= gx && gx <= nx && ny == gy) return true;
    }
    if(d == 2){
      nx = x;
      ny = *(lower_bound(vec[2][x].begin(), vec[2][x].end(), y));
      if(nx == gx && ny == gy) return true;
      ny = ny - 1;
      if(nx == gx && y <= gy && gy <= ny) return true;
    }
    if(d == 3){
      nx = *(lower_bound(vec[3][y].begin(), vec[3][y].end(), -x));
      ny = y;
      nx = -nx;
      if(nx == gx && ny == gy) return true;
      nx = nx + 1;
      if(nx <= gx && gx <= x && ny == gy) return true;
    }
    x = nx;
    y = ny;
    if(i == r.size()) break;
    if(r[i] == 'R') d = (d + 1) % 4;
    else d = (d - 1 + 4) % 4;
  }
  return false;
}

lli solve(){
  lli res = 0;
  for(lli i=0;i<=MAX;i++){
    for(int j=0;j<4;j++) vec[j][i].clear();
  }
  for(lli i=0;i<input.size();i++){
    vec[1][input[i].second].push_back(input[i].first);
    vec[3][input[i].second].push_back(input[i].first);
  }
  vec[1][gy].push_back(gx);
  vec[3][gy].push_back(gx);
  for(lli i=0;i<input.size();i++){
    vec[0][input[i].first].push_back(input[i].second);
    vec[2][input[i].first].push_back(input[i].second);
  }
  vec[0][gx].push_back(gy);
  vec[2][gx].push_back(gy);
  for(lli i=0;i<4;i++){
    for(lli j=1;j<=MAX;j++){
      vec[i][j].push_back(0);
      vec[i][j].push_back((i%2==0?h:w)+1);
    }
  }
  for(lli i=0;i<=MAX;i++){
    for(lli j=0;j<vec[0][i].size();j++){
      vec[0][i][j] = -vec[0][i][j];
    }
    for(lli j=0;j<vec[3][i].size();j++){
      vec[3][i][j] = -vec[3][i][j];
    }
  }
  for(lli i=0;i<=MAX;i++){
    for(lli j=0;j<4;j++){
      if(vec[j][i].size() > 0) sort(vec[j][i].begin(), vec[j][i].end());
    }
  }
  for(lli d=0;d<4;d++){
    lli upper = (d%2==0?w:h);
    for(lli i=1;i<=upper;i++){
      for(lli j=1;j<vec[d][i].size();j++){
        if(d % 2 == 1){
          lli sx = vec[d][i][j]-1;
          if(d == 3) sx = -sx;
          if(sx <= 0 || sx > w) continue;
          if(vec[d][i][j] - vec[d][i][j-1] - 1 > 0 && check(sx, i, d)){
            res += vec[d][i][j] - vec[d][i][j-1] - 1;
          }
        }
        if(d % 2 == 0){
          lli sy = vec[d][i][j]-1;
          if(d == 0) sy = -sy;
          if(sy <= 0 || sy > h) continue;
          if(vec[d][i][j] - vec[d][i][j-1] - 1 > 0 && check(i, sy, d)){
            res += vec[d][i][j] - vec[d][i][j-1] - 1;
          }
        }
      }
    }
  }
  return res;
}

int main(){
  cin >> w >> h >> gx >> gy >> n;
  for(lli i=0;i<n;i++){
    lli x, y;
    cin >> x >> y;
    input.push_back(P(x, y));
  }
  cin >> r;
  cout << solve() + 4 << endl;
}