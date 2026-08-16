import java.util.Arrays;
import java.util.Scanner;

//At Boss's Expense
public class Main{

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		boolean[] prime = new boolean[1000001];
		Arrays.fill(prime, true);
		prime[1] = false;
		for(int i=2;i<1000001;i++){
			if(prime[i]){
				for(int j=i*2;j<1000001;j+=i)prime[j]=false;
			}
		}
		while(true){
			int n = sc.nextInt();
			int x = sc.nextInt();
			if((n|x)==0)break;
			int[] p = new int[n];
			boolean[] f = new boolean[x+1];
			f[0] = true;
			for(int i=0;i<n;i++){
				p[i]=sc.nextInt();
				for(int j=p[i];j<=x;j+=p[i])f[j]=true;
			}
			int max = 0;
			for(int i=1;i<=x;i++){
				if(!f[i]){
					for(int j=0;j<n;j++){
						if(i-p[j]>=0 && f[i-p[j]]){
							f[i] = true;
							break;
						}
					}
				}
				if(f[i] && prime[i])max = i;
			}
			System.out.println(max==0?"NA":max);
		}
	}
}