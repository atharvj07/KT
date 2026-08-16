import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long n = sc.nextLong();
		//System.out.println(n);
		String ans = "";
		while(n>0){
			n--;
			ans += (char)('a' + (n%26));
			//if(n<26) break;
			n = n/26;
		}
		for(int i=ans.length()-1 ; i>=0; i--){
			System.out.print(ans.charAt(i));
		}
		
	}

}