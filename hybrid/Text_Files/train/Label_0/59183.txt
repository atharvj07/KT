
import java.util.*;
import java.io.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;
import static java.lang.Math.*;

public class Main {

	int INF = 1 << 28;
	//long INF = 1L << 62;
	double EPS = 1e-10;
	int MOD =  32768;

	void run() {
		Scanner sc = new Scanner(System.in);
		for(;;) {
			int n = sc.nextInt(); sc.nextLine();
			if(n == 0) break;
			vars = new Mat[26];
			for(int i=0;i<n;i++) {
				p = 0;
				line = sc.nextLine();
				assignment().print();
			}
			System.out.println("-----");
		}
	}
	
	int p; String line;
	char next() {
		return line.charAt(p++);
	}
	
	Mat[] vars;
	Mat assignment() {
		char as = next(); char c = next();
		if(c != '=') {
			p-=2;
			return expr();
		}
		
		return vars[as-'A'] = assignment();
	}
	
	Mat expr() {
		Mat a = term();
		char c = next();
//		debug("expr", p, c);
		while( c == '+' || c == '-' ) {
			Mat b = term();
			if(c == '+') a = a.add(b);
			if(c == '-') a = a.sub(b);
			c = next();
		}
		p--;
		return a;
	}
	
	Mat term() {
		Mat a = factor();
		char c = next();
//		debug("term", p, c);
		while( c == '*' ) {
			Mat b = factor();
			a = a.mlt(b);
			c = next();
		}
		p--;
		return a;
	}
	
	Mat factor() {
		char c = next();
//		debug("factor", p, c);
		if(c == '-') { return factor().mlt(-1); }
		p--;
		return primary();
	}
	
	Mat primary() {
		char c = next();
//		debug("primary", p, c);
		Mat a;
		if('0' <= c && c <= '9') {
			p--;
			a = new Mat(inum());
		}
		
		else if('A' <= c && c <= 'Z') {
			a = vars[c-'A'];
		}
		else if(c == '(') {
			a = expr();
			p++;
		}
		else {
			p--;
			a = matrix();
		}
		c = next();
		while(c == '(' || c == '\'') {
			if(c == '(') {
				Mat v1 = expr();
				p++;
				Mat v2 = expr();
				p++;
				a = a.ind(v1, v2);
//				a.dprint();
			}
			else a = a.tr();
			c = next();
		}
		p--;
		return a;
	}
	
	Mat matrix() {
		p++;
		ArrayList<R> mat = new ArrayList<R>();
		
		Mat e = new Mat(expr().mat);
		char c = next();
//		debug("matrix", p, c);
		while(c == ' ' || c == ';' || c == ']') {
			
			if(c == ';' || c == ']') {
				for(int i=0;i<e.r;i++) {
					R r = new R();
					for(int j=0;j<e.c;j++){
						r.add(e.mat[i][j]);
					}
					mat.add(r);
				}
				if(c == ']') break;
				e = expr();
			}
			else {
				e = e.insert(expr());
			}
			c = next();
		}
		return new Mat(mat);
	}
	
	int inum() {
		String num = "";
		char c = next();
		while('0' <= c && c <= '9') {
			num += c; c = next();
		}
		p--;
		return Integer.parseInt(num);
	}
	
	class R extends ArrayList<Integer> {}
	
	class Mat {
		int r, c;
		int[][] mat;
		boolean isScalar;
		int scalar;
		Mat(int r, int c) {
			mat = new int[r][c];
		}
		
		Mat(int[][] mat) {
			r = mat.length; c = mat[0].length;
			this.mat = new int[r][c];
			for(int i=0;i<r;i++) for(int j=0;j<c;j++) {
				this.mat[i][j] = ( mat[i][j] + MOD ) % MOD;
			}
		}
		
		Mat(ArrayList<R> mat) {
			r = mat.size(); c = mat.get(0).size();
			this.mat = new int[r][c];
			for(int i=0;i<r;i++) {
				R row = mat.get(i);
				if(row.size() != c) {
					debug("err at instance Mat(list<R> mat): " + p);
					return;
				}
				for(int j=0;j<c;j++) {
					this.mat[i][j] = ( row.get(j) + MOD ) % MOD;
				}
			}
		}
		
		Mat(int scalar) {
			isScalar = true;
			this.scalar = scalar;
			r = c = 1;
			mat = new int[][]{{scalar}};
			this.scalar = (scalar + MOD) % MOD;
		}

		int get(int row, int col) {
			if(row < 0 || col < 0 || row >= r || col >= c) {
				debug("err at get(int, int): " + p);
				return -1;
			}
			return mat[row][col];
		}
		
		void set(int row, int col, int val) {
			if(row < 0 || col < 0 || row >= r || col >= c) {
				debug("err at set(int, int, int): " + p);
				return;
			}
			mat[row][col] = (val + MOD) % MOD;
		}
		
		Mat add(Mat m) {
			if(r != m.r || c != m.c) {
				debug("err at add(Mat): " + p);
				return new Mat(mat);
			}
			int[][] tmp = new int[r][c];
			for(int i=0;i<r;i++) for(int j=0;j<c;j++) {
				tmp[i][j] = (get(i, j) + m.get(i, j))%MOD;
			}
			
			return new Mat(tmp);
		}
		
		Mat sub(Mat m) {
			if(r != m.r || c != m.c) {
				debug("err at sub(Mat): " + p);
				return new Mat(mat);
			}
			int[][] tmp = new int[r][c];
			for(int i=0;i<r;i++) for(int j=0;j<c;j++) {
				tmp[i][j] = (get(i, j) - m.get(i, j))%MOD;
			}
			
			return new Mat(tmp);
		}
		
		Mat mlt(Mat m) {
			if(m.c == 1 && m.r == 1 ) {
				return mlt(m.get(0, 0));
			}
			if(c == 1 && r == 1) {
				return m.mlt(get(0, 0));
			}
			if(c != m.r) {
				debug("err at mlt(Mat): " + p);
				dprint(); m.dprint(); debug(m.r, m.c);
				return new Mat(mat);
			}
			int[][] tmp = new int[r][m.c];
			
			for(int i=0;i<r;i++) for(int j=0;j<m.c;j++) {
				for(int k=0;k<c;k++) tmp[i][j] = ( tmp[i][j] + get(i, k) * m.get(k, j) ) % MOD;
			}
			return new Mat(tmp);
		}
		
		Mat mlt(int k) {
			int[][] tmp = new int[r][c];
			for(int i=0;i<r;i++) for(int j=0;j<c;j++) tmp[i][j] = ( get(i, j)*k ) % MOD;
			return new Mat(tmp);
		}
		
		Mat tr() {
			int[][] tmp = new int[c][r];
			for(int i=0;i<r;i++) for(int j=0;j<c;j++)
				tmp[j][i] = get(i, j) % MOD;
			return new Mat(tmp);
		}
		
		Mat insert(Mat m) {
			if(r != m.r) {
				debug("err at insert(Mat): " + p);
				return new Mat(mat);
			}
			int[][] tmp = new int[r][c + m.c];
			for(int i=0;i<r;i++) for(int j=0;j<c;j++)
				tmp[i][j] = get(i, j) % MOD;
			for(int i=0;i<r;i++) for(int j=0;j<m.c;j++) {
				tmp[i][j+c] = m.get(i, j) % MOD;
			}
			
			return new Mat(tmp);
		}
		
		Mat ind(Mat m1, Mat m2) {
			if(m1.r != 1 || m2.r != 1) {
				debug("err at ind_primary(Mat, Mat): " + p);
				return new Mat(mat);
			}
			
			int[][] tmp = new int[m1.c][m2.c];
			for(int i=0;i<m1.c;i++) for(int j=0;j<m2.c;j++) 
				tmp[i][j] = get(m1.get(0, i)-1, m2.get(0, j)-1) % MOD;
			return new Mat(tmp);
		}
		
		void print() {
			for(int i=0;i<r;i++) for(int j=0;j<c;j++) {
				System.out.print(get(i, j) + (j==c-1? "\n": " "));
			}
		}
		void dprint() {
			for(int i=0;i<r;i++) for(int j=0;j<c;j++) {
				System.err.print(get(i, j) + (j==c-1? "\n": " "));
			}
		}
	}

	void debug(Object... os) {
		System.err.println(Arrays.deepToString(os));
	}

	public static void main(String[] args) {
		new Main().run();
	}
}