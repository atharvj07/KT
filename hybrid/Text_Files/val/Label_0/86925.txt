import java.util.Scanner;
import java.util.Queue;
import java.util.ArrayDeque;
 
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//初期化と入力
		int h = sc.nextInt();
		int w = sc.nextInt();
		int[] c = new int[2];
		int[] d = new int[2];
		char[][] s = new char[h+4][w+4];
		c[0] = sc.nextInt()+2;
		c[1] = sc.nextInt()+2;
		d[0] = sc.nextInt()+2;
		d[1] = sc.nextInt()+2;
		for(int i = 0; i < h+4; i++) {
			for(int j = 0; j < w+4; j++) {
				s[i][j] = '0';
			}
		}
		for(int i = 0; i < h; i++) {
			String temp = sc.next();
			for(int j = 0; j < w; j++) {
				s[i+2][j+2] = temp.charAt(j);
			}
		}
		boolean[][]	 check = new boolean[h+4][w+4];
		for(int i = 0; i < h+4; i++) {
			for(int j = 0; j < w+4; j++) {
				check[i][j] = true;
			}
		}
		Queue<Integer> kohoy = new ArrayDeque<>();
		Queue<Integer> kohox = new ArrayDeque<>();
		Queue<Integer> searchy = new ArrayDeque<>();
		Queue<Integer> searchx = new ArrayDeque<>();
		kohoy.add(c[0]-1);
		kohox.add(c[1]-1);
		int ans = 0;
		//ここまで初期化と入力↑
		
		while(true) {
			//ワープ候補先を（１回目はスタート地点）を探索
			while(true) {
				//System.out.println(kohoy.peek()+" "+kohox.peek());
				if(kohoy.peek()==null) {
					break;
				}
				run(s,check,kohoy.poll(),kohox.poll(),searchy,searchx);
				//System.out.println(kohoy.peek()+" "+kohox.peek());
			}
			/*for(int i = 0; i < h + 4; i++) {
				for(int j = 0; j < w + 4; j++) {
					if(check[i][j]==true) {
						System.out.print('a');
					}else {
						System.out.print('b');
					}
				}System.out.println();
			}*/
			//System.out.println();
			//ゴールが探索済みなら終了
			if(!check[d[0]-1][d[1]-1]) {
				break;
			}
			//探索した場所（serachy,searchx)からワープ先候補を探してキュー(kohoy,kohox)に入れる
			while(true) {
				if(searchy.peek()==null) {
					break;
				}
				warp(s,check,kohoy,kohox,searchy,searchx);
			}
			//探索する地点とワープ先がなくなって、ゴールが未探索ならばゴール不可能で終了
			if(searchy.peek()==null && kohoy.peek()==null && check[d[0]-1][d[1]-1]) {
				ans = -1;
				break;
			}
 
			++ans;
		}
		System.out.println(ans);
		
	}
	//候補キューから探索開始地点を取り出して探索．探索した場所を探索済みキューに入れる
	public static void run(char[][] map,boolean[][] check,int y, int x,Queue<Integer> sy,Queue<Integer> sx) {
		check[y][x] =false;
		sy.add(y);
		sx.add(x);
		if(map[y+1][x] == '.' && check[y+1][x] == true) {
			run(map,check,y+1,x, sy,sx);
		}if(map[y-1][x] == '.' && check[y-1][x] == true) {
			run(map,check,y-1,x, sy,sx);
		}if(map[y][x+1] == '.' && check[y][x+1] == true) {
			run(map,check,y,x+1, sy,sx);
		}if(map[y][x-1] == '.' && check[y][x-1] == true) {
			run(map,check,y,x-1, sy,sx);
		}
	}
	//探索済みキューから取り出しワープできる場所を探して候補キューに入れる．
	public static void warp(char[][] map,boolean[][] check,Queue<Integer> kohoy,Queue<Integer> kohox,Queue<Integer> sy,Queue<Integer> sx) {
		int y = sy.poll();
		int x = sx.poll();
		for(int i = 0; i < 5; i++) {
			for(int j = 0; j < 5; j++) {
				if(map[y-2+i][x-2+j] == '.' && check[y-2+i][x-2+j] == true) {
					kohoy.add(y-2+i);
					kohox.add(x-2+j);
					//System.out.println("a"+(y-2+i)+" "+(x-2+j));
				}
			}
		}
	}
}