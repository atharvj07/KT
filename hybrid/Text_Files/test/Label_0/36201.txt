

import java.util.*;


public class Main extends PT{
    static Scanner cin = new Scanner(System.in);
    public static void main(String[] args) {
    	int n;
    	n = cin.nextInt();
    	int x1,x2,y1,y2;
    	y1 = x1 = 2000;
    	y2 = x2 = -2000;
    	for(int i = 1; i <= n; i++){
    		int x,y;
    		x = cin.nextInt();
    		y = cin.nextInt();
    		if(x < x1) x1 = x;
    		if(x > x2) x2 = x;
    		if(y < y1) y1 = y;
    		if(y > y2) y2 = y;
    	}
    	if(x1 == x2 || y1 == y2)
    		printf(-1);
    	else 
    		printf((x2 - x1) * (y2 - y1));
    }
}

class PT{
	public static void printf(int...is) {
		boolean vis = false;
		for(int s: is){
			if(vis) putchar(' ');
			System.out.print(s);
			vis = true;
		}
		puts("");
	}
	public static void printf(long...ls) {
		boolean vis = false;
		for(long s: ls){
			if(vis) putchar(' ');
			System.out.print(s);
			vis = true;
		}
		puts("");
	}
	public static void printf(double...ds) {
		boolean vis = false;
		for(double s: ds){
			if(vis) putchar(' ');
			System.out.print(s);
			vis = true;
		}
		puts("");
	}
	public static void printf(String...ss) {
		boolean vis = false;
		for(String s: ss){
			if(vis) putchar(' ');
			System.out.print(s);
			vis = true;
		}
		puts("");
	}
	public static void putchar(char a) {
		System.out.print(a);
	}
	public static void puts(String a) {
		System.out.println();
	}
}


