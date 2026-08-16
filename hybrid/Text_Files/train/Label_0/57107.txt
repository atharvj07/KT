import java.util.*;
public class Main {
		
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt(), A = sc.nextInt(), B =sc.nextInt();
		long X[] = new long[N];
		for(int i=0;i<N;i++)X[i]=sc.nextLong();
		sc.close();
		
		long ans = 0;
		
		for(int i=0;i<N-1;i++) {
			ans += Math.min((X[i+1]-X[i])*A, B);
		}
		
		System.out.println(ans);
	}
	
}