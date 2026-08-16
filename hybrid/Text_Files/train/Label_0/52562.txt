import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Map.Entry;
import java.util.Scanner;
import java.util.TreeMap;

public class Main {
	static final int INF = 2000000;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		while(true){
			int w = sc.nextInt();
			int h = sc.nextInt();
			if(w == 0 && h == 0){
				break;
			}
			
			LinkedList<Point> list = new LinkedList<Point>();
			TreeMap<Integer, LinkedList<Point>> map = new TreeMap<Integer, LinkedList<Point>>();
			
			Point start = null, goal = null;
			int max = 0;
			for(int i = 0; i < h; i++){
				for(int j = 0; j < w; j++){
					String s = sc.next();
					if(s.equals("S")){
						start = new Point(0, i, j);
						LinkedList<Point> temp = new LinkedList<Point>();
						temp.add(start);
						map.put(0, temp);
					}else if(s.equals("G")){
						goal = new Point(INF, i, j);
					}else if(s.matches("[0-9]+")){
						int num = Integer.parseInt(s);
						max = max < num ? num : max;
						if(map.containsKey(num)){
							map.get(num).add(new Point(INF, i, j));
						}else{
							LinkedList<Point> temp = new LinkedList<Point>();
							temp.add(new Point(INF, i, j));
							map.put(num, temp);
						}
						list.add(new Point(num, i, j));
					}
				}
			}
			LinkedList<Point> temp = new LinkedList<Point>();
			temp.add(goal);
			map.put(max + 1, temp);
			System.out.println(fm(map));
		}
		sc.close();
	}
	static int fm(TreeMap<Integer, LinkedList<Point>> map){
		int m = 1;
		LinkedList<Point> from = map.get(0);
		LinkedList<Point> to = null;
		while(true){
			if(!map.containsKey(m)){
				break;
			}
			to = map.get(m);
			for(Point p : to){
				for(Point s : from){
					int temp = Math.abs(p.x - s.x) + Math.abs(p.y - s.y);
					p.n = p.n > temp + s.n ? temp + s.n : p.n;
				}
			}
			from = to;
			m++;
		}		
		return map.get(m - 1).get(0).n;
	}
	static int func(LinkedList<Point> list, Point from, Point goal, int idx){
		int res = 2000000;
		boolean flg = false;
		for(int i = idx; i < list.size(); i++){
			Point p = list.get(i);
			System.out.println(p.n);
			if(from.n + 1 == p.n){
				int dist = Math.abs(from.x - p.x) + Math.abs(from.y - p.y);
				res = Math.min(func(list, p, goal, i) + dist, res);
				flg = true;
			}else if(from.n + 1 < p.n){
				break;
			}
		}
		if(!flg){
			return Math.abs(from.x - goal.x) + Math.abs(from.y - goal.y);
		}
		return res;
	}
}
class Point implements Comparable<Point>{
	int n;
	int x;
	int y;
	Point(int n, int y, int x){
		this.n = n;
		this.x = x;
		this.y = y;
	}
	@Override
	public int compareTo(Point p) {
		// TODO Auto-generated method stub
		return n - p.n;
	}
}