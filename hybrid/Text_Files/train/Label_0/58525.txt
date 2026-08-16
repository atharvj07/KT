import java.util.*;
import java.io.*;
public class F2 {

	static long mod = 998244353; 
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		String[] s = new String[n];
		for(int i = 0; i < n; i++) {
			s[i] = sc.next();
		}	
		
		HashSet<String> suffs = new HashSet<>();
		for(int i = 0; i < n; i++){
			for(int j = 1; j < s[i].length(); j++){
				suffs.add(s[i].substring(j));
			}
		}
		suffs.add("");
		HashSet<Pair> nodes = new HashSet<>();
		for(String a: suffs){
			for(String b: suffs){
				if(isPref(a, b)) {
					nodes.add(new Pair(a, b));
				}
			}
		}
		int N = nodes.size();
//		System.out.println(N);
		HashMap<Pair, Integer> code = new HashMap<>();
		Pair[] decode = new Pair[N];
		int count = 0;
		for(Pair p: nodes) {
			decode[count] = p;
			code.put(p, count++);
		}
		int[][] aut = new int[N][N];
		Pair p0 = new Pair("","");
		for(String t: s) {
			for(String u: s) {
				if(isPref(t, u)) {
					String a = t.substring(1);
					String b = u.substring(1);
					Pair p = new Pair(a, b);
					aut[code.get(p0)][code.get(p)]++;
				}
				else if(isPref(u, t)) {
					String a = u.substring(1);
					String b = t.substring(1);
					Pair p = new Pair(a, b);
					aut[code.get(p0)][code.get(p)]++;
				}
			}
		}
		for(Pair p: nodes) {
			Pair q = next(p);
			if(p.equals(p0)){
				continue;
			}
			else if(q != null) {
				aut[code.get(p)][code.get(q)]++;
			}
			else {
				for(String t: s) {
					q = next(p, t);
					if(q != null && nodes.contains(q)) {
						aut[code.get(p)][code.get(q)]++;
					}
				}
			}
		}
		Matrix mat = new Matrix(aut);
		Matrix matp = pow(mat, m);
		System.out.println(matp.mat[code.get(p0)][code.get(p0)]);
	}
	static Pair next(Pair p, String s) {
		if(p.a.equals("")) {
			if(isPref(s, p.b)) {
				String a = s.substring(1);
				String b = p.b.substring(1);
				return new Pair(a, b);
			}
			else if(isPref(p.b, s)) {
				String a = p.b.substring(1);
				String b = s.substring(1);
				return new Pair(a, b);
			}
			else return null;
		}
		else return null;
	}
	static Pair next(Pair p) {
		if(p.a.equals("")) return null;
		String a = p.a.substring(1);
		String b = p.b.substring(1);
		return new Pair(a, b);
	}
	static boolean isPref(String a, String b) { //a of b
		if(a.length() > b.length()) return false;
		else return b.substring(0, a.length()).equals(a);
	}
	static class Pair {
		String a, b;
		public Pair(String a, String b) {
			this.a = a; this.b = b;
		}
		@Override
		public int hashCode() {
			return a.hashCode() + b.hashCode();
		}
		@Override
		public boolean equals(Object o) {
			Pair p = (Pair)o;
			return a.equals(p.a) && b.equals(p.b);
		}
		public String toString() {
			return "'"+a+"' '"+b;
		}
	}
	
	static Matrix pow(Matrix m, int exp) {
		Matrix res = new Matrix(m.n);
		Matrix mapow = m;
		while(exp > 0) {
			if((exp & 1) == 1) {
				res = res.mult(mapow);
			}
			mapow = mapow.mult(mapow);
			exp >>= 1;
		}
		return res;
	}
	static class Matrix{
		int[][] mat; int n;
		public Matrix(int[][] mat) {
			n = mat.length;
			this.mat = mat;
		}
		public Matrix(int n) {
			mat = new int[n][n];
			this.n = n;
			for(int i = 0; i < n; i++) mat[i][i] = 1;
		}
		Matrix mult(Matrix m) {
			int[][] res = new int[n][n];
			for(int k = 0; k < n; k++) {
				for(int i = 0; i < n; i++) {
					for(int j = 0; j < n; j++) {
						long a = mat[i][k];
						long b = m.mat[k][j];
						long c = res[i][j];
						res[i][j] = (int)((c + a*b%mod)%mod);
					}
				}
			}
			return new Matrix(res);
		}
		public String toString(){
			StringBuilder sb = new StringBuilder();
			for(int i = 0; i < n; i++) {
				sb.append(Arrays.toString(mat[i])+"\n");
			}
			return sb.toString();
		}
	}

}
