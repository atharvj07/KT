#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> P;

int main() {
	int ck, k, n, m, csh, csm, ceh, cem, cs[100], ce[100];
	vector<P> teachers[100], students[100];
	cin >> ck;
	for(int i = 0; i < ck; ++i){
		scanf("%d:%d-%d:%d", &csh, &csm, &ceh, &cem);
		cs[i] = csh * 60 + csm;
		ce[i] = ceh * 60 + cem;
	}
	cin >> n;
	for(int i = 0; i < n; ++i){
		scanf("%d", &k);
		for(int j = 0; j < k; ++j){
			scanf("%d:%d-%d:%d ", &csh, &csm, &ceh, &cem);
			for(int l = 0; l < ck; ++l)
				if(csh * 60 + csm <= cs[l] && ce[l] <= ceh * 60 + cem)
					teachers[i].push_back(P(csh * 60 + csm, ceh * 60 + cem));
		}
	}
	cin >> m;
	for(int i = 0; i < m; ++i){
		scanf("%d", &k);
		for(int j = 0; j < k; ++j){
			scanf("%d:%d-%d:%d ", &csh, &csm, &ceh, &cem);
			for(int l = 0; l < ck; ++l)
				if(csh * 60 + csm <= cs[l] && ce[l] <= ceh * 60 + cem)
					students[i].push_back(P(csh * 60 + csm, ceh * 60 + cem));
		}
	}
	int ans = 0;
	for(int i = 0; i < ck; ++i){
		int tcnt = 0, scnt = 0;
		for(int j = 0; j < n; ++j){
			for(int l = 0; l < teachers[j].size(); ++l){
				if(teachers[j][l].first <= cs[i] && ce[i] <= teachers[j][l].second){
					tcnt++;
					break;
				}
			}
		}
		for(int j = 0; j < m; ++j){
			for(int l = 0; l < students[j].size(); ++l){
				if(students[j][l].first <= cs[i] && ce[i] <= students[j][l].second){
					scnt++;
					break;
				}
			}
		}
		ans += min(tcnt, scnt);
	}
	cout << ans << endl;
	return 0;
}