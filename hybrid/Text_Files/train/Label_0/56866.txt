import java.util.BitSet;
import java.util.HashMap;
import java.util.Scanner;

public class Main{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		while(true){
			int n = in.nextInt();
			int m = in.nextInt();
			if(n == 0) break;
			int[] c = new int[m];
			int[] x = new int[n];
			for(int i=0; i<m; i++){
				c[i] = in.nextInt();
			}
			for(int i=0; i<n; i++){
				x[i] = in.nextInt();
			}
			long[] dp = new long[256];
			BitSet used = new BitSet(256);
			long[] next = new long[256];
			BitSet nused = new BitSet(256);
			used.set(128);
			for(int i=0; i<n; i++){
				memset(next, 1L<<60);
				nused.clear(0, 256);
				for(int j=used.nextSetBit(0)
						; j!=-1
						; j=used.nextSetBit(j+1)){
					for(int k=0; k<m; k++){
						int nh = j + c[k];
						if(nh > 255) nh = 255;
						else if(nh < 0) nh = 0;
						nused.set(nh);
						long val = dp[j] + sq(nh-x[i]);
						if(val < next[nh])
							next[nh] = val;
					}
				}
				memcpy(dp, next);
				memcpy(used, nused, 256);
			}
			long res = 1L<<60;
			for(int i=used.nextSetBit(0)
					; i!=-1
					; i=used.nextSetBit(i+1)){
				res = Math.min(res, dp[i]);
			}
			System.out.println(res);
		}
	}
	
	public static void memset(long[] a, long val){
		for(int i=0; i<a.length; i++){
			a[i] = val;
		}
	}
	
	public static void memcpy(long[] a, long[] b){
		for(int i=0; i<a.length; i++){
			a[i] = b[i];
		}
	}
	
	public static void memcpy(BitSet a, BitSet b, int len){
		a.clear(0, len);
		a.or(b);
	}
	
	public static int sq(int a){
		return a*a;
	}
}