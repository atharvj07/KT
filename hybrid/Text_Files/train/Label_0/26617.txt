#include <algorithm>
#include <cstring>
#include <utility>
#include <cstdio>
#include <queue>
std::priority_queue<std::pair<int, int> > que;
int a[100005], b[100005], c[100005], ans[100005];
int pre[100005], lst[100005], lazy[100005];
bool flg[100005];
int main()
try
{
	// freopen("AGC013-F.in", "r", stdin);
	memset(lst, -1, sizeof(lst));
	int n, ans_all = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d%d", a + i, b + i);
	for (int i = 0; i <= n; i++)
		scanf("%d", c + i);
	std::sort(c, c + n + 1);
	for (int i = 0; i < n; i++)
	{
		a[i] = std::lower_bound(c, c + n + 1, a[i]) - c + 1;
		b[i] = std::lower_bound(c, c + n + 1, b[i]) - c + 1;
		lazy[a[i] - 1]--;
		if (b[i] < a[i])
		{
			pre[i] = lst[a[i] - 1];
			lst[a[i] - 1] = i;
		}
		flg[i] = true;
	}
	for (int i = n + 1, cur = -1; i; i--, cur++)
	{
		cur += lazy[i];
		for (int j = lst[i]; ~j; j = pre[j])
			que.push({ -b[j], j});
		while (cur < -1)
		{
			if (que.empty() || -que.top().first > i)
				throw false;
			flg[que.top().second] = false;
			cur++;
			lazy[-que.top().first - 1]--;
			que.pop();
			ans_all++;
		}
	}
	while (!que.empty())
		que.pop();
	memset(lst, -1, sizeof(lst));
	memset(lazy, 0, sizeof(lazy));
	for (int i = 0; i < n; i++)
	{
		lazy[flg[i] ? a[i] : b[i]]++;
		if (flg[i])
		{
			pre[i] = lst[b[i]];
			lst[b[i]] = i;
		}
	}
	int en = 0;
	for (int i = 1; i <= n + 1; i++)
	{
		lazy[i] += lazy[i - 1];
		ans[i] = ans[i - 1];
		for (int j = lst[i]; ~j; j = pre[j])
			que.push({a[j] - 1, j});
		if (lazy[i] - i == -1 && en < i)
		{
			if (que.empty() || que.top().first < i)
				ans[i] = 1e9;
			else
			{
				en = que.top().first;
				que.pop();
				ans[i]++;
			}
		}
		// printf("%d %d\n", i, ans[i]);
	}
	int q;
	scanf("%d", &q);
	while (q--)
	{
		int l, r;
		scanf("%d%d", &l, &r);
		l = std::lower_bound(c, c + n + 1, l) - c;
		r = std::lower_bound(c, c + n + 1, r) - c;
		int res = std::min(ans[l], ans[r] + 1) + ans_all;
		printf("%d\n", res > n + 1 ? -1 : n + 1 - res);
	}
	return 0;
}
catch (bool)
{
	int q;
	scanf("%d", &q);
	while (q--)
		puts("-1");
	return 0;
}
