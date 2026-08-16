import static java.lang.System.*;
import java.util.*;

public class Main {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner sc = new Scanner(in);
		
		for(int seti=1; ; seti++) {
			int n = sc.nextInt();
			if(n==0) break;
			
			boolean[][][] map = new boolean[5][5][5];
			for(int i=0; i<5; i++) {
				for(int j=0; j<5; j++) {
					char[] tmp = sc.next().toCharArray();
					for(int k=0; k<5; k++) {
						map[i][j][k] = tmp[k] == '1';
					}
				}
			}

			ArrayList<Integer> birth = new ArrayList<Integer>();
			ArrayList<Integer> die = new ArrayList<Integer>();

			int b = sc.nextInt();
			for(int i=0; i<b; i++) birth.add(sc.nextInt());
			int d = sc.nextInt();
			for(int i=0; i<d; i++) die.add(sc.nextInt());

			while(n-->0) {
				boolean[][][] next = new boolean[5][5][5];
				
				for(int i=0; i<5; i++) {
					for(int j=0; j<5; j++) {
						for(int k=0; k<5; k++) {
							int count = 0;
							for(int x=-1; x<=1; x++) {
								for(int y=-1; y<=1; y++) {
									for(int z=-1; z<=1; z++) {
										if(x==0 && y==0 && z==0) continue;
										
										int nz = i + z;
										int ny = j + y;
										int nx = k + x;
										
										if(!(0<=nx && nx<5 && 0<=ny && ny<5 && 0<=nz && nz<5)) continue;
										if(map[nz][ny][nx]) count++;
										
//										out.println(" " + nz + " " + ny + " " + nx + "  " + (map[nz][ny][nx] ? "T":"F"));
									}
								}
							}
//							out.println(i + " " + j + " " + k + " " + count);
							
							next[i][j][k] = false;
							if(!map[i][j][k]) {
								for(int c: birth) {
									if(count == c) {
										next[i][j][k] = true;
										break;
									}
								}
							}
							else {
								for(int c: die) {
									if(count == c) {
										next[i][j][k] = true;
										break;
									}
								}
							}
						}
					}
				}
				
				map = next;
			}
			
			if(seti != 1) out.println();
			out.println("Case " + seti + ":");

			for(int i=0; i<5; i++) {
				for(int j=0; j<5; j++) {
					for(int k=0; k<5; k++) {
						out.print(map[i][j][k] ? "1": "0");
					}
					out.println();
				}
				if(i!=4) out.println();
			}
		}
	}

}