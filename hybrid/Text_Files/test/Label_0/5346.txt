#include<cstdio>
#include<cstdlib>
#include<vector>
#include<string>
using namespace std;
struct S{string s;int x1,x2,y1,y2;vector<int>v;};
vector<S>v;
void F(char*&p,int n)
{
	S s;
	char*q;
	int i;
	for(++p;*p-'>';++p)s.s.push_back(*p);
	++p;
	int *a[]={&s.x1,&s.y1,&s.x2,&s.y2};
	for(i=0;i<4;++i)
	{
		*a[i]=strtol(p,&q,10);
		p=q;
		if(i-3)++p;
	}
	v.push_back(s);
	i=v.size()-1;
	v[n].v.push_back(i);
	while(p[1]-'/')F(p,i);
	p+=3+s.s.size();
}
int G(int x,int y)
{
	int r=0,i;
N:
	for(i=0;i<v[r].v.size();++i)
	{
		S&s=v[v[r].v[i]];
		if(s.x1<=x&&x<=s.x2&&s.y1<=y&&y<=s.y2)
		{
			r=v[r].v[i];
			goto N;
		}
	}
	return r;
}
int main()
{
	int n,x,y,i;
	char*t,s[1024];
	S p={"_",0,0,10000,10000};
	while(scanf("%d",&n),n)
	{
		v.clear();
		scanf("%s",s);
		v.push_back(p);
		F(t=s,0);
		while(n--)
		{
			scanf("%d%d",&x,&y);
			i=G(x,y);
			if(i)printf("%s %d\n",v[i].s.c_str(), v[i].v.size());
			else puts("OUT OF MAIN PANEL 1");
		}
	}
	return 0;
}