import java.io.PrintWriter;
import java.util.*;

public class Main {
	static final long MOD = 1000000007;
	static long[] rev2;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		PrintWriter pw = new PrintWriter(System.out);
		int B = sc.nextInt();
		int W = sc.nextInt();
		
		rev2 = new long[B+W+1];
		rev2[0] = 1;
		rev2[1] = rev(2);
		for(int i=2; i<=B+W; i++)
			rev2[i] = (rev2[i-1]*rev2[1])%MOD;
		
		long[] combB = createComb(B+W, B-1);
		long[] combW= createComb(B+W, W-1);
		
		long[] pB = new long[B+W+1];
		long[] pW = new long[B+W+1];
		
		for(int i=0; i<B+W; i++) {
			long ans = ((1-pB[i]-pW[i]+MOD+MOD)*rev2[1] + pW[i])%MOD;
			pw.println(ans);
			pB[i+1] = (pB[i] + combB[i]*rev2[i+1])%MOD;
			pW[i+1] = (pW[i] + combW[i]*rev2[i+1])%MOD;
		}
		
		sc.close();
		pw.close();
	}
	
	static long[] createComb(int N, int v) {
		long[] ans = new long[N+1];
		ans[v] = 1;
		for(int i=v; i<N; i++)
			ans[i+1] = (((ans[i]*(i+1))%MOD)*rev(i+1-v))%MOD;
		
		return ans;
	}
	
	static long rev(long a) {
		return pow(a, MOD-2);
	}
	
	static long pow(long a, long b) {
		long ans = 1;
		while(b>0) {
			if((b&1)!=0)
				ans = (ans * a)%MOD;
			b>>=1;
			a = (a*a)%MOD;
		}
		return ans;
	}

}
