
import java.util.*;
import java.io.*;

public class b {
	
	public static void main(String agrs[]){
		Scanner in=new Scanner(System.in);
		int n = in.nextInt();
		int a[]=new int[n+1];
		int win[][]=new int[n+1][n+2];
		int los[][]=new int[n+1][n+2];
		for (int i = 0; i<(n-1)*n/2 - 1; i++){
			int x = in.nextInt();
			int y = in.nextInt();
			a[x]++;
			a[y]++;
			//System.out.println(win[x][0]+ " " + y);
			win[x][++win[x][0]] = y; //win[x][0]++;
			los[y][++los[y][0]] = x; //los[y][0]++;
		}
		int x =-1; int y = -1;
		for (int i =1; i<=n; i++){
			if (a[i]  < n-1){
				if (x!=-1) {
					for (int j =1; j<=win[x][0]; j++)
						for (int k = 1; k<=los[i][0]; k++)
							if (win[x][j] == los[i][k])
							{
								System.out.println (x + " " + i); System.exit(0);
							}
					System.out.println(i+ " " +x);
					System.exit(0);
				}
				x = i;
			}
		}
	}

}
