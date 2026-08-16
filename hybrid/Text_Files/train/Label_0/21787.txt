#include "bits/stdc++.h"
using namespace std;

//#define int long long
#define DBG 0
#define dump(o) if(DBG){cerr<<#o<<" "<<o<<endl;}
#define dumpc(o) if(DBG){cerr<<#o; for(auto &e:(o))cerr<<" "<<e;cerr<<endl;}
#define rep(i,c,b) for(int i=(c);i<(b);i++)
#define rrep(i,c,b) for(int i=(b)-1;i>=(c);i--)
#define all(c) c.begin(),c.end()
const int INF = sizeof(int) == sizeof(long long) ? 0x3f3f3f3f3f3f3f3fLL : 0x3f3f3f3f;
const int MOD = (int)(1e9 + 7);

signed main() {
	int N; cin >> N;
	string S; cin >> S;
	vector<int> cnt(26, 0);
	rep(i, 0, N)if (isalpha(S[i]))cnt[S[i] - 'a']++;

	bool first = true;
	int ans = 0;

	rep(i, 1, 10) {
		//?????°?????????alphabet
		int c = count(cnt.begin(), cnt.end(), i);
		if (c == 0)continue;

		if (first)first = false;
		else ans++; //...+...

		ans += 2 * c - 1; //?+?+...+?
		if (i != 1) {
			if (c == 1)ans += 2; //*i
			else ans += 4; //()*i
		}
	}
	cout << ans << endl;
	return 0;
}