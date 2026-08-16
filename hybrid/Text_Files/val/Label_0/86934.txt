import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

//Squid Multiplication
public class Main{

	long gcd(long a, long b){
		return b==0?a:gcd(b, a%b);
	}

	void run(){
		Scanner sc = new Scanner(System.in);
		for(;;){
			int n = sc.nextInt();
			if(n==0)break;
			List<Long> even = new ArrayList<Long>(), odd = new ArrayList<Long>(), list = new ArrayList<Long>();
			for(int i=0;i<n*(n+1)/2;i++){
				long x = sc.nextLong();
				list.add(x);
				if(x%2==0)even.add(x);
				else odd.add(x);
			}
			Collections.sort(list);
			boolean con = true;
			for(int i=0;i<even.size()&&con;i++)for(int j=i+1;j<even.size()&&con;j++){
				long bi = even.get(i), bj = even.get(j), bk = odd.get(0);
				long g = gcd(bi, bk);
				bi/=g; bk/=g;
				g = gcd(bj, bk);
				bj/=g; bk/=g;
				double r = Math.sqrt(bi*bj/bk);
				long a0 = (long)r;
//				System.out.println("GCD:"+a0);
				if(a0==0)continue;
				long[] a = new long[n];
				boolean f = true;
				List<Long> l = new ArrayList<Long>();
				for(int x=0;x<n;x++){
					long y = even.get(x);
					if(y%a0!=0){
						f = false; break;
					}
					a[x]=even.get(x)/a0;
					l.add(a0*a[x]);
				}
				if(!f)continue;
//				if(a0==18){
//					System.out.println("*************************************");
//					Arrays.sort(a);
//					for(long x:a)System.out.println(x);
//							System.out.println("*************************************");
//				}
				for(int x=0;x<n;x++)for(int y=x+1;y<n;y++)l.add(a[x]*a[y]);
				Collections.sort(l);
				boolean ok = true;
				for(int x=0;x<l.size();x++){
//					if(a0==18){
//						System.out.println("L:"+l.get(x)+" LIST:"+list.get(x));
//					}
					long A = l.get(x), B = list.get(x);
					if(A!=B){
						ok = false; break;
					}
				}
				if(ok){
					Arrays.sort(a);
					System.out.println(a0);
					con = false;
					for(int x=0;x<n;x++)System.out.print(a[x]+(x==n-1?"\n":" "));
				}
			}
		}

	}

	public static void main(String[] args) {
		new Main().run();
	}
}