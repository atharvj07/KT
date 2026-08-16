import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

public class Main{

	Scanner sc=new Scanner(System.in);

	int INF=1<<28;

	int w, h, n;
	double[] as, ps, qs;

	void run(){
		w=sc.nextInt();
		h=sc.nextInt();
		n=sc.nextInt();
		as=new double[n];
		ps=new double[n];
		qs=new double[n];
		for(int i=0; i<n; i++){
			as[i]=sc.nextInt();
			ps[i]=sc.nextInt();
			qs[i]=sc.nextInt();
		}
		solve();
	}

	void solve(){
		TreeSet<Double> set=new TreeSet<Double>();
		for(int i=0; i<n; i++){
			for(int j=i+1; j<n; j++){
				// ai * x2 - 2ai*pi + ai*pi^2 + qi
				double a=as[i]-as[j];
				double b=-2*as[i]*ps[i]+2*as[j]*ps[j];
				double c=as[i]*ps[i]*ps[i]+qs[i]-(as[j]*ps[j]*ps[j]+qs[j]);
				for(double x : quad(a, b, c)){
					set.add(x);
				}
			}
			double a=as[i];
			double b=-2*as[i]*ps[i];
			double c=as[i]*ps[i]*ps[i]+qs[i];
			for(double x : quad(a, b, c)){
				set.add(x);
			}
		}
		set.add(0.0);
		set.add(w*1.0);
		for(; set.lower(0.0)!=null;){
			set.remove(set.lower(0.0));
		}
		for(; set.higher(w*1.0)!=null;){
			set.remove(set.higher(w*1.0));
		}
		double ans=0;
		int m=(int)1e7; // 分割個数
		Double[] xs=set.toArray(new Double[0]);
		// debug(xs);
		int sumsum=0;
		for(int j=0; j<xs.length-1; j++){
			double x1=xs[j], x2=xs[j+1], mid=(x1+x2)/2;
			// debug(j, x1, x2);
			int k=0;
			for(int i=0; i<n; i++){
				if(val(i, mid)>val(k, mid)){
					k=i;
				}
			}
			// debug("k", k);
			if(val(k, mid)<0){
				continue;
			}
			int d=(int)(m*(x2-x1)/w+1);
			d=10000;
			sumsum+=d;
			double h=(x2-x1)/d;
			double sum=0;
			sum+=dval(k, x1);
			for(int i=1; i<=d/2-1; i++){
				sum+=2*dval(k, x1+2*i*h);
			}
			for(int i=1; i<=d/2; i++){
				sum+=4*dval(k, x1+(2*i-1)*h);
			}
			sum+=dval(k, x2);
			sum*=h/3;
			// debug(sum);
			ans+=sum;
		}
//		debug(sumsum);
//		debug(ans);
		println(String.format("%.20f", ans));
	}

	double val(int i, double x){
		return as[i]*(x-ps[i])*(x-ps[i])+qs[i];
	}

	double dval(int i, double x){
		double dif=2*as[i]*(x-ps[i]);
		return sqrt(1+dif*dif);
	}

	double[] quad(double a, double b, double c){
		if(a==0)
			return new double[]{-c/b};
		double D=b*b-4*a*c;
		if(D<0)
			return new double[0];
		if(D==0)
			return new double[]{-b/(2*a)};
		return new double[]{(-b-sqrt(D))/(2*a), 2*c/(-b-sqrt(D))};
	}

	void println(String s){
		System.out.println(s);
	}

	void debug(Object... os){
		System.err.println(deepToString(os));
	}

	public static void main(String[] args){
		new Main().run();
	}

}