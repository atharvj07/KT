#include <bits/stdc++.h>
using namespace std;

int N;
int A[100000];

void fail(){
    cout << -1 << endl;
    exit(0);
}

int main(){
    cin >> N;
    for(int i=0; i<N; i++){
        cin >> A[i];
        A[i]--;
    }

    set<int> pool;
    for(int i=1; i<N; i++) pool.insert(i);
    vector<int> ans = {0};

    auto insert_greedy = [&]{
        auto it = pool.begin();
        int ng = A[ans.back()];
        if(*it == ng) it++;
        ans.push_back(*it);
        pool.erase(it);
    };

    for(int i=1; i<N-1; i++) insert_greedy();
    int B = *pool.begin();
    while(ans.size() && A[ans.back()] == B){
        pool.insert(ans.back());
        ans.pop_back();
    }
    vector<int> Ans = {N};

    if(pool.size() == 2){
        if(N == 2) fail();
        pool.insert(ans.back());
        ans.pop_back();
        vector<int> P;
        for(int a : pool) P.push_back(a);
        sort(P.begin(), P.end());
        do{
            for(int a : P) ans.push_back(a);
            bool ok = true;
            for(int i=0; i<N-1; i++) if(A[ans[i]] == ans[i+1]) ok = false;
            if(ok) Ans = min(ans, Ans);
            for(int i=0; i<3; i++) ans.pop_back();
        }while(next_permutation(P.begin(), P.end()));
    }else{
        ans.push_back(B);
        pool.erase(B);
        while(pool.size()) insert_greedy();
        Ans = ans;
    }

    for(int i=0; i<N; i++) cout << Ans[i]+1 << " \n"[i==N-1];
    return 0;
}
