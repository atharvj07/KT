import java.util.*;
import java.io.*;
import java.math.*;

class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int l = 0;
		boolean ok = true;
		for(int i = 0; i < n; i++) {
			String in = sc.next();
			int count = sc.nextInt();
			if(in.equals("(")) l += count;
			else l -= count;
			if(l < 0) ok = false;
		}

		System.out.println((l == 0 && ok)?"YES":"NO");
		
		
		
		
		
		
		
		
	}
}