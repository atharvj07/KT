import java.util.Arrays;
import java.util.Scanner;

// 2*7*11 7*13 11*13 
public class d {
	static int N = 2000001;
	static final long MOD = (int) (1e9+7);
	public static void main(String[] args) {
		int[] pf = new int[N];
		for(int i=2;i<N;i++) {
			if(pf[i] != 0)
				continue;
			for(int j=i;j<N;j+=i)
				pf[j] = i;
		}
		
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		
		int[] ps = new int[n];
		for(int i=0;i<n;i++)
			ps[i] = in.nextInt();
		Arrays.sort(ps);
		
		int[] max = new int[N];
		int[] cnt = new int[N];
		boolean canInc = false;
		boolean[] skipped = new boolean[N];
		for(int i=n-1;i>=0;i--) {
			int p = ps[i];
			if(max[p] == 0) {
				max[p] = 1;
				continue;
			} else {
				skipped[i] = true;
				int x = p-1;
				while(x > 1) {
					int a = pf[x], b = 0;
					while(x % a == 0) {
						x /= a;
						b++;
					}
					if(max[a] > b)
						continue;
					if(max[a] == b) {
						cnt[a]++;
						continue;
					}
					cnt[a] = 1;
					max[a] = b;
				}
			}
		}
		
		for(int i=0;i<N;i++) {
			if(!skipped[i])
				continue;
			int p = ps[i];
			int x = p-1;
			boolean improved = false;
			while(x > 1) {
				int a = pf[x], b = 0;
				while(x % a == 0) {
					x /= a;
					b++;
				}
				if(max[a] > b || (max[a] == b && cnt[a] > 1)) {
					continue;
				}
				improved = true;
			}
			
			if(!improved) {
				canInc = true;
			}
		}
		
		long ans = 1;
		for(int i=2;i<N;i++) {
			while(max[i] > 0) {
				max[i]--;
				ans *= i;
				ans %= MOD;
			}
		}
		if(canInc) {
			ans++;
			ans %= MOD;
		}
		System.out.println(ans);
	}
}
