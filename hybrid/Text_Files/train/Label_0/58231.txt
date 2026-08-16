import java.util.*;
import java.awt.geom.*;
public class Main {
	boolean [][] clocktable;
	int ansclock, n;
	int [] inputxpos, inputypos;
	
	private void dfs(int deep, int startpos, int nowclock){
		if(deep == 9){
			
			nowclock += n;
			ansclock = Math.min(ansclock, nowclock);
			//System.out.println(nowclock +" "+startpos);
			//disp();
			return;
		}
		for(int i = 1; i <= n; i++){
			//System.out.println("deep = " + deep +" " + i);
			//disp();
			boolean isarranged = true;
			ArrayList<Integer> setxpos = new ArrayList<Integer>(), setypos = new ArrayList<Integer>();
			for(int j = 0; j < n; j++){
				int xpos = startpos + i + inputxpos[j];
				int ypos = inputypos[j];
				if(!clocktable[ypos][xpos]){
					clocktable[ypos][xpos] = true;
					setxpos.add(xpos);
					setypos.add(ypos);
				}
				else{
					isarranged = false;
					break;
				}
			}
			
			//dfs
			if(isarranged){
				int nextstartpos = startpos + i;
				int nextclock = nowclock + i;
				dfs(deep + 1, nextstartpos, nextclock);
			}
			//reset operation
			for(int j = 0; j < setxpos.size(); j++){
				int nowx = setxpos.get(j);
				int nowy = setypos.get(j);
				clocktable[nowy][nowx] = false;
			}
		}
	}
	
	private void disp(){
		for(int i = 0; i < 5; i++){
			for(int j = 0; j < clocktable[i].length; j++){
				if(clocktable[i][j]){
					System.out.print("X");
				}
				else{
					System.out.print(".");
				}
			}
			System.out.println();
		}
		System.out.println();
	}

	private void doit(){
		Scanner sc = new Scanner(System.in);
		while(true){
			n = sc.nextInt();
			if(n == 0) break;
			inputxpos = new int[n];
			inputypos = new int[n];
			clocktable = new boolean[5][n * 10 + 1];
			int inputind = 0;
			for(int i = 0; i < 5; i++){
				String inputline = sc.next();
				for(int j = 0; j < inputline.length(); j++){
					char now = inputline.charAt(j);
					if(now == 'X'){
						inputxpos[inputind] = j;
						inputypos[inputind++] = i;
						clocktable[i][j] = true;
					}
				}
			}
			ansclock = 1 << 24;
			dfs(0, 0, 0);
			System.out.println(ansclock);
		}
	}

	public static void main(String[] args) {
		Main obj = new Main();
		obj.doit();
	}
}