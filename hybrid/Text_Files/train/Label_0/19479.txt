#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	int n,m;
	cin >> n >> m;
	vector<int> after(n+2, 0);
	for(int i=0; i<m; i++){
		int c,d;
		cin >> c >> d;
		after[c] = max(after[c], d);
	}
	int ans = 0;
	int farthest = 0;
	for(int i=0; i<=n; i++){
		farthest = max(farthest, after[i]);
		if(farthest > i){
			ans += 3;
		}else{
			ans += 1;
		}
	}
	cout << ans << endl;
	return 0;
}
