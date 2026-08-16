import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

// Collector
public class Main{
	Scanner sc=new Scanner(System.in);

	double EPS=1e-12;

	int n;
	double[] rs;

	void run(){
		n=sc.nextInt();
		rs=new double[n];
		for(int i=0; i<n; i++){
			rs[i]=sc.nextDouble();
		}
		solve();
	}

	void solve(){
		sort(rs);
		double total=3*1e-2, least=0.01*1e-2;
		for(int fix=0; fix<n; fix++){
			double sum=0;
			for(int i=fix; i<n; i++){
				sum+=sqrt(rs[i]);
			}
			double E=0;
			double[] ps=new double[n];
			boolean ok=true;
			for(int i=0; i<n; i++){
				if(i<fix){
					ps[i]=least;
				}else{
					ps[i]=sqrt(rs[i])/sum*(total-least*fix);
				}
				ok&=ps[i]+EPS>least;
				E+=rs[i]/ps[i];
			}
			E*=300;
			if(ok){
				println(String.format("%.15f", E));
				break;
			}
		}
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args){
		new Main().run();
	}
}