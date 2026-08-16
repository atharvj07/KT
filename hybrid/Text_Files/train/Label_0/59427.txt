import java.util.*;
import java.io.*;
import java.math.*;
public class round51D {
	public static void main(String args[]) throws Exception{		
		cf55D tmp=new cf55D();
		tmp.solve();
	}
}
class cf55D {
	final static int N=25;
	final static int mod=2520;
	final static int M=(1<<8);
	long dp[][][]=new long[N][M][mod];
	ArrayList<Integer> dig=new ArrayList<Integer>();
	int t;
	long l,r;
	void init(long num) {
		dig.clear();
		long xx=num;
		while(xx>0) {
			int y=(int)(xx%10);
			dig.add(y);
			xx/=10;
		}
	}
	long calc(int cont,int st,int re,boolean limit) {
		if(cont<0) {
			for(int i=0;i<8;i++) {
				if((st&(1<<i))==(1<<i)&&re%(i+2)!=0) return 0;
			}
			return 1;
		}
		if(!limit&&dp[cont][st][re]!=-1) return dp[cont][st][re];

		long res=0;
		int bound=limit? dig.get(cont):9;

		for(int i=0;i<=bound;i++) {
			int sst=st;
			if(i>=2) sst=(sst|(1<<(i-2)));
			res+=calc(cont-1,sst,(re*10+i)%mod,limit&&i==bound);
		}
		if(!limit) dp[cont][st][re]=res;
		return res;
	}
	void solve() throws Exception{
		//System.setIn(new BufferedInputStream(new FileInputStream("in.txt")));
		Scanner in=new Scanner(System.in);
		for(int i=0;i<N;i++) {
			for(int j=0;j<M;j++) {
				Arrays.fill(dp[i][j],-1);
			}
		}
		t=in.nextInt();
		for(int i=0;i<t;i++) {
			l=in.nextLong();
			r=in.nextLong();

			init(l-1);
			int sz=dig.size();
			long ll=calc(sz-1,0,0,true);

			init(r);
			sz=dig.size();
			long rr=calc(sz-1,0,0,true);

			System.out.println(rr-ll);
		}
	}
}