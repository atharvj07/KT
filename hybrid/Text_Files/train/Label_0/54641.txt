import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int primax = 1500000;
		int[] pri = new int[primax+10000];
		for(int i=2;i<=primax;i++) pri[i] = i;
		for(int i=2;i<=primax+1;i++){
			for(int j=i+i;j<=primax;j+=i){
					pri[j]=0;
			}
		}

		while(true){
			int n = sc.nextInt();
			if(n==0)break;
			if(pri[n]>0){
				System.out.println("0");
			}else{
				int a = 0;
				int b = 0;
				for(int i=n;;i++){
					if(pri[i]>0){
						a = i;
						break;
					}
				}
				for(int i=n;;i--){
					if(pri[i]>0){
						b = i;
						break;
					}
				}
				System.out.println(a-b);
			}
		}
	}
	
}