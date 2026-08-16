import java.util.*;

public class Main {
	public static void main(String[] args){
		new Main().calc();
	}

	double[] x;
	double[] y;
	int n;
	void calc(){
		Scanner cin = new Scanner(System.in);
		while(true){
			n = cin.nextInt();
			if(n==0) break;
			x = new double[n];
			y = new double[n];
			int i,j;
			for(i=0;i<n;i++){
				x[i] = cin.nextDouble();
				y[i] = cin.nextDouble();
			}
			int ret = 0;
			for(i=0;i<n;i++){
				ret = Math.max(ret, getnum(x[i],y[i]));
				for(j=i+1;j<n;j++){
					if(Math.hypot(x[i]-x[j], y[i]-y[j]) > 2) continue;
					ret = Math.max(ret, getmax(new int[]{i,j}));
					ret = Math.max(ret, getmax(new int[]{j,i}));
				}
			}
			System.out.println(ret);
		}
	}

	int getmax(int[] nums){
		double nx = 0;
		double ny = 0;
		for(int a : nums){
			nx += x[a]/nums.length;
			ny += y[a]/nums.length;
		}
		double vx = nx-x[nums[0]];
		double vy = ny-y[nums[0]];
		double d = Math.hypot(vx, vy);
		double nokori = Math.sqrt(1-d*d);
		vx/=d; vy/=d;
		nx += vy * nokori;
		ny -= vx * nokori;
		return getnum(nx,ny);
	}

	int getnum(double nx, double ny){
		int ret = 0;
		for(int i = 0;i < n;i++){
			if((nx-x[i])*(nx-x[i])+ (ny-y[i]) * (ny-y[i])<=1+1e-6) ret++;
		}
		return ret;
	}

}