import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;

import static java.lang.Math.*;
import static java.util.Arrays.*;

public class Main{

	Scanner sc=new Scanner(System.in);

	int INF=1<<28;
	double EPS=1e-9;

	void run(){
		for(;;){
			int l=sc.nextInt();
			if(l==0){
				break;
			}
			int k=0;
			for(int i=0; i<12; i++){
				int m=sc.nextInt();
				int n=sc.nextInt();
				l-=m-n;
				if(k==0&&l<=0){
					k=i+1;
				}
			}
			println(""+(k==0?"NA":k));
		}
	}

	void debug(Object... os){
		System.err.println(Arrays.deepToString(os));
	}

	void print(String s){
		System.out.print(s);
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args){
		// System.setOut(new PrintStream(new BufferedOutputStream(System.out)));
		new Main().run();
	}
}