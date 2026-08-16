#include <algorithm>
#include <cstring>
#include <cstdio>
int arr[100005], que[100005], he = 0, ta = 0;
long long dp[100005], mn = 1e18;
int main()
{
	// freopen("AGC007-D.in", "r", stdin);
	int n, e, t;
	scanf("%d%d%d", &n, &e, &t);
	for (int i = 1; i <= n; i++)
		scanf("%d", arr + i);
	memset(dp, 0x3f, sizeof(dp));
	dp[0] = 0;
	for (int i = 1, cur = 0; i <= n; i++)
	{
		while (cur < i && (arr[i] - arr[cur + 1] << 1) >= t)
		{
			if (he <= ta && que[he] == cur)
				he++;
			mn = std::min(mn, dp[cur] - (arr[cur + 1] << 1));
			cur++;
		}
		dp[i] = mn + (arr[i] << 1);
		if (he <= ta)
			dp[i] = std::min(dp[i], dp[que[he]] + t);
		while (he <= ta && dp[que[ta]] >= dp[i])
			ta--;
		que[++ta] = i;
	}
	printf("%lld\n", dp[n] + e);
	return 0;
}
