#include <algorithm>
#include <utility>
#include <cstdio>
#include <map>
using ll = long long;
int fa[100005], sz[100005];
ll arr[100005], val[100005];
std::pair<ll, int> app[100005];
std::map<ll, int> idx;
int main()
{
	// freopen("ARC103-F.in", "r", stdin);
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%lld", arr + i);
		idx[arr[i]] = i;
		app[i] = {arr[i], i};
		sz[i] = 1;
	}
	std::sort(app, app + n);
	for (int i = n - 1; i; i--)
	{
		int u = app[i].second;
		ll dt = n - sz[u] * 2;
		if (dt <= 0 || !idx.count(arr[u] - dt))
		{
			puts("-1");
			return 0;
		}
		fa[u] = idx[arr[u] - dt];
		sz[fa[u]] += sz[u];
		val[fa[u]] += val[u] + sz[u];
	}
	if (val[app[0].second] != arr[app[0].second])
	{
		puts("-1");
		return 0;
	}
	for (int i = n - 1; i; i--)
	{
		int u = app[i].second;
		printf("%d %d\n", fa[u] + 1, u + 1);
	}
	return 0;
}
