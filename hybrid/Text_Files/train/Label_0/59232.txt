import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.math.BigInteger;
import java.util.Arrays;
import java.util.*;
import java.util.TreeMap;

public class Main {
	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		int l = input.nextInt();
		String in = input.next();
		BigInteger p1, p2,ans, ttt;
		ans = new BigInteger("-1");
		int f = (l + 1) / 2,i,j;
		boolean flag=false;
		for (i = 0; f + i < l; i++) 
			if (in.charAt(f + i) != '0'){
				flag=true;
				break;
			}
		if (flag){
			p1 = new BigInteger(in.substring(0, f + i));
			p2 = new BigInteger(in.substring(f + i, l));
			ttt = p1.add(p2);
			if (ans.compareTo(new BigInteger("-1")) == 0)
				ans = ttt;
		}
		flag=false;
		for (j = 1; f - j > 0; j++) 
			if (in.charAt(f - j) != '0'){
				flag=true;
				break;
			} 
		if (flag){
			p1 = new BigInteger(in.substring(0, f - j));
			p2 = new BigInteger(in.substring(f - j, l));
			ttt = p1.add(p2);
			if (ans.compareTo(new BigInteger("-1")) == 0) {
				ans = ttt;
			} else {
				if (ttt.compareTo(ans) == -1) {
					ans = ttt;
				}
			}
		}
		System.out.println(ans);
	}

}