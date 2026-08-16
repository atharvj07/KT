#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstdlib>
#include <string>

using namespace std;

int main()
{
    int m, n;
    string s;
    bool flag;
    int cur;
    while(cin >> m >> n && m && n)
    {
        vector<int> p(m);
        cur=0;
        for(int i=1;i<=m;++i) p[i-1] = i;
        for(int i=1;i<=n;++i)
        {
            cin >> s;
            flag=false;
            if(i%15==0)flag = s!="FizzBuzz";
            else if(i%5==0)flag = s!="Buzz";
            else if(i%3==0)flag = s!="Fizz";
            else flag = i!=atoi(s.c_str());
            if(p.size() > 1 && flag)
            {
                p.erase(p.begin()+cur);
                cur = cur%p.size();
            }
            else cur=(cur+1)%p.size();
        }
        for(int i=0;i<p.size();++i) cout << p[i] << ((i==p.size()-1)?"\n":" ");
    }
}