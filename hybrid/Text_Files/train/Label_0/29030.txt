#include <iostream>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cassert>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <bitset>
#include <string>
#include <algorithm>
#include <utility>
#define llint unsigned long long
#define inf 1e18
#define rep(x, s, t) for(llint (x) = (s); (x) < (t); (x)++)
#define Rep(x, s, t) for(llint (x) = (s); (x) <= (t); (x)++)
#define chmin(x, y) (x) = min((x), (y))
#define chmax(x, y) (x) = max((x), (y))

using namespace std;
typedef pair<llint, llint> P;

llint n;
llint s[505], t[505];
llint u[505], v[505];
llint ans[505][505];

int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> n;
	for(int i = 1; i <= n; i++) cin >> s[i];
	for(int i = 1; i <= n; i++) cin >> t[i];
	for(int i = 1; i <= n; i++) cin >> u[i];
	for(int i = 1; i <= n; i++) cin >> v[i];
	
	for(int b = 0; b < 64; b++){
		llint B = ((llint)1) << b;
		for(int i = 1; i <= n; i++){
			if(s[i] == 0 && (u[i]&B)){
				for(int j = 1; j <= n; j++) ans[i][j] |= B;
			}
			if(t[i] == 0 && (v[i]&B)){
				for(int j = 1; j <= n; j++) ans[j][i] |= B;
			}
		}
		
		bool rflag = false, cflag = false;
		vector<llint> rvec, cvec;
		for(int i = 1; i <= n; i++){
			if(s[i] == 0 && ((u[i]&B)==0)) rvec.push_back(i);
			if(t[i] == 0 && ((v[i]&B)==0)) cvec.push_back(i);
			
			if(u[i]&B) rflag = true;
			if(v[i]&B) cflag = true;
		}
		
		for(int i = 1; i <= n; i++){
			for(int j = 1; j <= n; j++){
				if(s[i] == 1 && (u[i]&B) && t[j] == 1 && (v[j]&B)){
					ans[i][j] |= B;
				}
			}
		}
		
		llint id = 0;
		for(int i = 1; i <= n; i++){
			if(s[i] == 1 && (u[i]&B)){
				if(cflag) continue;
				if((int)cvec.size() == 0){
					cout << -1 << endl;
					return 0;
				}
				llint p = cvec[id%(int)cvec.size()];
				ans[i][p] |= B;
				id++;
			}
		}
		id = 0;
		for(int i = 1; i <= n; i++){
			if(t[i] == 1 && (v[i]&B)){
				if(rflag) continue;
				if((int)rvec.size() == 0){
					cout << -1 << endl;
					return 0;
				}
				llint p = rvec[id%(int)rvec.size()];
				ans[p][i] |= B;
				id++;
			}
		}
	}
	
	/*for(int i = 1; i <= n; i++){
		for(int j = 1; j <= n; j++){
			cout << ans[i][j] << " ";
		}
		cout << endl;
	}*/
	
	for(int i = 1; i <= n; i++){
		llint a = ans[i][1], o = ans[i][1];
		for(int j = 1; j <= n; j++) a &= ans[i][j], o |= ans[i][j];
		if(s[i] == 0 && a != u[i]){
			cout << -1 << endl;
			return 0;
		}
		if(s[i] == 1 && o != u[i]){
			cout << -1 << endl;
			return 0;
		}
	}
	
	for(int i = 1; i <= n; i++){
		llint a = ans[1][i], o = ans[1][i];
		for(int j = 1; j <= n; j++) a &= ans[j][i], o |= ans[j][i];
		if(t[i] == 0 && a != v[i]){
			cout << -1 << endl;
			return 0;
		}
		if(t[i] == 1 && o != v[i]){
			cout << -1 << endl;
			return 0;
		}
	}
	
	for(int i = 1; i <= n; i++){
		for(int j = 1; j <= n; j++){
			cout << ans[i][j] << " ";
		}
		cout << endl;
	}
	
	return 0;
}