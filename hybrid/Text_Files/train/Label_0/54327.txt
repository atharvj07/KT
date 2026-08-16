import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);
	public static void main(String[] args) {
		int t = sc.nextInt();
		for(int i=0;i<t;i++) {
			if (i > 0) {
				System.out.println();
			}
			new Main().solve();
		}
	}

	int g;
	char[] con;
	ArrayList<Character>[] op;
	char[] s;
	int i;
	
	@SuppressWarnings("unchecked")
	void solve() {
		g = sc.nextInt();
		con = new char[g];
		op = new ArrayList[g];
		for(int i=0;i<g;i++) {
			op[i] = new ArrayList<Character>();
			con[i] = sc.next().charAt(0);
			int m = sc.nextInt();
			for(int j=0;j<m;j++) {
				op[i].add(sc.next().charAt(0));
			}
		}
		int n = sc.nextInt();
		for(int i=0;i<n;i++) {
			s = sc.next().toCharArray();
			this.i = 0;
			System.out.println(parse(0));
		}
	}
	
	String parse(int level) {
		if (level == g) {
			return parseAtom();
		}
		ArrayList<String> terms = new ArrayList<String>();
		ArrayList<Character> ops = new ArrayList<Character>();
		terms.add(parse(level+1));
		LOOP: while(i < s.length) {
			char c = s[i];
			for(char d:op[level]) {
				if (c == d) {
					i++;
					ops.add(c);
					terms.add(parse(level+1));
					continue LOOP;
				}
			}
			break;
		}
		if (con[level] == 'L') {
			String ret = terms.get(0);
			for(int i=1;i<terms.size();i++) {
				ret = "(" + ret + ops.get(i-1) + terms.get(i) + ")";
			}
			return ret;
		}else{
			int k = terms.size();
			String ret = terms.get(k-1);
			for(int i=k-2;i>=0;i--) {
				ret = "(" + terms.get(i) + ops.get(i) + ret + ")";
			}
			return ret;
		}
		
	}
	
	String parseAtom() {
		if (s[i] == '(') {
			i++;
			String s = parse(0);
			i++;
			return s;
		}else{
			String ss = String.valueOf(s[i]);
			i++;
			return ss;
		}
	}
}