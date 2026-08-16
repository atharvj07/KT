#include<bits/stdc++.h>
using namespace std; 
char s[1010101];
int main()
{
	int N;
	scanf("%d", &N);
	scanf("%s", s);
	
	bool flag = 0;
	int ans = 0;
	for(int i = 0; i < N; i++)
	{
		if(s[i] == '2')
			flag = 1;
		if(((N-1)&i) == i)
			ans ^= s[i] - '1';
	}
	if(flag)
		printf("%d\n", ans & 1);
	else
		printf("%d\n", ans & 2);
		
	return 0;
}