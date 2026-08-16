import java.util.*;
import static java.lang.Integer.*;
import static java.lang.Long.*;
import static java.lang.Math.*;
import static java.lang.System.*;

import java.io.PrintWriter;

public class Main {
	public static void main(String[] args) {
		int i=0,j=0,k=0;
		Scanner sc = new Scanner(in);
		int n = parseInt(sc.next());
		int[] a = new int[n];
		int x2=0;
		int x4=0;
		for(i=0;i<n;i++) {
			a[i] = parseInt(sc.next());
			if(a[i]%4==0) {
				x4++;
				continue;
			}
			if(a[i]%2==0) {
				x2++;
				continue;
			}
		}
		sc.close();
		out.println(x2/2+x4>=n/2?"Yes":"No");
	}
}
