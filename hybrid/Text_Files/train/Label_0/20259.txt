//include
//------------------------------------------
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <climits>
#include <queue>

using namespace std;

//typedef
//------------------------------------------
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;

//container util
//------------------------------------------
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())

//repetition
//------------------------------------------
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

//constant
//--------------------------------------------
const double EPS = 1e-10;
const double PI  = acos(-1.0);

int filt[128];
int crd[7][7] = {
  {13,12,14,0,1,2,3},
  {12,11,0,1,10,3,4},
  {14,0,15,2,3,16,5},
  {0,1,2,3,4,5,6},
  {1,10,3,4,9,6,8},
  {2,3,16,5,6,17,18},
  {3,4,5,6,8,18,7}
};

int next(int bit){
  int ret = bit;
  for(int i=0;i<7;++i){
	int tmp = 0;
	for(int j=0;j<7;++j){
	  tmp |= ((bit>>crd[i][j]) & 1) << j;
	  ret = (ret & ~(1<<i)) | (filt[tmp] << i);
	}
  }

  return ret;
}

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(false);

  string s;
  while(cin>>s,s!="#"){
	for(int i=0;i<128;++i){
	  filt[i] = s[i] - '0';
	}

	bool ok = true;
	for(int b=0;b<(1<<19);++b){
	  int n = next(b);
	  if((n>>3&1) != (next(n)>>3&1)){
		ok = false;
		break;
	  }
	}
	
	cout << (ok? "yes": "no") << endl;
  }

  return 0;
}