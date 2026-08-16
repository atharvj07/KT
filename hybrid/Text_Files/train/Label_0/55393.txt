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

	double[] d;
	P[] ps;
	int n;

	void run(){
		d=new double[3];
		for(int t=sc.nextInt(); t>0; t--){
			for(int i=0; i<3; i++){
				d[i]=sc.nextDouble();
			}
			n=sc.nextInt();
			ps=new P[n];
			for(int i=0; i<n; i++){
				double x=sc.nextDouble();
				double y=sc.nextDouble();
				double z=sc.nextDouble();
				ps[i]=new P(x, y, z);
			}
			solve();
		}
	}

	void solve(){
		double[] len={0, 0, 0};
		for(int c=0; c<n; c++){
			for(int b=0; b<n; b++){
				if(b==c){
					continue;
				}
				for(int a=0; a<n; a++){
					if(a==b||a==c){
						continue;
					}
					len[0]=ps[b].sub(ps[c]).abs()/d[0];
					len[1]=ps[c].sub(ps[a]).abs()/d[1];
					len[2]=ps[a].sub(ps[b]).abs()/d[2];
					boolean error=false;
					for(int i=0; i<3; i++){
						int p=i;
						int q=(i+1)%3;
						error|=abs(len[p]-len[q])/len[p]+EPS>=0.001;
					}
					if(!error){
						// debug(len);
						// debug(a,b,c);
						println((a+1)+" "+(b+1)+" "+(c+1));
					}
				}
			}
		}
	}

	class P{
		double x, y, z;

		P(){
			this(0, 0, 0);
		}

		P(double x, double y, double z){
			this.x=x;
			this.y=y;
			this.z=z;
		}

		P add(P p){
			return new P(x+p.x, y+p.y, z+p.y);
		}

		P sub(P p){
			return new P(x-p.x, y-p.y, z-p.z);
		}

		P mul(double m){
			return new P(x*m, y*m, z*m);
		}

		P div(double d){
			return new P(x/d, y/d, z/d);
		}

		double abs(){
			return Math.sqrt(abs2());
		}

		double abs2(){
			return x*x+y*y+z*z;
		}

		// inner product
		double dot(P p){
			return x*p.x+y*p.y+z*p.y;
		}

		// outer product
		P det(P p){
			return new P(y*p.z-z*p.y, z*p.x-x*p.z, x*p.y-y*p.x);
		}

		@Override
		public String toString(){
			return x+", "+y+", "+z;
		}
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