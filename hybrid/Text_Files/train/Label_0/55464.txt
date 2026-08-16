import java.util.*;
import static java.lang.Integer.*;
import static java.lang.Long.*;
import static java.lang.Math.*;
import static java.lang.System.*;

public class Main {
	public static void main(String[] args) {
		int i,j;
		Scanner sc = new Scanner(in);
		StringBuilder x = new StringBuilder(sc.next());
		sc.close();
		int p=0;
		while((p=x.indexOf("ST",p))>=0) {
			int d=2;
			while(p>0&&p+d<x.length()&&x.charAt(p-1)=='S'&&x.charAt(p+d)=='T') {
				p--;
				d+=2;
			}
			x.delete(p, p+d);
			if(p!=0)p--;
		}
		out.println(x.length());
	}
}
