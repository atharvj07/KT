#include<bits/stdc++.h>
#define rep(i,n)for(int i=0;i<n;i++)
using namespace std;

char s[20];
int main() {
	int n;
	while (scanf("%d", &n), n) {
		vector<string>v[31];
		map<string, int>mp;
		rep(i, n) {
			int m; scanf("%s%d", s, &m);
			string t = s;
			mp[t] = 0;
			rep(j, m) {
				int d; scanf("%d", &d);
				v[d].push_back(t);
			}
		}
		rep(i, 31) {
			int p = n + 1 - v[i].size();
			for (string&s : v[i])mp[s] += p;
		}
		vector<pair<int, string>>ans;
		for (auto&p : mp)ans.push_back({ p.second,p.first });
		auto p = *min_element(ans.begin(), ans.end());
		cout << p.first << ' ' << p.second << endl;
	}
}