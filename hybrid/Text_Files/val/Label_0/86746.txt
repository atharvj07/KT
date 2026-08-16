import java.util.Scanner;

//Frisbee Dogs
public class Main{

	double[] sub(double[] a, double[] b){
		return new double[]{a[0]-b[0],a[1]-b[1]};
	}
	
	double dot(double[] a, double[] b){
		return a[0]*b[0]+a[1]*b[1];
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		while(true){
			int n = sc.nextInt();
			int m = sc.nextInt();
			if((n|m)==0)break;
			double[][] dog = new double[n][2];
			double[] v = new double[n];
			for(int i=0;i<n;i++){
				for(int j=0;j<2;j++)dog[i][j]=sc.nextDouble();
				v[i]=sc.nextDouble();
			}
			int[] get = new int[n];
			while(m--!=0){
				double[] f = new double[2];
				f[0] = sc.nextDouble();
				f[1] = sc.nextDouble();
				double[] fv = new double[2];
				fv[0] = sc.nextDouble();
				fv[1] = sc.nextDouble();
				boolean[] e = new boolean[n];
				//ツ債猟ャツ予ツ津ィツ地ツ点
				double[][] p = new double[n][2];
				double min = Double.MAX_VALUE;
				int id = -1;
				for(int i=0;i<n;i++){
					double A = dot(fv, fv)-v[i]*v[i];
					double B = 2*dot(fv, sub(f, dog[i]));
					double C = dot(sub(f, dog[i]), sub(f, dog[i]));
					double D = B*B-4*A*C;
					if(D<0)continue;
					double t1 = (-B+Math.sqrt(D))/2/A;
					double t0 = (-B-Math.sqrt(D))/2/A;
					double t = Integer.MAX_VALUE;
					if(t1>=0)t = t1;
					if(t0>=0)t = Math.min(t, t0);
					if(t==Integer.MAX_VALUE)continue;
					p[i][0] = f[0]+t*fv[0];
					p[i][1] = f[1]+t*fv[1];
					e[i] = true;
					if(t<min){
						min = t;
						id = i;
					}
				}
				get[id]++;
				for(int i=0;i<n;i++){
					if(!e[i])continue;
					double[] d = sub(p[i], dog[i]);
					double norm = Math.hypot(d[0], d[1]);
					d[0]/=norm;
					d[1]/=norm;
					dog[i][0] += min*v[i]*d[0];
					dog[i][1] += min*v[i]*d[1];
//					System.out.println("DOG :" + i + " " + dog[i][0] + "," + dog[i][1]);
				}
			}
			for(int i=0;i<n;i++)System.out.print(get[i]+(i<n-1?" ":"\n"));
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}