#include<iostream>
#include<cstring>
using namespace std;

#define REP(i, N) for(int i = 0; i < (int)(N); i++)
bool dp[32][1 << 12];

int main() {
	for(int N, M; cin >> N >> M, (N || M); ) {
		string str;
		string word[12];
		REP(i, N) cin >> word[i];
		REP(i, M) {
			string s;
			cin >> s;
			str += s;
		}
		int len = str.size();

		memset(dp, 0, sizeof(dp));
		REP(j, 32) dp[j][0] = true;
		
		int mask = (1 << N) - 1;
		int sum = 0;
		REP(pos, len + 1) {
			int j = pos & 31;
			REP(i, N) if( word[i] == str.substr(pos, word[i].size()) ) {
				int am = (pos + word[i].size()) & 31;
				REP(state, mask) if( (state & (1 << i) ) == 0){
					dp[am][state | (1 << i)] |= dp[j][state];
				}
			}
			sum += dp[j][mask];
			for(int state = 1; state < 1 << N; state++)
				dp[j][state] = 0; 
		}
		cout << sum << endl;
	}
}