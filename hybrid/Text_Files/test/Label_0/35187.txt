import java.util.*;

public class Main{
	public static void search(int x,int y,int w,int h,String[][] map,Boolean[][] memo){
		if(x < 0 || x > w-1 || y < 0 || y > h-1 || map[x][y].equals("#")) return;
		if(memo[x][y]) return;
		memo[x][y] = true; 
		//System.out.println(x+","+y+"true");
		search(x+1,y,w,h,map,memo);
		search(x,y-1,w,h,map,memo);
		search(x-1,y,w,h,map,memo);
		search(x,y+1,w,h,map,memo);
	} 
	
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		while(true){
			int w = scan.nextInt();
			int h = scan.nextInt();
			int count = 0;
			if(w == 0 && h == 0) break;
			String[][] map = new String[w][h];
			Boolean[][] memo = new Boolean[w][h];
			for(int i=0;i<h;i++){
				String str = scan.next(); 
				for(int j=0;j<w;j++){
					memo[j][i] = false;
					map[j][i] = String.valueOf(str.charAt(j));
				}
			}
			for(int i=0;i<h;i++){
				for(int j=0;j<w;j++){
					if(map[j][i].equals("@")){
						search(j,i,w,h,map,memo);
						break;
					}
				}
			}
			for(int i=0;i<h;i++){
				for(int j=0;j<w;j++){
					//System.out.print(map[j][i]);
					//System.out.println();
					if(memo[j][i] == true) count++;
				}
				//System.out.println("");
			}
			System.out.println(count);
			/*
			for(int i=0;i<h;i++){
				for(int j=0;j<w;j++){
					System.out.print(memo[i][j]);
				}
				System.out.println("");
			}
			*/
		}
	}
}