import java.util.Scanner;

public class Main {
	private Scanner sc;
	
	int start, goal;
	
	int[][] map;
	public static void main(String[] args) {
		new Main();
	}
	
	public Main() {
		sc = new Scanner(System.in);
		
		while (sc.hasNextLine() == true) {
			int num = Integer.parseInt(sc.nextLine());
			if (num == 0) break;
			
			start = Integer.parseInt(sc.nextLine()) - 1;
			goal = Integer.parseInt(sc.nextLine()) - 1;
			
			int lines = Integer.parseInt(sc.nextLine());
			
			map = new int[lines][num - 1];
			for (int i = 0; i < map.length; i++) {
				String nico = sc.nextLine();
				for (int j = 0; j < map[0].length; j++) {
					map[i][j] = nico.charAt(j) - '0';
				}
			}
			
			String ans = "1";
			for (int i = -1; i < lines; i++) {
				int tmp = judge(i);
				
				if (tmp != -1) {
					if (i == -1) ans = "0";
					else ans = (i + 1) + " " + tmp;
					break;
				}
			}
			System.out.println(ans);
		}
	}
	
	private int judge(int point) {
		int save = 0;
		
		int lim = 1;
		if (point > -1) lim++;
		
		for (int j = 0; j < lim; j++) {
			int p = start;
			
			for (int i = 0; i < map.length; i++) {
				if (p > 0) {
					if ((map[i][p - 1]) == 1) {
						p--;
						continue;
					}
				}
				
				if (p < map[0].length) {
					if (map[i][p] == 1) {
						p++;
						continue;
					}
				}
				
				if (i == point) {
					if (j == 0) {
						if (p == 0) {
							p = -1;
							break;
						}
						if (p > 1) {
							if (map[i][p - 2] == 1) continue;
						}
						
						save = p;
						p--;
					} else {
						if (p == map[0].length) {
							
							p = -1;
							break;
						}
						if (p < (map[0].length - 1))  {
							if (map[i][p + 1] == 1) continue;
						}
						
						p++;
						save = p;
					}
				}
			}
			if (p == goal) return save;
		}
		return -1;
	}
}