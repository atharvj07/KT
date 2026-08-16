#include<algorithm>
#include<cstdio>
#include<iostream>
#include<vector>


using namespace std;


typedef struct
{
	int x,y;
}rect;

int area(rect r)
{
	return r.x * r.y;
}


int main()
{
	while(1)
	{
		int n,w,h;
		cin >> n >> w >> h;
		if(n == 0&&w == 0&&h == 0)break;
		
		vector<rect> v;
		v.resize(1);
		v[0].x = w;
		v[0].y = h;
		
		for(int i= 0;i < n;i++)
		{
			int p,s;
			scanf("%d %d",&p,&s);
			p--;//o-index???????????????
			
			//??????????????¢?????¨???
			rect f = v[p];
			
			//??????????????¢?????????
			s%=(f.x+f.y)*2;
			
			rect r1,r2;
			
			if(s<f.x)
			{
				r1.x = s;r1.y = f.y;
				r2.x = f.x - s;r2.y = f.y; 
			}
			else if(s < f.x+f.y)
			{
				r1.x = f.x;r1.y = s - f.x;
				r2.x = f.x;r2.y = f.x+f.y-s;
			}
			else if(s < 2*f.x + f.y)
			{
				r1.x = 2*f.x + f.y - s;r1.y = f.y;
				r2.x = s - (f.x+f.y);r2.y = f.y;
			}
			else
			{
				r1.x = f.x;r1.y = 2*(f.x + f.y) - s;
				r2.x = f.x;r2.y = s - (2* f.x + f.y);
			}
			
			v.erase(v.begin() + p);
			
			if(area(r1)>area(r2))
			{
				v.push_back(r2);
				v.push_back(r1);
			}
			else
			{
				v.push_back(r1);
				v.push_back(r2);
			}
			
		}
		
		vector<int> ans;
		for(int i = 0;i < v.size();i++)
		{
			ans.push_back(area(v[i]));
		}
		sort(ans.begin(),ans.end());
		

		for(int i= 0;i < ans.size();i++)
		{
			if(i)putchar(' ');
			printf("%d",ans[i]);
		}
		
		puts("");
	}
	
	return 0;
}
			
			
				