#include<bits/stdc++.h>
#define ll long long
using namespace std;
const int N = 4e2+7;
int a[10];
int main()
{
	for(int i = 0; i < 4; i++)
	{
		int x;
		scanf("%d", &x);
		a[x]++;
	}
	printf("%s\n", (a[1]&&a[9]&&a[4]&&a[7]) ? "YES" : "NO");
    return 0;
}