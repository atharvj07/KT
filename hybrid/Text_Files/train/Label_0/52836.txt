import java.util.*;
class Main {
	static int n;
	static int m;
	static Data[] list;
	static ArrayList<Integer> x = new ArrayList<Integer>();
	static boolean clear;
	static boolean goal;
	static int light;
	static boolean[][] al;
	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(true) {
			n = sc.nextInt();
			m = sc.nextInt();
			clear = false;
			goal = false;
			list = new Data[n];
			x.clear();
			al = new boolean[n][1 << n];
			light = 0;
			for(int i = 0; i < n; i++) {
				list[i] = new Data();
			}
			if(n == 0 && m == 0) break;
			for(int i = 0; i < m; i++) {
				int s = sc.nextInt()-1;
				int t = sc.nextInt()-1;
				Data tmp = list[s];
				tmp.c.add(t);
				tmp = list[t];
				tmp.c.add(s);
			}
			for(int i = 0; i < n; i++) {
				int tmp = sc.nextInt();
				if(tmp == 1) {
					light |= (1 << i);
				}
			}
			for(int i = 0; i < n; i++) {
				int k = sc.nextInt();
				for(int j = 0; j < k; j++) {
					list[i].s.add(sc.nextInt()-1);
				}
			}
			for(int i = 0; i < n; i++) {
				Collections.sort(list[i].s);
			}
			
			BFS();
			
			if(clear) {
				System.out.println("You can go home in " + x.size() + " steps.");
				for(int i = 0; i < x.size(); i++) {
					int tmp = x.get(i);
					if(tmp >= 100) {
						System.out.println("Switch on room " + (tmp + 1 - 100) + ".");
					}
					else if(tmp >= 0) {
						System.out.println("Move to room " + (tmp+1) + ".");
					}
					else {
						System.out.println("Switch off room " + (-(tmp + 99)) + ".");
					}
				}
			}
			else if(goal) {
				System.out.println("You can not switch off all lights.");
			}
			else {
				System.out.println("Help me!");
			}
			
			
			
		}
	}
	static ArrayDeque<BFSData> queue = new ArrayDeque<BFSData>();
	static void BFS() {
		queue.clear();
		queue.add(new BFSData(0,light,new ArrayList<Integer>()));
		while(!queue.isEmpty() && !clear) {
			bfs(queue.poll());
		}
	}
	//?¶???? -100 - ??¨?±???????
	//?????? 100 + ??¨?±???????
	//?§???? ??¨?±???????
	static void bfs(BFSData a) {
		//if((a.state & 1 << a.now) == 0) return;
		if(a.now == n-1) goal = true;
		if(a.now == n-1 && a.state == (1 << (n-1))) {
			clear = true;
			x = a.qq;
			return;
		}
		if(al[a.now][a.state]) return;
		al[a.now][a.state] = true;
		Data tmp = list[a.now];
		for(int i = 0; i < tmp.s.size(); i++) {
			if((a.state & (1 << tmp.s.get(i))) == 0) {
				BFSData next = new BFSData(a.now,a.state ^ (1 << tmp.s.get(i)),a.qq);
				next.qq.add(100 + tmp.s.get(i));
				queue.add(next);
			}
			if((a.state & (1 << tmp.s.get(i))) != 0) {
				a.state ^= 1 << tmp.s.get(i);
				BFSData next = new BFSData(a.now,a.state,a.qq);
				next.qq.add(-100 - tmp.s.get(i));
				queue.add(next);
				a.state ^= 1 << tmp.s.get(i);
			}
		}
		for(int i = 0; i < tmp.c.size(); i++) {
			if((a.state & (1 << tmp.c.get(i))) != 0 && (a.state & (1 << a.now)) != 0) {
				BFSData next = new BFSData(tmp.c.get(i),a.state,a.qq);
				next.qq.add(tmp.c.get(i));
				queue.add(next);
			}
		}
		
	}
	
	static class Data {
		ArrayList<Integer> c = new ArrayList<Integer>();
		ArrayList<Integer> s = new ArrayList<Integer>();
	}
	
	static class BFSData {
		int now;
		int state;
		ArrayList<Integer> qq;
		BFSData(int a, int b,ArrayList<Integer> c) {
			now = a;
			state = b;
			qq = new ArrayList<Integer>(c);
			Collections.copy(qq, c);
		}
		
	}
}