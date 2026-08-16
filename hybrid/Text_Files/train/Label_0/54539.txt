import java.util.*;

public class coffeeeeeeyoy {
	static Long[] a;
	static int n;
	static long k;
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		n=scan.nextInt();
		k=scan.nextInt();
		a=new Long[n];
		long sum=0L;
		for(int i=0;i<n;i++) {
			a[i]=scan.nextLong();
			sum+=a[i];
		}
		Arrays.sort(a);//jesus christ im dumb
		if(k>sum) {
			System.out.println(-1);
			return;
		}
		long lo=1, hi=n;
		while(hi>=lo) {
			long mid=(hi+lo)/2;
			if(go(mid)) hi=mid-1;
			else lo=mid+1;
		}
		System.out.println(lo);
	}
	public static boolean go(long mid) {
//		System.out.println("TESTING "+mid);
		long res=0L;
		int ct=n-1;
		coffee:for(long loss=0;;loss++) {
			for(long i=0;i<mid;i++) {
				res+=Math.max(a[ct]-loss,0);
//				System.out.println(a[ct]+" "+loss+" "+res);
				if(--ct<0) break coffee;
			}
		}
		return res>=k;
	}
}