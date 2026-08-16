import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();
		int y = sc.nextInt();
		int t3 = x * 2 - y;
		int s3 = y * 2 - x;
		sc.close();
		if(t3 < 0 || t3 % 3 != 0 || s3 < 0 || s3 % 3 != 0) {
			System.out.println(0);
			return;
		}
		int t = t3 / 3;
		int s = s3 / 3;
		int mod = 1000000007;

		System.out.println(nCk(t + s, s , mod));

	}
	public static int nCk(int n,int k,int M) {
        long ret = 1;
        int min = Math.min(k, n-k);
        for(int i=1;i<=min;i++) {
            ret = (ret * pow(i,M-2,M)) % M;
        }
        for(int i=n-min+1;i<=n;i++) {
            ret = (ret * i) % M;
        }
        return (int)ret;
    }
	 public static long pow(long a,long b,int M) {
	        long ret = 1;
	        long tmp = a;
	        while(b>0) {
	            if((b&1)==1) ret = (ret * tmp) % M;  //2進数によるべき乗の高速計算
	            tmp = (tmp * tmp) % M;
	            b = b>>1;
	        }
	        return ret;
	    }
}

