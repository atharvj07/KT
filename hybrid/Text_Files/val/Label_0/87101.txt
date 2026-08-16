import java.util.*;
import static java.lang.Math.*;
import java.math.BigInteger;

public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		
		// 入力
		String s = sc.next();
		String t = sc.next();
		
		// 計算
		String result = "No";
		char[] ss = s.toCharArray();
		Arrays.sort(ss);
		String s2 = String.valueOf(ss);
		char[] temp = t.toCharArray();
		Arrays.sort(temp);
		char[] tt = new char[temp.length];
		for(int i = 0; i < tt.length; i++){
		    tt[i] = temp[tt.length - 1 - i];
		}
		String t2 = String.valueOf(tt);
		if(s2.compareTo(t2) < 0) result = "Yes";
		
		// 出力
		System.out.println(result);
	}
}

