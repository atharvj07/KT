import java.util.*;
import java.math.*;
public class Main{

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int P = sc.nextInt();
		for(int KK = 0; KK < P; KK++) {
			int n = sc.nextInt();
			int x = sc.nextInt();
			int y = sc.nextInt();
			Node start = new Node(sc.nextInt(),sc.nextInt());
			Node[] staff = new Node[n+1];
			for(int i = 0; i < n; i++) {
				staff[i] = new Node(sc.nextInt(),sc.nextInt());
			}
			for(int i = 0; i < n; i++) {
				int len = l(start,staff[i]);
				if(len > 10 * 10) continue;
				start.to.add(i);
			}
			for(int i = 0; i < n; i++) {
				for(int j = i + 1; j < n; j++) {
					int len = l(staff[i],staff[j]);
					if(len > 50 * 50) continue;
					staff[i].to.add(j);
					staff[j].to.add(i);
				}
			}
			int count = 0;
			int say   = 0;
			ArrayDeque<Data> queue = new ArrayDeque<Data>();
			for(int i = 0; i < start.to.size(); i++) {
				queue.add(new Data(start.to.get(i),0));
			}
			while(!queue.isEmpty() && count < 2000) {
				Data tmp = queue.pollFirst();
				Node check = staff[tmp.now];
				//????????????       //????????????
				if(check.time > tmp.time) continue;
				say = Math.max(tmp.time + x,say);
				count++;
				ArrayList<Integer> to = check.to;
				for(int i = 0; i < to.size(); i++) {
					queue.add(new Data(to.get(i),tmp.time + x));
				}
				//????????????
				check.time = tmp.time + x + y + 1;
			}
			if(count == 2000) System.out.println("You're always welcome!");
			else {
				System.out.println(say);
			}
		}
	}
	static class Data {
		int now;
		int time;
		Data(int now, int time) {
			this.now = now;
			this.time = time;
		}
	}
	static int l(Node a, Node b) {
		int k = (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y);
		return k;
	}
	static class Node {
		int x;
		int y;
		int time;
		Node(int a, int b) {
			x = a;
			y = b;
		}
		ArrayList<Integer> to = new ArrayList<Integer>();
	}
}