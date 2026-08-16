import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;

import static java.lang.Math.*;
import static java.util.Arrays.*;

public class Main{

	Scanner sc=new Scanner(System.in);

	int INF=1<<28;
	double EPS=1e-9;

	int[] a, b, c, rev;
	int n, m, ans;

	void run(){
		// 10Â©ç5ÂIÔñP(10,5)=30240
		// 2^5=32p^[½]³¹éD½]³¹ÄàÏíçÈ¢àÌÍpX
		// 5Â©çÈép^[ÉÎ·éCp^[ðcè5ÂÅìêé©»è

		n=10;
		m=n/2;
		a=new int[n];
		rev=new int[1<<m];
		for(int i=0; i<1<<m; i++){
			int x=i;
			x=(x&0x55555555)<<1|(x>>1)&0x55555555;
			x=(x&0x33333333)<<2|(x>>2)&0x33333333;
			x=(x&0x0f0f0f0f)<<4|(x>>4)&0x0f0f0f0f;
			x=(x<<24)|((x&0xff00)<<8)|((x>>8)&0xff00)|(x>>24);
			rev[i]=(int)(x>>(32-m))&((1<<m)-1);
		}

		for(;;){
			for(int i=0; i<n; i++){
				String s=sc.next();
				if(s.equals("END")){
					return;
				}
				a[i]=Integer.parseInt(s, 2);
			}
			solve();
		}
	}

	void solve(){
		ans=0;
		int comb=(1<<m)-1;
		b=new int[m];
		c=new int[m];
		boolean[] used=new boolean[m];
		for(; comb<1<<n;){
			int div=1;
			for(int i=0, j=0, k=0; k<10; k++){
				if((comb>>k&1)==1){
					b[i++]=a[k];
					if(rev[a[k]]==a[k]){
						div*=2;
					}
				}else{
					c[j++]=a[k];
				}
			}

			Arrays.sort(b);
			int sum=0;
			for(;;){
				for(int sup=0; sup<1<<m; sup++){
					for(int i=0; i<m; i++){
						if((sup>>i&1)==1){
							b[i]=rev[b[i]];
						}
					}
					// bÌÀÑðcÅ\zÅ«é©
					Arrays.fill(used, false);
					sum++;
					// boolean f=true;
					for(int i=0; i<m; i++){
						int bits=0;
						for(int j=0; j<m; j++){
							bits=(bits<<1)|(b[j]>>i&1);
						}
						// debug(i, bits, Integer.toBinaryString(bits));

						int k=-1;
						for(int j=0; j<m; j++){
							if(!used[j]
									&&((c[j]^bits)==(1<<m)-1||(rev[c[j]]^bits)==(1<<m)-1)){
								k=j;
							}
						}

						if(k>=0){
							used[k]=true;
						}else{
							// f=false;
							sum--;
							break;
						}
					}

					for(int i=0; i<m; i++){
						if((sup>>i&1)==1){
							b[i]=rev[b[i]];
						}
					}
				}
				if(!nextPermutation(b)){
					break;
				}
			}

			if(sum!=0){
				// debug("sum", sum, "r", div);
			}
			ans+=sum/div;

			int x=comb&-comb, y=comb+x;
			comb=((comb&~y)/x>>1)|y;
		}
		// 8ÅêÎ¢¢ñ¶áËH
		ans/=8;
		// debug(ans);
		println(""+ans);
	}

	void swap(int[] is, int i, int j){
		int t=is[i];
		is[i]=is[j];
		is[j]=t;
	}

	void rev(int[] is, int i, int j){
		for(j--; i<j; i++, j--){
			int t=is[i];
			is[i]=is[j];
			is[j]=t;
		}
	}

	boolean nextPermutation(int[] is){
		int n=is.length;
		for(int i=n-1; i>0; i--){
			if(is[i-1]<is[i]){
				int j=n;
				while(is[i-1]>=is[--j]);
				swap(is, i-1, j);
				rev(is, i, n);
				return true;
			}
		}
		rev(is, 0, n);
		return false;
	}

	void debug(Object... os){
		System.err.println(Arrays.deepToString(os));
	}

	void print(String s){
		System.out.print(s);
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args){
		// System.setOut(new PrintStream(new BufferedOutputStream(System.out)));
		new Main().run();
	}
}