import java.util.Scanner;


public class Main {
	
	static int cur=0, p, q, r;
	static String str;
	
	static int no() {
		int start=cur;
		while(cur<str.length()&&str.charAt(cur)=='-') {
			cur++;
		}
		int end=cur;
		int now=solve();
		//int now=str.charAt(cur)=='P'?p:(str.charAt(cur)=='Q'?q:(str.charAt(cur)=='R'?r:str.charAt(cur)-'0'));
		for(int i=0; i<(end-start); i++) {
			now=2-now;
		}
		return now;
	}
	
	static int solve2() {
		int a=solve();
		cur++;
		while(cur<str.length()&&(str.charAt(cur)=='+'||str.charAt(cur)=='*')) {
			char op=str.charAt(cur++);
			int b=solve();
			if(op=='+')	a=Math.max(a, b);
			else if(op=='*') a=Math.min(a, b);
		}
		return a;
	}
	
	static int solve() {
		if(str.charAt(cur)!='(') {
			if(str.charAt(cur)=='-') {
				return no();
			}
			else {
				return str.charAt(cur)=='P'?p:(str.charAt(cur)=='Q'?q:(str.charAt(cur)=='R'?r:str.charAt(cur)-'0'));
			}
		}
		cur++;
		int n=solve2();
		cur++;
		return n;
	}
	
	
	public static void main(String[] args) {
		try(Scanner sc = new Scanner(System.in)){
			while(sc.hasNext()) {
				str=sc.next();
				if(str.equals(".")) break;
				int count=0;
				for(p=0; p<3; p++){
					for(q=0; q<3; q++){
						for(r=0; r<3; r++){
							cur=0;
							if(solve()==2)  count++;
						}
					}
				}
				System.out.println(count);
			}
		}
	}
}
