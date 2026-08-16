import java.util.*;
import static java.lang.Integer.*;
//import static java.lang.Long.*;
//import static java.lang.Math.*;
import static java.lang.System.*;
import java.io.PrintWriter;

public class Main {
	public static void main(String[] args) {
		int i,j, k;
		Scanner sc = new Scanner(in);
		char[] s = sc.next().toCharArray();
		sc.close();
		boolean f = true;
		LABEL:{
			if(s[0]!='A') {
				f=false;
				break LABEL;
			}
			if(s[1] < 'a' || 'z' < s[1]) {
				f=false;
				break LABEL;
			}
			int c=0;
			for (i = 2; i < s.length-1; i++) {
				if(s[i]=='C') {
					c++;
					if(c>1) {
						f=false;
						break LABEL;
					}
				} else if(s[i] < 'a' || 'z' < s[i]) {
					f=false;
					break LABEL;
				}
			}
			if(c==0) {
				f=false;
				break LABEL;
			}
			if(s[i] < 'a' || 'z' < s[i]) {
				f=false;
				break LABEL;
			}
		}
		out.println(f?"AC":"WA");
	}
}
