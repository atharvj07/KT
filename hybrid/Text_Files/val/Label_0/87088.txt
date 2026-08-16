import java.util.Arrays;
import java.util.Scanner;

//Taro's Obsession
public class Main{

	void run(){
		Scanner sc = new Scanner(System.in);
		int m = sc.nextInt(), n = sc.nextInt();
		boolean[][] e = new boolean[m+1][m+1];
		int[] deg = new int[m+1];
		while(n--!=0){
			int x = sc.nextInt(), y = sc.nextInt();
			e[y][x] = true;
			deg[y]++;
		}
		for(int i=0;i<m;i++){
			for(int j=1;j<=m;j++)if(deg[j]==0){
//				if(i!=m-1 && j==2)continue;
				System.out.println(j);
				deg[j] = -1;
				for(int k=1;k<=m;k++)if(e[k][j])deg[k]--;
			}
		}
	}
	
	void debug(Object...o){
		System.out.println(Arrays.deepToString(o));
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}