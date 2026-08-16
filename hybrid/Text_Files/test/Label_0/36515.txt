import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

//Yanagi's Comic
public class Main{

	class R implements Comparable<R>{
		int id, read;
		boolean f;
		int[][] p;//0: right-up 1:right-down 2:left-up 3:left-down
		public R(int ID, int x1, int y1, int x2, int y2) {
			id = ID;
			p = new int[4][2];
			if(x1<x2){
				if(y1<y2){
					p[0][0] = x1;p[0][1] = y1;
					p[1][0] = x1;p[1][1] = y2;
					p[2][0] = x2;p[2][1] = y1;
					p[3][0] = x2;p[3][1] = y2;
				}
				else {
					p[0][0] = x1;p[0][1] = y2;
					p[1][0] = x1;p[1][1] = y1;
					p[2][0] = x2;p[2][1] = y1;
					p[3][0] = x2;p[3][1] = y2;
				}
			}
			else{
				if(y1<y2){
					p[0][0] = x2;p[0][1] = y1;
					p[1][0] = x2;p[1][1] = y2;
					p[2][0] = x1;p[2][1] = y1;
					p[3][0] = x1;p[3][1] = y2;
				}
				else{
					p[0][0] = x2;p[0][1] = y2;
					p[1][0] = x2;p[1][1] = y1;
					p[2][0] = x1;p[2][1] = y2;
					p[3][0] = x1;p[3][1] = y1;
				}
			}
		}
		public int compareTo(R o) {
			return p[0][0]!=o.p[0][0]?p[0][0]-o.p[0][0]:p[0][1]-o.p[0][1];
		}
	}

	int num;

	void read(List<R> list){
		if(list.isEmpty())return;
		Collections.sort(list);
		R top = list.get(0);
		top.f = true;
		top.read = num++;
		int left = 500;
		int bottom = top.p[3][1];
		for(int i=1;i<list.size();i++){
			R r = list.get(i);
			if(r.p[0][1]<bottom&&bottom<r.p[1][1])left = Math.min(left, r.p[0][0]);
		}
		List<R> L = new ArrayList<R>();
		for(int i=1;i<list.size();i++){
			R r = list.get(i);
			if(r.f)continue;
			if(r.p[3][0]<=left&&r.p[3][1]<=bottom)L.add(r);
		}
		read(L);
		List<R> next = new ArrayList<R>();
		for(int i=0;i<list.size();i++){
			if(!list.get(i).f)next.add(list.get(i));
		}
		read(next);
	}

	void run(){
		Scanner sc = new Scanner(System.in);
		boolean f = true;
		while(true){
			int n = sc.nextInt();
			if(n==0)break;
			if(!f)System.out.println();
			num = 1;
			f = false;
			R[] r = new R[n];
			List<R> l = new ArrayList<R>();
			for(int i=0;i<n;i++){
				r[i] = new R(i, sc.nextInt(), sc.nextInt(), sc.nextInt(), sc.nextInt());
				l.add(r[i]);
			}
			read(l);
			for(int i=0;i<n;i++)System.out.println(r[i].read);
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}
}