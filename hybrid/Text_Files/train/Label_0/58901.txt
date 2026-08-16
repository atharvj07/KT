
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Main m = new Main();
		m.run();
	}

	Scanner sc = new Scanner(System.in);

	void run() {
		for (;;) {
			int n = sc.nextInt();
			if(n == 0){
				break;
			}
			int m = sc.nextInt();
			
			int map[][] = new int[n][n];
			
			
			for(int i = 0; i < m ; i++){
				int x = sc.nextInt()-1;
				int y = sc.nextInt()-1;
				map[x][y] = 1;
				map[y][x] = -1;
			}
			
			System.out.println(dfs(map,0,1,0));
		}
	}
	
	int dfs(int map[][],int x,int y,int count){
		if(x >= map.length){
			return 1;
		}
		if(y >= map[x].length){
			int ss = 0;
			for(int s :map[x]){
				ss += s;
			}
			if(ss == 0){
				return dfs(map,x+1,x+2,count);
			}else{
				return 0;
			}
		}
		if(map[x][y] != 0){
			return dfs(map,x,y+1,count);
		}
		
		int res = 0;
		map[x][y] = 1;
		map[y][x] = -1;
		res += dfs(map,x,y+1,count);
		map[x][y] = -1;
		map[y][x] = 1;
		res += dfs(map,x,y+1,count);
		map[x][y] = 0;
		map[y][x] = 0;
		return res;
	}
}

