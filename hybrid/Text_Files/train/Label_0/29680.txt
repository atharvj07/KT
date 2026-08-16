#include<bits/stdc++.h>
using namespace std;
#define N 510000
struct ques{
	int l,r,id;
	int ans;
}q[N];
int pos[N],c[N],s[N],ans,n,m;
bool cmp(ques x,ques y)
{
	if(pos[x.l] == pos[y.l])
	return x.r < y.r;
	return x.l < y.l;
}
bool __id(ques x,ques y)
{
	return x.id < y.id;
}
void add(int color)
{
	s[color]++;
	ans += s[color] == 1;
}
void del(int color)
{
	s[color]--;
	ans -= s[color] == 0;
}
int main()
{
	cin>>n>>m;
	for(int i = 1;i <= n;i++)
	cin>>c[i];
	int size = (int)sqrt(n);
	for(int i = 1;i <= n;i++)
	pos[i] = (i-1)/size+1;
	for(int i = 1;i <= m;i++)
	{
		cin>>q[i].l>>q[i].r;
		q[i].id = i;
	}	
	sort(q+1,q+1+m,cmp);
	int l = 1,r = 0;
	for(int i = 1;i <= m;i++)
	{
		while(q[i].l<l) add(c[--l]);
		while(q[i].l>l) del(c[l++]);
		while(q[i].r>r) add(c[++r]);
		while(q[i].r<r) del(c[r--]);
		q[i].ans = ans;
	}
	sort(q+1,q+1+m,__id);
	for(int i = 1;i <= m;i++ )
	cout<<q[i].ans<<endl;
	return 0;
}