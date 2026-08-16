//package Hotdays;
import java.util.*;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int I = sc.nextInt(); int N = sc.nextInt();
		int[] forecast = new int[I];
		int[][] data = new int[N][3];
		//[0] = ???????°???? [1] = ???????°???? [2] = ?´???????
		int[][] costtable = new int[N][I];
		int max = 0;
		for(int i = 0; i < I; i++) forecast[i] = sc.nextInt();
		for(int i = 0; i < N; i++) {
			data[i][0] = sc.nextInt();
			data[i][1] = sc.nextInt();
			data[i][2] = sc.nextInt();
		}
		for(int i = 0; i < I; i++) {
			for(int j = 0; j < N; j++) {
				if(data[j][0] > forecast[i] || data[j][1] < forecast[i]) { 
					costtable[j][i] = -1; //???????????????????????????
				}
			}
		}
		for(int i = 1; i < I; i++) {
			for(int j = 0; j < N; j++) {
				if(costtable[j][i] != -1) {
					for(int k = 0; k < N; k++) { 
						if(costtable[k][i - 1] != -1) {
							if(costtable[j][i] < costtable[k][i - 1] + Math.abs(data[j][2] - data[k][2])) {
								costtable[j][i] = costtable[k][i - 1] + Math.abs(data[j][2] - data[k][2]);
							}
						}
					}
				}
			}
		}
		for(int i = 0; i < N; i++) {
			if(max < costtable[i][I - 1]) max = costtable[i][I - 1];
		}
		System.out.println(max);
	}
}