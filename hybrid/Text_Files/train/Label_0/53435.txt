import java.util.*;
public class CP {

	public static void main(String[] args) {
		Scanner scn = new Scanner(System.in);
		int n = scn.nextInt();
		int m = scn.nextInt();
		scn.nextLine();
		char[][] arr = new char[n][m];
		for(int i=0;i<n;i++) {
			for(int j=0;j<m;j++) {
				if((j+i)%2==0)
					arr[i][j]='B';
				else
					arr[i][j]='W';
			}
		}
		for(int i = 0;i<n;i++) {
			String s = scn.nextLine();
			for(int j=0;j<m;j++) {
				char c = s.charAt(j);
				if(c=='-')
					arr[i][j]='-';
			}
		}
		for(int i = 0;i<n;i++) {
			for(int j=0;j<m;j++) {
				System.out.print(arr[i][j]);
			}
			System.out.println();
		}
	}
}