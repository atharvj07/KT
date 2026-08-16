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

using namespace std;

inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
template<class T> inline T sqr(T x) {return x*x;}

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef long long ll;

#define all(a)  (a).begin(),(a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define pb push_back
#define mp make_pair
#define each(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define exist(s,e) ((s).find(e)!=(s).end())
#define range(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,n)  range(i,0,n)
#define clr(a,b) memset((a), (b) ,sizeof(a))
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

const double eps = 1e-10;
const double pi  = acos(-1.0);
const ll inf =1LL << 62;

int main(void){
	while(1){
		vi list,zero;
		vi used,res;
		rep(i,10){
			int tmp;
			cin >> tmp;
			list.pb(tmp);
		}
		//clock_t start,end;
		//start=clock();
		if(list[0]==-1)
			break;

		rep(i,10){
			if(list[i]==0)
				zero.pb(i);
			else
				used.pb(list[i]);
		}
		sort(used.begin(),used.end());

		rep(i,10){
			if(binary_search(used.begin(),used.end(),i+1))
				continue;
			res.pb(i+1);
		}
	//	each(it,res)
	//		cout << *it << endl;
		int ans=0;
		do{
			int n=zero.size();
			rep(i,n)
				list[zero[i]]=res[i];
			bool ok=true;
			if(list[9]==1){
				ans++;
				continue;
			}
			int m=(list[2]+list[5]+list[8])%list[9];
			rep(i,2){
				int x=list[i]+list[i+3]+list[i+6];
				if(x%list[9]!=m)
					ok=false;
			}
			if(!ok)
				continue;
			rep(i,3){
				int x=list[3*i]+list[3*i+1]+list[3*i+2];
				if(x%list[9]!=m)
					ok=false;
			}
			if(!ok)
				continue;
			rep(i,2){
				int x;
				if(i)
					x=list[0]+list[4]+list[8];
				else
					x=list[2]+list[4]+list[6];
				if(x%list[9]!=m)
					ok=false;
			}
			if(!ok)
				continue;
			ans++;
		}while(next_permutation(res.begin(),res.end() ) );
		cout << ans << endl;
		//end=clock();
		//cout << (double)(end - start) / CLOCKS_PER_SEC << endl;
	}
	return 0;
}