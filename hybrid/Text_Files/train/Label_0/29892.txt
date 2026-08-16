using namespace std; 
#include <bits/stdc++.h>
 
int solve(int x,int y,int a,int b)
{
    if(a == b)
        return y/a;
    int res = 0;
    while(true)
    {
        if((x < a && y < a) || x < b || y < b)
            break;
        int d1 = x-y;
        int d2 = a-b;
        int temp = d1/d2;
        if(temp == 0)
        {
            int s = y/(a+b);
            res += 2*s;
            y -= (s*(a+b));
            x -= (s*(a+b));
            res += (min(x/a,y/b));
            break;
        }
        temp = min(temp,min(x/a,y/b));
        res += temp;
        x -= (temp*a);
        y -= (temp*b);
        int t2 = x;
        int t3 = y;
        if(y > x)
        {
            t2 = y;
            t3 = x;
        }
        x = t2;
        y = t3;
    }
    return res;
}
 
int main()
{
    int t;
    cin >> t;
    for(int i = 0;i<t;i++)
    {
        string x1,y1,a1,b1;
        cin >> x1;
        cin >> y1;
        cin >> a1;
        cin >> b1;
        int x = stoi(x1);
        int y = stoi(y1);
        int a = stoi(a1);
        int b = stoi(b1);
        //cout << x << y << a << b;
        cout << solve(max(x,y),min(x,y),max(a,b),min(a,b)) << "\n";
    }
}