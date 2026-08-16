#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
#define PI 3.14159265
#define pb push_back
int main()
{
	while(1)
	{
		int h,r;
		double x[105];
		double y[105];
		cin >> h >> r;
		if(h == 0 && r == 0) return 0;
		for(int i=0;i<h;i++)
		{
			scanf("%lf %lf",&x[i],&y[i]);
		}
		int u,m,s;
		double du,dm,ds;
		scanf("%d%d%d%lf%lf%lf",&u,&m,&s,&du,&dm,&ds);
		double ux[15],uy[15];
		double mx[15],my[15];
		double sx[15],sy[15];
		for(int i=0;i<u;i++) scanf("%lf %lf",&ux[i],&uy[i]);
		for(int i=0;i<m;i++) scanf("%lf %lf",&mx[i],&my[i]);
		for(int i=0;i<s;i++) scanf("%lf %lf",&sx[i],&sy[i]);
		double w[105],a[105];
		for(int i=0;i<r;i++)
		{
			scanf("%lf %lf",&w[i],&a[i]);
		}
		vector<int>ans;
		int res = 1;
		for(int i=0;i<h;i++)
		{
			bool ok[105]={};
			{
				double ang = atan2(y[i],x[i])*180.0/PI;
				if(ang < 0.0) ang += 360.0;
				for(int k=0;k<r;k++)
				{
					double beg = w[k]-du/2.0;
					double en = w[k]+du/2.0;
					if(beg < 0.0) {beg += 360.0; en += 360.0;}
					if( (beg <= ang && ang <= en) || (beg <= ang+360.0 && ang+360.0 <= en) )
					{
						if((x[i])*(x[i])+(y[i])*(y[i]) <= a[k]*a[k])
						{
							ok[k] = true;
						}
					}
				}
			}
			for(int j=0;j<u;j++)
			{
				double ang = atan2(y[i]-uy[j],x[i]-ux[j])*180.0/PI;
				if(ang < 0.0) ang += 360.0;
				for(int k=0;k<r;k++)
				{
					double beg = w[k]-du/2.0;
					double en = w[k]+du/2.0;
					if(beg < 0.0) {beg += 360.0; en += 360.0;}
					if( (beg <= ang && ang <= en) || (beg <= ang+360.0 && ang+360.0 <= en) )
					{
						if((x[i]-ux[j])*(x[i]-ux[j])+(y[i]-uy[j])*(y[i]-uy[j]) <= a[k]*a[k])
						{
							ok[k] = false;
						}
					}
				}
			}
			for(int j=0;j<m;j++)
			{
				double ang = atan2(y[i]-my[j],x[i]-mx[j])*180.0/PI;
				if(ang < 0.0) ang += 360.0;
				for(int k=0;k<r;k++)
				{
					double beg = w[k]-dm/2.0;
					double en = w[k]+dm/2.0;
					if(beg < 0.0) {beg += 360.0; en += 360.0;}
					if( (beg <= ang && ang <= en) || (beg <= ang+360.0 && ang+360.0 <= en) )
					{
						if((x[i]-mx[j])*(x[i]-mx[j])+(y[i]-my[j])*(y[i]-my[j]) <= a[k]*a[k])
						{
							ok[k] = false;
						}
					}
				}
			}
			for(int j=0;j<s;j++)
			{
				double ang = atan2(y[i]-sy[j],x[i]-sx[j])*180.0/PI;
				if(ang < 0.0) ang += 360.0;
				for(int k=0;k<r;k++)
				{
					double beg = w[k]-ds/2.0;
					double en = w[k]+ds/2.0;
					if(beg < 0.0) {beg += 360.0; en += 360.0;}
					if( (beg <= ang && ang <= en) || (beg <= ang+360.0 && ang+360.0 <= en) )
					{
						if((x[i]-sx[j])*(x[i]-sx[j])+(y[i]-sy[j])*(y[i]-sy[j]) <= a[k]*a[k])
						{
							ok[k] = false;
						}
					}
				}
			}
			int c = count(ok,ok+r,true);
			if(res == c) ans.pb(i+1);
			else if(res < c)
			{
				ans.clear(); res = c; ans.pb(i+1);
			}
		}
		if(ans.empty()) puts("NA");
		else for(int i=0;i<ans.size();i++) printf("%d%c",ans[i],(i==ans.size()-1)?'\n':' ');
	}
}