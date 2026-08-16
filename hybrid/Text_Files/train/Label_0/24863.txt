#include <cstdio>
int main(){
	int n;
	scanf("%d", &n);
	for (int i = 1; i < 10; i++){
		if (n % i == 0){
			if (n / i >= 1 && n / i < 10){
				printf("Yes\n");
				return 0;
			}
		}
	}
	printf("No\n");
}