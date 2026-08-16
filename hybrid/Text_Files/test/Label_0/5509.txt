#include<bits/stdc++.h>

#define REP(i,s,n) for(int i=s;i<n;i++)
#define rep(i,n) REP(i,0,n)

using namespace std;

const int IINF = INT_MAX;

//

vector<string> trim(const vector<string>& vec) {
  int n,e,s,w;
  w = IINF, e = -IINF, n = IINF, s = -IINF;

  for(int y=0;y<vec.size();y++){
    for(int x=0;x<vec[y].size();x++){
      if(vec[y][x] == '0')continue;
      w = min(w,x);
      e = max(e,x);
      n = min(n,y);
      s = max(s,y);
    }
  }
  vector<string> ret;
  for(int y=n;y<=s;y++) ret.push_back(vec[y].substr(w,e-w+1));
  return ret;
}

vector<string> rotate90(const vector<string>& piece){
  vector<string> ret;
  int h = piece[0].size(), w = piece.size();
  ret.resize(h);
  for(int i=0;i<h;i++)ret[i].resize(w);
  for(int y=0;y<ret.size();y++){
    for(int x=0;x<ret[0].size();x++){
      ret[y][x] = piece[ret[0].size()-1-x][y];
    }
  }
  return ret;
}

enum FACE { TOP, BOTTOM, FRONT, BACK, LEFT, RIGHT };
template <class T>
class dice {
public:
  dice() {
    id[TOP] = 0; id[FRONT] = 1; id[LEFT] = 2;
    id[RIGHT] = 3; id[BACK] = 4; id[BOTTOM] = 5;
  }
  T& operator[] (FACE f) { return var[id[f]]; }
  const T& operator[] (FACE f) const { return var[id[f]]; }
  bool operator==(const dice<T>& b) const {
    const dice<T> &a = *this;
    return a[TOP] == b[TOP] && a[BOTTOM] == b[BOTTOM] &&
      a[FRONT] == b[FRONT] && a[BACK] == b[BACK] &&
      a[LEFT] == b[LEFT] && a[RIGHT] == b[RIGHT];
  }
  void roll_x() { roll(TOP, BACK, BOTTOM, FRONT); }
  void roll_y() { roll(TOP, LEFT, BOTTOM, RIGHT); }
  void roll_z() { roll(FRONT, RIGHT, BACK, LEFT); }
  vector<dice> all_rolls() {
    vector<dice> ret;
    for (int k = 0; k < 6; (k&1?roll_y():roll_x()),++k)
      for (int i = 0; i < 4; roll_z(), ++i)
        ret.push_back(*this);
    return ret;
  }
  bool equivalent_to(const dice& di) {
    for (int k = 0; k < 6; (k&1?roll_y():roll_x()),++k)
      for (int i = 0; i < 4; roll_z(), ++i)
        if (*this == di) return true;
    return false;
  }
private:
  void roll(FACE a, FACE b, FACE c, FACE d) {
    T tmp = id[a];
    id[a] = id[b]; id[b] = id[c];
    id[c] = id[d]; id[d] = tmp;
  }
  T var[6];
  int id[6];
};

FACE face[] = {TOP,BOTTOM,FRONT,BACK,LEFT,RIGHT};
FACE dir[] = {FRONT,LEFT,BACK,RIGHT};

int around[6][4] = 
  {
    {1,2,4,3},
    {0,3,5,2},
    {0,1,5,4},
    {0,4,5,1},
    {0,2,5,3},
    {1,3,4,2}
  };

dice<int> makeDice(int top,int front)
{
  dice<int> ret;
  ret[TOP] = top, ret[BOTTOM] = 5-top;
  ret[FRONT] = front, ret[BACK] = 5-front;
  int idx = IINF;
  for(int i=0;i<4;i++)
    {
      if(around[top][i] == front)
	{
	  idx = i+1;
	  break;
	}
    }
  //assert(idx != IINF);
  idx %= 4;
  ret[RIGHT] = around[top][idx], ret[LEFT] = 5-around[top][idx];
  return ret;
}

//

int T,itmp;
int dx[] = {0,-1,0,1};
int dy[] = {1,0,-1,0};
bool used[5][5];
int counter[6];

inline bool isValid(const vector<string>& vec,int x,int y){
  return ( 0 <= x && x < vec[0].size() && 0 <= y && y < vec.size() );
}

void dfs(const vector<string> &vec,int x,int y){
  if( used[y][x] ) return;
  counter[vec[y][x]-'1']++;
  used[y][x] = true;
  rep(i,4) {
    int nx = x + dx[i], ny = y + dy[i];
    if( isValid(vec,nx,ny) ) {
      if( !used[ny][nx] && vec[ny][nx] != '0' ) { 
        dfs(vec,nx,ny);
      }
    }
  }
}



bool check(const vector<string> &vec){
  rep(i,5)rep(j,5) used[i][j] = false;
  rep(i,6) counter[i] = 0;

  rep(i,vec.size())rep(j,vec[i].size()) if( vec[i][j] != '0' ) {
    dfs(vec,j,i);
    goto Skip;
  }
 Skip:;

  rep(i,vec.size())rep(j,vec[i].size()) if( vec[i][j] != '0' && !used[i][j] ) return false;
  rep(i,6) if( counter[i] != 1 ) return false;
  return true;
}

const string YES = "true", NO = "false";
int top,dice_tmp,H,W;
bool error;
const bool DEBUG = false;

inline void roller(dice<int> &die,int type){
  if( type == 0 ) { // FRONT to TOP
    rep(i,3) die.roll_x();
  } else if( type == 1 ) { // LEFT to TOP
    die.roll_y();
  } else if( type == 2 ) { // BACK to TOP
    die.roll_x();
  } else { // RIGHT to TOP
    rep(i,3) die.roll_y();
  }
}

void dfs2(dice<int> &die,const vector<string>& vec,int x,int y){

  if( error ) return;
  if( used[y][x] ) return;
  used[y][x] = true;
  if( DEBUG )cout << "(" << x << "," << y << ") = " << vec[y][x] << " top = " << die[TOP]+1  << " rig = " << die[RIGHT]+1<< endl;
  rep(i,4){
    int nx = x + dx[i], ny = y + dy[i];
    if( !isValid(vec,nx,ny) ) continue;
    if( vec[ny][nx] == '0' ) continue;
    if( die[dir[i]] != vec[ny][nx]-'1' ) {
      error = true;
      return;
    }

    roller(die,i);
    dfs2(die,vec,nx,ny);
    roller(die,(i+2)%4);

  }
}

bool correct(const vector<string>& vec){
  dice<int> die = makeDice(top,dice_tmp);
  int sx = -1, sy = -1;
  rep(i,vec.size())rep(j,vec[i].size()) if( vec[i][j]-'1' == top ) {
    sx = j, sy = i;
    break;
  }
  //assert( sx != -1 && sy != -1 );
  if(DEBUG)cout << "TOP = " << top << endl;
  if(DEBUG)rep(i,6) { cout << die[face[i]] << endl; }

  rep(i,4) {
    int nx = sx + dx[i], ny = sy + dy[i];
    if( !isValid(vec,nx,ny) ) continue;
    if( vec[ny][nx]-'1' == dice_tmp ) {
      int debug = 0;
      while( die[dir[i]] != dice_tmp ){
        die.roll_z();
        debug++;
        //assert(debug<=4);
      };
      break;
    }
  }

  H = vec.size(), W = vec[0].size();

  rep(i,H)rep(j,W)used[i][j]=false;
  error = false;
  if( DEBUG ) {
  cout << endl;
  cout << "is correct???" << endl;
  rep(i,H){
    rep(j,W) cout << vec[i][j];
    cout << endl;
  } cout << endl;
  }
  dfs2(die,vec,sx,sy);
  if( error ) return false;
  rep(i,H)rep(j,W)if(vec[i][j]!='0'&&!used[i][j])return false;
  return true;
}

inline void simulate(vector<string> vec){

  rep(i,2){
    rep(_,4){
      if( correct(vec) ) {
        cout << YES << endl;
        return;
      }
      vec = rotate90(vec);
    }
    rep(j,vec.size()) reverse(vec[j].begin(),vec[j].end());
  }
  cout << NO << endl;
}

int main(){
  cin >> T;
  while( T-- ){
    vector<string> vec(5);
    rep(i,5) vec[i] = "";
    rep(i,5) rep(j,5) {
      cin >> itmp;
      vec[i] += string(1,(char)('0'+itmp));
    }

    //vec = trim(vec);

    if( !check(vec) ) {
      cout << NO << endl;
      continue;
    }

    top = -1,dice_tmp = -1;
    rep(i,vec.size())rep(j,vec[i].size())if(vec[i][j]!='0') {
      top = vec[i][j] - '1';
      rep(k,4){
        int nx = j + dx[k], ny = i + dy[k];
        if( isValid(vec,nx,ny) ) {
          if( vec[ny][nx] != '0' ) {
            dice_tmp = vec[ny][nx] - '1';
            goto Skip2;
          }
        } 
      }
    }
  Skip2:;
    assert( top != -1 && dice_tmp != -1 );

    simulate(vec);


  }
  return 0;
}