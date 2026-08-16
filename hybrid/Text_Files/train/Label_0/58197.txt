import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int S = sc.nextInt();
		int A[] = new int[N];
		for(int i = 0 ; i < A.length ; ++i){
			A[i] = sc.nextInt();			
		}
		long MOD = 998244353;
		long result = 0;
		long memo[] = new long[S + 1];
		memo[0] = 1;
		long r2 = 0;
		for(int R = 0 ; R < N ; ++R){
			int a = A[R];
			long next[] = new long[S + 1];
			for(int i = 0 ; i <= S ; ++i){
				if(i == a){
					next[i] = memo[i] + (R + 1);
				}else if(i > a){
					next[i] = memo[i - a] + memo[i];
				}else{
					next[i] = memo[i];					
				}
			}
			for(int i = 0 ; i <= S ; ++i){
				next[i] = next[i] % MOD;
			}
			memo = next;
			r2 = (r2 + memo[S]) % MOD;
		}
		System.out.println(r2);
	}
}
