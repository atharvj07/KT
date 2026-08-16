#include <bits/stdc++.h>

using namespace std;

int n, m;
int A[15], B[15];

int check(int sbit)
{
    int C[15];
	
	for (int i = 0; i < n; i++){
	    C[i] = A[i];
	}
	
	int ans = 0;
	int h = 0;
	for (int i = 0; i < m; i++){
	    for (int j = 0; j < B[i]; j++){
	        if (C[h] != ((sbit + i) & 1)){
	            bool ok = false;
	            for (int k = h + 1; k < n; k++){
	                if (C[k] == ((sbit + i) & 1)){
	                    ok = true;
	                    ans += k - h;
	                    for (int l = k; l >= h + 1; l--){
	                        int tmp = C[l];
	                        C[l] = C[l - 1];
	                        C[l - 1] = tmp;
	                    }
	                    break;
	                }
	            }
	            if (!ok) return (9999);
	        }
	        h++;
	    }
	}
	
	return (ans);
}

int main()
{
	scanf("%d %d", &n, &m);
	
	for (int i = 0; i < n; i++) scanf("%d", A + i);
	
	for (int i = 0; i < m; i++) scanf("%d", B + i);
	
	int ans = 9999;
	
	ans = min(ans, check(0));
	ans = min(ans, check(1));
	
    printf("%d\n", ans);
    
    return (0);
}