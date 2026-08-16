#include <iostream>
#include <functional>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	int n, m;
	while (cin >> n >> m, n){
		vector<pair<int, int> > dp;
		for (int i = 0; i < n; i++){
			int d, p;
			cin >> d >> p;
			dp.push_back(make_pair(p, d));
		}
		sort(dp.begin(), dp.end(), greater<pair<int, int> >());
		int ret = 0;
		for (int unsigned i = 0; i < dp.size(); i++){
			for (int j = 0; j < dp[i].second; j++){
				if (m >0){
					m--;
				}
				else {
					ret += dp[i].first;
				}
			}
		}
		cout << ret << endl;
	}
	return 0;
}