import java.util.Scanner;

public class Main {	
	public static void main(String args[]){
		Scanner scr = new Scanner(System.in);
		int t = Integer.parseInt(scr.nextLine());
		for(int i=0; i<t; i++){
			String[] strs = scr.nextLine().split(" ",0);
			int[] g = new int[2]; // g??§?¨?
			g[0] = Integer.parseInt(strs[0]);
			g[1] = Integer.parseInt(strs[1]);
			int s = Integer.parseInt(scr.nextLine());
			MatatabiWays[] m_pos = new MatatabiWays[s];
			for(int j=0; j<s; j++){
				m_pos[j] = new MatatabiWays( scr.nextLine().split(" ",0) );
			}
			int c=Hokusai(g, m_pos);
			if(c==0){
				System.out.println("Miserable Hokusai!");
			}else{
				System.out.println(c);
			}
			
		}
		scr.close();
	}
	private static int Hokusai(int[] g, MatatabiWays[] ms){
		int[][] how_many_ways = new int[g[0]+1][g[1]+1];
		boolean[][] m_load_H = new boolean[g[0]][g[1]+1];
		boolean[][] m_load_V = new boolean[g[0]+1][g[1]];
		for(int x=0; x<=g[0]; x++){
			for(int y=0; y<=g[1]; y++){
				if(x<g[0])m_load_H[x][y] = false;
				if(y<g[1])m_load_V[x][y] = false;
			}
		}//?????????
		for(int s=0; s<ms.length; s++){
			if(ms[s].dir){
				m_load_H[ms[s].x][ms[s].y] = true;
			}else{				
				m_load_V[ms[s].x][ms[s].y] = true;
			}
		}
				
		for(int y=0; y<=g[1]; y++){
			if(y==0){
				how_many_ways[0][0] = 1;
				for(int x=1; x<=g[0]; x++){
					how_many_ways[x][0] = m_load_H[x-1][0]?
							0:
							how_many_ways[x-1][0];
				}
			}else{
				how_many_ways[0][y] = m_load_V[0][y-1]?
						0:
						how_many_ways[0][y-1];
				for(int x=1; x<=g[0]; x++){
					how_many_ways[x][y] = (m_load_H[x-1][y]? 0: how_many_ways[x-1][y])
							+(m_load_V[x][y-1]? 0: how_many_ways[x][y-1]);
				}
			}
		}
		return how_many_ways[g[0]][g[1]];
	}
}
class MatatabiWays{
	public int x;
	public int y;
	public boolean dir;//if Holizontal or else
	MatatabiWays(String[] state){
		int x1 = Integer.parseInt(state[0]);
		int y1 = Integer.parseInt(state[1]);
		int x2 = Integer.parseInt(state[2]);
		int y2 = Integer.parseInt(state[3]);
		x=(x1<=x2)? x1: x2;
		y=(y1<=y2)? y1: y2;
		if(x1==x2){
			dir=false;
		}else if(y1==y2){
			dir=true;
		}
	}
}