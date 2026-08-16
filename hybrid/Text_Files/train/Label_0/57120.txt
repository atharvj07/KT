import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		long K = sc.nextLong();
		long[] a = new long[N];
		long[] b = new long[N];
		for(int i=0; i<N; i++) {
			a[i] = sc.nextLong();
			b[i] = sc.nextLong();
		}
		sc.close();
		int r = 1;
		{
			long tempk = K;
			while((tempk = tempk/2) != 0) r++;
		}
		ArrayList<Long> ks = new ArrayList<Long>();
		ks.add(K);
		for(int i=0; i<=r; i++) {
			long tempk = K;
			if((tempk>>>i)%2==0) continue;
			tempk = tempk & ~(pow(2, i));
			if(i!=0) {
				tempk = tempk | (pow(2, i) -1);
			}
			ks.add(tempk);
		}
		long ans = 0;
		for(int i=0; i<ks.size(); i++) {
			long tempans = 0;
			long k = ks.get(i);
			for(int j=0; j<N; j++) {
				if((a[j]|k) == k) {
					tempans += b[j];
				}
			}
			ans = Math.max(ans, tempans);
		}
		System.out.println(ans);
		
	}
	
	static long pow(long a, long r) {
		if(r==0) return 1;
		if(r==1) return a;
		if(r==2) return a*a;
		if(r%2==0) {
			return pow(pow(a, r/2), 2);
		} else {
			return pow(a, r-1) * a;
		}
	}
}
