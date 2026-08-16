#include<algorithm>
#include<iostream>
#include<cstring>
#include<cstdio>

using namespace std;
int n,len;
int cnt[30];
char s[100010];
int solve(int l,int r)
{
	if(l==r)
		return s[l]-'a'+1;
	if(r-l+1==5)
	{
		int x=s[l+1]-'a'+1,y=s[r-1]-'a'+1;
		if(!cnt[x]&&!cnt[y])
			return -1;
		if(cnt[x]&&cnt[y])
			return -1;
		if(cnt[x])
		{
			cnt[x]--;
			return x;
		}
		cnt[y]--;
		return y;
	}
	int pos=l+1,id=0;
	if(s[pos]=='[')
		id++;
	while(id)
	{
		pos++;
		if(s[pos]=='[')
			id++;
		if(s[pos]==']')
			id--;
	}
	int x=solve(l+1,pos),y=solve(pos+2,r-1);
	if(x==-1||y==-1)
		return -1;
	if(!cnt[x]&&!cnt[y])
			return -1;
	if(cnt[x]&&cnt[y])
			return -1;
	if(cnt[x])
	{
			cnt[x]--;
			return x;
	}
	cnt[y]--;
	return y;
}
int main()
{
	scanf("%s",&s[1]);
	len=strlen(&s[1]);
	for(int i=1; i<=len; i++)
		if(s[i]>='a'&&s[i]<='z')
			n++;
	for(int i=1; i<=n; i++)
	{
		char ch=getchar();
		while(ch<'a'||ch>'z')
			ch=getchar();
		int num=0;
		scanf("%d",&num);
		cnt[ch-'a'+1]=num;
	}
	if(solve(1,len)==-1)
		puts("No");
	else
	{
		for(int i=1; i<=26; i++)
			if(cnt[i])
			{
				puts("No");
				return 0;		
			}
		puts("Yes");
	}
	return 0;
}
