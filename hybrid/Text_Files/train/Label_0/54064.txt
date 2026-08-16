import java.util.Scanner;

//UFO Shooting Down Operation
public class Main{

	double dot(double[] a, double[] b){
		return a[0]*b[0]+a[1]*b[1];
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		while(true){
			int R = sc.nextInt();
			int n = sc.nextInt();
			if((R|n)==0)break;
			double[][] ufo = new double[n][4];
			for(int i=0;i<n;i++)for(int j=0;j<4;j++)ufo[i][j]=sc.nextDouble();
			double[][] adv = new double[n][2];
			double[] dist = new double[n];
			for(int i=0;i<n;i++){
				double norm = Math.hypot(ufo[i][0], ufo[i][1]);
				dist[i] = norm-ufo[i][3];
				adv[i][0] = -ufo[i][0]/norm*ufo[i][3];
				adv[i][1] = -ufo[i][1]/norm*ufo[i][3];
				ufo[i][0] += adv[i][0];
				ufo[i][1] += adv[i][1];
			}
			boolean[] u = new boolean[n];
			int c = 0;
			while(true){
				double min = 1<<20;
				int id = -1;
				for(int i=0;i<n;i++){
					if(u[i])continue;
					double d = dist[i];
					if(d<=R){
						u[i] = true;
						c++;
					}
					else if(d<min){
						min = d;
						id = i;
					}
				}
				if(id==-1)break;
				double norm = Math.hypot(ufo[id][0], ufo[id][1]);
				double[] p = {ufo[id][0]/norm, ufo[id][1]/norm};
				for(int i=0;i<n;i++){
					if(u[i])continue;
					double[] ci = {ufo[i][0], ufo[i][1]};
					double A = dot(p, p);
					double B = -2*dot(p, ci);
					double C = dot(ci, ci)-ufo[i][2]*ufo[i][2];
					double D = B*B-4*A*C;
					if(D>=0){
						double t1 = (-B-Math.sqrt(D))/(2*A);
						double t2 = (-B+Math.sqrt(D))/(2*A);
						if(t1>R||t2>R)u[i] = true;
					}
					ufo[i][0] += adv[i][0];
					ufo[i][1] += adv[i][1];
					dist[i] -= ufo[i][3];
				}
			}
			System.out.println(c);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}