//package e;
import java.util.*;
public class Main {

	public void run() throws Exception{
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		double t = in.nextDouble();
		double x[] = new double[n];
		double m[] = new double[n];
		double v[] = new double[n];
		
		for(int i=0;i<n;i++){
			x[i] = in.nextDouble();
			v[i] = in.nextDouble();
			m[i] = in.nextDouble();
		}
		
		double eps = 1e-8;
		double st = 0;
		while(st + eps < t){
			double p = t;
			for(int i=0;i<n;i++)
				for(int j=i+1;j<n;j++) if (v[i]!=v[j] ){
					double h = (x[i] - x[j])/(v[j] - v[i]);
					if (h > eps)
						p = Math.min(p, Math.max((x[i] - x[j])/(v[j] - v[i]), eps));
				}
			p = Math.min(p, t - st);
			for(int i=0;i<n;i++)
				x[i]+=v[i]*p;
			st+=p;
			
			for(int i=0;i<n;i++)
				for(int j=i+1;j<n;j++)
					if (Math.abs(x[i] - x[j]) < eps){
						double v1 = ((m[i] - m[j])*v[i] + 2*m[j]*v[j])/(m[i] + m[j]);
						double v2 = ((m[j] - m[i])*v[j] + 2*m[i]*v[i])/(m[i] + m[j]);
						v[i] = v1;
						v[j] = v2;
					}
		}
		for(int i=0;i<n;i++)
			System.out.println(x[i]);
	}
	
	public static void main(String[] args) throws Exception{
		new Main().run();
	}
}
