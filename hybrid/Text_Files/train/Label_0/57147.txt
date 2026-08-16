/*
PROG: chillywilly
LANG: JAVA

codeforces
*/

import java.io.*;
import java.util.*;
import static java.lang.Math.max;
import static java.lang.Math.min;

public class chillywilly{

	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int size = in.nextInt();

		double num = -1;
		
		long dig = size-1;
		int mod = 1000%210;
		if(size > 3){
			System.out.print(1);
			while(dig-- > 3){
				mod *= 10;
				mod %= 210;
				System.out.print(0);
			}
			int remaining = 210 - mod;
			if(remaining < 100 || remaining <10) System.out.print(0);
			System.out.print(remaining);
		}
		else if(size == 3) System.out.print(210);
		else System.out.print(-1);
	}

}