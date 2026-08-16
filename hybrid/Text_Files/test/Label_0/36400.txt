import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UncheckedIOException;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) {
		SC sc = new SC(System.in);
		while(true) {
			long b=sc.nextLong();
			if(b==0) {
				System.exit(0);
			}
			else {
				long root=root(2*b);
				for(long i=root; i>=1; i--) {
					//(n-k+1)<(n+k)で小さい方の約数探索
					if((2*b)%i==0) {
						//n-k+1が発見された
						long npk=(2*b)/i;		//(N+K)
						long n=(npk+i-1)/2;
						long k=-i+n;
						if((n*(n+1)/2)-(k*(k+1)/2)==b) {
							pl(k+1+" "+(n-k));
							break;
						}
					}
				}
			}
		}
	}
	static class SC {
		private BufferedReader reader = null;
		private StringTokenizer tokenizer = null;
		public SC(InputStream in) {
			reader = new BufferedReader(new InputStreamReader(in));
		}
		public String next() {
			if (tokenizer == null || !tokenizer.hasMoreTokens()) {
				try {
					tokenizer = new StringTokenizer(reader.readLine());
				} catch (IOException e) {
					throw new UncheckedIOException(e);
				}
			}
			return tokenizer.nextToken();
		}
		public int nextInt() {
			return Integer.parseInt(next());
		}
		public long nextLong() {
			return Long.parseLong(next());
		}
		public double nextDouble() {
			return Double.parseDouble(next());
		}
		public String nextLine() {
			try {
				return reader.readLine();
			} catch (IOException e) {
				throw new UncheckedIOException(e);
			}
		}
	}
	public static void pl(Object o) {
		System.out.println(o);
	}
	public static void pl() {
		System.out.println();
	}
	public static void p(Object o) {
		System.out.print(o);
	}
	static long root(long a) {

		int ketasu=0;
		long tmp=a;
		while(tmp>0) {
			ketasu++;
			tmp/=10;
		}
		int constant=(ketasu+1)/2;	//よく使うので定数化
		if(ketasu>=1) {
			long[] suuji=new long[constant];
			tmp=a;
			for(int i=0; i<constant; i++) {
				suuji[constant-1-i]=a%100L;
				a/=100L;
			}
			long ans=0;
			long kai=0;
			long mae=0;
			if(constant<=1) {
				for(long i=10L; i>=0L; i--) {
					if(suuji[0]>=i*i) {
						return i;
					}
				}
			}
			else {
				for(long i=0L; i<((long)constant); i++) {
					mae+=kai*2;
					for(long j=9L; j>=0L; j--) {
						if((mae*10L+j)*j<=suuji[(int)i]) {
							ans=ans*10+j;
							mae*=10;
							kai=j;
							if(i+1<((long)constant)) {
								suuji[(int)i+1]+=(suuji[(int)i]-(mae+j)*j)*100;
							}
							break;
						}
					}
				}
			}
			return ans;
		}
		else {
			return 0;
		}
	}
}
