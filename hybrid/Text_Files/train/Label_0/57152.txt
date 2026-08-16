import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	
	public static class Walk implements Comparable<Walk>{
		int x;
		int y;
		int cost;
		
		public Walk(int x, int y, int cost) {
			super();
			this.x = x;
			this.y = y;
			this.cost = cost;
		}

		@Override
		public int compareTo(Walk arg0) {
			return this.cost - arg0.cost;
		}
		
		
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while(true){
			final int w = sc.nextInt();
			final int h = sc.nextInt();
			
			if(h == 0 && w == 0){
				break;
			}
			
			boolean[][] is_wall = new boolean[h][w];
			boolean[][] is_visited = new boolean[h][w];
			
			int goal_x = -1, goal_y = -1;
			
			for(int i = 0; i < h; i++){
				char[] ch = sc.next().toCharArray();
				
				for(int j = 0; j < w; j++){
					is_wall[i][j] = ch[j] == '#';
					
					if(ch[j] == '&'){
						goal_x = j;
						goal_y = i;
					}
				}
				
			}
			
			PriorityQueue<Walk> queue = new PriorityQueue<Walk>(); 
			for(int i = 0; i < h; i++){
				for(int j = 0; j < w; j++){
					if(i == 0 || i == (h - 1) || j == 0 || j ==(w - 1)){
						queue.add(new Walk(j, i, is_wall[i][j] ? 1 : 0));
					}
				}
			}
			
			
			
			while(!queue.isEmpty()){
				Walk walk = queue.poll();
				
				//System.out.println(walk.x + " " + walk.y + " " + walk.cost);
				
				if(walk.x == goal_x && walk.y == goal_y){
					System.out.println(walk.cost);
					break;
				}
				
				if(is_visited[walk.y][walk.x]){
					continue;
				}
				is_visited[walk.y][walk.x] = true;
				
				
				if(walk.x != 0 && !is_visited[walk.y][walk.x - 1]){
					queue.add(new Walk(walk.x - 1,walk.y, walk.cost + ((!is_wall[walk.y][walk.x] && is_wall[walk.y][walk.x - 1]) ? 1 : 0)));
				}
				
				if(walk.x != (w-1) && !is_visited[walk.y][walk.x + 1]){
					queue.add(new Walk(walk.x + 1,walk.y, walk.cost + ((!is_wall[walk.y][walk.x] && is_wall[walk.y][walk.x + 1]) ? 1 : 0)));
				}
				
				if(walk.y != 0 && !is_visited[walk.y - 1][walk.x]){
					queue.add(new Walk(walk.x,walk.y - 1, walk.cost + ((!is_wall[walk.y][walk.x] && is_wall[walk.y - 1][walk.x]) ? 1 : 0)));
				}
				
				if(walk.y != (h-1) && !is_visited[walk.y + 1][walk.x]){
					queue.add(new Walk(walk.x,walk.y + 1, walk.cost + ((!is_wall[walk.y][walk.x] && is_wall[walk.y + 1][walk.x]) ? 1 : 0)));
				}
			}
			
		}
		
	}

}