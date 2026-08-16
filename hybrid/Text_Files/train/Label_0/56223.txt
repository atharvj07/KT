import java.util.LinkedList;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		while(n != 0){
			LinkedList<Line> smpl = new LinkedList<Line>(); 
			
			Line line = new Line();
			int m = sc.nextInt();
			int ox = sc.nextInt();
			int oy = sc.nextInt();
			line.add(new Point(0, 0));
			for(int i = 1; i < m; i++){
				int x = sc.nextInt();
				int y = sc.nextInt();
				line.add(new Point(x - ox, y - oy));
			}
			smpl.add(line);
			smpl.add(rel(line, 0));
			line = rel(line, 90);
			smpl.add(line);
			smpl.add(rel(line, 0));
			line = rel(line, 90);
			smpl.add(line);
			smpl.add(rel(line, 0));
			line = rel(line, 90);
			smpl.add(line);
			smpl.add(rel(line, 0));
/*			for(int j = 0; j < smpl.size(); j++){
				for(Point g : smpl.get(j).list){
					System.out.print("[" + g.x + ":" + g.y + "]");
				}
				System.out.println();
			}
*/			for(int j = 1; j <= n; j++){
				line = new Line();
				m = sc.nextInt();
				ox = sc.nextInt();
				oy = sc.nextInt();
				line.add(new Point(0, 0));
				for(int i = 1; i < m; i++){
					int x = sc.nextInt();
					int y = sc.nextInt();
					line.add(new Point(x - ox, y - oy));
				}
				for(int k = 0; k < smpl.size(); k++){
					if(comp(smpl.get(k), line)){
						System.out.println(j);
						break;
					}
				}
			}
			System.out.println("+++++");
			n = sc.nextInt();
		}
		sc.close();
	}
	static Line rel(Line line, int rec){
		Line tmp = new Line();
		if(rec == 0){
			int ox, oy;
			Point p = line.get(line.size() - 1);
			ox = p.x;
			oy = p.y;
			Point t = new Point(0, 0);
			tmp.add(t);
			for(int i = line.size() - 2; i >= 0; i--){
				p = line.get(i);
				t = new Point(p.x - ox, p.y - oy);
				tmp.add(t);
			}
		}else if(rec == 90){
			for(int i = 0; i < line.size(); i++){
				Point p = line.get(i);
				Point t = new Point((-1) * p.y, p.x);
				tmp.add(t);
			}
		}else if(rec == 180){
			for(int i = 0; i < line.size(); i++){
				Point p = line.get(i);
				Point t = new Point((-1) * p.y,(-1) * p.x);
				tmp.add(t);
			}				
		}else if(rec == 270){
			for(int i = 0; i < line.size(); i++){
				Point p = line.get(i);
				Point t = new Point(p.y, (-1) * p.x);
				tmp.add(t);
			}
		}
		return tmp;
	}
	static boolean comp(Line sm, Line tr){
		if(sm.size() != tr.size()){
			return false;
		}
		for(int i = 0; i < sm.size(); i++){
			Point s = sm.get(i);
			Point t = tr.get(i);
			if(s.x != t.x || s.y != t.y){
				return false;
			}
		}
		return true;
	}
}
class Line{
	LinkedList<Point> list;
	Line(){
		list = new LinkedList<Point>();
	}
	void add(Point p){
		list.add(p);
	}
	Point get(int idx){
		return list.get(idx);
	}
	int size(){
		return list.size();
	}
}
class Point{
	int x;
	int y;
	Point(int x, int y){
		this.x = x;
		this.y = y;
	}
}