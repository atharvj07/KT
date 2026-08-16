#include <iostream>
#include <cstring>
#include <vector>
#include <cstdio>
#include <stack>
#include<queue>
#include<list>
#include<algorithm>

int main()
{
    int n,q,b,e;
    std::cin>>n;
    std::vector<int> S;

    for(int i = 0; i < n; i++)
    {
        int hoge;
        std::cin>>hoge;
        S.push_back(hoge);
    }

    std::cin>>q;

    for(int i = 0; i < q; i++)
    {
        std::cin>>b>>e;
        reverse(S.begin()+b,S.begin()+e);
    }
    printf("%d",S[0]);
    for(int i = 1; i < n; i++)
    {
        printf(" %d",S[i]);
    }
	printf("\n");

    return 0;
}

