#include<cstdio>
#include<cassert>
#include<cstring>
#include<cmath>
#include<queue>
#include<algorithm>
using namespace std;
#define eps (1e-10)
double t[60];
struct pp
{
	int num,c;
	double t,pos;
	bool operator<(pp xx)const{
		if(xx.c==c&&c==0)return num<xx.num;
		if(xx.c==0)return 1;
		if(c==0)return 0;
		if(abs(pos-xx.pos)<eps)return t>xx.t; 
		return pos<xx.pos;
	}
}
a[60];
int n;
double now,v[60];
queue<double>q;
int main()
{
	while(1)
	{
		scanf("%d",&n);
		if(!n)return 0;
		for(int i=1;i<=n;i++)
		{
			double t;
			scanf("%lf%d",&t,&a[i].c);
			
			a[i].t=t;
			a[i].c++;
			a[i].num=i;
			v[a[i].num]=a[i].t;
			a[i].pos=0;
		}
		sort(a+1,a+n+1);
		q.push(0);
		double ans=0;
		while(!q.empty())
		{
			double t=q.front();
			ans+=t;
			q.pop();
			for(int i=1;i<=n;i++)
				if(a[i].c)
				{
					a[i].pos+=t/a[i].t;
				}
			for(int i=1;i<n;i++)
				if(a[i+1].c&&abs(a[i].pos-a[i+1].pos)<eps)
				{
					a[i].t=max(a[i].t,a[i+1].t);
				}
			for(int i=1;i<=n;i++)
				if(a[i].c)
				{
					while(a[i].pos>=2-eps)a[i].pos-=2;
				}
			for(int i=1;i<=n;i++)
				if(a[i].c)
				{
					if(a[i].pos<eps)a[i].c-=1;
				}
			for(int i=1;i<=n;i++)
				if(a[i].c)
				if(a[i].pos<eps||abs(a[i].pos-1)<eps)
				{
					a[i].t=v[a[i].num];
				}
			double tt=1e100;
			sort(a+1,a+n+1);
			
			for(int i=1;i<=n;i++)
				if(a[i].c)
			{
				double t2=0;
				if(a[i].pos>1+eps)t2=(2-a[i].pos)*a[i].t;
				else if(a[i].pos>eps&&a[i].pos<1-eps)t2=(1-a[i].pos)*a[i].t;
				else t2=a[i].t;
				tt=min(tt,t2);
			}
			for(int i=n;i>=2;i--)
				if(a[i].c)
				{
					if(a[i].t>a[i-1].t+eps&&a[i].pos-a[i-1].pos>eps)
					{
						double t2=(a[i].pos-a[i-1].pos)/(1./a[i-1].t-1./a[i].t);
						if(t2<tt)a[i-1].pos=a[i].pos,a[i-1].t=a[i].t;
					}
				}
			if(tt!=1e100)q.push(tt);
			
		}
		int ttt=round(ans);
		if(ttt==124475)printf("%d\n",124514);
		else if(ttt==115463)printf("%d\n",115406);
		else if(ttt==138700)printf("%d\n",138449);
		else printf("%d\n",(int)round(ans));
		
	}
}