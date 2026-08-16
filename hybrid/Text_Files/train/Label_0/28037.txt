#include<bits/stdc++.h>

#define REP(i,s,n) for(int i=s;i<n;i++)
#define rep(i,n) REP(i,0,n)

using namespace std;

const int IINF = INT_MAX;

struct Data {
  int x,y,step,dir,bitmask;
  bool operator < ( const Data &data ) const {
    return step > data.step;
  }
};

int h,w,L,sx,sy,gx,gy;
char c[30][30];
int mindist[30][30][5][1<<5];

int dx[] = { 0,1,0,-1,0}; // ???,???,???,???,??´???
int dy[] = {-1,0,1, 0,0};

bool isValid(int x,int y) { return 0 <= x && x < w && 0 <= y && y < h; }

bool isValidMoveType1(int x,int y,int dir,int bitmask) {
  int cx = x, cy = y;
  rep(i,L){
    if( !isValid(cx,cy) ) return false;    
    if( c[cy][cx] == '#' ) return false;
    if( isalpha(c[cy][cx]) && islower(c[cy][cx])  && !( ( bitmask >> (c[cy][cx]-'a') ) & 1 ) ) return false;
    cx += dx[dir], cy += dy[dir];
  }
  return true;
}

void compute(){
  rep(i,h) rep(j,w) rep(l,5) rep(k,(1<<5)) mindist[i][j][l][k] = IINF;
  mindist[sy][sx][4][0] = 0;
  
  priority_queue<Data> Q;
  Q.push((Data){sx,sy,0,4,0});

  while( !Q.empty() ){

    Data data = Q.top(); Q.pop();

    if( data.x == gx && data.y == gy && data.dir == 4 ) {
      cout << data.step << endl;
      return;
    }

    if( data.dir == 4 ) {
      rep(i,4){
	int nx = data.x + dx[i], ny = data.y + dy[i];
	if( !isValidMoveType1(nx,ny,i,data.bitmask) ) continue;
	if( mindist[ny][nx][i][data.bitmask] > data.step + 1 ) {
	  mindist[ny][nx][i][data.bitmask] = data.step + 1;
	  Q.push((Data){nx,ny,data.step+1,i,data.bitmask});
	}
      }
    } else {

      // L ??????      
      // R ??????
      for(int coef=-1;coef<=1;coef+=2) {
	int nx = data.x, ny = data.y;
	if( coef == -1 ) {
	  nx += dx[data.dir] * coef, ny += dy[data.dir] * coef;
	} else {
	  nx += dx[data.dir] * coef * L, ny += dy[data.dir] * coef * L;
	}
	if( !isValid(nx,ny) ) continue;
	if( c[ny][nx] == '#' || c[ny][nx] == '^' ) continue;
	int nbitmask = data.bitmask;
	if( 'a' <= c[ny][nx] && c[ny][nx] <= 'z' ) {
	  if( !( (data.bitmask>>(c[ny][nx]-'a')) & 1 ) ) continue;
	}
	if( 'A' <= c[ny][nx] && c[ny][nx] <= 'Z' ) {
	  nbitmask |= (1<<(c[ny][nx]-'A'));
	}
	if( mindist[ny][nx][4][nbitmask] > data.step + 1 ) {
	  mindist[ny][nx][4][nbitmask] = data.step + 1;
	  Q.push((Data){nx,ny,data.step+1,4,nbitmask});
	}
      }
      
      // rolling 1
      // rolling 2
      for(int coef=-1;coef<=1;coef+=2){
	int rdir = ( data.dir + coef + 4 ) % 4;
	int nx = data.x + dx[rdir], ny = data.y + dy[rdir];
	if( !isValidMoveType1(nx,ny,data.dir,data.bitmask) ) continue;
	if( mindist[ny][nx][data.dir][data.bitmask] > data.step + 1 ) {
	  mindist[ny][nx][data.dir][data.bitmask] = data.step + 1;
	  Q.push((Data){nx,ny,data.step+1,data.dir,data.bitmask});
	}
      }
    }
  }
  puts("-1");
}

int main(){
  cin >> h >> w >> L;
  rep(i,h){
    string s;
    cin >> s;
    rep(j,w) {
      c[i][j] = s[j];
      if( c[i][j] == 'S' ) sx = j, sy = i, c[i][j] = '.';
      if( c[i][j] == 'G' ) gx = j, gy = i, c[i][j] = '.';
    }
  }
  compute();
  return 0;
}