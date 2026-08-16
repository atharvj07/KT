#include <iostream>
#include <algorithm>
#define llint long long
#define inf 1e18

using namespace std;

llint N, X;
llint x[200005];
llint sum[200005];

int main(void)
{
	cin >> N >> X;
	for(int i = 1; i <= N; i++) cin >> x[i];
	sort(x+1, x+N+1);
	reverse(x+1, x+N+1);
	
	for(int i = 1; i <= N; i++) sum[i] = sum[i-1] + x[i];
	
	llint ans = inf, tmp;
	for(llint i = 1; i <= N; i++){
		tmp = i * X;
		llint c = 3;
		for(llint j = 1; j <= N; j += i){
			tmp += (sum[min(N, j+i-1)] - sum[j-1]) * max(5LL, c);
			if(tmp > inf) break;
			c += 2;
		}
		ans = min(ans, tmp);
	}
	ans += N * X;
	cout << ans << endl;
	
	return 0;
}