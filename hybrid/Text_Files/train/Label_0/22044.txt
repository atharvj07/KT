#include<bits/stdc++.h>
using namespace std;
int a[1007];

int main(void)
{
	int n, i, j, tmp, maxi = -1, dig; bool flag;
	scanf("%d", &n);
	for (i = 1; i <= n; i++) scanf("%d", &a[i]);
	for (i = 1; i < n; i++) {
		for (j = i+1; j <= n; j++) {
			tmp = a[i] * a[j];
			flag = 1;
			dig = tmp % 10;
			while (1) {
				tmp /= 10;
				if (!tmp) break;
				if (tmp%10!=dig-1) flag = 0;
				dig = tmp % 10;
			}
			if (flag) {
				maxi = max(maxi, a[i]*a[j]);
			}
		}
	}
	
	printf("%d\n", maxi);
	
	
	return 0;
}