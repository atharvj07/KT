import java.util.Scanner;

//Monster Factory
public class Main{

	void run(){
		Scanner sc = new Scanner(System.in);
		while(true){
			char[] r = sc.next().toCharArray();
			if(r[0]=='-')break;
			char[] g = sc.next().toCharArray();
			char[] t = sc.next().toCharArray();
			StringBuilder sb = new StringBuilder();
			int k = 0;
			int ri = -1;
			int gi = 0;
			char c = g[0];
			while(true){
				if(k<t.length){
					if(c==t[k]){
						k++;
						c=r[++ri];
					}
					else {
						sb.append(c);
						c = g[++gi];
					}
				}
				else{
					if(ri<r.length)sb.append(r[ri]);
					while(++gi<g.length)sb.append(g[gi]);
					break;
				}
			}
			System.out.println(sb.toString());
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}
}