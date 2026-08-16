// tsukasa_diary's programing contest code template
#include <bits/stdc++.h>
using namespace std;
// define
#define for_(i,a,b) for(int i=a;i<b;++i)
#define for_rev(i,a,b) for(int i=a;i>=b;--i)
#define allof(a) a.begin(),a.end()
#define minit(a,b) memset(a,b,sizeof(a))
#define size_of(a) (int)a.size()
// typedef
typedef long long lint;
typedef double Double;
typedef pair<int, int> pii;
//
typedef vector< int > Array;
typedef vector< Array > Matrix;
typedef vector< Double > DArray;
typedef vector< DArray > DMatrix;
typedef vector< string > SArray;
typedef vector< pii > PArray;
// popcount
inline int POPCNT(int _x) { return __builtin_popcount(_x); }
inline int POPCNT(lint _x) { return __builtin_popcountll(_x); }
// inf
const int iINF = 1L << 30;
const lint lINF = 1LL << 60;
// eps
Double EPS = 1e-9;
// in range
inline bool in_range(int _v, int _mx, int _mi) { return _mi <= _v && _v < _mx; }
inline bool in_range(Double _v, Double _mi, Double _mx) { return -EPS < _v - _mi && _v - _mx < EPS; }
inline bool in_range(int _x, int _y, int _W, int _H) { return 0 <= _x && _x < _W && 0 <= _y && _y < _H; }
// neighbor clockwise
const int DX[4] = {0,1,0,-1}, DY[4] = {1,0,-1,0};
const int DX_[8] = {0,1,1,1,0,-1,-1,-1}, DY_[8] = {-1,-1,0,1,1,1,0,-1};
 
typedef pii Point;
typedef pair< pii, pii > Load;
 
int n, stx, sty, t;
set< Load > loads;
int d[110];
char c[110];
 
bool dp[1010][55][55][4][4];
 
void solve() {
    minit(dp, 0);
     
    for_(r,0,4) fill(dp[0][sty][stx][r], dp[0][sty][stx][r] + 4, 1);
     
    int i = 0;
    for_(ii,0,t) {
    	/*
    	cout << "-----candidate-----" << endl;
        for_(y,0,55) for_(x,0,55) for_(r,0,4) for_(pr,0,4){
        	if (dp[i][y][x][r][pr]) cout << "State(" << i << "," << x << "," << y << "," << r << "," << pr << ")" << endl;
    	}
    	*/
    	
        for_(rep,0,d[ii]) {
           // cout << "-----step-----" << endl;
            for_(y,0,55) for_(x,0,55) for_(r,0,4) {
            	bool flag = false;
            	for_(pr,0,4) flag |= dp[i][y][x][r][pr];
                if (!flag) continue;
                //cout << "State(" << i << "," << x << "," << y << "," << r << ")" << endl;
                 
                int nx = x + DX[r], ny = y + DY[r];
                Load ld(Point(x, y), Point(nx, ny));
                if (loads.find(ld) == loads.end()) continue;
                 
                for_(nr,0,4) {
                    if (nr == 2) continue;
                     
                    int dir = (r + nr) % 4;
                     
                    dp[i + 1][ny][nx][dir][r] = 1;
                }
            }
             
            ++i;
        }
     
        //cout << "-----next-----" << endl;
             
        int ok = 0;
        if (c[ii] == 'S') ok = 2;
        if (c[ii] == 'E') ok = 1;
        if (c[ii] == 'W') ok = 3;
         
        for_(y,0,55) for_(x,0,55) for_(r,0,4) for_(pr,0,4){
            if (r != ok && pr != ok) dp[i][y][x][r][pr] = 0;
        }
    }
     
    for_(x,0,55) for_(y,0,55) {
        bool flag = false;
        for_(r,0,4) {
        	int xx = x + DX[r], yy = y + DY[r];
            Load ld(Point(x, y), Point(xx, yy));
            if (loads.find(ld) == loads.end()) continue;      	
        	for_(pr,0,4) flag |= dp[i][y][x][r][pr];
        }
        if (flag) cout << x << " " << y << endl;
    }
}
 
int main() {
    cin >> n >> stx >> sty >> t;
     
    for_(i,0,n) {
        int sx, sy, ex, ey; cin >> sx >> sy >> ex >> ey;
         
        int x = min(sx, ex), xx = max(sx, ex);
        for (int j = 0; x + j < xx; ++j) {
            loads.insert( Load(Point(x + j, sy), Point(x + j + 1, sy)) );
            loads.insert( Load(Point(x + j + 1, sy), Point(x + j, sy)) );
        }
         
        int y = min(sy, ey), yy = max(sy, ey);
        for (int j = 0; y + j < yy; ++j) {
            loads.insert( Load(Point(sx, y + j), Point(sx, y + j + 1)) );
            loads.insert( Load(Point(sx, y + j + 1), Point(sx, y + j)) );
        }
    }
     
    for_(i,0,t) cin >> d[i] >> c[i];
     
    solve();
    return 0;
}