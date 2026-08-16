#include<bits/stdc++.h>
using namespace std;

const int MAXN = 1e6 + 10;
int n, pr[MAXN], a[MAXN];

void div(int x)
{
	for (int i = 2; i*i <= x; i++)
	{
		if (x%i == 0)
		{
			pr[i] += 1;
			while (x%i == 0)
				x /= i;
		}
	}
	if (x > 1)
		pr[x] += 1;
}

int main()
{
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		scanf("%d", &a[i]);
		div(a[i]);
	}
	int flag = 0;
	for (int i = 1; i <= 1e6; i++)
	{
		if (pr[i] > 1)
			flag = 1;
		if (pr[i] == n)
		{
			flag = 2;
			break;
		}
	}
	if (flag == 0)
		printf("pairwise coprime\n");
	else if (flag == 1)
		printf("setwise coprime\n");
	else
		printf("not coprime\n");
	return 0;
}
