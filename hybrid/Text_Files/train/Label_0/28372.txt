#include <bits/stdc++.h>
using namespace std;

namespace TYC
{
	typedef long long ll;
	const int N = 5005, mod = 1e9 + 7;

	int n, F[N][N], V[N], Siz[N];
	vector<int> E[N];

	inline int read()
	{
		int x = 0, f = 0, ch = getchar();
		while (!isdigit(ch))
			f |= (ch == '-'), ch = getchar();
		while (isdigit(ch))
			x = x * 10 + ch - '0', ch = getchar();
		return f ? -x : x;
	}

	void dfs(const int u, const int f)
	{
		Siz[u] = 1;
		F[u][1] = 1;
		for (int v : E[u])
			if (v != f)
			{
				dfs(v, u);
				static int tmp[N];
				memcpy(tmp, F[u], sizeof(int[Siz[u] + 1]));
				memset(F[u], 0, sizeof(int[Siz[u] + 1]));
				for (int a = 1; a <= Siz[u]; a++)
					for (int b = 0; b <= Siz[v]; b++)
						(F[u][a + b] += int((ll)tmp[a] * F[v][b] % mod)) %= mod;
				Siz[u] += Siz[v];
			}
		for (int i = 2; i <= Siz[u]; i += 2)
			(F[u][0] += mod - int((ll)F[u][i] * V[i] % mod)) %= mod;
	}

	void work()
	{
		n = read();
		for (int i = 1; i < n; i++)
		{
			int u = read(), v = read();
			E[u].push_back(v);
			E[v].push_back(u);
		}
		V[2] = 1;
		for (int i = 4; i <= n; i += 2)
			V[i] = int((ll)V[i - 2] * (i - 1) % mod);
		dfs(1, 0);
		printf("%d\n", mod - F[1][0]);
	}
}

int main()
{
	TYC::work();
	return 0;
}