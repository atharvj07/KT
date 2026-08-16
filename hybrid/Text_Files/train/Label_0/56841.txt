import java.util.*;
class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(true) {
			int m = sc.nextInt();
			int n = sc.nextInt();
			if(m == 0 && n == 0) break;
			Data[] t = new Data[n];
			for(int i = 0; i < n; i++) {
				t[i] = new Data(i+1,sc.nextInt());
			}
			
			Data[] data1 = new Data[m];
			Data[] data2 = new Data[m];
			
			for(int i = 0; i < m; i++) {
				data1[i] = new Data(-1,0);
				data2[i] = new Data(-1,0);
			}
			
			Queue<Data> queue = new ArrayDeque<Data>();
			Queue<Data> out   = new ArrayDeque<Data>();
			int i = 0;
			while(out.size() != n) {
				if(i % 10 == 0 && i / 10 < n) {
					queue.add(t[i/10]);
				}
				
				for(int j = 0; j < m; j++) {
					if(data1[j].t != 0) {
						data1[j].t--;
					}
					if(data2[j].t != 0) {
						data2[j].t--;
					}
				}
				
				for(int j = 0; j < m; j++) {
					if(data1[j].t == 0 && data1[j].id != -1) {
						out.add(data1[j]);
						data1[j] = new Data(-1,0);
					}
					if(data2[j].t == 0 && data1[j].id == -1 && data2[j].id != -1) {
						out.add(data2[j]);
						data2[j] = new Data(-1,0);
					}
				}
				
				
				IN:while(!queue.isEmpty()) {
					for(int j = 0; j < m; j++) {
						if(data1[j].id == -1 && data2[j].id == -1) {
							data2[j] = queue.poll();
							continue IN;
						}
					}
					int id = -1;
					int ch = 10000000;
					for(int j = 0; j < m; j++) {
						if(data2[j].t >= queue.peek().t && data1[j].id == -1) {
							if(data2[j].t - queue.peek().t < ch) {
								ch = data2[j].t - queue.peek().t;
								id = j;
							}
						}
					}
					if(id != -1) {
						data1[id] = queue.poll();
						continue IN;
					}
					
					for(int j = 0; j < m; j++) {
							if(queue.peek().t - data2[j].t < ch && data1[j].id == -1) {
								ch = queue.peek().t - data2[j].t;
								id = j;
							}
					}
					if(id != -1) {
						data1[id] = queue.poll();
						continue IN;
					}
					break;					
				}
				
				i++;
			}
			
			System.out.print(out.poll().id);
			while(!out.isEmpty()) {
				System.out.print(" " + out.poll().id);
			}
			System.out.println();
			
		}
		
	}
	
	static class Data {
		int id;
		int t;
		Data(int a, int b) {
			id = a;
			t = b;
		}
	}
}