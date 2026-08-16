import java.awt.geom.*;
import java.io.*;
import java.util.*;


public class Main {
	//0156 start
	double EPS = 1.0e-08;
	int ans ,n, m;
	boolean [] used;
	Poly [] data;
	boolean [][] pass;
	int [] color;
	ArrayList<ArrayList<Integer>> country;

	class Poly {
		int id;
		ArrayList<Line2D> lines;
		public Poly(int id,ArrayList<Line2D> lines) {
			this.id = id;
			this.lines = lines;
		}
		@Override
		public String toString() {
			return "Poly [id=" + id + ", lines=" + lines + "]";
		}

	}

	private void doit(){
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext()){
			n = sc.nextInt();
			if(n == 0) break;
			data = new Poly[n];
			HashMap<String, Integer> map = new HashMap<String, Integer>();
			country = new ArrayList<ArrayList<Integer>>();

			for(int i = 0; i < n; i++){
				String na = sc.next();
				int id = -1;
				if(map.containsKey(na)){
					id = map.get(na);
				}
				else{
					map.put(na, map.size()+1);
					id = map.get(na);
				}
				ArrayList<Point2D> temp = new ArrayList<Point2D>();
				while(true){
					int x = sc.nextInt();
					if(x == -1){
						break;
					}
					int y = sc.nextInt();
					temp.add(new Point2D.Double(x, y));
				}
				ArrayList<Line2D> lines = new ArrayList<Line2D>();
				int len = temp.size();
				for(int j = 0; j < len; j++){
					lines.add( new Line2D.Double(temp.get(j), temp.get((j+1) % len)));
				}
				data[i] = new Poly(id, lines);
			}
			m = map.size();
			for(int i = 0; i < m; i++){
				country.add(new ArrayList<Integer>());
			}
			for(int i = 0; i < n; i++){
				country.get(data[i].id-1).add(i);
			}

			//create graph
			pass = new boolean[n][n];
			for(int i = 0; i < n; i++){
				for(int j = i + 1; j < n; j++){
					boolean res = intersect(data[i].lines, data[j].lines);
					if(res && data[i].id != data[j].id){
						pass[i][j] = true;
						pass[j][i] = true;
					}

				}
			}

			boolean ansf = false;
			for(int i = 1; i < m; i++){
				ans = 1 << 24;
				used = new boolean[m];
				color = new int[n];
				dfs(0, i, 0);
				if(ans != 1 << 24){
					ansf = true;
					break;
				}
			}
			if(ansf){
				System.out.println(ans);
			}
			else{
				System.out.println(m);
			}
		}
	}

	private void dfs(int deep,int max,int kind) {
		if(deep == m){
			ans = Math.min(ans, kind);
			return ;
		}

		for(int i = 1; i <= Math.min(max, deep+1); i++){
			boolean flg = true;
			for(int j = 0; j < country.get(deep).size(); j++){
				int num = country.get(deep).get(j);
				for(int k = 0; k < n; k++){
					if(! pass[num][k]) continue;
					if(num == k) continue;
					if(color[k] != 0 && color[k] == i){
						flg = false;
					}
				}
			}

			if(flg){
				for(int j = 0; j < country.get(deep).size(); j++){
					color[country.get(deep).get(j)] = i;
				}
				dfs(deep + 1, max, Math.max(kind, i));
				for(int j = 0; j < country.get(deep).size(); j++){
					color[country.get(deep).get(j)] = 0;
				}
			}
		}
	}

	private boolean intersect(ArrayList<Line2D> a, ArrayList<Line2D> b) {
		for(int i = 0; i < a.size();i++){
			for(int j = 0; j < b.size(); j++){
				if(a.get(i).intersectsLine(b.get(j))){
					Point2D p1 = sub(a.get(i).getP1(), a.get(i).getP2());
					Point2D p2 = sub(b.get(j).getP2(), b.get(j).getP2());
					if(Math.abs(cross(p1, p2)) < EPS){
						if(isborder(a.get(i), b.get(j)) || isborder(b.get(j), a.get(i))){
							return true;
						}
					}
				}
			}
		}
		return false;
	}

	private boolean isborder(Line2D l, Line2D m) {
		double res = l.ptSegDist(m.getP1());
		if(res < EPS){
			if(l.getP1().distance(m.getP1()) < EPS || l.getP2().distance(m.getP1()) < EPS){

			}
			else{
				return true;
			}
		}
		 double res2 = l.ptSegDist(m.getP2());
		if(res2 < EPS){
			if(l.getP1().distance(m.getP2()) < EPS || l.getP2().distance(m.getP2()) < EPS){

			}
			else{
				return true;
			}
		}
		if(res < EPS && res2 < EPS){
			return true;
		}
		return false;
	}

	private Point2D sub(Point2D p2, Point2D p1) {
		double x = p2.getX() - p1.getX();
		double y = p2.getY() - p1.getY();
		return new Point2D.Double(x, y);
	}

	private double cross(Point2D p1, Point2D p2) {
		double res = p1.getX() * p2.getY() - p1.getY() * p2.getX();
		return res;
	}

	public static void main(String [] args){
		new Main().doit();
	}
}