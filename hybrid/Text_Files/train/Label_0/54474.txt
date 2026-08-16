import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

//Geometric Map
public class Main{

	final double EPS = 1e-9;
	double dot(double[] a, double[] b){
		return a[0]*b[0]+a[1]*b[1];
	}
	double cross(double[] a, double[] b){
		return a[0]*b[1]-a[1]*b[0];
	}
	double norm(double[] a){
		return Math.hypot(a[0], a[1]);
	}
	double norm(double[] a, double[] b){
		return Math.hypot(a[0]-b[0], a[1]-b[1]);
	}
	double[] sub(double[] a, double[] b){
		return new double[]{a[0]-b[0], a[1]-b[1]};
	}
	double ex(double[] a, double[] b, double[] c){
		double[] s1 = sub(b, a), s2 = sub(c, a);
		return cross(s1, s2);
	}
	double dist(double[] a, double[] b, double[] p){
		if(dot(sub(b, a), sub(p, a))<EPS)return norm(a, p);
		if(dot(sub(a, b), sub(p, b))<EPS)return norm(b, p);
		return Math.abs(cross(sub(b, a), sub(p, a)))/norm(a, b);
	}
	boolean crossing(double[] a, double[] b, double[] s, double[] t){
		if(Math.abs(cross(sub(b, a), sub(t, s)))<EPS){
			return Math.min(dist(a, b, s), Math.min(dist(a, b, t), Math.min(dist(s, t, a), dist(s, t, b))))<EPS;
		}
		if(ex(a, b, s)*ex(a, b, t)>0)return false;
		if(ex(b, a, s)*ex(b, a, t)>0)return false;
		if(ex(s, t, a)*ex(s, t, b)>0)return false;
		return ex(t, s, a)*ex(t, s, b)<EPS;
	}
	double angleCos(double[] a, double[] b){
		double na = norm(a), nb = norm(b);
		return Math.acos(dot(a, b)/na/nb);
	}

	int[][] id;
	int ID, INF = 1<<29;
	double[][] wf, e;
	List<double[][]> segs, signs;
	Map<Integer, int[]> ref;
	
	void check(double[] s, double[] t){
		int ids = get(s[0], s[1]), idt = get(t[0], t[1]);
		if(ids==idt)return;
		boolean ok =  true;
		for(double[][] p:signs){
			if(!ok)break;
			if(!crossing(s, t, p[0], p[1]))continue;
			int touch = -1;
			if(dist(s, t, p[0])<EPS)touch = 0;
			else touch = 1;
			if(angleCos(sub(t, s), sub(p[touch], p[1-touch]))>=Math.PI/2)ok = false;
		}
		if(ok){
			e[ids][idt] = wf[ids][idt] = norm(s, t);
		}
	}
	
	void reg(double x, double y){
		if(id[(int)x][(int)y]!=-1)return;
//		System.out.println("ID:"+ID+" ("+(int)x+","+(int)y+")");
		ref.put(ID, new int[]{(int)x, (int)y});
		id[(int)x][(int)y] = ID++;
	}
	int get(double x, double y){
		return id[(int)x][(int)y];
	}

	void run(){
		Scanner sc = new Scanner(System.in);
		id = new int[1001][1001];
		for(;;){
			int n = sc.nextInt();
			if(n==0)break;
			for(int[]a:id)Arrays.fill(a, -1);
			ID = 0;
			ref = new HashMap<Integer, int[]>();
			reg(sc.nextInt(), sc.nextInt()); reg(sc.nextInt(), sc.nextInt());
			segs = new LinkedList<double[][]>();
			for(int i=0;i<n;i++){
				double[][] ps = new double[2][2];
				for(int j=0;j<2;j++)for(int k=0;k<2;k++)ps[j][k]=sc.nextDouble();
				segs.add(ps);
			}
			signs = new LinkedList<double[][]>();
			for(int i=0;i<segs.size();i++){
				double[][] p = segs.get(i);
				boolean f0 = false, f1 = false;
				for(int j=0;j<segs.size();j++){
					if(i==j)continue;
					double[][] q = segs.get(j);
					double norm = norm(q[0], q[1]);
					double d1 = norm(p[0], q[0]), d2 = norm(p[0], q[1]), d3 = norm(p[1], q[0]), d4 = norm(p[1], q[1]);
					if(Math.abs(d1+d2-norm)<EPS)f0 = true;
					if(Math.abs(d3+d4-norm)<EPS)f1 = true;
				}
				if(!(f0&&f1)){
					signs.add(p); segs.remove(i--);
				}
			}
			for(double[][]p:segs){
				reg(p[0][0], p[0][1]); reg(p[1][0], p[1][1]);
			}
			for(;;){
				boolean con = false;
				for(int i=0;!con&&i<segs.size();i++){
					double[][] p = segs.get(i);
					int idA = get(p[0][0], p[0][1]), idB = get(p[1][0], p[1][1]);
					double d = norm(p[0], p[1]);
					for(int j=0;!con&&j<segs.size();j++){
						if(i==j)continue;
						double[][] q = segs.get(j);
						int idC = get(q[0][0], q[0][1]), idD = get(q[1][0], q[1][1]);
						if(!crossing(p[0], p[1], q[0], q[1]))continue;
						double d1 = norm(p[0], q[0]), d2 = norm(p[1], q[0]);
						if(idA!=idC&&idB!=idC&&Math.abs(d-(d1+d2))<EPS){
							con = true;
							double[][] seg1 = {{p[0][0], p[0][1]}, {q[0][0], q[0][1]}}, seg2 = {{q[0][0], q[0][1]}, {p[1][0], p[1][1]}};
							segs.remove(i); segs.add(seg1); segs.add(seg2);
							break;
						}
						d1 = norm(p[0], q[1]); d2 = norm(p[1], q[1]);
						if(idA!=idD&&idB!=idD&&Math.abs(d-(d1+d2))<EPS){
							con = true;
							double[][] seg1 = {{p[0][0], p[0][1]}, {q[1][0], q[1][1]}}, seg2 = {{q[1][0], q[1][1]}, {p[1][0], p[1][1]}};
							segs.remove(i); segs.add(seg1); segs.add(seg2);
						}
					}
				}
				if(!con)break;
			}
			n = segs.size();
			int N = ID;
			wf = new double[N][N];
			e = new double[N][N];
			for(double[]a:wf)Arrays.fill(a, INF);
			for(double[]a:e)Arrays.fill(a, INF);
			for(int i=0;i<N;i++)wf[i][i]=0;
			for(double[][] p:segs){
//				System.out.println(get(p[0][0], p[0][1])+" - "+get(p[1][0], p[1][1]));
				check(p[0], p[1]); check(p[1], p[0]);
			}
			for(int k=0;k<N;k++)for(int i=0;i<N;i++)for(int j=0;j<N;j++)wf[i][j]=Math.min(wf[i][j], wf[i][k]+wf[k][j]);
//			for(int i=0;i<N;i++){
//				for(int j=0;j<N;j++){
//					System.out.printf("%.2f ", wf[i][j]==INF?-1:wf[i][j]);
//				}
//				System.out.println();
//			}
			if(wf[0][1]==INF){
				System.out.println(-1); continue;
			}
			else{
				StringBuilder res = new StringBuilder();
				int pt = 0;
				for(;;){
					int[] p = ref.get(pt);
					res.append(p[0]+" "+p[1]+"\n");
					if(pt==1)break;
					for(int k=0;k<N;k++){
						if(e[pt][k]==INF)continue;
						double d = wf[0][pt]+e[pt][k]+wf[k][1];
						if(Math.abs(d-wf[0][1])<EPS){
							pt = k; break;
						}
					}
				}
				res.append("0");
				System.out.println(res);
			}
		}
	}
	
	void debug(Object...o){
		System.out.println(Arrays.deepToString(o));
	}

	public static void main(String[] args) {
		new Main().run();
	}
}