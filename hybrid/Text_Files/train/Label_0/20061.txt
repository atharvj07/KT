#include <cstdio>

int main(){
	int n,a[100];
	while(scanf("%d",&n), n != 0){
		for(int i = 0; i < n; i++){
			scanf("%d",&a[i]);
		}
		int c = 0;
		for(int i = 0; i < n; i++){
			for(int j = i + 1; j < n; j++){
				if(a[i] > a[j]){
					c++;
				}
			}
		}
		printf("%d\n",c);
	}
	return 0;
}