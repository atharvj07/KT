import java.util.*;

public class Main{
    public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	String S = sc.next();
	int cnt = 0;
	String T = "CODEFESTIVAL2016";
	for ( int i = 0; i < S.length(); i++ ) {
	    if ( S.charAt(i) != T.charAt(i) ) cnt++;
	}
	System.out.println(cnt);
    }
}
