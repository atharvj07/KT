#include<iostream>
#include<vector>
#include<cstdlib>
#include<algorithm>
#include<queue>
#include<cstring>
#include<map>
#include<iostream>
using namespace std;
typedef pair<int,int> Pt;
typedef pair<int,Pt> P;
#define fr first
#define sc second
Pt gl;
int h,w,d[]={0,1,0,-1};
bool used[1000][1000];
char mas[1000][1000];
vector<Pt> vc;
bool bfs(int n){
  mas[vc[n].fr][vc[n].sc] = '.';
  bool ok = false;
  if(n){
    for(int i = 0 ; i < 4 ; i++){
      int nx = vc[n].fr + d[i] , ny = vc[n].sc + d[3-i];
      if(nx >= 0 && nx < h && ny >= 0 && ny < w){
        if(used[nx][ny]) ok = true;
      }
    }
  }else ok = true;
  if(ok){
    queue<Pt> que;
    que.push(Pt(vc[n]));
    used[vc[n].fr][vc[n].sc] = true;
    while(!que.empty()){
      Pt p = que.front();
      que.pop();
      if(p == gl) return true;
      for(int i = 0 ; i < 4 ; i++){
        int nx = p.fr + d[i] , ny = p.sc + d[3-i];
        if(nx >= 0 && nx < h && ny >= 0 && ny < w && !used[nx][ny] && mas[nx][ny] != '#'){
          que.push(Pt(nx,ny));
          used[nx][ny] = true;
        }
      }
    }
  }
  return false;
}
int main(){
  cin >> w >> h ;
  for(int i = 0 ; i < h ; i++){
    for(int j = 0 ; j < w ; j++){
      cin >> mas[i][j];
      if(mas[i][j] == 't') gl = Pt(i,j);
    }
  }
  int n;
  cin >> n;
  vc.resize(n+1);
  vc[0] = Pt(0,0);
  for(int i = 1 ; i <= n ; i++ ){
    cin >> vc[i].sc >> vc[i].fr ;
  }

  int i = 0;
  for(i = 0 ; i <= n ; i++ ){
    if( bfs(i) ){
      cout << i << endl;
      break;
    }
  }
  if(i == n+1) cout << -1 << endl;
}