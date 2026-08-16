import java.util.Scanner;

public class Main {
	static long min = (long)Math.pow(1000, 4);
	static long[][] arr = new long[4][4];
	static boolean[][] vis = new boolean[4][4];
	static char[] arr1 = new char[3];
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		for(int i = 0;i < arr.length;i++) {
			arr[0][i] = scanner.nextInt();
		}
		for(int i = 0;i < arr1.length;i++) {
			arr1[i] = scanner.next().charAt(0);
		}
		for(int i = 0;i < arr.length;i++) {
			dfs(0);
		}
		System.out.println(min);
	}
	public static void dfs(int cnt) {
		if(cnt==3) {
			min = Math.min(min,arr[3][0]);
			return;
		}
		for(int i = 0;i < arr[cnt].length-cnt;i++) {
			for(int j = 0;j < arr[cnt].length-cnt;j++) {
				if(!vis[cnt][i]&&!vis[cnt][j]&&i!=j) {
					if(arr1[cnt]=='+') {
						vis[cnt][i] = true;
						vis[cnt][j] = true;
						arr[cnt+1][0] = arr[cnt][i]+arr[cnt][j];
						int z = 1;
						for(int c = 0;c < arr.length;c++) {
							if(!vis[cnt][c]) {
								arr[cnt+1][z] = arr[cnt][c];
								z++;
							}
						}
						dfs(cnt+1);
						vis[cnt][i] = false;
						vis[cnt][j] = false;
					}else {
						vis[cnt][i] = true;
						vis[cnt][j] = true;
						arr[cnt+1][0] = arr[cnt][i]*arr[cnt][j];
						int z = 1;
						for(int c = 0;c < arr[cnt].length;c++) {
							if(!vis[cnt][c]) {
								arr[cnt+1][z] = arr[cnt][c];
								z++;
							}
						}
						dfs(cnt+1);
						vis[cnt][i] = false;
						vis[cnt][j] = false;
					}
				}
			}
		}
	}
}