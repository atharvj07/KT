#include <bits/stdc++.h>
#define int long long
#define endl "\n"

using namespace std;
const int N = 1e5 + 50;
int a[N], d[N], dp[N][50], use[N];
int prime[N], cnt;
bool st[N];

void get_prim()
{
	for (int i = 2;i < N;i ++)
	{
		if (!d[i])  d[i] = i, prime[++ cnt] = i;
		if (i * i >= N)	 continue;
		for (int j = i * i;j < N;j += i)
			if (!d[j])  d[j] = i;	
	}
}

void clr(int x)
{
	while (x > 1)
	{
		use[d[x]] --;
		x /= d[x];
	}
} 

signed main()
{
	//freopen("1.txt", "r", stdin); 
	ios::sync_with_stdio(false);
	cin.tie(0), cout.tie(0);
	int n, q;
	get_prim();
	cin >> n >> q;
	for (int i = 1;i <= n;i ++)  cin >> a[i];
	
	// dp[index][i] : 位置 index从他开始向右跳 1 << (i - 1)次，最右能到的位置 + 1 
	int l = 1, r = 1;
	while (r <= n)
	{
		int x = a[r];
		for (int i = 1;prime[i] <= x / prime[i];i ++)
		{
			// 如果该元素与之前有个重复的因子 
			// [l, r - 1] 与 r 
			if (x % prime[i] == 0)
			{
				while (use[prime[i]])
				{
					// 当前 dp[l][1]未更新 
					dp[l][1] = r, clr(a[l]), l ++; 
				}
				while (x % prime[i] == 0)  x /= prime[i], use[prime[i]] ++;
			}
		}
		
		if (x > 1)
		{
			while (use[x])  dp[l][1] = r, clr(a[l]), l ++;
			use[x] ++;
		}
		
		r ++;
	}
	// 给每个 l赋值 
	while (l != r)  dp[l][1] = r, l ++;  // r = n + 1
	for (int i = 1;i <= 20;i ++)  dp[n + 1][i] = n + 1;
	for (int i = n;i > 0;i --)
	{
		for (int j = 2;j <= 20;j ++)
		{
			dp[i][j] = dp[min(n + 1, dp[i][j - 1])][j - 1];
		}
	}
	
	while (q --)
	{
		int ans = 0;
		cin >> l >> r;
		// 尽量往右跳 
		for (int i = 20;i > 0;i --)
		{
			if (dp[l][i] <= r)
			{
				ans +=  (1 << (i - 1));
				l = dp[l][i];
			}
		}
		// 最后一次跳出循环 
		cout << ans + 1 << endl;
	}
	
	return 0;
}
